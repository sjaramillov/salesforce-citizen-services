# Agentforce: referencia extraída

`benefit-agent.reference.agent` es el contenido legible del AgentScript previamente generado para la demostración. Conserva instrucciones y topic names internos para poder relacionarlo con el diseño previo. Se retiró la identidad del usuario de servicio y se limitaron los registros embebidos a dos ejemplos ficticios.

El archivo se conserva fuera de `force-app`: **no es un paquete de despliegue validado**. No se copiaron el planner bundle ni el grafo generados, porque incorporan vínculos específicos del tenant y componentes de plataforma que no deben presentarse como implementación portable propia.

Para un piloto, recrear la configuración en la organización autorizada y verificar sintaxis, herramientas, bindings de variables, permiso de lectura de cada caso y derivación. La instrucción de escalar no demuestra que una cola humana esté conectada. La base de requisitos con citas y la creación de solicitud no están implementadas por esta referencia.

La extracción conserva una configuración heredada de citas deshabilitadas. El piloto exige una configuración y evaluación nuevas de fuentes; no debe describirse este archivo como solución RAG desplegada.

## Alcance de licencia

El archivo `benefit-agent.reference.agent` deriva de una exportación de plataforma
y contiene estructura, descripciones y referencias internas heredadas. **El archivo
completo está excluido de la concesión Apache 2.0 del repositorio** mientras no se
acredite la facultad de relicenciar sus componentes generados, incluidas las partes
que conviven con instrucciones del escenario. Se conserva sin modificar en esta
revisión de licencia. No se afirma autorización de Salesforce para redistribuir o
relicenciar material de terceros ni se deduce esa autorización de los hashes.

Consulta los [avisos de terceros](../../THIRD_PARTY_NOTICES.md) y el
[alcance general](../../docs/licensing.md). Para un piloto, recrea la configuración
en la organización autorizada con los términos y permisos correspondientes.
