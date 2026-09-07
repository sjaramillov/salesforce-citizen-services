# Contratos de servicio ciudadano

Los tres contratos conservan nombres API y referencias del origen. Los archivos `.openapi.yaml` son documentos de diseño: no son URLs operativas ni demuestran que haya instancias desplegadas.

| Activo | Capa | Consumidor previsto | Estado |
|---|---|---|---|
| `benefit-status-sys-api` | System | Process API | Contrato y flujo preliminar |
| `benefit-case-prc-api` | Process | Experience API | Solo contrato |
| `agentforce-benefit-exp-api` | Experience | Portal o acción Agentforce | Solo contrato |

Consultar el [estado y bloqueos del flujo System](benefit-status-sys-api/README.md). La vista de arquitectura actual y el trabajo futuro están en [arquitectura](../docs/architecture.md).

Las recomendaciones de autenticación, control de tráfico y auditoría requieren implementación y prueba antes de un piloto con datos reales. El campo `security` de una especificación, un `correlationId` o un ejemplo de evento no acreditan que exista una política aplicada o una bitácora persistida.

Referencias oficiales heredadas para revisar en el entorno de destino; no se verificaron versiones vigentes en esta extracción:

- [Database Connector](https://docs.mulesoft.com/db-connector/latest/)
- [Secure Configuration Properties](https://docs.mulesoft.com/mule-runtime/latest/secure-configuration-properties)
- [MUnit](https://docs.mulesoft.com/munit/latest/)
- [Documentación Salesforce Developers](https://developer.salesforce.com/docs)
