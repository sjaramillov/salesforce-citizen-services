# Base recuperada: adaptador del registro

El flujo preliminar consulta una tabla Oracle de demostración mediante un parámetro de caso, y transforma la fila al contrato System. El esquema representa un registro legacy, sin afirmar integración real a un mainframe.

La decisión durable es conservar un contrato estable y un adaptador reemplazable. Un futuro destino puede ser una fachada autorizada de servicio o una vista de datos permitida. Antes de implementarlo, conocer propietario, mecanismo de autenticación, contrato, timeout, límites, semántica de errores y responsabilidades de operación.

No se copió ningún wallet, host operativo ni dato de una entidad. El SQL incluido crea una tabla y dos filas ficticias; no es una migración productiva ni debe ejecutarse sobre una base existente sin revisión.

Fuentes: `docs/legacy-integration-cobol-java.md`, `docs/oracle-cobolsim.md` y el módulo System API del origen. Compatibilidad de versiones/conectores y operación del destino quedan pendientes.
