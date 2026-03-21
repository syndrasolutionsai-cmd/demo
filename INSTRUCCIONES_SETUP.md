# AutoProspect Demo — Instrucciones de Setup

## Requisitos previos

- n8n instalado (self-hosted v1.x o superior) — [docs.n8n.io](https://docs.n8n.io)
- API Key de Anthropic Claude — [console.anthropic.com](https://console.anthropic.com)
- Navegador Chrome o Firefox

---

## Paso 1 — Configurar la variable de entorno de Claude

La API key de Claude debe estar disponible como variable de entorno en n8n.

### Si usas n8n con Docker:

```bash
docker run -d \
  --name n8n \
  -p 5678:5678 \
  -e N8N_CLAUDE_API_KEY=sk-ant-api03-TU_API_KEY_AQUI \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

### Si usas n8n con npm (local):

**En Linux/Mac** — añade al archivo `~/.bashrc` o `~/.zshrc`:
```bash
export N8N_CLAUDE_API_KEY="sk-ant-api03-TU_API_KEY_AQUI"
```
Luego ejecuta: `source ~/.bashrc && n8n start`

**En Windows** — desde PowerShell:
```powershell
$env:N8N_CLAUDE_API_KEY = "sk-ant-api03-TU_API_KEY_AQUI"
n8n start
```

### Si usas n8n Cloud:

Ve a **Settings → Variables** y crea:
- Nombre: `N8N_CLAUDE_API_KEY`
- Valor: tu API key de Anthropic

> ⚠️ **Importante:** La API key debe empezar por `sk-ant-api03-...`
> La obtienes en [console.anthropic.com/settings/api-keys](https://console.anthropic.com/settings/api-keys)

---

## Paso 2 — Importar el workflow en n8n

1. Abre n8n en tu navegador (por defecto: `http://localhost:5678`)
2. En el menú lateral, haz clic en **Workflows**
3. Haz clic en el botón **+ New** (esquina superior derecha)
4. En el editor de workflow, haz clic en el menú de los **tres puntos** (⋯) o en **Import**
5. Selecciona **Import from file**
6. Navega hasta el archivo `autoprospect_n8n_workflow.json` y selecciónalo
7. El workflow se importará con todos los nodos en su posición correcta

**Alternativa (copiar/pegar):**
1. Abre el archivo `autoprospect_n8n_workflow.json` con cualquier editor de texto
2. Copia todo el contenido (Ctrl+A → Ctrl+C)
3. En n8n, en el editor de workflow: **⋯ → Import from clipboard**

---

## Paso 3 — Verificar la configuración

Una vez importado, verifica que:

**Nodo 05 · Generar Email con Claude:**
- Haz doble clic en el nodo
- Confirma que la URL es `https://api.anthropic.com/v1/messages`
- Confirma que el header `x-api-key` tiene el valor `={{ $env.N8N_CLAUDE_API_KEY }}`

**Si prefieres poner la API key directamente (sin variable de entorno):**
- En el nodo 05, cambia el valor del header `x-api-key` de:
  `={{ $env.N8N_CLAUDE_API_KEY }}`
  a:
  `sk-ant-api03-TU_API_KEY_DIRECTA`

---

## Paso 4 — Ejecutar el workflow

1. Haz clic en el botón **Test workflow** (triángulo ▶ en la esquina inferior derecha)
   — o —
   Haz clic en el nodo **01 · Inicio — Manual Trigger** y luego en **Execute step**
2. Observa cómo los nodos se van ejecutando uno a uno (se iluminan en verde)
3. El workflow tardará entre **30-60 segundos** (5 llamadas a Claude en loop)
4. Al finalizar, el nodo 10 mostrará el resumen de ejecución

> **Duración esperada:** ~45 segundos para 5 prospectos

---

## Paso 5 — Encontrar y abrir el archivo HTML

El dashboard HTML se guarda automáticamente en:
```
/tmp/autoprospect_demo.html
```

### Cómo acceder al archivo:

**Si n8n corre en tu máquina local:**
- Abre el explorador de archivos y navega a `/tmp/`
- Haz doble clic en `autoprospect_demo.html`
- Se abrirá directamente en Chrome/Firefox

**Si n8n corre en Docker:**
```bash
# Copiar el archivo del contenedor a tu máquina
docker cp n8n:/tmp/autoprospect_demo.html ~/Desktop/autoprospect_demo.html
```
Luego abre el archivo desde tu escritorio.

**Si n8n corre en un servidor remoto (VPS):**
```bash
# Descargar con scp
scp usuario@tu-servidor:/tmp/autoprospect_demo.html ~/Desktop/
```

**Alternativa — ver el HTML desde n8n:**
- Haz clic en el nodo **08 · Construir Dashboard HTML**
- En el panel de output, busca el campo `binary.data`
- Haz clic en el icono de descarga para guardar el HTML

---

## Solución de problemas frecuentes

| Problema | Causa | Solución |
|----------|-------|----------|
| Error 401 en Claude | API key inválida o no configurada | Verifica `N8N_CLAUDE_API_KEY` |
| Error 429 en Claude | Rate limit alcanzado | Espera 1 minuto y vuelve a ejecutar |
| HTML vacío | Error en nodo 07 (Aggregate) | Revisa que el nodo 06 devuelve datos |
| Loop infinito | Nodo 04 no cierra el loop | Verifica la conexión loop-back del nodo 06 al 04 |
| `$env` undefined | n8n no detecta la variable | Reinicia n8n tras añadir la variable de entorno |

---

## Estructura del workflow — mapa visual

```
[01 Trigger] → [02 Config Agencia] → [03 Lista Prospectos (5 items)]
                                              ↓
                                    [04 Loop por Empresa] ←────────────┐
                                      │ output[0]                      │
                                      ↓                                │
                              [05 Claude API]                          │
                                      ↓                                │
                              [06 Parsear + Score] ─────────────────────┘

                                    [04 Loop por Empresa]
                                      │ output[1] (done — cuando termina el loop)
                                      ↓
                              [07 Consolidar (Aggregate)]
                                      ↓
                              [08 Construir HTML]
                                      ↓
                              [09 Guardar /tmp/autoprospect_demo.html]
                                      ↓
                              [10 Resumen Final]
```

---

## Modelos de Claude compatibles

El workflow usa `claude-opus-4-6` por defecto (mejor calidad de escritura).
Para reducir costes en pruebas, puedes cambiar a `claude-haiku-4-5-20251001` en el nodo 05.

**Coste estimado por ejecución completa (5 prospectos):**
- claude-opus-4-6: ~$0.08 USD
- claude-haiku-4-5-20251001: ~$0.002 USD
