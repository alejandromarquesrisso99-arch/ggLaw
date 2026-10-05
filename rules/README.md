# rules/

Motivos de defensa en YAML, uno por fichero: `rules/<ámbito>/<nombre>.yaml`, con id
`<ámbito>.<nombre>`. Sus condiciones las evalúa `core/<ámbito>/`, nunca el LLM. Todo motivo
nuevo entra con `estado: borrador`.

Cada YAML declara:

- `fundamento`: norma, artículo y el fichero de `knowledge/` donde está transcrito. Los tests
  fallan si el artículo no figura en la lista `articulos` de ese fichero.
- `condiciones`: id, descripción y fundamento de cada condición. El evaluador solo puede
  informar de condiciones declaradas aquí.
- `datos_necesarios`: datos del caso que puede usar la regla (alias de
  `core/trafico/caso.py`).
- `parametros`: los plazos y supuestos de la norma, en datos y no en código.
- `parrafo_tipo`: plantilla del párrafo del escrito (pendiente, tarea 6).

Resultados posibles: `procede`, `no_procede`, `dudoso` (depende de una duda jurídica abierta:
ver los `TODO(juridico)` en `notas`) y `faltan_datos` (nombra cuáles).

| Regla | Fundamento principal |
|---|---|
| `trafico.prescripcion_infraccion` | art. 112.1-2 RDL 6/2015 |
| `trafico.caducidad_procedimiento` | art. 112.3 RDL 6/2015 |
| `trafico.defecto_notificacion_denuncia` | arts. 90 y 91 RDL 6/2015 |
| `trafico.identificacion_conductor` | arts. 11, 77.j y 93.1 RDL 6/2015 |
| `trafico.control_metrologico_cinemometro` | art. 83.2 RDL 6/2015 (alcance limitado) |
