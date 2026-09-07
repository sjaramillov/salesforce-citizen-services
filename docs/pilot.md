# Piloto y acompañamiento de implementación

## Problema y cliente

Para una entidad o un operador de servicio con consultas repetitivas sobre un trámite: las personas necesitan saber qué falta y quién puede resolver una excepción. El equipo de atención necesita recibir contexto suficiente para continuar sin repetir la recogida de información.

El patrocinador del piloto es el responsable del trámite o servicio. Participan el equipo de atención, el dueño de Salesforce y quien administra el sistema de registro. Un piloto exitoso demuestra un recorrido pequeño, reproducible y medible.

## Primer alcance

Un trámite; un corpus de requisitos aprobado; un canal web; un equipo de revisión. Se utilizan datos ficticios hasta que se acuerden y verifiquen los controles del entorno de la entidad.

1. El ciudadano consulta un requisito y recibe una respuesta con documento, sección y versión.
2. Si consulta un caso, el sistema comprueba identidad y autorización antes de recuperar su estado.
3. El asistente explica el documento pendiente y propone un borrador de solicitud de apoyo.
4. El ciudadano revisa y confirma el envío. Un reintento no duplica la solicitud.
5. Un funcionario recibe el caso, el resumen, las fuentes y la razón de derivación; registra su decisión.
6. El ciudadano puede consultar la recepción y el avance autorizado.

La concesión de un beneficio, una apelación, decisiones legales y la elegibilidad quedan fuera del alcance del asistente. Los canales WhatsApp, voz y atención presencial aparecen en la interfaz como visión de servicio, no como integraciones operativas incluidas.

## Qué se conserva y qué hay que construir

| Trabajo | Punto de partida | Entregable de piloto |
|---|---|---|
| Experiencia | LWC existente | Adaptación del trámite y conexión verificada |
| Orientación | Instrucciones Agentforce | Fuentes aprobadas, referencias y evaluación |
| Consulta | Tres contratos y flujo preliminar | Autorización, adaptador probado y errores seguros |
| Solicitud | Recorrido ilustrativo | Contrato de escritura, confirmación e idempotencia |
| Revisión | Señales de derivación en contrato | Cola real, dueño, estados y registro de resolución |
| Evidencia | Validación estática | Ejecución end-to-end documentada y ensayo con usuarios |

## Criterios de aceptación propuestos

- El conjunto acordado de preguntas tiene fuente y respuesta esperada; el informe incluye aciertos, errores y abstenciones, sin ocultar casos fallidos.
- Una pregunta ambigua pide aclaración y una respuesta sin soporte no se presenta como requisito oficial.
- Un usuario no puede consultar el caso de otro usando solo su número.
- La misma confirmación repetida produce una sola solicitud.
- Una caída del registro devuelve una respuesta segura y permite seguimiento humano.
- El funcionario puede reconstruir quién confirmó, qué se consultó y por qué se derivó.
- El equipo ejecuta el runbook y puede desactivar el canal sin perder solicitudes recibidas.

Estos son criterios de contrato de piloto, no resultados ya alcanzados. El tamaño del conjunto de evaluación y los umbrales se acuerdan antes de las pruebas.

## Cómo medir valor

Comparar un periodo base y el piloto con definiciones iguales: tiempo hasta información útil, proporción de solicitudes completas al primer envío, transferencias que conservan contexto, consultas repetidas y errores de orientación. Reportar tamaño de muestra y cambios de carga o mezcla de casos. No atribuir causalidad a una comparación simple si cambiaron otras condiciones.

## Modalidad de servicio

Discovery del trámite y datos → diseño con responsables → integración acotada → evaluación → transferencia al equipo. Cada paso entrega decisiones, código y evidencia revisable. El alcance, cronograma y costo se calculan después de verificar dependencias y licencias; esta base no implica un despliegue ni un precio cerrado.
