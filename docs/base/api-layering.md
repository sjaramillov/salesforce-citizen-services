# Base recuperada: contratos y límites del agente

La separación System / Process / Experience evita que el canal tenga que conocer detalles del registro. Se mantienen los nombres de API y referencias internos del origen.

| Capa | Entrada y responsabilidad | Consumidor |
|---|---|---|
| System | Caso autorizado; lectura mínima del registro y errores | Process |
| Process | Estado normalizado; siguiente paso, motivo de derivación y auditoría | Experience |
| Experience | Información útil para explicar al ciudadano y campos minimizados | Portal o acción del agente |

`correlationId` permite relacionar una operación entre componentes. `auditEventId` representa un evento de auditoría en los contratos de proceso/experiencia. Que aparezcan esos campos no significa que exista hoy persistencia de eventos ni medición operativa.

El agente debe pedir aclaración ante identidad ambigua; no inventar estado, documentos o elegibilidad; explicar límites; y preparar derivación cuando faltan datos o hay una excepción. Los datos se autorizan en código, fuera de las instrucciones del modelo. Las instrucciones solas no garantizan esos controles.

Fuentes: `mulesoft/api-led-portfolio.md`, `docs/architecture.md` y AgentScript del origen. Controles y políticas aparecen como trabajo por implementar/verificar, no como configuración aplicada.
