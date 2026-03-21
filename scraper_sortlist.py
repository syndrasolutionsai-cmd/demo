"""
Scraper de agencias de marketing en sortlist.es
Extrae: nombre, URL perfil, ciudad, especialidad, URL web
Exporta a CSV con paginación automática.

Requisitos:
    pip install playwright
    playwright install chromium
"""

import asyncio
import csv
import re
import sys
from dataclasses import dataclass, fields
from pathlib import Path

from playwright.async_api import async_playwright, Page, TimeoutError as PlaywrightTimeout

BASE_URL = "https://www.sortlist.es/es/agencias-de-marketing"
OUTPUT_FILE = "agencias_marketing.csv"
# Espera máxima por elementos (ms)
TIMEOUT = 15_000
# Pausa entre páginas para no sobrecargar el servidor (segundos)
PAGE_DELAY = 2.0


@dataclass
class Agency:
    nombre: str
    url_perfil: str
    ciudad: str
    especialidad: str
    url_web: str


# ---------------------------------------------------------------------------
# Helpers de extracción
# ---------------------------------------------------------------------------

def _clean(text: str | None) -> str:
    if not text:
        return ""
    return re.sub(r"\s+", " ", text).strip()


async def _extract_agencies(page: Page) -> list[Agency]:
    """Extrae todas las agencias visibles en la página actual."""
    agencies: list[Agency] = []

    # Esperar a que carguen las tarjetas
    try:
        await page.wait_for_selector("[data-testid='agency-card'], .agency-card, article[class*='agency']", timeout=TIMEOUT)
    except PlaywrightTimeout:
        # Intentar con selector alternativo
        try:
            await page.wait_for_selector("a[href*='/agencies/'], a[href*='/agencias/']", timeout=TIMEOUT)
        except PlaywrightTimeout:
            print("  [WARN] No se encontraron tarjetas de agencias en esta página.")
            return agencies

    # Capturar todos los datos mediante evaluate para un único round-trip
    raw = await page.evaluate("""() => {
        const results = [];

        // Selectores candidatos para tarjetas de agencia
        const cardSelectors = [
            '[data-testid="agency-card"]',
            '[data-testid="provider-card"]',
            'article[class*="agency"]',
            'div[class*="AgencyCard"]',
            'div[class*="agency-card"]',
            'li[class*="agency"]',
        ];

        let cards = [];
        for (const sel of cardSelectors) {
            cards = Array.from(document.querySelectorAll(sel));
            if (cards.length > 0) break;
        }

        // Fallback: buscar por enlaces a perfiles de agencia
        if (cards.length === 0) {
            const links = Array.from(document.querySelectorAll('a[href]')).filter(a => {
                const href = a.getAttribute('href') || '';
                return href.includes('/agencies/') || href.includes('/agencias/');
            });
            // Subir al ancestro raíz de cada enlace (contenedor de la tarjeta)
            const seen = new Set();
            for (const link of links) {
                let el = link;
                for (let i = 0; i < 5; i++) {
                    el = el.parentElement;
                    if (!el) break;
                    const tag = el.tagName.toLowerCase();
                    if (['li', 'article', 'section', 'div'].includes(tag)) {
                        if (!seen.has(el)) {
                            seen.add(el);
                            cards.push(el);
                        }
                        break;
                    }
                }
            }
        }

        for (const card of cards) {
            // --- Nombre ---
            const nameEl = card.querySelector(
                '[data-testid="agency-name"], [class*="name"], [class*="Name"], h2, h3, h4'
            );
            const nombre = nameEl ? nameEl.innerText.trim() : '';

            // --- URL perfil ---
            const linkEl = card.querySelector('a[href*="/agencies/"], a[href*="/agencias/"]')
                        || card.querySelector('a[href]');
            let urlPerfil = linkEl ? linkEl.getAttribute('href') : '';
            if (urlPerfil && urlPerfil.startsWith('/')) {
                urlPerfil = 'https://www.sortlist.es' + urlPerfil;
            }

            // --- Ciudad ---
            const cityEl = card.querySelector(
                '[data-testid="agency-location"], [class*="location"], [class*="Location"], [class*="city"], [class*="City"]'
            );
            const ciudad = cityEl ? cityEl.innerText.trim() : '';

            // --- Especialidad ---
            const specEl = card.querySelector(
                '[data-testid="agency-tag"], [class*="tag"], [class*="Tag"], [class*="specialty"], [class*="Specialty"], [class*="service"], [class*="Service"]'
            );
            const especialidad = specEl ? specEl.innerText.trim() : '';

            // --- URL web (puede estar como atributo data o enlace externo) ---
            const webEl = card.querySelector('a[href^="http"]:not([href*="sortlist"])');
            const urlWeb = webEl ? webEl.getAttribute('href') : '';

            if (nombre || urlPerfil) {
                results.push({ nombre, urlPerfil, ciudad, especialidad, urlWeb });
            }
        }
        return results;
    }""")

    for item in raw:
        agencies.append(Agency(
            nombre=_clean(item.get("nombre")),
            url_perfil=_clean(item.get("urlPerfil")),
            ciudad=_clean(item.get("ciudad")),
            especialidad=_clean(item.get("especialidad")),
            url_web=_clean(item.get("urlWeb")),
        ))

    return agencies


