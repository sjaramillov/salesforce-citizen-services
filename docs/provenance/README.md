# Procedencia y transformación

Origen local: proyecto `citizen-services-baseline`. La extracción es selectiva y deja el proyecto original intacto. `manifest.json` registra rutas relativas de origen, SHA-256 de los archivos leídos y cambios por archivo técnico importado. Los hashes identifican esa versión de la fuente; no acreditan por sí solos autoría ni derechos.

## Material seleccionado

LWC propio de la experiencia ciudadana; contratos OpenAPI redactados para el escenario; flujo Mule preliminar y ejemplos; SQL de datos declarados ficticios; instrucciones AgentScript extraídas a referencia legible. La documentación de `docs/base` sintetiza el conocimiento técnico previo; `docs/pilot.md`, `docs/architecture.md` y `docs/runbook.md` agregan alcance comercial y pasos futuros sin convertirlos en evidencia implementada.

## Cambios

- Conservación de estructura, CSS, nombres de componente, nombres API y referencias internas relevantes.
- Identificación visible de demostración local, sin afirmar backend, autenticación, avisos enviados ni chat en vivo.
- Normalización de las dos personas ficticias y reducción de datos embebidos de AgentScript.
- Eliminación del vínculo de usuario de servicio; AgentScript fuera del paquete desplegable.
- Declaración del namespace XML `doc` ausente en el flujo; ningún cambio se presenta como corrección completa de runtime.
- Alias de servicio sustituido por placeholder; ningún valor operativo copiado.
- Documentación del producto con alcance de piloto, decisiones y límites de integración.

## Material excluido

Documentación privada ajena al producto; `.env*`, `.sf`, `.sfdx`, wallets, credenciales y URLs operativas; exportación completa del sitio y metadata generada del tenant; grafos y planner bundles generados; datos CRM y archivos CSV; logs completos; capturas y grabaciones; logos, mascotas, fuentes, imágenes y assets de procedencia incierta; HTML descargado, librerías y vendor.

No se reenvía la historia Git del origen. Retirar logos o cambiar textos no concede licencia de código, plantillas, herramientas ni material de terceros. Las referencias oficiales de producto y los nombres de tecnología se conservan para atribución técnica, sin afirmar afiliación. La extracción autorizada reúne los artefactos propios seleccionados; las condiciones de publicación y los derechos reservados se describen en [LICENSE](../../LICENSE) y [NOTICE](../../NOTICE.md).

Las versiones de plataforma heredadas son referencias pendientes de verificación en el destino. Las validaciones de esta extracción se describen por su alcance real en `docs/evidence/status.md`.
