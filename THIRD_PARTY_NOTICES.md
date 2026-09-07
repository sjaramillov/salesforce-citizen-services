# Avisos de terceros y excepciones

Apache License 2.0 cubre el material original descrito en el
[alcance de licencia](docs/licensing.md), dentro de los derechos que su titular
pueda otorgar. No cambia los términos de una plataforma, dependencia, marca ni
componente generado por un tercero. La procedencia registrada mediante hashes
no acredita autoría ni facultad para relicenciar.

## Referencia AgentScript excluida de Apache 2.0

[`salesforce/agentforce/benefit-agent.reference.agent`](salesforce/agentforce/benefit-agent.reference.agent)
es una referencia derivada de una exportación de plataforma: combina instrucciones
del escenario con estructura, descripciones y referencias internas heredadas.
**El archivo completo queda excluido de la concesión Apache 2.0 de este repositorio
mientras no se acredite la facultad de relicenciar sus componentes generados.**
Se conserva sin modificaciones en esta revisión; no se le añade una cabecera de
licencia propia ni se afirma que Salesforce haya autorizado su redistribución o
relicenciamiento. Su disponibilidad aquí no concede permisos sobre contenido de
terceros. No es un paquete desplegable validado. Su origen y límites técnicos se
explican en el [README de Agentforce](salesforce/agentforce/README.md).

Para implementar un agente, recrea la configuración en una organización autorizada
y comprueba los términos y capacidades de la plataforma. La concesión Apache del
código propio no sustituye esa comprobación.

## Componentes referenciados, sin binarios redistribuidos

| Tecnología o dependencia | Referencia en este repositorio | Alcance de distribución |
|---|---|---|
| Salesforce, Lightning Web Components y Experience Cloud | Componente de `force-app/`, importación de `lwc`, metadata y `sfdx-project.json` | Se distribuye el componente y su configuración propios. No se distribuye ni relicencia el runtime, la implementación del framework o el servicio alojado. |
| Agentforce | Archivo de referencia excluido arriba; nombres de modelos, variables y utilidades de plataforma | No se distribuyen modelos, runtime, grafo ni planner bundle. Aplican los términos y permisos propios de la plataforma. |
| MuleSoft: Mule runtime, Maven Plugin, MUnit, HTTP Connector, Database Connector y Secure Configuration Properties | Coordenadas Maven en `mulesoft/benefit-status-sys-api/pom.xml`; namespaces y configuración XML | Son referencias de integración. No se distribuyen conectores, plugins, runtimes ni bibliotecas compiladas. Sus licencias, avisos y posibles requisitos de suscripción se verifican para la versión y el destino elegidos. |
| Oracle JDBC y bibliotecas de seguridad: `ojdbc11`, `oraclepki`, `osdt_core`, `osdt_cert` | Coordenadas Maven y nombre de driver en el flujo Mule | No se distribuyen JAR, wallets, bases de datos ni software Oracle. Cada artefacto mantiene sus propios términos; esta licencia no concede derechos sobre ellos. |
| PyYAML | `requirements-dev.txt`, para la validación local | Se referencia la dependencia; no se incluye su código ni un wheel. Conserva su licencia y avisos. |
| GitHub Actions y herramientas de CI | Workflows en `.github/workflows/` | Se distribuye la configuración del proyecto; las acciones y herramientas externas conservan sus propios términos. |

Las coordenadas y versiones declaradas no acreditan compatibilidad, disponibilidad
ni licencia para un despliegue. Antes de distribuir un ejecutable, bundle,
contenedor o aplicación Mule, inventaría los componentes realmente incorporados
y entrega sus licencias y avisos aplicables. Este inventario describe el código
fuente publicado, no una distribución binaria futura.

## Marcas, documentación y visuales

Salesforce, Agentforce, Experience Cloud y MuleSoft son marcas de Salesforce o de
sus afiliadas. Oracle y las demás tecnologías citadas conservan los derechos de
sus respectivos titulares. Su uso identifica tecnologías y no implica afiliación, patrocinio,
aval, certificación ni autorización comercial del proveedor.

Los diagramas son composiciones propias de texto y formas SVG, sin logos oficiales,
imágenes de proveedores ni fuentes incrustadas. La referencia a Salesforce
Well-Architected conserva los nombres del marco y enlaza sus fuentes; las decisiones
y brechas representadas son una interpretación del proyecto, no una evaluación
oficial. Apache 2.0 no relicencia la documentación enlazada ni sus marcas.

Las portadas están documentadas como generación con IA en
[`docs/visuals/assets.json`](docs/visuals/assets.json). Se ofrecen en la medida de
los derechos que el titular pueda otorgar, sin promesa de exclusividad. La fuente
tipográfica Arial se menciona como preferencia de representación y no se distribuye.
La procedencia de los visuales está en la [galería](docs/visuals/README.md) y sus
[fuentes](docs/visuals/sources.json).
