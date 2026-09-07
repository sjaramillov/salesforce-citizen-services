# Estado de evidencia

Fecha de extracción: 2026-09-07. No se modificó, publicó ni desplegó el proyecto de origen.

| Elemento | Estado de esta extracción | Límite |
|---|---|---|
| LWC | Código seleccionado y marcado como demostración | No compilado con herramienta Salesforce ni probado visualmente en esta copia |
| Sintaxis de metadata | Comprobación XML/JSON local | No es validación contra schema Salesforce/Mule |
| OpenAPI | Parseo, estructura mínima y resolución de `$ref` locales | No equivale a validación exhaustiva de OpenAPI ni tráfico real |
| AgentScript | Decodificado y sanitizado; revisión de referencia | No compilado, desplegado ni probado en Preview en esta extracción |
| MUnit | Tres esqueletos heredados | No ejecutados; quedan TODO de mocks y eventos |
| Runtime Mule | No verificado | Sin evidencia local de despliegue funcional |
| Agentforce→Mule→registro | No verificado | Contratos y arquitectura no demuestran conexión |
| Portal público original | No confirmado operativo en la comprobación de 2026-09-07 | La URL de consulta mostró preparación y después un mensaje de error de Salesforce; causa no establecida |
| AWS | Fuera de este proyecto | La arquitectura objetivo conserva Salesforce |

Los resultados exactos de la comprobación local están en `local-validation.json`.

## Comprobación pública de 2026-09-07

A las **16:08:55 UTC**, se abrió en navegador la URL de consulta derivada del dominio CSC y del prefijo documentado del sitio. La página mostró el título `Error Page` y el aviso de Salesforce `Stay Tuned...`, indicando que el sitio se estaba preparando y que se actualizaría automáticamente.

En una segunda lectura de la misma sesión, después del autorefresco, el título y la URL permanecieron iguales y el mensaje cambió a `We've hit a snag.`, con indicación de contactar soporte o consultar su página de estado. No se suministró una marca UTC independiente para esa segunda lectura; no se infiere su hora a partir del timestamp de la página.

No se observó el portal ciudadano ni se pudieron ensayar sus interacciones. Este resultado no establece la causa ni demuestra por sí solo un cierre definitivo del sitio: describe esa URL y ese momento. La publicación histórica no permite afirmar que el portal esté actualmente operativo.

El registro estructurado está en `public-portal-check.json`. Se omiten hostname del tenant, tokens, identificadores, rutas de administración y datos de sesión. No se realizaron cambios administrativos como parte de esta comprobación.

## Evidencia histórica referenciada, no reproducida aquí

El proyecto de origen registra una publicación Experience Cloud y capturas de Agentforce Preview en julio de 2026. Sus documentos específicos de Mule señalan APIs registradas con cero instancias y sin conformance validada. No se copiaron capturas, grabaciones, metadata completa del sitio ni URLs del tenant; deben revisarse sus derechos y datos antes de compartirlas.

El README y una nota de estado del origen contenían una frase más fuerte sobre una API real. La extracción sigue la evidencia más acotada de `mulesoft/api-led-portfolio.md` y del README System API: contratos registrados no equivalen a runtime desplegado.
