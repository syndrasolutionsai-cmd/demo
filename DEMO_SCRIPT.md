# AutoContent — Script de Demo (4 minutos)
## Para llamadas de ventas con fundadores de agencias de social media en España

> **Antes de la llamada:**
> - Workflow ejecutado al menos 1 vez y HTML generado ✓
> - n8n abierto en el canvas con los nodos visibles ✓
> - HTML abierto en otra pestaña del navegador, en la pestaña de Forja Gym ✓
> - Pantalla compartida lista para activar ✓

---

## [0:00 – 0:30] LA PREGUNTA QUE DUELE

> *Comparte pantalla. Canvas de n8n visible. No ejecutes nada todavía.*
> *Tono: directo, como si llevases años en su sitio.*

---

**"Antes de enseñarte nada, dime una cosa..."**

*[Pausa de 2 segundos]*

**"¿Cuántas horas pierde tu equipo cada semana creando contenido para los clientes? ¿Cuántas veces alguien se queda en blanco delante de un calendario editorial vacío?"**

*[Espera respuesta o continúa]*

**"En la mayoría de agencias de social media, son entre 10 y 15 horas a la semana. Por cliente. Alguien tiene que pensar los temas, adaptar el tono a cada marca, escribir los copies, estructurar el calendario... y al viernes siguiente, a empezar de nuevo desde cero."**

**"Lo que te voy a mostrar genera el plan de contenido completo de una semana, para tres clientes completamente distintos, en menos de 40 segundos."**

---

## [0:30 – 1:30] EJECUTAS EL WORKFLOW

> *Haz clic en "Test workflow" (▶ naranja). Narra mientras los nodos se iluminan.*

---

**"Ejecuto ahora mismo. Cada nodo verde es un paso del proceso."**

*[Haz clic en ejecutar]*

**[Nodo trigger — verde]**
**"Arranca. En producción esto se dispara solo cada lunes a las 7 de la mañana."**

**[Nodo de configuración de clientes — verde]**
**"Aquí carga los perfiles de los clientes: sector, objetivo, pilares de contenido, tono de comunicación... Esta semana tenemos tres: Forja Gym, Legado Notaría y Piel de Luna. Tres negocios que no tienen nada que ver entre sí."**

**[Nodo Claude — verde, tarda 10-15 segundos]**
**"Ahora mismo estamos llamando a Claude, la IA de Anthropic. Le pasamos cada perfil de cliente y le pedimos que genere el plan semanal completo: temas, copies, hashtags, formato para cada red... adapta el tono a cada marca. No es un template. Está generando contenido nuevo desde cero."**

*[Mientras espera:]*
**"Fíjate que no le damos un prompt genérico. Le hemos enseñado a pensar como el account manager de cada cliente."**

**[Nodos de construcción y exportación — verde]**
**"Monta el HTML con el calendario visual, organiza las 42 piezas por cliente y por día... y exporta el archivo listo para usar."**

**[Nodo final — verde]**
**"¿Cuánto ha tardado?"**

*[Mira el tiempo — unos 30-35 segundos]*
**"Treinta y pocos segundos. 42 piezas de contenido. Tres clientes. Vamos a verlo."**

---

## [1:30 – 3:00] NAVEGAS POR EL HTML

> *Cambia a la pestaña del navegador con el HTML abierto.*
> *Desplázate lentamente. Deja que el diseño hable.*

---

**"Este es el entregable. Un HTML que se abre directamente en el navegador, sin servidor, sin login."**

*[Muestra la estructura general: pestañas de los 3 clientes en la parte superior]*

**"Tres pestañas, un cliente cada una. Empezamos por Forja Gym."**

*[Haz clic en la pestaña de Forja Gym]*

**"Gimnasio. Comunidad. Energía. ¿Ves cómo suena esto?"**

*[Lee en voz alta 2-3 copies del calendario — los más potentes, con emojis, lenguaje motivacional]*

**"Directo, con punch, con emojis. El lenguaje de alguien que entrena."**

*[Haz clic en la pestaña de Legado Notaría]*

