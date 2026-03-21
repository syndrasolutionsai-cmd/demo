# AutoReport — Script de Demo (4 minutos)
## Para llamadas de ventas con fundadores de agencias en España

> **Antes de la llamada:**
> - Workflow importado y probado al menos 1 vez ✓
> - n8n abierto en el canvas del workflow (nodo "Iniciar Demo" visible) ✓
> - Gmail abierto en otra pestaña para mostrar el email en tiempo real ✓
> - Pantalla compartida lista para activar al empezar ✓
> - Cronómetro preparado (o cuenta mentalmente: cada bloque es aprox. 30-60s) ✓

---

## [0:00 – 0:30] EL PROBLEMA (sin ejecutar nada todavía)

> *Comparte pantalla. Muestra el canvas de n8n pero NO ejecutes nada aún.*
> *Tono: cercano, directo, como si conocieras su dolor de primera mano.*

---

**"Antes de enseñarte algo, déjame preguntarte una cosa..."**

*[Pausa de 2 segundos]*

**"¿Cuántas horas pierde tu equipo cada semana preparando los reportes para los clientes? ¿Dos horas? ¿Cuatro? ¿Más?"**

*[Espera respuesta o continúa si es grabación]*

**"En agencias como la tuya, la media son entre 15 y 20 horas a la semana. Solo en reportes. Alguien tiene que entrar en Google Ads, copiar métricas, entrar en Meta, copiar más métricas, abrir el PowerPoint o el Google Slides, cuadrar los números, escribir el análisis, formatearlo, mandarlo... y al lunes siguiente, a empezar de nuevo."**

**"Lo que te voy a mostrar ahora mismo hace todo eso en menos de 30 segundos. Sin que nadie lo toque."**

---

## [0:30 – 2:00] EJECUTAS EL WORKFLOW (nodo a nodo)

> *Haz clic en "Test workflow" o en el botón ▶ del nodo "🚀 Iniciar Demo".*
> *Narra en tiempo real mientras los nodos se iluminan en verde.*

---

**"Voy a darle a ejecutar ahora mismo. ¿Ves estos nodos? Cada uno es un paso del proceso."**

*[Haz clic en ejecutar]*

**[Nodo 1 — Trigger se ilumina en verde]**
**"Arrancamos. Esto en producción se dispara automáticamente cada lunes a las 8 de la mañana. Sin que nadie lo recuerde, sin que nadie lo olvide."**

**[Nodo 2 — Datos del Cliente se ilumina]**
**"Aquí el sistema carga los datos del cliente. En producción, esta información viene directamente de la API de Google Ads y Meta Ads, en tiempo real. Para la demo, tenemos cargados los datos reales de una clínica dental ficticia, Clínica Dental Sonrisas: Google Ads, Meta Ads, gasto, pacientes captados, coste por paciente... todo."**

*[Si tienes tiempo, haz clic en el nodo para mostrar los datos en el panel derecho]*

**[Nodo 3 — Claude API se ilumina — este tarda 5-10 segundos]**
**"Ahora mismo... estamos llamando a Claude, la inteligencia artificial de Anthropic. Le estamos pasando todos los datos y le estamos pidiendo que escriba el resumen semanal como si fuera el account manager de la agencia. Sin tecnicismos. En el idioma del cliente."**

*[Espera que termine — aprovecha para decir:]*
**"Fíjate que esto no es un template con variables. Claude está analizando los números, comparándolos con la semana anterior, viendo si están en ritmo con el objetivo mensual... y escribiendo un texto completamente nuevo. Como lo haría una persona."**

**[Nodo 4 — Construye HTML se ilumina]**
**"Ya tenemos el análisis. Ahora montamos el email: cabecera con el logo de la agencia, tarjetas con las métricas de Google y Meta, una barra de progreso visual del objetivo del mes, el texto de Claude... Un email que parece que lo ha preparado el equipo durante dos horas."**

**[Nodo 5 — Gmail se ilumina]**
**"Y aquí... lo enviamos. Directamente al cliente. O a quien la agencia decida: puede ir al cliente, al director de la clínica, al gerente..."**

**[Nodo 6 — Airtable se ilumina]**
**"Aquí registramos el envío en la base de datos: qué cliente, qué fecha, qué métricas. Para el historial de la agencia y para los informes internos."**

**[Nodo 7 — Confirmación Final se ilumina en verde]**
**"¿Ves el check verde? Reporte generado y enviado. ¿Cuánto tiempo ha pasado desde que pulsé ejecutar?"**

*[Mira el tiempo — normalmente 20-30 segundos]*
**"Menos de 30 segundos."**

---

## [2:00 – 3:00] MUESTRAS EL EMAIL EN TIEMPO REAL

> *Cambia a la pestaña de Gmail. Refresca la bandeja de entrada.*
> *El email tiene que estar ahí. Si tarda, di: "Gmail tarda unos segundos en entregarlo..."*

---

**"Vamos a ver qué ha recibido el cliente."**

