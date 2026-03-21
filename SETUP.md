# AutoReport Demo — Guía de Setup Completa

> Tiempo estimado de configuración: **10-15 minutos**
> Una vez configurado, la demo se ejecuta en menos de 30 segundos.

---

## Prerequisitos

- n8n instalado (cloud en [app.n8n.cloud](https://app.n8n.cloud) o self-hosted)
- Cuenta de Google con Gmail activo
- API Key de Anthropic ([console.anthropic.com](https://console.anthropic.com))

---

## PASO 1 — Importar el Workflow en n8n

1. Abre tu instancia de n8n
2. En el panel lateral izquierdo, haz clic en **"Workflows"**
3. Haz clic en el botón **"Add workflow"** (esquina superior derecha)
4. En el menú de opciones (tres puntos `...` arriba a la derecha del editor), selecciona **"Import from file"**
5. Sube el archivo `autoreport_workflow.json`
6. El workflow aparecerá con los 7 nodos conectados en cadena

> **¿No ves todos los nodos?** Usa `Ctrl+Shift+H` (o `Cmd+Shift+H` en Mac) para centrar el canvas y ver todos los nodos.

---

## PASO 2 — Crear la Credencial de Anthropic en n8n

> n8n bloquea el acceso a variables de entorno (`$env`) en nodos HTTP Request por seguridad.
> La API key se guarda como **credencial cifrada** en n8n. Así es como se hace:

### 2a — Obtener tu API Key de Anthropic
1. Ve a [console.anthropic.com](https://console.anthropic.com)
2. Navega a **API Keys** en el menú lateral
3. Haz clic en **"Create Key"**
4. Copia la key (empieza por `sk-ant-api03-`)
5. ⚠️ Asegúrate de tener saldo o un plan activo (mínimo $5 de crédito)

### 2b — Crear la credencial "Header Auth" en n8n
1. En n8n, ve al menú lateral → **Credentials**
2. Haz clic en **"Add credential"**
3. Busca y selecciona **"Header Auth"**
4. Rellena los campos:
   - **Name** (nombre de la credencial): `Anthropic API Key (x-api-key)`
   - **Name** (nombre del header): `x-api-key`
   - **Value**: `sk-ant-api03-XXXXXXXXXXXXXXXX` ← tu API key real
5. Haz clic en **"Save"**

### 2c — Conectar la credencial al nodo Claude
1. Abre el workflow importado
2. Haz clic sobre el nodo **"🤖 Claude AI — Genera Resumen"**
3. En el panel derecho, campo **"Credential"**, selecciona la credencial recién creada: `Anthropic API Key (x-api-key)`
4. Guarda el nodo

### 2d — Configurar tu email en el nodo Gmail
1. Haz clic sobre el nodo **"📨 Gmail — Envía Reporte"**
2. En el campo **"To"**, reemplaza `TU_EMAIL@gmail.com` con tu email real
3. Guarda el nodo

---

## PASO 3 — Conectar Gmail en n8n

El nodo **"Gmail — Envía Reporte"** necesita autenticación OAuth2 con Google.

1. **Haz clic** sobre el nodo de Gmail en el canvas
2. En el panel derecho, en el campo **"Credential"**, haz clic en **"Create new credential"**
3. Se abrirá un popup — haz clic en **"Sign in with Google"**
4. Selecciona la cuenta de Gmail donde quieres recibir los reportes
5. Google pedirá permisos — acepta todos (enviar emails en tu nombre)
6. Verás el mensaje **"Account connected"** — cierra el popup

> **Alternativa si no tienes Gmail:** Cambia el nodo Gmail por un nodo **"Send Email"** usando SMTP (con Brevo, Resend o cualquier proveedor SMTP).

---

## PASO 4 — Verificar los Nodos

Antes de ejecutar, comprueba que:

- [ ] **Nodo Claude API**: Campo "Credential" muestra `Anthropic API Key (x-api-key)` (credencial Header Auth)
- [ ] **Nodo Gmail**: Muestra tu cuenta de Gmail conectada (OAuth2)
- [ ] **Nodo Gmail → To**: Tiene tu email real (no `TU_EMAIL@gmail.com`)

---

## PASO 5 — Ejecutar la Demo

1. En el canvas del workflow, haz clic en el botón **"Test workflow"** (triángulo ▶ naranja, arriba a la derecha)
2. Alternativamente, haz clic directamente sobre el nodo **"🚀 Iniciar Demo"** y luego en **"Execute node"**
3. Observa cómo los nodos se iluminan en verde uno por uno (cada nodo tarda 1-5 segundos)
4. En **20-30 segundos**, recibirás el email en tu bandeja de entrada

> **¿El workflow se detiene en el nodo de Claude?** Verifica que la API Key es válida y tiene saldo. Puedes testear en [console.anthropic.com/workbench](https://console.anthropic.com/workbench).

---

## PASO 6 (Opcional) — Activar Ejecución Automática Semanal

Para que el reporte se envíe automáticamente cada lunes a las 8:00h:

1. Haz clic sobre el nodo **"🚀 Iniciar Demo"**
2. En el panel derecho, haz clic en **"Change trigger"**
3. Selecciona **"Schedule Trigger"**
4. Configura:
   - **Trigger interval**: Week
   - **Weekday**: Monday
   - **Hour**: 8
   - **Minute**: 0
5. Haz clic en **"Activate workflow"** (toggle en la esquina superior derecha del canvas)

---

## Estructura del Workflow

```
🚀 Iniciar Demo
    ↓
📊 Datos del Cliente     ← Datos ficticios de Momentum Digital / Clínica Dental
    ↓
🤖 Claude AI            ← Llama a claude-opus-4-5 vía HTTP Request
    ↓
📧 Construye HTML        ← Genera el email HTML con métricas + análisis de Claude
    ↓
📨 Gmail                 ← Envía el reporte por email
    ↓
🗄️ Registro Airtable    ← Simula el log en base de datos (objeto JSON)
    ↓
✅ Confirmación Final    ← Mensaje de éxito con timestamp
```

---

## Solución de Problemas Frecuentes

| Error | Causa | Solución |
|-------|-------|----------|
| `401 Unauthorized` en Claude | API Key incorrecta en la credencial | Edita la credencial "Anthropic API Key" en n8n Credentials y verifica el valor |
| `access to env vars denied` | n8n bloquea `$env` en nodos HTTP | Asegúrate de usar credencial Header Auth, no `$env` (ya corregido en v2 del JSON) |
| `400 Bad Request` en Gmail | Credencial de Gmail no conectada | Reconecta la cuenta en el nodo Gmail |
| Email no llega | Variable `DEMO_EMAIL` vacía | Verifica que la variable está guardada y es un email válido |
| Nodo se queda cargando | Timeout de la API de Anthropic | Espera 60s o verifica el estado en [status.anthropic.com](https://status.anthropic.com) |
| Variables no disponibles | n8n no reiniciado tras editar `.env` | Reinicia el servicio n8n si es self-hosted |

---

## Costes Estimados

| Componente | Coste por reporte |
|-----------|-------------------|
| Claude API (claude-opus-4-5, ~800 tokens) | ~$0.012 |
| Gmail API | Gratuito |
| n8n Cloud (plan Starter) | Incluido en plan |
| **Total por reporte** | **< $0.02** |

Para una agencia con 20 clientes enviando reportes semanales:
- **Coste tecnológico**: ~$1.60/semana (~$83/año)
- **Horas ahorradas**: 15-20h/semana × $30/h = **$450-600/semana en valor**
