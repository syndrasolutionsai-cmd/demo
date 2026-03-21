# AutoProspect — Script de Demo (4 minutos exactos)

> **Contexto:** Llamada de ventas con un fundador de agencia de marketing en España.
> El workflow ya está importado en n8n y el navegador tiene el dashboard abierto en otra pestaña.
> Tienes la pestaña de n8n visible al iniciar la llamada.

---

## 0:00 — 0:30 · El problema (30 segundos)

*Tono: conversacional, curioso, nada agresivo*

> "Antes de mostrarte nada, cuéntame — **¿cómo conseguís clientes nuevos ahora mismo?**"

*[Dejar que responda. La respuesta habitual es "por referidos" o "boca a boca".]*

> "Exacto. El 90% de las agencias en España funcionan así. El problema es que los referidos no se pueden escalar, no se pueden predecir, y cuando se secan… el pipeline se vacía.
>
> Lo que voy a mostrarte en los próximos 3 minutos es un sistema que encuentra empresas target, analiza sus datos y les escribe emails personalizados con IA, **automáticamente, mientras dormís.**
>
> Se llama AutoProspect. Vamos a ejecutarlo ahora mismo."

---

## 0:30 — 1:30 · Ejecutas el workflow y narras en vivo (60 segundos)

*[Tienes n8n abierto con el workflow. Haz clic en "Execute workflow".]*

> "Le doy a ejecutar..."

*[Los nodos empiezan a iluminarse. Narra mientras ocurre:]*

**Cuando se ilumina el Nodo 2:**
> "Lo primero que hace el sistema es saber quién es vuestra agencia y qué tipo de cliente buscáis. En este caso está configurado para Escala Agency, una agencia de paid media en Madrid que busca tiendas de moda, decoración y cosmética con 5 a 50 empleados."

**Cuando se ilumina el Nodo 3:**
> "Aquí el sistema haría el scraping de Google Maps y LinkedIn. Para la demo tenemos 5 empresas reales del mercado español ya cargadas."

**Cuando se ilumina el Nodo 4-5 (loop ejecutando):**
> "Y ahora viene lo interesante. Para cada empresa, el sistema llama a Claude — la IA de Anthropic — con todos los datos de la empresa: cuántos seguidores tiene en Instagram, si tienen el píxel de Meta instalado, si están gastando en ads o no. Y le pide que escriba un email de outreach personalizado."

*[El loop tardará ~45 segundos. Durante la espera:]*
> "Fijaos que el sistema no escribe el mismo email para todos. Analiza si la empresa tiene infraestructura de ads o no, qué tamaño tiene, cómo es su presencia digital… y elige el ángulo de apertura más efectivo para cada una."

**Cuando el workflow termina (nodo 10 en verde):**
> "Listo. 5 empresas procesadas, 5 emails generados. Abrimos el dashboard."

---

## 1:30 — 3:00 · El dashboard en el navegador (90 segundos)

*[Cambias a la pestaña del navegador con autoprospect_demo.html abierto.
Si aún no lo has abierto, este es el momento — ve a /tmp/autoprospect_demo.html]*

*[Tomarse 5 segundos para que el prospecto asimile el diseño del dashboard.]*

> "Este sería el panel de control que recibiría vuestra agencia cada lunes a las 7 de la mañana."

**Señala las métricas del header:**
> "5 empresas encontradas, 5 emails listos. Y aquí lo importante: **3 de ellas no tienen ads activos** — eso significa que tienen tienda online, tienen audiencia en Instagram, pero no están invirtiendo en paid media. Para vosotros, eso es un cliente que está dejando dinero encima de la mesa y lo sabe."

**Señala la tabla:**
> "Cada empresa tiene su puntuación de oportunidad. Las que no tienen pixel ni ads están al 9/10 — son las más urgentes de contactar."

**Abre el email de Alma Atelier (primera empresa — "Sin ads"):**
*[Haz clic en "Ver email" de Alma Atelier.]*

