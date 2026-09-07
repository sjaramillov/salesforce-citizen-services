# Agentforce: referencia extraída

`benefit-agent.reference.agent` es el contenido legible del AgentScript previamente generado para la demostración. Conserva instrucciones y topic names internos para poder relacionarlo con el diseño previo. Se retiró la identidad del usuario de servicio y se limitaron los registros embebidos a dos ejemplos ficticios.

El archivo se conserva fuera de `force-app`: **no es un paquete de despliegue validado**. No se copiaron el planner bundle ni el grafo generados, porque incorporan vínculos específicos del tenant y componentes de plataforma que no deben presentarse como implementación portable propia.

Para un piloto, recrear la configuración en la organización autorizada y verificar sintaxis, herramientas, bindings de variables, permiso de lectura de cada caso y derivación. La instrucción de escalar no demuestra que una cola humana esté conectada. La base de requisitos con citas y la creación de solicitud no están implementadas por esta referencia.

La extracción conserva una configuración heredada de citas deshabilitadas. El piloto exige una configuración y evaluación nuevas de fuentes; no debe describirse este archivo como solución RAG desplegada.