async def _get_next_page_url(page: Page) -> str | None:
    """Devuelve la URL de la siguiente página o None si no existe."""
    # Buscar botón/enlace «siguiente» o paginación numérica
    next_url: str | None = await page.evaluate("""() => {
        // 1. rel="next"
        const rel = document.querySelector('a[rel="next"]');
        if (rel) return rel.href;

        // 2. Botones/enlaces con texto «siguiente», «›», «>», etc.
        const candidates = Array.from(document.querySelectorAll('a, button'));
        for (const el of candidates) {
            const txt = el.innerText.trim().toLowerCase();
            if (['siguiente', 'next', '›', '>', '»'].includes(txt)) {
                return el.href || null;
            }
        }

        // 3. Patrón ?page=N en la URL actual — incrementar
        const params = new URLSearchParams(window.location.search);
        const current = parseInt(params.get('page') || '1', 10);

        // Verificar si existe enlace a la página siguiente numéricamente
        const pageLinks = Array.from(document.querySelectorAll('a[href]'))
            .map(a => a.getAttribute('href'))
            .filter(h => h && h.includes('page='));
        const nextPage = current + 1;
        const found = pageLinks.find(h => h.includes(`page=${nextPage}`));
        if (found) {
            return found.startsWith('http') ? found : 'https://www.sortlist.es' + found;
        }

        return null;
    }""")
    return next_url if next_url else None


# ---------------------------------------------------------------------------
# Flujo principal
# ---------------------------------------------------------------------------

async def scrape() -> list[Agency]:
    all_agencies: list[Agency] = []
    visited: set[str] = set()

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent=(
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1280, "height": 900},
            locale="es-ES",
        )
        page = await context.new_page()

        # Bloquear recursos innecesarios para acelerar la carga
        await page.route(
            "**/*.{png,jpg,jpeg,gif,webp,svg,woff,woff2,ttf,eot}",
            lambda route: route.abort(),
        )

        current_url = BASE_URL
        page_num = 1

        while current_url:
            if current_url in visited:
                print(f"  [WARN] URL ya visitada, deteniendo: {current_url}")
                break
            visited.add(current_url)

            print(f"Página {page_num}: {current_url}")
            try:
                await page.goto(current_url, wait_until="domcontentloaded", timeout=30_000)
            except Exception as exc:
                print(f"  [ERROR] No se pudo cargar la página: {exc}")
                break

            # Scroll suave para activar lazy-loading
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight / 2)")
            await page.wait_for_timeout(800)
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            await page.wait_for_timeout(800)

            agencies = await _extract_agencies(page)
            if not agencies:
                print("  No se encontraron agencias. Fin de la paginación.")
                break

            print(f"  Encontradas {len(agencies)} agencias.")
            all_agencies.extend(agencies)

            next_url = await _get_next_page_url(page)
            current_url = next_url
            page_num += 1

            if current_url:
                await page.wait_for_timeout(int(PAGE_DELAY * 1000))

        await browser.close()

    # Deduplicar por URL de perfil
    seen_urls: set[str] = set()
    unique: list[Agency] = []
    for ag in all_agencies:
        key = ag.url_perfil or ag.nombre
        if key and key not in seen_urls:
            seen_urls.add(key)
            unique.append(ag)

    return unique


def save_csv(agencies: list[Agency], path: str = OUTPUT_FILE) -> None:
    fieldnames = [f.name for f in fields(Agency)]
    out = Path(path)
    with out.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for ag in agencies:
            writer.writerow({
                "nombre": ag.nombre,
                "url_perfil": ag.url_perfil,
                "ciudad": ag.ciudad,
                "especialidad": ag.especialidad,
                "url_web": ag.url_web,
            })
    print(f"\nCSV guardado: {out.resolve()}  ({len(agencies)} registros)")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    output = sys.argv[1] if len(sys.argv) > 1 else OUTPUT_FILE
    print(f"Iniciando scraping de {BASE_URL} …\n")
    data = asyncio.run(scrape())
    if data:
        save_csv(data, output)
    else:
        print("[WARN] No se extrajeron datos. Revisa la estructura del sitio.")