> "Mirad este email para Alma Atelier, una marca de moda sostenible de Malasaña con 8.400 seguidores en Instagram. El asunto es corto, curioso, no parece spam. Y el cuerpo…"

*[Lee en voz alta las primeras dos líneas del email generado.]*

> "¿Veis? Menciona algo específico de su negocio. No empieza con 'Espero que estés bien'. Es directo. Y termina con una pregunta que invita a responder, no pide una reunión directamente. Así es como escribe una persona real."

**Abre el email de Casa Nórdica (segunda empresa — "Ads bajo presupuesto"):**
*[Haz clic en "Ver email" de Casa Nórdica.]*

> "Aquí el ángulo es distinto. Casa Nórdica sí tiene pixel y sí invierte, pero con menos de 500 euros al mes. La IA lo detecta y cambia el mensaje: no habla de 'empezar con ads', habla de **escalar lo que ya funciona**. Completamente diferente al anterior."

*[Pausa de 3 segundos.]*

> "Esto es lo que hace el sistema: adapta el mensaje a la realidad de cada empresa. No es un template. Son 5 emails distintos para 5 empresas distintas."

---

## 3:00 — 4:00 · ROI y cierre (60 segundos)

*[Vuelves a mirarle a la cara / a la cámara. Tono tranquilo, no de cierre agresivo.]*

> "Pensad en cuánto tiempo os lleva ahora mismo encontrar 5 empresas target, investigarlas una por una y escribirles un email que no parezca spam. ¿Dos horas? ¿Tres?
>
> Este sistema hace eso en 45 segundos, cada semana, sin que nadie lo supervise.
>
> Y lo mejor: esto es la versión demo. En producción, el Nodo 3 no tiene empresas ficticias — tiene un scraper conectado a Google Maps y LinkedIn que encuentra empresas reales según vuestro ICP actualizado."

*[Pausa de 2 segundos.]*

> "La pregunta que me hago cuando veo agencias como la vuestra es: si conseguís un cliente nuevo al mes con referidos, **¿cuántos podrías conseguir con 50 emails personalizados saliendo cada semana?**
>
> ¿Tiene sentido esto para vuestra situación ahora mismo?"

*[Dejar que respondan. La pregunta final es abierta y los invita a reflexionar, no a comprar.]*

---

## Notas para el presentador

### Si el workflow tarda más de 2 minutos:
Explica que en producción se puede paralelizar para procesar 50 empresas a la vez. La demo usa el modelo más potente de Claude para máxima calidad de escritura.

### Si preguntan "¿funciona con nuestro sector?":
> "El ICP es completamente personalizable en el Nodo 2. Lo configuramos con vuestro sector, vuestra ciudad, el tamaño de empresa que buscáis, y las señales de dolor que tenéis identificadas."

### Si preguntan "¿y el scraping es legal?":
> "Usamos datos públicos: Google Maps, perfiles de LinkedIn públicos, webs de empresas. Todo lo que cualquier persona podría buscar manualmente. La diferencia es que lo hacemos a escala."

### Si preguntan "¿cuánto cuesta?":
Derivar a la conversación de propuesta. El sistema AutoProspect se entrega como parte del servicio de implementación, no como producto standalone.

### Objección "ya tenemos un comercial":
> "Perfecto. Imaginad que vuestro comercial llega el lunes con 50 leads ya investigados y con el primer email listo para aprobar. ¿Cuánto más podría cerrar?"

---

## Checklist antes de la demo

- [ ] n8n corriendo en local o servidor con API key configurada
- [ ] Workflow importado y visible en el editor
- [ ] Ejecutar el workflow UNA VEZ antes de la demo para verificar que funciona
- [ ] Archivo `/tmp/autoprospect_demo.html` abierto en Chrome (pestaña lista)
- [ ] Conexión a internet estable (Claude necesita llamadas salientes)
- [ ] Pantalla compartida preparada antes de que empiece la llamada
