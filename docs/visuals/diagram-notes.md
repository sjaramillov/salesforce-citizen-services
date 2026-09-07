# Notas de arquitectura visual

Proyecto independiente `salesforce-citizen-services`, presentado como **Servicios ciudadanos**. Salesforce identifica la tecnología y el marco de arquitectura utilizado; no se afirma patrocinio, afiliación, certificación ni un cliente desplegado.

Los dos diagramas son SVG editables de 1800 × 1200: texto, formas y conectores permanecen vectoriales. Utilizan Arial con alternativas sans-serif y no contienen logos, imágenes incrustadas, recursos remotos ni identificadores operativos. Fecha de revisión técnica y consulta de fuentes: **2026-09-07**.

## Arquitectura de solución

`solution-architecture.svg` separa dos vistas. La primera muestra artefactos disponibles en el repositorio: el LWC trabaja con constantes ficticias; AgentScript conserva instrucciones como referencia; las tres APIs son contratos y solo System tiene un flujo preliminar. No hay flechas que los presenten como una integración local completa.

La segunda vista describe un **piloto propuesto**. Todas sus conexiones son discontinuas. El ciudadano accede a un portal Experience Cloud/LWC, la identidad y autorización se comprueban antes de recuperar un caso, y Agentforce recibe contenido aprobado para orientar. La cadena de consulta conserva las responsabilidades documentadas:

| Capa | Responsabilidad prevista | Consumidor |
|---|---|---|
| Experience API | Mensaje útil y datos mínimos adecuados al canal | Portal o acción del agente |
| Process API | Reglas reutilizables y siguiente paso | Experience API |
| System API | Consulta del registro mediante un contrato estable | Process API |

El sistema legacy es un destino autorizado aún por integrar; su adaptador es reemplazable. La propuesta de escritura se desprende de Process, pide confirmación explícita y necesita una acción nueva, estados e idempotencia. La solicitud puede almacenarse como Case o como borrador según el diseño final; el gráfico no implica que esa elección esté cerrada. La revisión humana registra una decisión y su resultado. Las piezas de escritura y revisión aparecen en coral para hacer visible que siguen pendientes.

Las flechas comunican dependencias y recorrido funcional, no un protocolo detallado de petición/respuesta. Se omiten respuestas de retorno para conservar legibilidad. Autorización en código, gestión de errores y auditoría se muestran como obligaciones transversales **propuestas**, no como políticas aplicadas. El número de caso y las instrucciones del modelo no sustituyen controles de acceso.

La observación del portal público mostró primero preparación y después un mensaje de error en la misma sesión. No se vio el portal ciudadano; su operación no quedó confirmada y la causa no se estableció. El diagrama no deduce una indisponibilidad permanente ni atribuye el error a un componente. Véase [estado de evidencia](../evidence/status.md) y [registro de observación](../evidence/public-portal-check.json).

Base local: [arquitectura](../architecture.md), [capas API](../base/api-layering.md), [piloto](../pilot.md) y [estado de evidencia](../evidence/status.md). La selección de licencias, acciones, herramientas, objetos y versiones del destino sigue pendiente.

## Salesforce Well-Architected

`well-architected.svg` aplica cualitativamente el marco publicado en Salesforce Architects. La estructura consultada contiene **tres capacidades y ocho comportamientos**. Se conservan los nombres oficiales en inglés; las traducciones al español son de trabajo. [Visión general oficial](https://architect.salesforce.com/docs/architect/well-architected/guide/overview.html).

| Capacidad | Traducción de trabajo | Comportamientos del marco |
|---|---|---|
| Trusted | Confiable | Secure, Compliant, Reliable |
| Easy | Sencilla | Intentional, Automated, Engaging |
| Adaptable | Adaptable | Resilient, Composable |

**Confiable.** El gráfico distingue seguridad, conformidad legal/ética y funcionamiento fiable. Sus criterios corresponden a seguridad de organización, sesión y datos; obligaciones legales, ética y accesibilidad; y disponibilidad, rendimiento y escalabilidad. Datos ficticios y contratos acotados son evidencia del alcance de la demostración: no prueban autorización efectiva ni conformidad de un servicio. [Trusted](https://architect.salesforce.com/docs/architect/well-architected/guide/trusted-overview.html).

**Sencilla.** Se refiere al valor entregado y a una solución que las personas puedan usar y mantener. El gráfico relaciona intención con estrategia, mantenibilidad y legibilidad; automatización con eficiencia e integridad de datos; y una experiencia atractiva con simplificación y ayuda. La palabra «atractiva» traduce una experiencia que facilita adopción, no solamente apariencia. El LWC y la guía de piloto son el punto de partida; la usabilidad y accesibilidad deben comprobarse. [Easy](https://architect.salesforce.com/docs/architect/well-architected/guide/easy-overview.html).

**Adaptable.** Resiliencia comprende ciclo de vida, respuesta a incidentes y continuidad. Composición comprende separación de responsabilidades, interoperabilidad y capacidad de empaquetar componentes. Los contratos separados apoyan esa intención; sin compilar el destino, ejecutar MUnit y ensayar cambios/recuperación, no se demuestra resiliencia operativa. «Componible» conserva la idea de unidades que pueden combinarse e intercambiarse. [Adaptable](https://architect.salesforce.com/docs/architect/well-architected/guide/adaptable-overview).

La columna de **decisión** describe la propuesta del proyecto; la de **evidencia** se limita a lo presente y documentado; la de **pendiente** identifica qué debe verificarse antes de sostener una afirmación mayor. Estas correspondencias son interpretación de diseño, no una evaluación emitida por Salesforce. El gráfico no ofrece puntuación, nivel de madurez, certificación ni un juicio de conformidad.

## Validación y uso

- XML bien formado; dimensiones y `viewBox` iguales a 1800 × 1200.
- Geometría de rectángulos dentro del lienzo; anchura de textos comprobada con métricas de Arial.
- Títulos y descripciones accesibles en cada SVG; texto seleccionable y editable.
- Las ocho categorías coinciden con las fuentes oficiales consultadas; no se agregan otras capacidades ni se traslada un marco de otro proveedor.
- No se ejecutaron pruebas de aplicación, despliegues, accesos administrativos ni llamadas al runtime al producir los diagramas.

El texto pequeño de las fuentes está pensado para el SVG a resolución completa. Para una miniatura, enlazar al original ampliable y a estas notas. Antes de una publicación final, comprobar visualmente la renderización del editor o navegador de destino; esta validación geométrica no sustituye esa inspección.
