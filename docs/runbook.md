# Runbook de revisión y prueba

## 1. Inspección local sin conexión

Desde la raíz:

```bash
python3 scripts/validate_local.py
```

El script escribe `docs/evidence/local-validation.json`. Inspecciona `docs/provenance/manifest.json` para contrastar los archivos técnicos importados y sus transformaciones. Ningún comando de esta sección autentica, publica, despliega o consulta una organización.

Leer `force-app/main/default/lwc/cscBenefitPortal/cscBenefitPortal.js`: el caso y la conversación son constantes. El caso válido ficticio es `BEN-2026-004219`. Otro valor cambia el mensaje de estado; la tarjeta ilustrativa permanece visible. Esto no demuestra búsqueda ni control de acceso en un backend.

## 2. Comprobar un portal público existente

La URL operativa no se incluye en el repositorio. El dueño proporciona o abre la URL pública, sin tokens ni rutas de administración. Registrar UTC, URL sanitizada, resultado HTTP si está disponible y evidencia visual revisada antes de publicarla.

Comprobar que aparece el componente; ensayar su consulta de demostración y un caso inexistente. Registrar por separado: página accesible, componente visible, interacción local, autenticación, llamada al agente y llamada al backend. Una página que abre no prueba las cinco restantes.

Si el sitio pide autenticación, ha caducado o devuelve error, registrar el resultado. No actualizar cuentas, publicar cambios ni resetear credenciales como parte de esta comprobación.

## 3. Preparar un nuevo entorno Salesforce — pendiente

Estas son tareas futuras para un operador autorizado. Antes de ejecutar comandos de despliegue, confirmar organización de destino, licencia/capacidades, versión de API soportada, usuario de servicio y permisos mínimos. No utilizar la identidad de la demo anterior.

- Crear un proyecto/sitio autorizado o seleccionar uno de prueba.
- Validar y desplegar únicamente el LWC; colocarlo en una página de Experience Cloud y probarlo antes de publicar.
- Recrear el agente en la organización usando las instrucciones de referencia; vincular variables, usuario, acciones y herramientas según la metadata que genere ese entorno.
- Mantener las credenciales y URLs privadas fuera del repositorio.

No ejecutar directamente `benefit-agent.reference.agent` como paquete de despliegue. Se retiró el binding del usuario y no se copiaron el grafo ni los vínculos generados del tenant original.

## 4. Preparar Mule — pendiente

Antes de cualquier runtime, resolver lo listado en `mulesoft/benefit-status-sys-api/README.md`, validar el XML contra la versión elegida y completar los mocks/eventos MUnit. Comprobar la configuración de propiedades seguras y del listener HTTP en un entorno aislado; usar el SQL solo en una base de demostración vacía autorizada.

La prueba funcional debe cubrir: éxito, caso inválido, no encontrado, acceso ajeno, registro caído, correlación y ausencia de datos internos en el contrato Experience. Registrar comandos, versión de runtime, resultado y referencia a artefactos sanitizados.

## 5. Cerrar evidencia

Actualizar `docs/evidence/status.md` solo cuando existan resultados. No convertir una especificación parseada, un asset de catálogo ni una captura histórica en una afirmación de runtime desplegado. Documentar el commit probado cuando exista Git y separar resultado local de resultado en organización.
