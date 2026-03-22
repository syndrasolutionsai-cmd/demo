# AutoContent — Guía de Setup

---

## PASO 1 — Importar el workflow en n8n

1. Abre tu instancia de n8n
2. Panel lateral → **Workflows** → **Add workflow**
3. Menú `...` (arriba derecha del editor) → **Import from file**
4. Selecciona el archivo `autocontent_workflow.json`

> Usa `Ctrl+Shift+H` para centrar el canvas si no ves todos los nodos.

---

## PASO 2 — Configurar la API Key de Anthropic

**Si usas n8n cloud:**

1. Ve a **Settings → Variables** en n8n
2. Crea una variable llamada `N8N_CLAUDE_API_KEY`
3. Como valor, pega tu API Key de Anthropic (empieza por `sk-ant-api03-`)

**Si usas n8n self-hosted:**

1. Abre el archivo `.env` de tu instalación de n8n
2. Añade la línea: `N8N_CLAUDE_API_KEY=sk-ant-api03-XXXXXXXX`
3. Reinicia el servicio n8n

> Obtén tu API Key en [console.anthropic.com](https://console.anthropic.com) → **API Keys** → **Create Key**.
> Asegúrate de tener saldo activo (mínimo $5 de crédito).

---

## PASO 3 — Conectar la credencial al nodo Claude

1. Abre el workflow importado
2. Haz clic sobre el nodo **"🤖 Claude — Genera Contenido"**
3. En el panel derecho → campo **Credential** → selecciona o crea **Header Auth**:
   - **Header name:** `x-api-key`
   - **Header value:** `{{ $env.N8N_CLAUDE_API_KEY }}`
4. Guarda el nodo

---

## PASO 4 — Ejecutar el workflow y generar el HTML

1. En el canvas, haz clic en **"Test workflow"** (▶ naranja, arriba derecha)
2. El workflow ejecutará los nodos en verde uno a uno (20-40 segundos)
3. Al terminar, el nodo final muestra la ruta del archivo generado:
   `~/autocontent_output/plan_semana_[FECHA].html`

---

## PASO 5 — Abrir el HTML generado

1. Abre el explorador de archivos de tu sistema
2. Navega a la carpeta `autocontent_output` en tu directorio de usuario
3. Haz doble clic sobre el archivo `.html` más reciente
4. Se abre directamente en el navegador — no necesita servidor

> **Alternativa rápida:** en la terminal, ejecuta `open ~/autocontent_output/plan_semana_*.html` (Mac/Linux) o arrastra el archivo a Chrome/Firefox.

---

## PASO 6 — Añadir un cliente nuevo al sistema

1. Abre el nodo **"📋 Clientes — Configuración"** en el canvas
2. En el array `clientes`, añade un nuevo objeto con esta estructura:

```json
{
  "nombre": "Nombre del Cliente",
  "sector": "sector del negocio",
  "tono": "cercano | formal | inspiracional | técnico",
  "pilares": ["pilar 1", "pilar 2", "pilar 3"],
  "objetivo": "descripción del objetivo de contenido",
  "redes": ["Instagram", "LinkedIn", "TikTok"]
}
```

3. Guarda el nodo y vuelve a ejecutar el workflow
4. El HTML generado incluirá automáticamente la pestaña del nuevo cliente

---

## PASO 7 — Activar ejecución automática semanal (opcional)

1. Haz clic sobre el nodo trigger **"🚀 Inicio"**
2. Cambia el tipo a **Schedule Trigger**
3. Configura: **Every week · Monday · 07:00**
4. Activa el workflow con el toggle de la esquina superior derecha

---

## Solución de problemas rápida

| Error | Solución |
|-------|----------|
| `401` en nodo Claude | API Key incorrecta o sin saldo — verifica en Anthropic Console |
| `access to env vars denied` | Usa credencial Header Auth en lugar de `$env` directamente |
| HTML no se genera | Verifica permisos de escritura en la carpeta `autocontent_output` |
| Nodo Claude se queda cargando | Timeout de Anthropic — espera 60s o verifica [status.anthropic.com](https://status.anthropic.com) |