*[Abre el email — muestra el asunto primero]*

**"Mira el asunto: '📊 Reporte Semanal | Clínica Dental Sonrisas | Semana 10-16 Mar'. Limpio, profesional."**

*[Abre el email y desplázate lentamente por el diseño]*

**"Header con el nombre de la agencia. Nombre del cliente. Fecha del reporte."**

**"Las dos tarjetas de métricas: Google Ads a la izquierda, Meta Ads a la derecha. ¿Ves los triángulos verdes? Indican mejora respecto a la semana anterior. Si hubiera bajado algo, aparecería en rojo. El cliente entiende de un vistazo si va bien o mal."**

**"La barra de progreso del objetivo mensual. Este cliente quiere 80 pacientes nuevos en marzo. Van en el 51% del objetivo con el 51% del mes transcurrido. Perfecto ritmo."**

*[Desplázate hasta el análisis de Claude]*

**"Y aquí está lo que ha escrito Claude. Léete esto..."**

*[Lee en voz alta 3-4 líneas del resumen, las más específicas con datos]*

**"¿Te das cuenta? No dice 'el CTR fue del 3.91%'. Dice 'esta semana captamos 23 pacientes nuevos desde Google y 18 desde redes sociales'. Lo mismo, pero en el idioma de un dentista."**

**"Este email lo puede entender el propietario de la clínica. Sin necesitar que nadie le explique nada."**

---

## [3:00 – 4:00] EL ROI Y LA PREGUNTA DE CIERRE

> *Vuelve a tu cámara o a la presentación. Tono más pausado, más directo.*

---

**"Ahora vamos a hacer los números juntos un momento."**

**"Si tu equipo dedica 15 horas a la semana a hacer reportes, y una hora de trabajo en tu agencia vale 30€ conservadoramente... son 450€ a la semana. 1.800€ al mes. 21.600€ al año. Solo en reportes."**

**"¿Cuánto cuesta AutoReport? El coste de IA por reporte es de menos de 2 céntimos. Para 20 clientes semanales, son menos de 2 euros a la semana."**

**"Pero hay algo que va más allá del coste. Cuando los reportes llegan el lunes a las 8 de la mañana, sin fallar, sin retrasos, bien presentados... los clientes perciben a tu agencia diferente. Más profesional. Más grande. Y eso se traduce en retención."**

**"La pregunta no es si esto tiene sentido. La pregunta es..."**

*[Pausa de 2 segundos]*

**"¿Cuántos de tus clientes actuales llevan más de tres meses sin recibir un reporte bien hecho porque el equipo no da abasto?"**

*[Espera respuesta — escucha]*

**"Podemos tener esto configurado para tu agencia en una tarde. Con tus colores, tus datos reales de Google Ads y Meta Ads, y enviando a tus clientes. ¿Cuándo tienes 90 minutos esta semana para montar la primera versión?"**

---

## Notas para el Demo

### Si el workflow falla en directo:
- Mantén la calma. Di: **"Déjame reiniciarlo, a veces la primera ejecución tarda un poco más..."**
- Vuelve a ejecutar. Casi siempre funciona al segundo intento.
- Si falla de nuevo: **"Perfecto, esto me permite enseñarte cómo funciona la gestión de errores... pero mejor te mando la grabación de la demo para que lo veas al 100%."** Pasa a hablar del ROI directamente.

### Si el cliente pregunta "¿esto es solo para reportes?":
**"No, esto es la punta del iceberg. El mismo sistema puede generar propuestas de presupuesto, alertas cuando una campaña baja de rendimiento, resúmenes para reuniones de estrategia... Empezamos con reportes porque es donde más tiempo se pierde, pero el framework sirve para automatizar cualquier proceso repetitivo de la agencia."**

### Si el cliente pregunta "¿necesito saber programar?":
**"Cero. Si sabes usar Gmail y sabes copiar-pegar, sabes usar n8n. Y si en algún momento quieres añadir algo nuevo, en una tarde te lo montamos. No hay código."**

### Si el cliente pregunta "¿y los datos de mis clientes están seguros?":
**"Todo corre en tu propio servidor o en tu cuenta privada de n8n. Los datos no pasan por ningún intermediario. La IA de Anthropic recibe los números —igual que cuando los pegas en ChatGPT para que te ayude a escribir— pero no los almacena para entrenamiento si usas la API con la configuración estándar."**

---

## Checklist Pre-Demo

- [ ] Workflow ejecutado al menos 1 vez antes de la llamada (para verificar que todo funciona)
- [ ] Email de prueba recibido en bandeja de entrada (no en spam)
- [ ] n8n en modo canvas con workflow visible y nodo "Iniciar Demo" centrado en pantalla
- [ ] Gmail abierto en segunda pestaña, bandeja de entrada vacía o visible
- [ ] Cronómetro preparado (recomendado: reloj del teléfono)
- [ ] Micrófono testeado, cámara encendida
- [ ] Notificaciones del sistema silenciadas
