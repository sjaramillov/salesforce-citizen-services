# Benefit Status System API — implementación preliminar

System API de lectura para el contrato `benefit-status-sys-api`. El consumidor previsto es la Process API. Oracle representa un registro legacy ficticio; no es una integración productiva probada.

Se conservan el contrato, flujo Mule, configuración de ejemplo, Maven, SQL y tres esqueletos MUnit. La extracción solo corrige la declaración XML ausente del prefijo `doc`, neutraliza nombres ficticios y reemplaza un alias de servicio por un placeholder.

## Bloqueos antes de probar runtime

- Validar versiones de Mule, plugin, conectores, JDBC y API del destino; los valores heredados no fueron verificados en esta sesión.
- Revisar el uso heredado de `set-property` y el manejo de códigos/cabeceras HTTP contra el runtime elegido. El parseo XML no acredita compatibilidad.
- Revisar las rutas de propiedades: el ejemplo anida `secure.oracle`, mientras el flujo referencia `secure::oracle.*`. Resolverlo en configuración probada antes de conexión.
- Revisar configuración de listener, errores propagados y timeout efectivo del conector. Un parámetro de timeout en YAML no prueba que el flujo lo aplique.
- Completar los TODO de mocks y eventos MUnit y ejecutar la suite.
- Agregar y probar autorización por caso, minimización, logging seguro y respuestas Experience antes de exponer el endpoint.

Los secretos se representan solo como placeholders. El ejemplo no se puede usar como configuración real. No se ejecutó Maven, Mule, SQL ni operación remota en esta extracción.

El contrato fue registrado históricamente como asset en el origen, con cero instancias y conformance no validada. Eso se mantiene como evidencia de diseño, sin afirmar runtime.