**"Mismo sistema. Cliente completamente diferente."**

*[Lee 2-3 copies — formales, sin emojis, lenguaje de autoridad y confianza]*

**"¿Notas la diferencia? No hay un solo emoji. El tono es de experto, de institución. Es lo que necesita una notaría para generar confianza."**

*[Haz clic en la pestaña de Piel de Luna]*

**"Y aquí... Piel de Luna. Cosmética natural."**

*[Lee 2-3 copies — sensorial, evocador, femenino, cuidadoso]*

**"Completamente distinto. Poético, sensorial. El mismo sistema, tres voces que no se parecen en nada."**

*[Haz clic en el botón "Copiar" de cualquier pieza de contenido]*

**"Y esto es lo que le encanta al equipo: botón de copiar en cada pieza. Un clic y está en el portapapeles, listo para pegar en Metricool, en Buffer, en el grupo de WhatsApp del cliente... donde sea."**

**"El equipo no tiene que escribir nada. Solo revisar, ajustar si quieren, y publicar."**

---

## [3:00 – 4:00] EL ROI Y EL CIERRE

> *Vuelve a cámara o pantalla neutra. Tono más pausado.*

---

**"Vamos a hacer los números un momento."**

**"Si tu equipo dedica 11 horas y media a la semana en crear contenido para los clientes — y esa es la media real que hemos medido — y una hora de trabajo en tu agencia vale 25€... son casi 290€ a la semana. Más de 1.100€ al mes. Solo en producción de contenido."**

**"¿Cuánto cuesta AutoContent en API? Menos de 5 céntimos por cliente y semana."**

**"Pero más allá del coste: cuando tu equipo no está atascado generando contenido desde cero, está cerrando nuevos clientes, está mejorando las estrategias, está haciendo el trabajo que realmente diferencia a tu agencia."**

**"Y tus clientes reciben su plan cada lunes. Sin retrasos. Sin 'lo tenemos casi listo'. Eso también retiene clientes."**

*[Pausa de 2 segundos]*

**"La pregunta que me hago yo es..."**

**"¿Cuántos clientes tienes ahora mismo en los que el contenido va con retraso porque el equipo no da abasto?"**

*[Espera respuesta — escucha]*

**"Podemos configurar AutoContent para tu agencia con tus clientes reales en una tarde. Con sus voces, sus pilares, sus redes. ¿Qué hueco tienes esta semana para montar la primera versión?"**

---

## Si algo falla en directo

**Si el workflow no ejecuta:**
> *"Déjame reiniciarlo, a veces la primera llamada a la API tarda un poco más..."*
> Vuelve a ejecutar. Si falla de nuevo: *"Perfecto, te mando la grabación de la demo y lo ves al 100% — mientras tanto hablamos del ROI para tu agencia específicamente."*

**Si el cliente pregunta "¿se puede conectar a nuestras herramientas?":**
> *"Sí. n8n tiene conectores nativos para Notion, Airtable, Google Drive, Slack, WhatsApp Business... El calendario se puede exportar directamente donde trabaje tu equipo."*

**Si el cliente pregunta "¿mis clientes necesitan tener perfil de empresa claro?":**
> *"Cuanto mejor definido está el perfil, mejor el resultado. Con 10 minutos rellenando la ficha de cada cliente — sector, tono, tres pilares de contenido — el sistema ya genera algo usable. Y mejora con cada semana."*

**Si el cliente pregunta "¿necesito saber programar?":**
> *"Cero líneas de código. Si sabes usar Gmail, sabes usar esto. Y si quieres añadir algo nuevo, en una tarde lo montamos."*

---

## Checklist Pre-Demo

- [ ] Workflow ejecutado y HTML generado (archivo `.html` en `autocontent_output`)
- [ ] HTML abierto en el navegador, pestaña Forja Gym activa
- [ ] n8n en canvas con workflow visible y centrado (`Ctrl+Shift+H`)
- [ ] Botón "copiar" probado — confirmar que funciona en tu navegador
- [ ] Notificaciones del sistema silenciadas
- [ ] Cronómetro preparado
