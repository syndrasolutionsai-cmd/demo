# AutoNurture — Instrucciones de Setup
> Tiempo estimado: **10 minutos**. Una vez configurado, la demo corre en menos de 30 segundos.

---

## PASO 1 — Importar el workflow en n8n

1. Abre tu instancia de n8n (cloud o self-hosted)
2. Panel lateral izquierdo → **Workflows** → botón **"Add workflow"**
3. Menú de tres puntos `...` (arriba a la derecha del editor) → **"Import from file"**
4. Sube el archivo `autonurture_workflow.json`
5. El workflow aparece con todos los nodos conectados

> **¿No ves todos los nodos?** Pulsa `Ctrl+Shift+H` (o `Cmd+Shift+H` en Mac) para centrar el canvas.

---

## PASO 2 — Configurar la API Key de Claude

1. En n8n, ve al menú lateral → **Credentials** → **"Add credential"**
2. Busca y selecciona **"Header Auth"**
3. Rellena los campos:
   - **Name** (nombre de la credencial): `Anthropic Claude API`
   - **Name** (nombre del header): `x-api-key`
   - **Value**: tu API key de Anthropic (empieza por `sk-ant-api03-`)
4. Haz clic en **"Save"**
5. En el workflow, haz clic sobre el nodo **"🤖 Claude — Genera Mensaje"** y selecciona esta credencial en el campo **"Credential"**

> Obtén tu API key en [console.anthropic.com](https://console.anthropic.com) → API Keys → Create Key. Necesitas mínimo $5 de saldo.

---

## PASO 3 — Ejecutar el workflow y localizar el HTML

1. En el canvas, haz clic en **"Test workflow"** (botón ▶ naranja, arriba a la derecha)
2. Los nodos se iluminan en verde uno por uno (20-30 segundos en total)
3. Al terminar, haz clic en el nodo final **"💾 Genera Dashboard HTML"**
4. En el panel derecho, copia la ruta del archivo generado — algo como `/tmp/autonurture_dashboard.html`
5. Abre esa ruta en tu navegador (arrastra el archivo o escribe la ruta en la barra de direcciones)

---

## PASO 4 — Añadir un lead nuevo al sistema

1. En el workflow, haz clic sobre el nodo **"📋 Leads — Base de Datos"**
2. En el panel derecho verás el array JSON con los 6 leads de demo
3. Añade un objeto nuevo al array con esta estructura:
```json
{
  "nombre": "Nombre Apellido",
  "empresa": "Nombre de la Empresa",
  "sector": "Sector",
  "temperatura": "caliente|tibio|frío",
  "dias_silencio": 14,
  "valor_estimado": 1500,
  "historial": "Descripción breve del historial del lead y dónde se quedó"
}
```
4. Guarda el nodo y vuelve a ejecutar el workflow

---

## PASO 5 — Cambiar el nombre de la agencia

1. Haz clic sobre el nodo **"⚙️ Configuración"** (el primero del workflow)
2. En el panel derecho, localiza el campo `nombre_agencia`
3. Reemplaza el valor por el nombre de tu agencia
4. Guarda el nodo — el nombre aparecerá automáticamente en el dashboard y en todos los mensajes generados

---

## PASO 6 — Activar seguimiento automático de 45 días

1. Haz clic sobre el nodo trigger **"🚀 Iniciar AutoNurture"**
2. Haz clic en **"Change trigger"** → selecciona **"Schedule Trigger"**
3. Configura: **Every Day** a las **9:00** (o el horario que prefieras)
4. Activa el workflow con el toggle **"Active"** (esquina superior derecha del canvas)

> A partir de ahora el sistema analiza y actualiza los leads cada día de forma autónoma durante 45 días sin intervención humana.

---

## PASO 7 — Checklist antes de la demo

- [ ] Workflow ejecutado al menos 1 vez y todos los nodos en verde
- [ ] HTML del dashboard abierto en el navegador y visible
- [ ] n8n en el canvas con el workflow centrado en pantalla
- [ ] Notificaciones del sistema silenciadas
- [ ] Pantalla compartida lista para activar
