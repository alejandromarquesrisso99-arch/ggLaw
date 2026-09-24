---
norma: Control metrológico de los cinemómetros (art. 83.2 RDL 6/2015) — Ley 32/2014 de Metrología, RD 244/2016 y Orden ICT/155/2020 (anexo XII)
identificador: [BOE-A-2014-13359, BOE-A-2016-5530, BOE-A-2020-2573, BOE-A-2022-8355]
articulos:
  ley_32_2014: [7, 8, 9, 12]
  rd_244_2016: ["2 (selección)", 6, 7, 16, 18, 19, 21, "anexo III art. 2", "anexo III art. 5"]
  orden_ict_155_2020: [1, 2, 3, 9, 10, 11, 12, 14, 15, 16, 17, 18, "DT 2ª", "DD (letra m)", "DF 5ª", "anexo XII (completo)"]
  directriz_1_2022: ["anexo, apartado 1", "2", "3", "4", "6", "7"]
fuente: https://www.boe.es/buscar/act.php?id=BOE-A-2020-2573
# Otras fuentes: https://www.boe.es/buscar/act.php?id=BOE-A-2014-13359
#                https://www.boe.es/buscar/act.php?id=BOE-A-2016-5530
#                https://www.boe.es/buscar/act.php?id=BOE-A-2022-8355
# Versión consolidada de cada norma (página act.php del BOE, 2026-09-23):
#   Orden ICT/155/2020: "Última actualización publicada el 03/10/2025" (Orden ITU/1072/2025,
#     solo anexo III.4, contadores de agua; no afecta a lo transcrito).
#   RD 244/2016: "Última actualización publicada el 12/04/2025" (RD 249/2025, anexos III y IV).
#   Ley 32/2014: sin actualizaciones (texto original).
#   Directriz 1/2022: sin actualizaciones.
version_consolidada: 2025-10-03
consultado: 2026-09-24
estado: borrador
---

# Control metrológico de los cinemómetros (radares de velocidad)

> **Aviso:** material de referencia para ggLaw, no asesoramiento jurídico.
> Contenido en `estado: borrador`, pendiente de revisión por Alex o por un abogado.

**Cómo se ha obtenido el texto.** Todo lo que aparece bajo las secciones 1 a 5 es
transcripción literal de la versión consolidada del BOE, descargada con
`scripts/boe_fetch.py` (API de datos abiertos del BOE) el 2026-09-23 y el 2026-09-24. Cada bloque lleva un
comentario `<!-- bloque … -->` con la fecha de publicación y de vigencia de la redacción
transcrita. Las líneas `> _Nota BOE: …_` son notas editoriales del BOE. Las marcas `[…]`
y las notas `> **Nota ggLaw …**` son de elaboración propia. `boe_fetch.py` aplana las
tablas en una sola línea en negrita: las dos tablas de errores máximos permitidos se
reconstruyen además, fila a fila, a partir de las celdas del XML del BOE (ver la nota
tras el apéndice I del anexo XII).

**Qué se ha dejado fuera (a propósito).** De la Orden ICT/155/2020 solo se transcribe la
parte general aplicable a cinemómetros y el anexo XII completo; los anexos I-XI y XIII-XXI
regulan otros instrumentos (el XIII, etilómetros, queda pendiente). Del RD 244/2016 se
omiten los capítulos sobre patrones, organismos, registro y vigilancia de mercado, y los
anexos I, II y IV-XVI. De la Ley 32/2014 se omiten los capítulos I, II y IV-VI.

**Relación con la LSV.** El art. 83.2 LSV (en `knowledge/rdl-6-2015-procedimiento-sancionador.md`)
somete los aparatos usados para denunciar «a control metrológico en los términos
establecidos por la normativa de metrología». La normativa de metrología es la de este
fichero.

## Vigencia (comprobada con `--meta`, `--index` y el análisis del BOE el 2026-09-23)

| Norma | Identificador | Publicación | Vigencia | Estado a 2026-09-23 | Modificaciones posteriores registradas |
|---|---|---|---|---|---|
| Ley 32/2014, de 22 de diciembre, de Metrología | BOE-A-2014-13359 | BOE núm. 309, de 23/12/2014 | 24/12/2014 | `estatus_derogacion: N`, `vigencia_agotada: N` | Ninguna (todos los bloques son de 20141223). SSTC 117/2017 y 63/2018 desestiman recursos contra otros preceptos |
| RD 244/2016, de 3 de junio | BOE-A-2016-5530 | BOE núm. 137, de 07/06/2016 | 08/06/2016 | `estatus_derogacion: N`, `vigencia_agotada: N` | Orden ICT/155/2020 (anexo III, desde 24/10/2020); RD 249/2025 (anexos III y IV; el índice también fecha el art. 2 en 20250412; vigente desde 02/05/2025) |
| Orden ICT/155/2020, de 7 de febrero | BOE-A-2020-2573 | BOE núm. 47, de 24/02/2020 | 24/10/2020 | `estatus_derogacion: N`, `vigencia_agotada: N` | Orden ICT/397/2020 (entrada en vigor a 24/10/2020); corrección de errores BOE núm. 126, de 06/05/2020; Orden ITU/1475/2024 (arts. 9, 11, 12, 14, 15, 17-19 y apéndice II del anexo XII, vigente desde 16/01/2025); Orden ITU/1072/2025 (anexo III.4) |
| Directriz 1/2022, de 19 de mayo (cabinas) | BOE-A-2022-8355 | BOE núm. 121, de 21/05/2022 | «a los veinte días de su publicación» (apartado 7) | `estatus_derogacion: N`, `vigencia_agotada: N` | Ninguna |
| Orden ITC/3123/2010 (norma anterior de cinemómetros) | BOE-A-2010-18556 | BOE núm. 292, de 03/12/2010 | 04/12/2010 | **Derogada**: `fecha_derogacion: 20201024` (DD única, letra m, Orden ICT/155/2020) | — |

No se ha encontrado en el BOE ninguna norma posterior que sustituya a la Orden ICT/155/2020
para cinemómetros (búsqueda en legislación consolidada por los términos "control metrológico" y
"cinemómetros", y en el diario por "velocidad de circulación de vehículos a motor control
metrológico"). **Atención a la fecha de los hechos:** la Orden ICT/155/2020 se aplica a
mediciones desde el 24/10/2020. Para hechos anteriores rige la Orden ITC/3123/2010, que no
se ha leído (`TODO(juridico)` en dudas). Y dentro de la Orden ICT/155/2020, los arts. 9,
11, 12, 14, 15, 17 y 18 y el apéndice II del anexo XII tienen una redacción vigente desde
el 16/01/2025; la anterior (2020) difiere en plazos de certificados e informes, no en los
errores máximos ni en la periodicidad.

## Respuesta práctica (elaboración propia, `estado: borrador`)

**1. Qué controles se exigen a un cinemómetro.**
- **Antes de usarlo: evaluación de la conformidad.** Anexo XII, apartado 3: «Módulo B,
  examen de tipo, más Módulo F, conformidad con el tipo basada en la verificación del
  producto». El módulo F tiene una segunda fase, «Verificación de producto después de la
  instalación», con «al menos 50 medidas realizadas en condiciones de tráfico real»
  (apéndice II, B.2). Los cinemómetros puestos en servicio antes del 24/10/2020 siguen
  siendo válidos si superan las verificaciones en servicio (DT 2ª): «No se les podrá
  exigir el cumplimiento de requisitos adicionales a los determinados durante el proceso
  de su puesta en servicio».
- **Verificación después de reparación o modificación.** Si se rompen precintos, el
  instrumento no puede usarse hasta superarla (art. 12.2 Ley 32/2014; art. 7.1 Orden). Los
  ensayos son los del módulo F y los errores máximos, los de la evaluación de la
  conformidad (apéndice III). Tiene «efectos de verificación periódica respecto al cómputo
  del plazo» (art. 11.3 Orden).
- **Verificación periódica anual.** Anexo XII, apartado 5: «El plazo de verificación
  periódica será de un año». Para la primera, el plazo cuenta «desde la fecha de la puesta
  en servicio» (art. 14.2); para las siguientes, «a contar desde la fecha del certificado
  de la verificación anterior» (art. 14.4). Vencido el plazo, el instrumento «no podrá ser
  utilizado» para sanciones «hasta que no la supere» (art. 14.1, párr. 2, en relación con
  el art. 8.1 Ley 32/2014, que incluye las «sanciones administrativas»).
- **Cabinas de los radares fijos: revisión cada cuatro años**, coincidiendo con la
  verificación periódica (apéndice IV: «cada cuatro años y coincidiendo con el proceso de
  verificación periódica de los cinemómetros fijos se revisarán las cabinas que los
  alojan»). La Directriz 1/2022 lo desarrolla (certificado de revisión de cabina).

**2. Errores máximos permitidos (emp).** El texto distingue **tipo de instalación**
(fija, estática, móvil, de tramo, en aeronave; apéndice I, 1.6) y **fase de control**:

| Fase | Instalación | Ensayos en laboratorio | Ensayos en carretera (tráfico real) |
|---|---|---|---|
| Evaluación de la conformidad y verificación después de reparación (tabla 1) | Fija, estática y de tramo | ± 2 km/h | ± 3 km/h si v ≤ 100 km/h; ± 3 % si v > 100 km/h; ± 1 km/h (error medio en examen de tipo) |
| Íd. | Móvil sobre vehículo | ± 2 km/h | ± 5 km/h si v ≤ 100 km/h; ± 5 % si v > 100 km/h |
| **Verificación periódica** (tabla 2) | Fija o estática | ± 2 km/h si v ≤ 200 km/h; ± 3 km/h si v > 200 km/h | **± 5 km/h si v ≤ 100 km/h; ± 5 % si v > 100 km/h** |
| **Verificación periódica** | Móvil sobre vehículo | ± 2 km/h si v ≤ 200 km/h; ± 3 km/h si v > 200 km/h | **± 7 km/h si v ≤ 100 km/h; ± 7 % si v > 100 km/h** |
| Verificación periódica | De tramo y en aeronave | Los de la tabla 1 | Los de la tabla 1 |

Esta tabla resume las dos tablas del apéndice I (reconstruidas de las celdas del XML; la
columna de laboratorio abarca en ambas tablas las filas «fija» y «móvil»). Un radar en
vehículo **parado** se considera estático (apéndice I, 1.6.iii).

**3. Qué tiene que poder acreditar la Administración.** Ninguna de estas normas regula el
contenido del expediente sancionador. Lo que sí dicen: la medición goza de «presunción de
exactitud de medida, salvo prueba en contrario» si el instrumento ha «superado las fases de
control metrológico que les sean de aplicación» (art. 8.6 Ley 32/2014). De ahí se deduce
(interpretación, certeza `B`) que, si se discute, la Administración debe poder aportar:
- el certificado de evaluación de la conformidad (examen de tipo, módulo B, y
  verificación del producto, módulo F) o, para equipos anteriores a 2020, el título que
  permitió su puesta en servicio (DT 2ª);
- el **certificado de verificación periódica vigente en la fecha de la medición** (art.
  17.2; art. 21.1 RD 244/2016: «Se emitirá asimismo el correspondiente certificado de
  verificación») y, si hubo reparación, el certificado de verificación después de
  reparación (art. 11.2);
- en radares fijos, el certificado de revisión de la cabina (apéndice IV; Directriz 1/2022);
- la documentación fotográfica con los datos del apéndice I, 1.2 (fecha y hora, velocidad
  medida, sentido si mide en ambos, identificación del cinemómetro y ubicación) y, en los
  que funcionan sin operador y no siguen el objetivo, «al menos dos fotogramas» (1.10).

**4. Lo que estas normas NO dicen.** No se ha encontrado en los textos leídos ninguna regla
que obligue a restar el emp a la velocidad medida antes de encuadrar la infracción en el
anexo IV de la LSV. Es una práctica administrativa conocida por fuentes secundarias
(pista no verificada; ver dudas). ggLaw **no** debe presentar el descuento del emp como
obligación legal hasta que se localice la fuente primaria.

## Índice (elaboración propia)

| Materia | Norma y precepto | Texto literal clave |
|---|---|---|
| Sometimiento de los instrumentos para sanciones | Ley 32/2014, art. 8.1 | «que sean utilizados por razones de […] sanciones administrativas» |
| Presunción de exactitud | Ley 32/2014, art. 8.6 | «Gozarán de presunción de exactitud de medida, salvo prueba en contrario, las mediciones realizadas con instrumentos o sistemas de medida sometidos a control metrológico del Estado que hayan superado las fases de control metrológico que les sean de aplicación» |
| Fases del control | Ley 32/2014, art. 9; RD 244/2016, art. 7; Orden, art. 2 | «fase de evaluación de la conformidad y la fase de control metrológico de instrumentos en servicio» |
| Reparación y precintos | Ley 32/2014, art. 12.2 | «la intervención en un instrumento que requiera levantamiento de precintos impedirá su puesta en servicio hasta que no haya superado la correspondiente verificación» |
| Módulos de conformidad | Orden, anexo XII, ap. 3 | «Módulo B, examen de tipo, más Módulo F, conformidad con el tipo basada en la verificación del producto» |
| Periodicidad | Orden, anexo XII, ap. 5 | «El plazo de verificación periódica será de un año» |
| Solicitud y uso tras el vencimiento | Orden, art. 14.1 | «Como mínimo un mes antes de que transcurra el periodo»; «este no podrá ser utilizado para los fines estipulados en el apartado 1 del artículo 8 de la Ley 32/2014 […] hasta que no la supere» |
| Cómputo del plazo | Orden, art. 14.2 y 14.4 | «desde la fecha de la puesta en servicio del instrumento de medida»; «a contar desde la fecha del certificado de la verificación anterior» |
| Certificado de verificación | Orden, art. 17.2 | «emitirá el correspondiente certificado de verificación en un plazo máximo de diez días» |
| No superación | Orden, art. 18 | «deberá colocar la etiqueta de inhabilitación para el servicio» |
| Tipos de instalación | Orden, anexo XII, ap. I, 1.6 | «Fijos», «estáticos», «móviles» |
| Datos de la foto | Orden, anexo XII, ap. I, 1.2 | «La fecha y hora de la medida», «la velocidad medida del vehículo infractor», «identificación del cinemómetro que realizó la medida y ubicación (si procede)» |
| Dos fotogramas | Orden, anexo XII, ap. I, 1.10 | «se les exigirá al menos dos fotogramas del vehículo infractor tomados en diferentes instantes» |
| Deriva anual | Orden, anexo XII, ap. I, 2.a | «El cinemómetro estará concebido para que pueda respetar los errores máximos permitidos sin ajustes durante un período de un año de uso normal» |
| emp en servicio | Orden, anexo XII, ap. I, 3.1.2 | «Los errores máximos permitidos en la verificación periódica de cinemómetros son los que se indican en la tabla 2» |
| Ensayos de verificación periódica | Orden, anexo XII, ap. IV | «podrán ser sustituidos por, al menos, 30 medidas realizadas en condiciones de tráfico real» |
| Cabinas | Orden, anexo XII, ap. IV; Directriz 1/2022, ap. 4 | «cada cuatro años»; «Cuatro años desde la fecha del primer certificado de revisión de cabinas» |
| Instrumentos anteriores | Orden, DT 2ª | «podrán seguir siendo utilizados mientras superen las verificaciones establecidas para los instrumentos en servicio» |
| Derogación de la orden anterior | Orden, DD única, m) | «Orden ITC/3123/2010, de 26 de noviembre» |

---

## 1. Ley 32/2014, de 22 de diciembre, de Metrología (BOE-A-2014-13359)

<!-- bloque a7 · versión publicada 20141223 · vigente desde 20141224 -->

### Artículo 7. Control metrológico del Estado.

De conformidad con la normativa de la Unión Europea y con las resoluciones de la Organización Internacional de Metrología Legal, el control metrológico del Estado es el conjunto de actividades que contribuyen a garantizar la certeza y corrección del resultado de las mediciones, regulando las características que deben tener los instrumentos, medios, materiales de referencia, sistemas de medida y programas informáticos relacionados con la medición; los procedimientos adecuados para su utilización, mantenimiento, evaluación y verificación; así como la tipología y obligaciones de los agentes intervinientes.

<!-- bloque a8 · versión publicada 20141223 · vigente desde 20141224 -->

### Artículo 8. Elementos sometidos al control metrológico del Estado.

1. Los instrumentos, medios, materiales de referencia, sistemas de medida y programas informáticos que sirvan para medir o contar y que sean utilizados por razones de interés público, salud y seguridad pública, orden público, protección del medio ambiente, protección o información a los consumidores y usuarios, recaudación de tributos, cálculo de aranceles, cánones, sanciones administrativas, realización de peritajes judiciales, establecimiento de las garantías básicas para un comercio leal, y todas aquellas que se determinen con carácter reglamentario, estarán sometidos al control metrológico del Estado en los términos que se establezca en su reglamentación específica.

2. Cuando así se determine en la reglamentación específica de cada instrumento, será posible la utilización de instrumentos testigo, con características metrológicas o requisitos de verificación especiales, que estén a disposición de los ciudadanos para la comprobación de las medidas efectuadas por otros instrumentos situados en el mismo recinto. En ese caso podrán ampliarse por su regulación específica los periodos de la verificación periódica de los instrumentos instalados en el ámbito de influencia del instrumento testigo.

3. Cuando los costes asociados al control metrológico de instrumentos en servicio sean similares o superiores a los de reposición del instrumento, podrá establecerse reglamentariamente un periodo máximo de vida útil y, o, la prohibición de reparación o modificación del mismo. También podrá establecerse reglamentariamente un periodo de caducidad para la utilización de los materiales de referencia.

4. Se determinarán reglamentariamente la modalidad y el alcance del control aplicable en cada caso, así como los principios y normas generales de la designación y supervisión de los agentes que en él intervienen. También podrán determinarse reglamentariamente los métodos y procedimientos de utilización, ajuste, calibración, evaluación y verificación.

En todo caso, se tendrá en cuenta que las medidas de control habrán de ser proporcionadas en relación con el interés público perseguido, así como que puedan cumplirse de la forma menos costosa para los operadores económicos.

5. Las actuaciones de control metrológico llevadas a cabo por la Administración Pública competente y los documentos reglamentarios emitidos por una autoridad competente o, de acuerdo con lo previsto en esta ley, por los agentes u organismos designados que intervienen en el control metrológico del Estado, serán válidos y eficaces en todo el territorio nacional.

6. Gozarán de presunción de exactitud de medida, salvo prueba en contrario, las mediciones realizadas con instrumentos o sistemas de medida sometidos a control metrológico del Estado que hayan superado las fases de control metrológico que les sean de aplicación.

7. Reglamentariamente se establecerá el régimen de marcado y precintado de los instrumentos y sistemas de medida sometidos al control metrológico, que deberá proporcionar información clara y precisa a los ciudadanos, consumidores y usuarios y a las autoridades inspectoras sobre su evaluación de la conformidad y estado de verificación. Los precintos colocados de acuerdo con la reglamentación aplicable serán válidos y eficaces en todo el territorio nacional.

<!-- bloque a9 · versión publicada 20141223 · vigente desde 20141224 -->

### Artículo 9. Fases del control metrológico del Estado.

1. El control previsto en el artículo anterior comprende la fase de evaluación de la conformidad y la fase de control metrológico de instrumentos en servicio.

2. En la fase de evaluación de la conformidad se comprueba el cumplimiento de los requisitos reglamentarios que los instrumentos, aparatos, medios, materiales de referencia y sistemas de medida deben satisfacer en su primera utilización.

3. La fase de control metrológico de instrumentos en servicio puede comprender, según corresponda en cada caso, verificaciones después de reparación, verificaciones después de modificación y verificaciones periódicas. Dicha fase tiene por objeto comprobar y confirmar que un instrumento o sistema de medida en servicio mantiene el cumplimiento de requisitos reglamentarios concordantes con los originales.

4. Los instrumentos y sistemas de medida sometidos al control metrológico del Estado pero no regulados en fase de control metrológico de instrumentos en servicio deberán respetar, mientras se sigan utilizando, los errores máximos permitidos en su evaluación de la conformidad.

5. Las Administraciones Públicas competentes para la ejecución de la legislación sobre metrología serán las responsables del cumplimiento de lo dispuesto en este capítulo respecto al control metrológico del Estado.

<!-- bloque a12 · versión publicada 20141223 · vigente desde 20141224 -->

### Artículo 12. Reparación o modificación de instrumentos sometidos al control metrológico del Estado.

1. Se considera reparación de un instrumento o sistema de medida a toda intervención, consecuencia de una avería, que requiera levantamiento de precintos y le devuelva a su estado original. Se considera modificación la intervención que sustituye o altera partes, elementos o módulos del instrumento o sistema por otros distintos de los que disponía en el momento de su evaluación inicial.

2. Cuando la verificación después de reparación o modificación haya sido reglamentariamente establecida, la intervención en un instrumento que requiera levantamiento de precintos impedirá su puesta en servicio hasta que no haya superado la correspondiente verificación.

3. No obstante, las disposiciones específicas reguladoras del control metrológico del Estado para cada tipo de instrumento o sistema de medida podrán establecer, atendiendo a las repercusiones de su utilización, la posibilidad de su puesta en servicio después de una reparación o modificación, y a la espera de la correspondiente verificación, bajo la responsabilidad y los precintos de quien los repare o modifique. Esta puesta en servicio requerirá, en todo caso, de la solicitud previa de verificación a la autoridad competente.

4. Cuando la evaluación de la conformidad de un instrumento sometido al control metrológico del Estado no requiera de una certificación por tercera parte de cada unidad de producto, no será necesaria la verificación después de reparación en los casos en los que ese instrumento sea reparado por el responsable de su puesta en mercado y servicio, y precintado por él con los precintos que le identifican y siempre que la intervención no suponga una modificación de dicho instrumento. La reparación que se lleve a cabo en estos términos no podrá alterar el plazo de verificación periódica.

## 2. Real Decreto 244/2016, de 3 de junio, que desarrolla la Ley 32/2014 (BOE-A-2016-5530)

<!-- bloque a2 · versión publicada 20250412 · vigente desde 20250502 -->

### Artículo 2. Definiciones.

Debe siempre utilizarse el Vocabulario Internacional de Metrología, publicado por la Oficina Internacional de Pesas y Medidas. Además, a los efectos de la aplicación del presente real decreto, se entenderá por:

[…]

e) «Certificado de verificación»: documento emitido por un organismo autorizado de verificación metrológica, en relación con un instrumento o sistema de medida declarando que éste es conforme con los requisitos establecidos en la regulación específica que le sea aplicable, este certificado podrá ser de verificación periódica o de verificación después de reparación en función de la actuación realizada.

[…]

ai) «Organismo autorizado de verificación metrológica», entidad, pública o privada, designada por habilitación de una Administración Pública competente española, para la realización y emisión de las oportunas certificaciones relativas a los controles metrológicos determinados en el artículo 9.3 de la Ley 32/2014, de 22 de diciembre, de Metrología.

[…]

an) «Puesta en servicio»: la primera utilización por el usuario final, en la Unión Europea, de un instrumento de medida para los fines que fue concebido.

[…]

ap) «Reparación»: toda intervención, consecuencia de una avería, que requiera levantamiento de precintos y devuelva el instrumento de medida a su estado original.

[…]

aw) «Verificación después de reparación o modificación»: el conjunto de exámenes administrativos, visuales y técnicos que pueden ser realizados en un laboratorio o en el lugar de uso, que tienen por objeto comprobar y confirmar que un instrumento o sistema de medida en servicio mantiene, después de una reparación o modificación que requiera rotura de precintos, las características metrológicas que le sean de aplicación, en especial en lo que se refiere a los errores máximos permitidos, así como que funcione conforme a su diseño y sea conforme a su regulación específica y, en su caso, al diseño o modelo aprobado.

ax) «Verificación periódica»: el conjunto de exámenes administrativos, visuales y técnicos que pueden ser realizados en un laboratorio o en el lugar de uso, que tienen por objeto comprobar y confirmar que un instrumento de medida en servicio mantiene desde su última verificación o, en el caso de la primera verificación periódica, desde su puesta en servicio, las características metrológicas que le sean de aplicación, en especial en lo que se refiere a los errores máximos permitidos, así como que funcione conforme a su diseño y sea conforme a su regulación específica y en su caso, al diseño o modelo aprobado.

<!-- bloque a6 · versión publicada 20160607 · vigente desde 20160608 -->

### Artículo 6. Instrumentos de medida sometidos a control.

1. De conformidad con lo establecido en el artículo 8 de la Ley 32/2014, de 22 de diciembre, de Metrología, los materiales de referencia y los instrumentos, aparatos, medios, sistemas de medida y programas informáticos, que sirvan para medir o contar y que sean utilizados en aplicaciones de medida por razones de interés público, salud y seguridad pública, orden público, protección del medio ambiente, protección de los consumidores y usuarios, recaudación de impuestos y tasas, cálculo de aranceles, cánones, sanciones administrativas, realización de peritajes judiciales, establecimiento de las garantías básicas para un comercio leal y todas aquellas que puedan determinarse con carácter reglamentario, estarán sometidos al control metrológico del Estado, cuando esté establecido, o se establezca, por regulación específica.

2. Los elementos citados en el punto 1 anterior cuya utilización sea distinta a las aplicaciones que en él se determinan, podrán ser comercializados y puestos en servicio libremente de acuerdo con las condiciones particulares establecidas para estos casos en el artículo 12.4.

3. Las disposiciones de este real decreto serán también de aplicación a los subconjuntos para los que se establezcan requisitos particulares en las regulaciones específicas para cada tipo de instrumento de medida. Los instrumentos de medida y sus subconjuntos podrán evaluarse de forma independiente con el propósito de establecer su conformidad.

<!-- bloque a7 · versión publicada 20160607 · vigente desde 20160608 -->

### Artículo 7. Fases del control metrológico del Estado.

1. La fase de evaluación de la conformidad del control metrológico del Estado será aplicable a los instrumentos de medida con carácter previo a su comercialización y puesta en servicio, utilizando los procedimientos de evaluación de la conformidad establecidos en el artículo 10.2 y desarrollados en el anexo I o en la regulación específica de los instrumentos de medida. Esta fase se establece, para cada instrumento sometido a control, bien como transposición de una directiva europea que apruebe una legislación armonizada o bien por legislación específica española para los instrumentos de medida no regulados por la Unión Europea.

2. El control metrológico del Estado de los instrumentos de medida en servicio puede comprender la verificación después de reparación o modificación y, o, la verificación periódica. También puede establecerse la prohibición de reparación de determinados instrumentos de medida y fijar su vida útil en un tiempo máximo.

<!-- bloque a1-8 · versión publicada 20160607 · vigente desde 20160608 -->

### Artículo 16. El control metrológico del Estado durante la vida útil de un instrumento de medida.

1. La regulación específica de un instrumento de medida sometido al control metrológico del Estado podrá establecer la obligatoriedad de su verificación periódica y, o, la de su verificación después de reparación o modificación.

2. En los casos determinados por el artículo 8.3 de la Ley 32/2014, de 22 de diciembre, de Metrología, la regulación específica del instrumento de medida podrá establecer un periodo máximo de vida útil del mismo. Podrán establecerse diferentes periodos de vida útil a los instrumentos de medida que, destinados al mismo fin, utilicen tecnologías diferentes. Se tendrá en cuenta, para ello, la mejor previsión técnica y, de haberla, la experiencia sobre la duración de los equipos, su uso y la previsible deriva en la medida. Los sistemas de etiquetado y marcado de estos instrumentos de medida se recogen en el anexo III.

3. También podrá establecerse la prohibición de reparación o modificación de los instrumentos de medida. Está prohibición solo podrá ser establecida para los instrumentos de medida para los que no se regule la obligatoriedad de una verificación periódica.

<!-- bloque a1-10 · versión publicada 20160607 · vigente desde 20160608 -->

### Artículo 18. Requisitos esenciales y procedimientos de verificación.

1. Los requisitos esenciales que un instrumento de medida debe cumplir desde su puesta en servicio serán los que estén establecidos por este real decreto y por su regulación específica.

2. La conformidad de un instrumento de medida con los requisitos esenciales aplicables deberá evaluarse con arreglo a los procedimientos de verificación establecidos en su regulación específica, que contemplará además de los requisitos metrológicos, técnicos y administrativos que deben satisfacer, los procedimientos a emplear, período de validez de la verificación, documentos que se deben emitir y mantener y cualquier otro aspecto que, en función de las características del instrumento de medida, se considere necesario.

<!-- bloque a1-11 · versión publicada 20160607 · vigente desde 20160608 -->

### Artículo 19. Sujetos obligados.

Quienes utilicen o posean, a título de propiedad, arrendamiento financiero u otras fórmulas semejantes, un instrumento de medida en servicio para los fines a los que se refiere el artículo 6.1, estarán obligados a someterlo a su verificación en las situaciones o períodos que se establezcan en su regulación específica que determinará el sujeto obligado en cada caso.

<!-- bloque a2-3 · versión publicada 20160607 · vigente desde 20160608 -->

### Artículo 21. Marcado de verificación.

1. Superado el control metrológico del Estado objeto de esta sección, se hará constar la conformidad del instrumento de medida para efectuar su función, adhiriéndole una etiqueta en un lugar visible del instrumento verificado o de la instalación que lo soporte, que deberá reunir las características y requisitos que se establecen en el anexo III. Se emitirá asimismo el correspondiente certificado de verificación.

2. Cuando un instrumento de medida no supere la fase de control metrológico objeto de esta sección, deberá ser puesto fuera de servicio hasta que se subsane la deficiencia que ha dado lugar a la no superación. En el caso de que dicha deficiencia no se subsane se adoptarán las medidas oportunas para garantizar que sea retirado definitivamente del servicio. Se hará constar esta circunstancia mediante una etiqueta de inhabilitación de uso, cuyas características se indican en el anexo III, situada en un lugar visible del instrumento de medida.

### Anexo III (selección): etiquetas de verificación y de inhabilitación

> **Nota ggLaw:** el art. 2 del anexo III termina en «serán los siguientes:» porque el modelo de etiqueta es una imagen que la API no transcribe. Ver el BOE.

<!-- bloque a2-14 · versión publicada 20250412 · vigente desde 20250502 -->

### Artículo 2. Verificación después de reparación o modificación y de verificación periódica.

1. Todo instrumento de medida que haya superado una verificación, en cualquiera de sus modalidades, deberá llevar adherida una etiqueta que lo acredite, cuyas características, formato y contenido serán los siguientes:

2. El fondo de la etiqueta será de color blanco. En la parte inferior derecha de la etiqueta, mediante la perforación de las casillas correspondientes, se indican los meses y los años hasta los que son válidas las verificaciones realizadas.

3. La etiqueta estará confeccionada con un material resistente a los agentes externos, tanto atmosféricos como abrasivos y a los impactos. Será de tipo adhesivo y autodestructiva al desprendimiento. Tendrá forma rectangular y sus dimensiones, si el instrumento lo permite, serán de 60 mm x 70 mm, debiéndose mantener las proporciones para otros tamaños.

4. Cuando un instrumento de medida conste de un grupo de dispositivos que funcionen juntos, que no tenga la condición de subconjuntos, la etiqueta se situará en el dispositivo principal del instrumento.

5. Si por razones de tamaño o sensibilidad del instrumento de medida no fuera posible aplicar la etiqueta en el mismo o si dicha etiqueta al adherirla sobre el instrumento no fuera visible, se colocará sobre la instalación que lo soporte o en la periferia de la misma y en la documentación correspondiente exigida en las disposiciones de su regulación específica.

6. En casos excepcionales y debidamente justificados, estas etiquetas en formato físico podrán sustituirse por otras en formato digital, siempre que contengan la información establecida en este artículo y se cumplan las condiciones de inviolabilidad y accesibilidad a dicha información y se autorice expresamente por la Administración pública competente.

> _Nota BOE: Se modifica por el art. único.1 del Real Decreto 249/2025, de 25 de marzo. Ref. BOE-A-2025-7438_

<!-- bloque a5-14 · versión publicada 20250412 · vigente desde 20250502 -->

### Artículo 5. Inhabilitación para el servicio.

1. Todo instrumento de medida que no haya superado una verificación, en cualquiera de sus modalidades, deberá llevar adherida en un lugar visible una etiqueta de inhabilitación para el servicio cuyas características, formato y contenido, serán los siguientes:

El texto “CONTROL METROLÓGICO”, el del tipo de instrumento y la calificación de “FUERA DE SERVICIO” será en letra mayúscula en negro sobre fondo rojo. También figurará el nombre de la entidad verificadora, su número de identificación, el número de serie del instrumento y la fecha en la que se realizó el control que dio lugar a la inhabilitación para el servicio.

2. La etiqueta estará confeccionada con un material resistente a los agentes externos, tanto atmosféricos como abrasivos y a los impactos. Será de tipo adhesivo y autodestructiva al desprendimiento. Tendrá forma rectangular y sus dimensiones serán las adecuadas al instrumento en cuestión y a su visibilidad.

> _Nota BOE: Se modifica por el art. único.1 del Real Decreto 249/2025, de 25 de marzo. Ref. BOE-A-2025-7438_

## 3. Orden ICT/155/2020, de 7 de febrero (BOE-A-2020-2573): parte general aplicable a cinemómetros

<!-- bloque a1 · versión publicada 20200224 · vigente desde 20201024 -->

### Artículo 1. Objeto.

Constituye el objeto de esta orden la regulación del control metrológico del Estado en la fase de evaluación de la conformidad y/o en las fases de control metrológico de instrumentos en servicio, según corresponda, de los instrumentos de medida que figuran en los anexos y que sean utilizados para alguno de los fines previstos en el artículo 8.1 de la Ley 32/2014, de 22 de diciembre, es decir, los instrumentos, medios, materiales de referencia, sistemas de medida y programas informáticos que sirvan para medir o contar y que sean utilizados por razones de interés público, salud y seguridad pública, orden público, protección del medio ambiente, protección o información a los consumidores y usuarios, recaudación de tributos, cálculo de aranceles, cánones, sanciones administrativas, realización de peritajes judiciales, establecimiento de las garantías básicas para un comercio leal, y todas aquellas que se determinen con carácter reglamentario, estarán sometidos al control metrológico del Estado en los términos que se establezca en su reglamentación específica.

<!-- bloque a2 · versión publicada 20200224 · vigente desde 20201024 -->

### Artículo 2. Fases del control metrológico.

1. El control metrológico del Estado regulado en esta orden es el que se establece en las secciones 3.ª y 4.ª del capítulo III del Real Decreto 244/2016, de 3 de junio, que se refieren, respectivamente, a la fase de evaluación de la conformidad y a la de control metrológico de los instrumentos en servicio.

2. El control metrológico de los instrumentos en servicio puede comprender la verificación después de reparación o modificación y/o la verificación periódica. También puede establecer la prohibición de reparación o modificación de determinados instrumentos de medida y fijar su vida útil en un tiempo máximo.

<!-- bloque a3 · versión publicada 20200224 · vigente desde 20201024 -->

### Artículo 3. Requisitos esenciales.

1. Los requisitos esenciales que deben cumplir los instrumentos de medida, son los establecidos en el anexo II del Real Decreto 244/2016, de 3 de junio, y los que, en su caso, se recojan en esta orden en el correspondiente anexo específico del instrumento.

Se presumirá la conformidad de los instrumentos de medida con los requisitos esenciales, cuando aquellos cumplan los requisitos del artículo 14 del Real Decreto 244/2016, de 3 de junio, o los que, en su caso, se describen en los anexos específicos de esta orden.

2. En el anexo específico de cada instrumento se establecen los errores máximos permitidos.

3. Los instrumentos no explotarán el error máximo permitido ni favorecerán sistemáticamente a ninguna de las partes.

### Capítulo III (selección). Verificación después de reparación o modificación

<!-- bloque a9 · versión publicada 20241227 · vigente desde 20250116 -->

### Artículo 9. Examen y ensayos.

Los instrumentos de medida deberán superar un examen administrativo y un examen metrológico.

a) Examen administrativo:

1.º El examen administrativo consiste en la identificación completa del instrumento de medida y la comprobación de que este reúne los requisitos exigidos para estar legalmente en servicio. El examen se realizará tomando como base la información aportada por el solicitante mediante la solicitud de verificación que se recoge en el anexo XIX. Asimismo, el examen comprenderá la comprobación de que el instrumento de medida tiene los precintos en la localización indicada en su evaluación de la conformidad o en su figura equivalente y que dispone de placa de características y de los marcados metrológicos reglamentariamente establecidos. En caso de que el instrumento de medida disponga de precintos electrónicos, se constatará que estos no han sido alterados y se dejará constancia de su valor en el certificado de verificación que se emita.

2.º En el caso de que el organismo autorizado de verificación metrológica observara que el precintado realizado por el fabricante del instrumento o por un reparador no cumpliera su función aun estando colocado en la posición y forma establecida en el procedimiento de evaluación de la conformidad correspondiente, informará de ello electrónicamente y en un plazo máximo de tres días, a la administración pública competente para que esta adopte las medidas que considere oportunas.

3.º Si en el examen administrativo, el organismo autorizado de verificación metrológica detectase incumplimientos relativos a los requisitos que los instrumentos de medida deben cumplir para estar legalmente en servicio, este lo pondrá inmediatamente en conocimiento del titular del instrumento de medida. La existencia de dichos incumplimientos no interrumpirá la realización del control de verificación solicitado.

4.º El organismo autorizado de verificación metrológica comunicará, de manera inmediata, a la administración pública competente los indicios de manipulación fraudulenta del instrumento de medida que haya detectado.

5.º El organismo autorizado de verificación metrológica deberá comprobar que los precintos accesibles colocados con motivo de la reparación o modificación por el reparador son conformes con lo dispuesto en la sección 4.ª del anexo III, del Real Decreto 244/2016, de 3 de junio.

b) Examen metrológico:

1.º El examen metrológico lo constituyen los exámenes y ensayos a realizar en la verificación después de reparación o modificación y se ajustará a lo indicado en el presente capítulo y en el anexo de cada instrumento de medida.

2.º En los instrumentos que cuenten con software legalmente relevante para su funcionamiento, se debe comprobar que este coincide en denominación y versión con el utilizado durante la puesta en servicio o las evaluaciones de la conformidad adicionales realizadas o la posible verificación después de una modificación.

3.º En aquellos instrumentos en los que la exactitud del resultado de la medida pueda verse afectado dependiendo del distinto uso que se dé al mismo, se comprobará que estos se utilizan para las aplicaciones de medida para los que fueron puestos en servicio.

4.º El resultado de la verificación no podrá ser favorable hasta que no se supere el examen administrativo y todos los ensayos previstos en el examen metrológico.

> _Nota BOE: Se modifica la letra a) por el art. único.1 de la Orden ITU/1475/2024, de 17 de diciembre. Ref. BOE-A-2024-27147_

<!-- bloque a1-2 · versión publicada 20200224 · vigente desde 20201024 -->

### Artículo 10. Errores máximos permitidos.

1. En el anexo de cada instrumento de medida se establecen los errores máximos permitidos en la verificación después de reparación o modificación.

2. El instrumento de medida no explotará el error máximo permitido ni favorecerá sistemáticamente a ninguna de las partes.

<!-- bloque a1-3 · versión publicada 20241227 · vigente desde 20250116 -->

### Artículo 11. Conformidad.

1. Superada la verificación después de reparación o modificación, el organismo autorizado de verificación metrológica hará constar la conformidad del instrumento de medida para efectuar su función mediante la adhesión de una etiqueta en un lugar visible del instrumento de medida verificado, que deberá reunir las características y requisitos que se establecen en el anexo III del Real Decreto 244/2016, de 3 de junio, especificando en la misma el tipo de instrumento de medida de que se trate.

2. El organismo autorizado de verificación metrológica que haya llevado a cabo la verificación precintará el instrumento manteniendo los precintos colocados por el reparador como consecuencia de su actuación y emitirá el correspondiente certificado de verificación en un plazo máximo de 10 días. Se deberá anotar en el certificado de verificación la identificación y localización de todos los precintos accesibles, incluidos los electrónicos, y distinguirá en el mismo si la verificación ha sido verificación después de reparación o verificación después de modificación.

3. A excepción de aquellos casos previstos en el artículo 12.4 de la Ley 32/2014, de 22 de diciembre, para los que la reparación no podrá alterar el plazo de verificación periódica, la verificación después de reparación o modificación tendrá efectos de verificación periódica respecto al cómputo del plazo para la solicitud de la misma.

> _Nota BOE: Se modifica el apartado 2 por el art. único.2 de la Orden ITU/1475/2024, de 17 de diciembre. Ref. BOE-A-2024-27147_

<!-- bloque a1-4 · versión publicada 20241227 · vigente desde 20250116 -->

### Artículo 12. No superación de la verificación.

Cuando un instrumento de medida no supere la verificación después de reparación o modificación, el organismo autorizado de verificación metrológica deberá colocar la etiqueta de inhabilitación para el servicio, de acuerdo con el artículo 5 del anexo III del Real Decreto 244/2016, de 3 de junio, especificando en la misma el tipo de instrumento de medida de que se trata. También emitirá un informe desfavorable de la verificación en un plazo máximo de 5 días, en el que se especifiquen los motivos concretos de la no superación de la verificación, y comunicará electrónicamente la no superación, en este mismo plazo, a la administración pública competente. El instrumento de medida no podrá utilizarse para los fines estipulados en el apartado 1 del artículo 8 de la Ley 32/2014, de 22 de diciembre, hasta que se subsane la deficiencia y se solicite una nueva verificación después de reparación. Estos instrumentos, en su caso, estarán a lo dispuesto en el artículo 8 de esta orden.

> _Nota BOE: Se modifica por el art. único.3 de la Orden ITU/1475/2024, de 17 de diciembre. Ref. BOE-A-2024-27147_

### Capítulo IV (selección). Verificación periódica

<!-- bloque a1-6 · versión publicada 20241227 · vigente desde 20250116 -->

### Artículo 14. Sujetos obligados y solicitudes.

1. Como mínimo un mes antes de que transcurra el periodo determinado en el anexo de cada instrumento de medida, el titular del mismo solicitará su verificación ante un organismo autorizado de verificación metrológica, o, si es el caso, ante la administración pública competente que actúe como organismo. Dicha solicitud se realizará electrónicamente y tendrá los datos establecidos en el anexo XIX.

Transcurrido el plazo para que un instrumento de medida tenga que ser objeto de verificación periódica, este no podrá ser utilizado para los fines estipulados en el apartado 1 del artículo 8 de la Ley 32/2014, de 22 de diciembre, hasta que no la supere.

2. El plazo que se establece en los anexos de cada instrumento de medida comenzará a contar para la primera verificación desde la fecha de la puesta en servicio del instrumento de medida, entendida como la primera utilización por el usuario final. Se podrá acreditar la fecha de puesta en servicio, conforme a las reglas siguientes:

a) Mediante el acta, certificado o documento análogo de puesta en servicio del instrumento de medida, suscrita por el vendedor y el usuario final.

b) En defecto del documento anterior, serán válidos para determinar la fecha de puesta en servicio el albarán de entrega o la factura de compra y, si no existiesen tales documentos, se podrá acreditar por cualquier otro medio, válido en derecho que deje constancia fidedigna de la fecha de la puesta en servicio.

3. En caso de que no se pueda acreditar la fecha de puesta en servicio del instrumento de medida por ninguno de los medios previstos en los apartados anteriores se considerará que esta se produjo el día 1 de enero del año en el que se colocó el marcado de conformidad definido en el artículo 2.y) del Real Decreto 244/2016, de 3 de junio.

4. La segunda verificación periódica y siguientes, salvo que se establezca otra cosa en el anexo específico del instrumento de medida, se realizarán en los mismos plazos y con los mismos condicionamientos que la primera, a contar desde la fecha del certificado de la verificación anterior.

5. Una vez realizada la solicitud de verificación periódica de un instrumento de medida, los organismos autorizados de verificación metrológica dispondrán de un periodo máximo de un mes para proceder a su verificación.

> _Nota BOE: Se modifica el apartado 1 por el art. único.4 de la Orden ITU/1475/2024, de 17 de diciembre. Ref. BOE-A-2024-27147_

<!-- bloque a1-7 · versión publicada 20241227 · vigente desde 20250116 -->

### Artículo 15. Examen y ensayos.

Los instrumentos de medida deberán superar un examen administrativo y un examen metrológico.

a) Examen administrativo:

1.º El examen administrativo consiste en la identificación completa del instrumento de medida y la comprobación de que este reúne los requisitos exigidos para estar legalmente en servicio. El examen se realizará tomando como base la información aportada por el solicitante mediante la solicitud de verificación que se recoge en el anexo XIX de esta orden. Asimismo, el examen comprenderá la comprobación de que el instrumento de medida tiene los precintos en la localización indicada en su evaluación de la conformidad o en su figura equivalente y que dispone de placa de características y de los marcados metrológicos reglamentariamente establecidos. En caso de que el instrumento de medida disponga de precintos electrónicos, se constatará que estos no han sido alterados y se dejará constancia de su valor en el certificado de verificación que se emita.

2.º En el caso de que el organismo autorizado de verificación metrológica observara que el precintado realizado por el fabricante del instrumento o por un reparador no cumpliera su función aun estando colocado en la posición y forma establecida en el procedimiento de evaluación de la conformidad correspondiente, informará de ello, electrónicamente y en un plazo máximo de tres días, a la administración pública competente para que esta adopte las medidas que considere oportunas.

3.º Si en el examen administrativo, el organismo autorizado de verificación metrológica detectase incumplimientos relativos a los requisitos que los instrumentos de medida deben cumplir para estar legalmente en servicio, este lo pondrá inmediatamente en conocimiento del titular del instrumento de medida. La existencia de dichos incumplimientos no interrumpirá la realización del control de verificación solicitado.

4.º El organismo autorizado de verificación metrológica comunicará, de manera inmediata, a la administración pública competente los indicios de manipulación fraudulenta del instrumento de medida que haya detectado.

5.º El organismo autorizado de verificación metrológica deberá comprobar que los precintos accesibles del instrumento son conformes con lo establecido en su evaluación de la conformidad o con los indicados en su último certificado de verificación, según proceda.

b) Examen metrológico:

1.º El examen metrológico lo constituye los exámenes y ensayos a realizar en la verificación periódica se ajustarán a lo indicado en el presente capítulo y en el anexo de cada instrumento de medida.

2.º En los instrumentos que cuenten con software legalmente relevante para su funcionamiento, se debe comprobar que este coincide en denominación y versión con el utilizado durante la puesta en servicio o las evaluaciones de la conformidad adicionales realizadas o la posible verificación después de una modificación.

3.º En aquellos instrumentos en los que la exactitud del resultado de la medida pueda verse afectado dependiendo del distinto uso que se dé al mismo, se comprobará que estos se utilizan para las aplicaciones de medida para los que fueron puestos en servicio.

4.º El resultado de la verificación no podrá ser favorable hasta que no se supere el examen administrativo y todos los ensayos previstos en el examen metrológico.

> _Nota BOE: Se modifica la letra a) por el art. único.5 de la Orden ITU/1475/2024, de 17 de diciembre. Ref. BOE-A-2024-27147_

<!-- bloque a1-8 · versión publicada 20200224 · vigente desde 20201024 -->

### Artículo 16. Errores máximos permitidos.

1. En el anexo de cada instrumento de medida se establecen los errores máximos permitidos en la verificación periódica.

2. El instrumento de medida no explotará el error máximo permitido ni favorecerá sistemáticamente a ninguna de las partes.

<!-- bloque a1-9 · versión publicada 20241227 · vigente desde 20250116 -->

### Artículo 17. Conformidad.

1. Superada la verificación periódica, el organismo autorizado de verificación metrológica hará constar la conformidad del instrumento de medida para efectuar su función mediante la adhesión de una etiqueta en un lugar visible del instrumento verificado, que deberá reunir las características y requisitos que se establecen en el anexo III del Real Decreto 244/2016, de 3 de junio, especificando en la misma el tipo de instrumento de medida de que se trate.

2. El organismo autorizado de verificación metrológica que haya llevado a cabo la verificación emitirá el correspondiente certificado de verificación en un plazo máximo de diez días. Se deberá anotar en el certificado de verificación la identificación y localización de todos los precintos accesibles, incluidos los electrónicos.

> _Nota BOE: Se modifica el apartado 2 por el art. único.6 de la Orden ITU/1475/2024, de 17 de diciembre. Ref. BOE-A-2024-27147_

<!-- bloque a1-10 · versión publicada 20241227 · vigente desde 20250116 -->

### Artículo 18. No superación de la verificación.

Cuando un instrumento de medida no supere la verificación periódica, el organismo autorizado de verificación metrológica deberá colocar la etiqueta de inhabilitación para el servicio, de acuerdo con el artículo 5 del anexo III del Real Decreto 244/2016, de 3 de junio, especificando en la misma el tipo de instrumento de medida de que se trata. También emitirá un informe desfavorable de la verificación en un plazo máximo de 5 días, en el que se especifiquen los motivos concretos de la no superación de la verificación, y comunicará electrónicamente la no superación, en este mismo plazo, a la administración pública competente. El instrumento de medida no podrá utilizarse para los fines estipulados en el apartado 1 del artículo 8 de la Ley 32/2014, de 22 de diciembre, hasta que se subsane la deficiencia y se solicite una nueva verificación después de reparación. Estos instrumentos, en su caso, estarán a lo dispuesto en el artículo 8 de esta orden.

> _Nota BOE: Se modifica por el art. único.7 de la Orden ITU/1475/2024, de 17 de diciembre. Ref. BOE-A-2024-27147_

### Disposiciones (selección)

<!-- bloque dt-2 · versión publicada 20200224 · vigente desde 20201024 -->

### Disposición transitoria segunda. Instrumentos en servicio.

Los instrumentos de medida que se encuentren legalmente en servicio a la entrada en vigor de esta orden podrán seguir siendo utilizados mientras superen las verificaciones establecidas para los instrumentos en servicio en los términos indicados en el capítulo IV de esta orden y en los anexos correspondientes. No se les podrá exigir el cumplimiento de requisitos adicionales a los determinados durante el proceso de su puesta en servicio.

<!-- bloque dd · versión publicada 20200224 · vigente desde 20201024 -->

### Disposición derogatoria única. Derogación normativa.

Quedan derogadas cuantas disposiciones de igual o inferior rango se opongan a lo dispuesto en esta orden y en particular las siguientes:

[…]

m) Orden ITC/3123/2010, de 26 de noviembre, por la que se regula el control metrológico del Estado de los instrumentos destinados a medir la velocidad de circulación de vehículos a motor.

[…]

<!-- bloque df-5 · versión publicada 20200509 · vigente desde 20200510 -->

### Disposición final quinta. Entrada en vigor.

Esta orden entrará en vigor a los ocho meses de su publicación en el “Boletín Oficial del Estado”.

> _Nota BOE: Se modifica por la disposición final 1 de la Orden ICT/397/2020, de 30 de abril. Ref. BOE-A-2020-4901_

## 4. Orden ICT/155/2020, anexo XII: cinemómetros (completo)

<!-- bloque ax-3 · versión publicada 20200224 · vigente desde 20201024 -->

ANEXO XII

Instrumentos destinados a medir la velocidad de circulación de vehículos a motor

<!-- bloque a1-23 · versión publicada 20200224 · vigente desde 20201024 -->

### Apartado 1. Objeto.

Constituye el objeto de este anexo la regulación del control metrológico del Estado de los instrumentos que miden la velocidad de circulación de vehículos a motor, denominados en adelante cinemómetros, tanto cuando realizan su función básica de medir velocidad, como cuando dispongan de otras opciones de medida, tales como la distancia intervehicular, cuantificada en tiempo de separación entre vehículos, o la distancia al objetivo necesaria para la identificación o determinación del carril de circulación.

<!-- bloque a2-13 · versión publicada 20200224 · vigente desde 20201024 -->

### Apartado 2. Fases del control metrológico del Estado.

El control metrológico del Estado establecido en este anexo es el que se regula en las secciones 3.ª y 4.ª del capítulo III del Real Decreto 244/2016, de 3 de junio, que se refieren respectivamente a las fases de evaluación de la conformidad y de instrumentos en servicio.

<!-- bloque a3-13 · versión publicada 20200224 · vigente desde 20201024 -->

### Apartado 3. Fase de evaluación de la conformidad.

La fase de la evaluación de la conformidad aplicable a la comercialización y puesta en servicio de los cinemómetros está recogida en el capítulo II de esta orden.

Los cinemómetros deberán cumplir los requisitos esenciales comunes de los instrumentos de medida aplicables del anexo II del Real Decreto 244/2016, de 3 de junio, además de los requisitos específicos incluidos en el apéndice I de este anexo, cuyo cumplimiento se constatará a través del procedimiento técnico de ensayos establecido en el apéndice II de este anexo.

El módulo que se utilizará para llevar a cabo la evaluación de la conformidad de los cinemómetros es:

a) Módulo B, examen de tipo, más Módulo F, conformidad con el tipo basada en la verificación del producto.

<!-- bloque a4-13 · versión publicada 20200224 · vigente desde 20201024 -->

### Apartado 4. Verificación después de reparación o modificación.

La verificación después de reparación o modificación de los cinemómetros se realizará conforme al capítulo III de esta orden y a lo indicado en el apéndice III de este anexo.

<!-- bloque a5-12 · versión publicada 20200224 · vigente desde 20201024 -->

### Apartado 5. Verificación periódica.

La verificación periódica se realizará conforme al capítulo IV de esta orden y a lo indicado en el apéndice IV de este anexo.

El plazo de verificación periódica será de un año.

<!-- bloque a6-12 · versión publicada 20200224 · vigente desde 20201024 -->

### Apartado 6. Ensayos y errores máximos permitidos en la verificación después de reparación o modificación y en la verificación periódica.

Los ensayos a realizar en la verificación después de reparación o modificación y en la verificación periódica de estos instrumentos serán los indicados en los apéndices III y IV de este anexo, respectivamente.

Los errores máximos permitidos se establecen en el apéndice I.

Estos instrumentos deberán seguir cumpliendo los requisitos que dieron origen a su comercialización y puesta en servicio.

<!-- bloque ai-34 · versión publicada 20200224 · vigente desde 20201024 -->

APÉNDICE I

Requisitos esenciales específicos para cinemómetros

1. Requisitos generales.

1.1 El cinemómetro debe estar concebido de tal manera que todos los elementos que lo componen puedan funcionar y mostrar resultados autónomamente a efectos de que puedan ensayarse de forma independiente.

1.2 Los cinemómetros se conectarán a un dispositivo de filmación o de registro fotográfico. Debe asegurarse la correspondencia de la identificación del vehículo cuya velocidad mide el cinemómetro con la que aparece en los registros. También debe identificarse, sin ambigüedad, en la filmación o en el registro fotográfico el vehículo cuya velocidad se mide, así como garantizar la integridad de esta filmación. Los datos recogidos en la filmación o en el registro fotográfico deben coincidir con los indicados por el cinemómetro e informará, al menos, sobre los siguientes aspectos:

i. La fecha y hora de la medida,

ii. la velocidad medida del vehículo infractor,

iii. si el cinemómetro mide en ambos sentidos, indicación del sentido de desplazamiento del vehículo infractor,

iv. identificación del cinemómetro que realizó la medida y ubicación (si procede).

1.3 Los cinemómetros deben estar dotados de un dispositivo selector de velocidades que permita identificar las velocidades superiores a un valor predeterminado.

1.4 El resultado de cada medida, igual o superior al valor predeterminado por el dispositivo selector de velocidades, debe visualizarse mientras no intervenga el operador, o hasta la siguiente medida. Cuando deje de visualizarse el resultado, y salvo en el caso de que este quede registrado, la medida siguiente no podrá efectuarse antes de un periodo de tres segundos.

1.5 El cinemómetro no deberá medir simultáneamente la velocidad de los vehículos en los dos sentidos de circulación cuando no puedan asegurarse estas mediciones.

1.6 En función de su tipo de instalación y a efectos de considerar los errores máximos permitidos, los cinemómetros pueden ser:

i. Fijos, cuando van instalados sobre emplazamientos permanentes y funcionan de forma autónoma sin la presencia de un operador;

ii. estáticos, cuando van instalados de forma no permanente sobre un emplazamiento inmóvil, al menos, durante la realización de la medición y con la intervención del operador, presencial o remoto;

iii. móviles, cuando van instalados firmemente sobre un vehículo y realizan mediciones con este en movimiento, teniendo en cuenta su propia velocidad. Estos también pueden realizar mediciones con el vehículo parado, en este caso se consideran estáticos.

1.7 Los cinemómetros fijos para la medida de la velocidad instantánea, generalmente, van ubicados en contenedores o cabinas, que le sirven de alojamiento, soporte y protección. Si la cabina influye en las características metrológicas del cinemómetro, deberá cumplir los requisitos que se establecen en este anexo.

1.8 Los cinemómetros móviles deben determinar de forma simultánea la velocidad de los dos vehículos (del que mide y en el que va instalado). La instalación de los cinemómetros móviles en vehículos que utilizan su señal tacométrica, debe realizarse disponiendo de los precintos que garanticen y aseguren su conexión al tacómetro.

1.9 Los cinemómetros que funcionen desde emplazamientos estáticos, en presencia de un operador que vigile su funcionamiento, deberán colocarse sobre trípode u otro tipo de soporte estable, respetando los ángulos de apuntamiento, siguiendo las instrucciones del manual del equipo y las que indique su certificado de evaluación de la conformidad.

1.10 A los cinemómetros que funcionen sin la presencia continua de un operador que vigile su funcionamiento y que no sean capaces de detectar, seguir e identificar inequívocamente el objetivo durante todo el proceso de medición, se les exigirá al menos dos fotogramas del vehículo infractor tomados en diferentes instantes: uno de ellos mostrará una visión panorámica del vehículo y el otro, su placa de identificación.

1.11 La instalación de los cinemómetros en su ubicación definitiva deberá realizarse por medio de un dispositivo que permita ajustarlo de manera estable siguiendo las instrucciones del fabricante. Su contribución a la incertidumbre relativa del sistema de medida no debe ser mayor que el 0,5 %.

1.12 Cuando dos o más vehículos con velocidades diferentes entren simultáneamente en el campo de medida, el cinemómetro no debe dar lectura de velocidad a no ser que sea capaz de detectar, seguir e identificar inequívocamente los objetivos durante todo el proceso de medición.

1.13 La documentación técnica suministrada por el fabricante debe especificar los elementos que forman el cinemómetro, así como el número y ubicación de los precintos, tanto en el cinemómetro como en otros elementos de soporte y conexión, y explicar los detalles para el correcto posicionamiento y ajuste del cinemómetro para todas las instalaciones posibles (vehículos, cabinas, trípodes, aeronaves u otras ubicaciones). Los precintos asegurarán la correcta alineación y el mantenimiento de las características metrológicas del cinemómetro.

1.14 Requisitos adicionales en caso de medida de distancia intervehicular:

i. Se documentará mediante dos fotografías tomadas durante la medición de la velocidad de ambos vehículos. Cada fotografía indicará la velocidad de los vehículos, la distancia entre ellos y la hora de la medida,

ii. la distancia entre vehículos se determinará en función de la velocidad medida de los vehículos y del tiempo que el segundo vehículo, circulando detrás del primero, necesita para alcanzar el punto en el que se realizó la medición de la velocidad del primer vehículo,

iii. el tiempo de separación entre vehículos, vendría dado por la fórmula:

t = d / v

donde,

d es la distancia entre vehículos;

v es la velocidad del vehículo que precede.

iv. El cinemómetro debe incluir evidencias del proceso de medición, como puede ser el registro en video con un campo de visión lo suficientemente amplio como para que durante varios segundos se aprecien las maniobras y se descarten situaciones en la vía que hubieran forzado a reducir la distancia de seguridad.

1.15 Requisitos adicionales en caso de control semafórico. Un cinemómetro combinado con sistema de vigilancia para la fase roja de semáforo (foto-rojo) funcionará como foto-rojo solo cuando se encuentre en la fase roja y cambiará automáticamente para funcionar como cinemómetro cuando no lo esté.

En el supuesto de que el cinemómetro se combine con sistemas de vigilancia para la fase roja de semáforos, deberá satisfacer los requisitos siguientes:

i. Los requisitos funcionales establecidos en la Norma UNE 199142-1. «Equipamiento para la gestión del tráfico. Visión artificial. Detección de vehículos infractores. Parte 1: especificación funcional y protocolos aplicativos para semáforo rojo», en vigor.

ii. Deberán garantizar en todo momento la seguridad de la circulación. Los tiempos de transición (duración de la fase amarilla entre verde y rojo) son los establecidos en las regulaciones aplicables.

iii. Estarán ubicados en emplazamientos fijos y de manera que se posibilite la conexión e intercambio de información de forma normalizada con uno o varios centros de control y tramitación de denuncias.

iv. La duración de la diferencia de tiempo (tiempo que transcurre entre el inicio de la fase rojo y la activación de la vigilancia correspondiente) no debe ser inferior a 0,5 segundos.

v. Las evidencias de infracción se documentarán mediante una secuencia de fotos, al menos cuatro fotografías que recojan una imagen de la parte trasera del vehículo y la luz roja del semáforo en las situaciones de vehículo antes de la línea de parada, vehículo sobrepasando la línea de parada y vehículo sobrepasado el cruce o paso de peatones completamente. Los registros fotográficos indicarán el tiempo en el que se tomaron las fotografías, el tiempo en el que el semáforo se puso en rojo y el tiempo en el que el vehículo cruzó la línea de parada. El tiempo se indicará con una resolución de 0,01 segundos.

La información generada y la integridad de los datos deben quedar garantizadas según el punto 2.1 de este apéndice.

Los dispositivos foto-rojo que no tienen asociada la función de medida de velocidad, pueden ser objeto de una comprobación de sus funcionalidades y parámetros de configuración, de acuerdo con la Norma UNE 199142-1 y según se establece en el punto 1.1 de este apéndice y en el apartado A), punto 2 del apéndice II.

1.16 Requisitos para las cabinas que influyan en las características metrológicas del cinemómetro:

i. Se entiende por cabina el contenedor que le sirve al cinemómetro de alojamiento, soporte y protección y dispone de los medios para su orientación y alimentación. Incorporará una placa de características que, al menos, indique su modelo, su número de serie, los datos de identificación del fabricante, la fecha de fabricación. No se considera cabina el vehículo sobre el que vaya instalado un cinemómetro móvil ni los emplazamientos sobre los que estén instalados los cinemómetros estáticos.

ii. El diseño y la fabricación de las cabinas y de sus anclajes al suelo o a la estructura en la que se ubique, así como a los elementos activos del cinemómetro, deberán tener la rigidez mecánica, aislamiento, seguridad y protección adecuados para su uso. A estos efectos, el fabricante deberá aportar la documentación acreditativa y la relación de las normas que cumple.

Una cabina que disponga de los necesarios anclajes, conexiones de datos y de alimentación normalizados puede acoger diferentes cinemómetros del mismo modelo o incluso de diferentes modelos o marcas, siempre que se garantice la orientación correcta de los sensores de captación o antenas del cinemómetro. De igual modo, un mismo cinemómetro puede instalarse en diferentes cabinas del mismo modelo.

2. Requisitos técnicos.

a) El cinemómetro estará concebido para que pueda respetar los errores máximos permitidos sin ajustes durante un período de un año de uso normal.

b) El cinemómetro estará equipado con un reloj de tiempo real para mantener la hora del día y la fecha. Se aplicarán al reloj los requisitos siguientes:

i. El registro horario tendrá una exactitud tal que su variación diaria sea inferior a 17 segundos,

ii. la posibilidad de corrección del reloj no será superior a dos minutos a la semana,

iii. la corrección del horario de verano y de invierno se efectuará automáticamente,

iv. para la medida del tiempo intervehicular, dispondrá de sensores que determinen los instantes en que se mide este tiempo, con la resolución suficiente y con ventanas de visualización del intervalo de tiempo medido y si procede, visualización de las distancias.

2.1 Protección.

2.1.1 Comunicaciones. Si el cinemómetro es capaz de comunicarse con otros dispositivos externos, las interfaces necesarias para estas comunicaciones deben estar protegidas de tal manera que no interfieran en el funcionamiento normal del cinemómetro.

Cuando se transfieran datos de medida a través de una red abierta, es necesario aplicar métodos criptográficos. Los códigos o claves de acceso que se utilizan para estos propósitos, deben ser confidenciales y mantenerse secretos y seguros en los cinemómetros, en sus dispositivos electrónicos, o en los subconjuntos implicados.

2.1.2 Software. La documentación de software suministrada por el fabricante, debe incluir como mínimo:

a) Una descripción del software relevante,

b) una descripción de la exactitud de los algoritmos de medición (por ejemplo, el algoritmo de redondeo al calcular la velocidad),

c) una descripción de la interfaz de usuario, de al menos los menús y los diálogos,

d) la identificación inequívoca del software,

e) una descripción del sistema informático,

f) los medios de aseguramiento del software,

g) el manual de operación,

h) cualquier otra información relevante a las características de software.

Los requisitos generales del software se describen en el anexo IV del Real Decreto 244/2016, de 3 de junio.

2.1.3 Precintos. Deben poder precintarse aquellos elementos en los que la manipulación puede conducir a errores de medida o a una reducción de la seguridad metrológica.

En la memoria técnica presentada para el examen de tipo se indicará el lugar de estos precintos, así como su naturaleza.

2.2 Inscripciones. Los cinemómetros o cada unidad que lo forma, deben presentar las siguientes inscripciones indelebles y legibles:

i. Nombre, nombre comercial registrado o marca registrada del fabricante,

ii. datos de identificación del cinemómetro e información sobre su exactitud,

iii. espacio para los marcados de conformidad.

3. Requisitos específicos.

3.1 Errores máximos permitidos (emp).

3.1.1 En la fase de evaluación de la conformidad. Los errores máximos permitidos en el examen de tipo, módulo B, y en la conformidad con el tipo basada en la verificación del producto, módulo F, se indican en la tabla 1.

Tabla 1. Errores máximos permitidos en la fase de evaluación de la conformidad

**Errores máximos permitidos Según tipo de instalación Para ensayos en laboratorio (por simulación) Para ensayos en carretera (tráfico real) Cinemómetro en instalación fija o estática y de tramo ± 2 km/h ± 3 km/h, para v ≤ 100 km/h ± 3 %, para v > 100 km/h ±1 km/h(1) Cinemómetro en instalación móvil sobre vehículo ± 5 km/h, para v ≤ 100 km/h ± 5 %, para v > 100 km/h Cinemómetro en aeronave Para la posición y medida de distancias: ± 3 % (valor mínimo 5 m) Para el tiempo transcurrido en recorrido de distancias: ± 0,1 % (valor mínimo 0,2 s) Para la medida de velocidad: ± 5 % Tiempo intervehicular (para distancia entre vehículos) ± 0,2 s ± 0,5 s**

(1) Error medio de todos los resultados en el examen de tipo.

3.1.2 En la fase de instrumentos en servicio. Los errores máximos permitidos en la verificación después de reparación o modificación son los mismos que los indicados en la tabla 1 de este apéndice.

Los errores máximos permitidos en la verificación periódica de cinemómetros son los que se indican en la tabla 2.

Tabla 2. Errores máximos permitidos en la verificación periódica

**Errores máximos permitidos Según tipo de instalación Para ensayos en laboratorio (por simulación de señales) Para ensayos en carretera (tráfico real) Cinemómetro en instalación fija o estática ± 2 km/h, para v ≤ 200 km/h ± 3 km/h, para v > 200 km/h ± 5 km/h, para v ≤ 100 km/h ± 5 %, para v > 100 km/h Cinemómetro en instalación móvil sobre vehículo ± 7 km/h, para v ≤ 100 km/h ± 7 %, para v > 100 km/h Tiempo intervehicular (para distancia entre vehículos) ± 0,2 s ± 0,8 s**

Para los cinemómetros de tramo y en aeronave, los errores máximos permitidos son los mismos que para la evaluación de la conformidad, indicados en el punto 3.1.1.

3.2 Condiciones de funcionamiento:

i. El intervalo de temperatura deberá estar comprendido como mínimo entre –10 ºC y 55 ºC.

ii. La clase de entorno mecánico aplicable es la M2 o en su lugar, la adecuada al emplazamiento previsto del cinemómetro, según lo establecido en el anexo II del Real Decreto 244/2016, de 3 de junio.

iii. La clase de entorno electromagnético aplicable es la E2 o en su lugar, la adecuada al emplazamiento previsto del cinemómetro, según lo establecido en el anexo II del Real Decreto 244/2016, de 3 de junio.

3.3 Influencias permitidas en perturbaciones mecánicas y electromagnéticas. La variación de un resultado de medida bajo la influencia de perturbaciones mecánicas y electromagnéticas no excederá al emp en laboratorio, en caso contrario debe indicar claramente que la indicación de la medida no es válida o el instrumento debe dejar de funcionar.

3.4 Requisitos específicos para cinemómetros de efecto Doppler. Los cinemómetros de efecto Doppler son los que utilizan un transmisor y un receptor de onda continua en la banda de las microondas y que operan bajo el principio Doppler. Miden la velocidad instantánea y están compuestos, generalmente, de una antena emisora y receptora, un elemento de evaluación y un dispositivo fotográfico, y deben satisfacer las exigencias siguientes:

i. La potencia de pico del lóbulo principal de emisión deberá ser superior al menos en 15 dB a la de los lóbulos secundarios en medidas directas, o en 30 dB después de la reflexión de la señal,

ii. el ancho del lóbulo principal a 3 dB, no debe sobrepasar los 7º en el plano de medida horizontal y, en el caso de medir en otros planos, los 9º en el plano de medida vertical; la desviación del eje mecánico respecto al eje de radiación no debe ser superior a 0,5º,

iii. la velocidad teórica v, en función de la frecuencia fd de la señal simulada de Doppler, se calculará por la fórmula:

v = 0,5 fd λ / cos α

donde,

λ es la longitud de onda de la radiación emitida por el radar;

α es el ángulo de incidencia respecto al eje de la calzada.

iv. los circuitos de microondas deben garantizar una estabilidad de frecuencia mejor que 0,15 % durante el periodo transcurrido entre verificaciones,

v. los puntos i) y ii) anteriores, no serán exigibles si el cinemómetro es capaz de detectar, seguir e identificar inequívocamente el objetivo y conocer su posición, durante todo el proceso de medición.

Estos cinemómetros irán dotados de un dispositivo que permita la simulación de una o más velocidades preestablecidas y representativas de las velocidades medidas en la práctica.

3.5 Requisitos específicos para cinemómetros de sensor. Los cinemómetros de sensor son aquellos que utilizan cables u otros dispositivos que van colocados sobre la calzada de tal manera que, cuando un vehículo cruza a través de él se produce algún cambio en sus propiedades físicas. Miden la velocidad instantánea y generalmente están formados por bandas piezoeléctricas que se insertan en la calzada a distancias conocidas y que al ejercerse sobre ellas una presión emiten impulsos que sirven para medir tiempos de corte.

Deberán estar diseñados para proporcionar dos lecturas de velocidad procedentes de, al menos, tres sensores. Las dos velocidades deberán compararse y, si la diferencia es menor que 2 km/h, se mostrará la velocidad más baja. Pueden utilizarse excepcionalmente dos sensores, en este caso, la medición deberá incluir al menos dos registros de la medida de la velocidad mediante la detección de la entrada y salida del vehículo por ambos sensores.

3.6 Requisitos específicos para cinemómetros ópticos. Los cinemómetros ópticos son los que utilizan haces de luz en la región visible o infrarroja del espectro electromagnético. Miden la velocidad instantánea del vehículo, que puede determinarse o por el procesamiento de la energía reflejada, o por la medición de los intervalos de tiempo entre interrupciones de los haces provocadas al ser atravesados por un vehículo. Estarán provistos de medios que permitan comprobar su verdadera alineación con el haz de luz.

La potencia de emisión de los cinemómetros que utilizan radiación láser, no debe ser dañina al ojo humano debiendo exceder la Clase 1, de acuerdo con las recomendaciones establecidas en la Norma UNE-EN 60825-1/A1. «Seguridad de los productos láser. Parte 1: Clasificación del equipo, requisitos y guía de seguridad», en vigor, relativa a la seguridad de los productos láser. El fabricante o solicitante presentará informes que justifiquen estos requisitos.

Estos cinemómetros pueden ser:

i. De barra láser: Consisten en doble o triple barrera luminosa, formada por emisiones láser y detectores que marcan el momento de interrupción del haz luminoso o el corte del haz por el vehículo. Conociendo la distancia que existe entre las barreras luminosas y el tiempo que transcurre entre cortes sucesivos del haz determina la velocidad del vehículo.

ii. de láser de mano: Cinemómetros estáticos que operan bajo el principio «distancia/tiempo». La velocidad se determina midiendo el tiempo de vuelo de una serie de pulsos cortos de luz generados por diodos láser infrarrojo, que al chocar contra un objetivo se reflejan y que una vez filtrados son detectados por los diodos. Un sistema controlado por un microprocesador mide el tiempo transcurrido entre la generación y detección de estos pulsos.

3.7 Requisitos específicos para cinemómetros de tramo. Los cinemómetros de tramo se utilizan para determinar la velocidad media en una distancia conocida.

a) Definiciones:

i. Distancia a medir. Es la longitud del carril de circulación de un tramo sometido a control de este tipo de cinemómetro. Dicho tramo está delimitado por los puntos referenciados y su distancia es la longitud de la línea de medición imaginaria más corta que lo recorre, acotada a ambos lados por las líneas de señalizaciones reales o imaginarias que lo delimitan,

ii. puntos referenciados. Son marcas o referencias en el terreno que indican o delimitan la distancia a medir. Poseen identificación propia y pueden servir también de ubicación o alojamiento para las cámaras de visión,

iii. cámaras de visión. Son cámaras de video para la visión o captación de matrículas de los vehículos objetos de la medición. Su funcionamiento, como regla general, se desarrolla en parejas de forma sincronizada, con relojes incorporados para la medición del tiempo y sensores que determinan el instante en que se empieza a medir este tiempo.

b) Composición.

Estos sistemas están formados generalmente por:

i. Cámaras de video o cualquier tipo de sensores o detectores interconectados e instalados en los puntos de referencia. Las instalaciones o ubicaciones de estas cámaras o sensores estarán perfectamente referenciados de tal manera que las cámaras puedan ser desmontadas e intercambiadas sin posibilidad de confusión,

ii. sistema o dispositivo de monitorización y registro. Es en el que se almacenan los datos de la medición, como son al menos: la distancia a medir, la identificación de los puntos o emplazamientos, los tiempos de registro y las velocidades resultantes,

iii. elementos de control. Son los que procesan las señales de todo tipo para el gobierno y control del proceso de medición. Estos elementos de control pueden ir integrados en las cámaras, formar parte de las cámaras y estar ubicados en la instalación o alejada de ella, o bien formar parte de un centro de control independiente y común para diferentes modelos de cámaras; este centro de control también puede asumir las funciones de monitorización y registro.

iv. otros dispositivos complementarios.

c) Funcionamiento.

El modo de operación o funcionamiento sería el siguiente:

i. Localización e identificación de la matrícula del vehículo u objetivo por la primera cámara y registro del tiempo, t,

ii. desplazamiento del vehículo a lo largo del tramo a medir,

iii. identificación del vehículo anterior por la segunda cámara y registro del tiempo, t2,

iv. cálculo del tiempo transcurrido entre t1 y t2, y, como consecuencia, de la velocidad media.

d) Otros requisitos.

i. El cinemómetro debe ser capaz de reconocer los puntos o ubicaciones donde están instaladas las cámaras que forman el sistema, a efectos de tener en cuenta los parámetros necesarios para la medición.

ii. El cinemómetro debe ser capaz de identificar de manera inequívoca el objetivo a medir, así como el punto de inicio y final de la medición.

iii. Los relojes de las cámaras emparejadas estarán perfectamente sincronizados entre sí, con desfases de tiempo inferiores a 1 segundo.

iv. Los valores de la distancia, así como del tiempo transcurrido entre los puntos de identificación del vehículo, cuando se visualicen o se impriman, se expresarán en las unidades siguientes:

– Distancia recorrida: en kilómetros o metros,

– tiempo transcurrido: en horas, minutos o segundos según corresponda teniendo en cuenta la resolución necesaria,

– velocidad: en kilómetros por hora.

3.8 Requisitos específicos para cinemómetros en aeronave. Estos cinemómetros pueden ir ubicados en helicópteros, drones, aviones de ala fija u otros sistemas de navegación y se utilizan para determinar la velocidad de un vehículo desde el aire. Van montados generalmente sobre plataformas o torretas aeronáuticas a bordo de aeronaves y son capaces de medir la velocidad de los vehículos a motor por identificación y seguimiento.

a) Algunas definiciones.

i. Torretas optrónicas. Son plataformas aeronáuticas giroestabilizadas que sirven para determinar las coordenadas de posición del vehículo (longitud, latitud y altura).

ii. Línea de mira georreferenciada. Es la dirección en el espacio terrestre que señalan las cámaras del sistema.

iii. Sistema de medición inercial. Es la combinación de un sistema de navegación inercial propio alojado en la torreta y un receptor GNSS, que sirve para determinar con precisión la línea de mira.

iv. Latitud. Es la distancia angular, medida sobre un meridiano, entre una localización terrestre y el Ecuador. Se mide en unidades angulares, generalmente grados y decimales de grado o grados, minutos y segundos.

v. Longitud. Es la medida que expresa la distancia horizontal, paralela al Ecuador, entre el meridiano de Greenwich y un determinado punto de la tierra. Se mide en unidades angulares, generalmente grados y decimales de grado o grados, minutos y segundos.

vi. Geolocalización. Es la capacidad de conocer o localizar el objetivo mediante la línea de mira georreferenciada y su intersección con la superficie de la Tierra, a través de su longitud y su latitud.

vii. Geoseñalización. Es la capacidad de definir la latitud, la longitud y altura de un punto en la superficie terrestre dentro de un sistema.

viii. Geoseguimiento. Es la capacidad de seguir un vehículo en el tiempo a través de la evolución de su latitud y longitud.

b) Composición.

Este tipo de cinemómetros pueden estar formados por:

i. Plataforma giro estabilizada, pudiendo llevar los siguientes elementos:

– Cámaras de video,

– sistema de seguimiento automático por video (autotracker),

– sistema de seguimiento por coordenadas geográficas (geotracking),

ii. sistema inercial de medidas (IMU),

iii. sistema de recepción de señales GNSS,

iv. sistema de medición de distancias o telémetro láser,

v. sistema de cálculo o unidad de proceso, que recoge la información de la cámara, la procesa y calcula la velocidad del vehículo identificado,

vi. otros dispositivos complementarios, que integran el sistema sobre la aeronave, como monitores de visualización, sistemas de grabación y registro de datos.

c) Funcionamiento.

A modo de ejemplo, sin que se excluyan futuras tecnologías, el funcionamiento de un sistema formado por los dispositivos enumerados anteriormente, sería el siguiente:

i. Localización del vehículo,

ii. seguimiento del mismo mediante autotracker y geotracking,

iii. determinación de la velocidad del vehículo en las siguientes etapas:

– determinación de la latitud y longitud (georreferencia) de un vehículo en movimiento en el tiempo t1,

– determinación de la latitud y longitud (georreferencia) del mismo vehículo en el tiempo t2,

– cálculo del tiempo transcurrido entre t1 y t2,

– diferencia entre las posiciones georreferenciadas (t1 y t2),

– cálculo de la velocidad a partir de las posiciones y del tiempo transcurrido.

Las torretas aeronáuticas tendrán capacidad de autoalineación independiente de la aeronave donde están instaladas, pudiendo ser intercambiables entre distintas aeronaves.

El cinemómetro debe proporcionar y monitorizar de forma clara e independiente los siguientes datos a través de una o varias interfaces protegidas y adecuadas:

– La posición del objetivo en distintos tiempos de observación,

– la distancia medida entre dos puntos observados,

– el tiempo transcurrido entre ambas observaciones.

Si las características de la aeronave son importantes para la corrección de las medidas realizadas por el cinemómetro, este contará con medios para garantizar la conexión del mismo a la aeronave en el que va instalado.

Para la realización de ensayos después de la instalación, el cinemómetro tendrá la opción de poder comprobar por métodos auxiliares la exactitud de las medidas de tiempo y distancia, de forma independiente, así como del cálculo de la velocidad.

3.9 Requisitos específicos para otros cinemómetros. Otros tipos de cinemómetros, pueden ser: de visión artificial, de ultrasonidos, de definición, y de otras tecnologías válidas.

Los cinemómetros que utilizan otro tipo de tecnologías diferentes a las descritas en este apéndice, tendrán que demostrar que cumplen con los requisitos establecidos en este anexo.

> _Nota BOE: Redactado conforme a la corrección de errores publicada en BOE núm. 126 de 6 de mayo de 2020. Ref. BOE-A-2020-4833_

> **Nota ggLaw (no es texto legal): reconstrucción de las tablas 1 y 2 del apéndice I.**
> `boe_fetch.py` las aplana en una línea (arriba, en negrita). Aquí se reproducen las
> mismas celdas del XML del BOE, fila a fila, con sus atributos `rowspan`/`colspan`. El
> texto de cada celda es literal; la disposición en filas es de elaboración propia.
>
> **Tabla 1. Errores máximos permitidos en la fase de evaluación de la conformidad**
>
> | Según tipo de instalación | Para ensayos en laboratorio (por simulación) | Para ensayos en carretera (tráfico real) |
> |---|---|---|
> | Cinemómetro en instalación fija o estática y de tramo | ± 2 km/h *(celda con rowspan=2: vale también para la fila siguiente)* | ± 3 km/h, para v ≤ 100 km/h · ± 3 %, para v > 100 km/h · ±1 km/h(1) |
> | Cinemómetro en instalación móvil sobre vehículo | *(la celda anterior)* | ± 5 km/h, para v ≤ 100 km/h · ± 5 %, para v > 100 km/h |
> | Cinemómetro en aeronave | *(celda con colspan=2)* Para la posición y medida de distancias: ± 3 % (valor mínimo 5 m) · Para el tiempo transcurrido en recorrido de distancias: ± 0,1 % (valor mínimo 0,2 s) · Para la medida de velocidad: ± 5 % | |
> | Tiempo intervehicular (para distancia entre vehículos) | ± 0,2 s | ± 0,5 s |
>
> (1) Error medio de todos los resultados en el examen de tipo.
>
> **Tabla 2. Errores máximos permitidos en la verificación periódica**
>
> | Según tipo de instalación | Para ensayos en laboratorio (por simulación de señales) | Para ensayos en carretera (tráfico real) |
> |---|---|---|
> | Cinemómetro en instalación fija o estática | ± 2 km/h, para v ≤ 200 km/h · ± 3 km/h, para v > 200 km/h *(rowspan=2)* | ± 5 km/h, para v ≤ 100 km/h · ± 5 %, para v > 100 km/h |
> | Cinemómetro en instalación móvil sobre vehículo | *(la celda anterior)* | ± 7 km/h, para v ≤ 100 km/h · ± 7 %, para v > 100 km/h |
> | Tiempo intervehicular (para distancia entre vehículos) | ± 0,2 s | ± 0,8 s |

<!-- bloque ai-35 · versión publicada 20241227 · vigente desde 20250116 -->

APÉNDICE II

Procedimiento técnico de ensayos para la evaluación de la conformidad de cinemómetros

En la fase de evaluación de conformidad, el solicitante aportará los medios necesarios para garantizar la correcta alineación del equipo.

La evaluación de la conformidad de un cinemómetro con los requisitos que le son de aplicación se llevará a cabo aplicando el módulo B (examen de tipo) y el módulo F (conformidad con el tipo basada en la verificación del producto).

El sistema de medida utilizado como referencia para la comparación de los resultados de los cinemómetros debe tener una incertidumbre inferior a 1/3 del error máximo permitido para el cinemómetro sometido a ensayo.

A) Examen de tipo de cinemómetros (módulo B).

El examen de tipo de los cinemómetros deberá efectuarse de acuerdo con lo dispuesto en el artículo 5 del anexo I, del Real Decreto 244/2016, de 3 de junio.

Los ensayos se realizarán sobre el equipo completo, para lo cual el solicitante deberá aportar todas las partes integrantes del cinemómetro, junto con los dispositivos complementarios destinados a imprimir o registrar los resultados de las medidas efectuadas. En caso de cinemómetros de tramo que utilicen un centro de control independiente como elemento de control del proceso de medición, se deberá aportar un certificado o informe de evaluación de software del centro, que asegure y garantice las mediciones realizadas y cumplir los demás requisitos establecidos en este anexo.

Para la realización de los ensayos de simulación de velocidad y distancia, en su caso, el fabricante facilitará un conjunto de simulación adecuado a cada tipo de cinemómetro que deberá ir provisto de salidas o tomas de información del tipo bus CAN, puertos RS 232 o similares, con posibilidad de transmisión de la información vía radio al centro de verificación para su comparación. En caso de que el fabricante no pueda facilitar el conjunto de simulación, por motivos técnicamente justificados, los ensayos podrán ser sustituidos por ensayos en circuitos con medida de velocidades de hasta 250 km/h.

Junto con el equipo, se acompañará la documentación técnica que se establece en el artículo 13 del Real Decreto 244/2016, de 3 de junio.

El fabricante especificará las condiciones de funcionamiento aplicables al cinemómetro. En particular:

i. El entorno climático que deberá estar comprendido como mínimo entre –10 ºC y 55 ºC,

ii. la clase de entorno mecánico en la que el cinemómetro debe utilizarse,

iii. la clase de entorno electromagnético.

Se examinará la documentación presentada, se comprobará la conformidad con este anexo y se realizarán los siguientes ensayos:

1. Ensayos en laboratorio en condiciones nominales.

1.1 Ensayos de funcionamiento:

– Funcionamiento general. Comprobación del dispositivo de selección de velocidades, del visualizador de las medidas y de los demás dispositivos o subsistemas,

– dispositivos de calibración interna. Comprobación de la exactitud de las velocidades simuladas,

– alarma de tensión. Comprobación de la alarma del cinemómetro ante variaciones de la tensión de alimentación por debajo de los límites establecidos,

– disparo de la cámara fotográfica: Después de conectar el cinemómetro con la cámara, se comprobará la transmisión de los datos a la misma una vez conformado el valor de la medida.

1.2 Ensayos de simulación. Estos ensayos consisten en proyectar, de forma no intrusiva, sobre el cinemómetro a ensayar escenarios virtuales o en transmitir señales ópticas o eléctricas representativas, capaces de simular el paso de vehículos u objetivos, a diferentes velocidades y distancias si procede.

Este método de ensayo será de aplicación a los cinemómetros cuya evaluación de la conformidad se realice a partir de la entrada en vigor de esta orden.

1.3 Ensayo de antena (para equipos que utilizan el efecto Doppler). Estos ensayos deben realizarse en cámaras anecoicas con anecoización completa sobre recinto apantallado, y con características y dimensiones adecuadas a las frecuencias de emisión de los cinemómetros.

Se deben realizar ensayos que permitan obtener, para cada plano de polarización de medida, los siguientes parámetros de antena:

– La atenuación de los lóbulos secundarios respecto del lóbulo principal,

– el ancho del lóbulo principal a 3 dB de atenuación,

– la desviación del eje mecánico respecto al eje de radiación,

– la estabilidad de la frecuencia de radiación.

1.4 Ensayos de factores de influencia y perturbaciones. Los procedimientos aplicables a los ensayos que se describen a continuación serán conformes con las versiones en vigor de los documentos normativos o normas armonizadas aprobadas internacionalmente. Todos estos ensayos se realizarán con el cinemómetro en condiciones de operación.

Durante estos ensayos los cinemómetros deberán:

i. Funcionar correctamente y respetar los errores máximos permitidos, o

ii. no mostrar indicación del resultado de la medida, volviendo a la normalidad después del ensayo.

1.4.1 Ensayos en entorno climático.

– Calor seco. Normativa aplicable: Norma UNE-EN 60068-2-2. «Ensayos ambientales. Parte 2-2: Ensayos. Ensayo B: Calor seco. (IEC)», y Norma UNE-EN 60068-3-1. «Ensayos ambientales. Parte 3-1: Información básica. Ensayos de frío y de calor seco».

Consiste en una exposición del cinemómetro a una temperatura de +55 ºC durante 2 horas.

– Frío. Normativa aplicable: Norma UNE-EN 60068-2-1. «Ensayos ambientales. Parte 2-1: Ensayos. Ensayo A: Frío», y Norma UNE-EN 60068-3-1 «Ensayos ambientales. Parte 3-1: Información básica. Ensayos de frío y de calor seco».

Consiste en una exposición del cinemómetro a una temperatura de –10 ºC durante 2 horas.

– Calor húmedo. Normativa aplicable: Norma UNE-EN 60068-2-30. «Ensayos ambientales. Parte 2-30: Ensayos. Ensayo Db: Ensayo cíclico de calor húmedo (ciclo de 12 h + 12 h)», y Norma UNE-EN 60068-3-4. «Ensayos ambientales. Parte 3-4: Documentación de acompañamiento y guía. Ensayos de calor húmedo».

Consiste en una exposición del cinemómetro a variaciones cíclicas de temperatura entre 25 ºC y 55 ºC, manteniendo la humedad relativa entre 93 % y 95 %.

Se realizarán dos ciclos de este ensayo.

– Salpicaduras de partes expuestas al agua. Se proyectará un volumen de agua de aproximadamente 10 litros, desde una distancia de 3 metros, contra cada lado del cinemómetro sobre las partes expuestas al aire libre, una vez por la parte superior y otra por la parte inferior, estando el cinemómetro operativo. Las salpicaduras no deben penetrar en el interior del cinemómetro ni provocar indicaciones erróneas.

Este ensayo no será necesario aplicarlo a los cinemómetros destinados a ser operados desde vehículos terrestres o aéreos o desde soportes portátiles tipo trípode.

1.4.2 Ensayos en entorno mecánico. Estos ensayos se aplicarán exclusivamente a los cinemómetros destinados a ser operados desde vehículos terrestres o aéreos o desde soportes portátiles tipo trípode.

– Vibraciones aleatorias. Normativa aplicable: Norma UNE-EN 60068-2-64. «Ensayos ambientales. Parte 2-64: Métodos de ensayo. Ensayo Fh: Vibración aleatoria de banda ancha y guía».

Consiste en hacer vibrar al cinemómetro barriendo la frecuencia en el rango (10 - 150) Hz, a un nivel RMS (nivel eficaz total) de aceleración de 7 m·s-2, con un nivel DSA (densidad espectral de aceleración) de:

1 m2·s-3 para (10 - 20) Hz.

-3 dB/octava para (20 - 150) Hz.

Se aplicarán vibraciones sucesivamente según los tres ejes principales perpendiculares entre sí, con una duración mínima de 2 minutos por eje.

– Choque mecánico. Normativa aplicable: Norma UNE-EN 60068-2-31. «Ensayos ambientales. Parte 2-31: Ensayos. Ensayo Ec: Choques debidos a manejo brusco», ensayo destinado principalmente a equipos.

Consiste en dejar caer libremente el cinemómetro sobre una de sus aristas en la superficie de ensayo desde una altura de 25 mm.

1.4.3 Ensayos de perturbaciones eléctricas.

– Variaciones de la tensión de alimentación. Normativa aplicable: Norma UNE-EN 61000-4-11. «Compatibilidad electromagnética (CEM). Parte 4-11: Técnicas de ensayo y de medida. Ensayos de inmunidad a los huecos de tensión, interrupciones breves y variaciones de tensión».

Consiste en una exposición del cinemómetro a una variación de tensión de la alimentación eléctrica indicada por el fabricante, y que debe comprender las tensiones que van de menos 15 % a más 10 % de la tensión eléctrica nominal prevista.

– Descargas electrostáticas. Normativa aplicable: Norma UNE-EN 61000-4-2. «Compatibilidad electromagnética (CEM). Parte 4-2: Técnicas de ensayo y de medida. Ensayo de inmunidad a las descargas electrostáticas».

Consiste en exponer el cinemómetro a descargas electrostáticas de 6 kV en contacto y de 8 kV en el aire.

– Ráfagas eléctricas. Normativa aplicable: Norma UNE-EN 61000-4-4. «Compatibilidad electromagnética (CEM). Parte 4-4: Técnicas de ensayo y de medida. Ensayos de inmunidad a los transitorios eléctricos rápidos en ráfagas».

Consiste en exponer el cinemómetro a ráfagas de tensión transitoria en forma de onda doblemente exponencial. Cada impulso debe tener un tiempo de subida de 5 ns y una duración a mitad de amplitud de 50 ns.

La duración de la ráfaga debe ser de 15 ms, con una periodicidad de 300 ms.

La amplitud del pico del impulso será de 1.000 V.

Debe aplicarse durante el tiempo necesario para simular 5 velocidades de medida, con errores dentro de los márgenes permitidos.

– Inmunidad electromagnética radiada. Normativa aplicable: Norma UNE-EN 61000-4-3. «Compatibilidad electromagnética (CEM). Parte 4-3: Técnicas de ensayo y de medida. Ensayos de inmunidad a los campos electromagnéticos, radiados y de radiofrecuencia».

Consiste en exponer el cinemómetro a campos electromagnéticos radiados en el rango de frecuencia de 80 MHz a 2.000 MHz; con un nivel de intensidad de campo eléctrico de 10 V/m, y una señal senoidal de 1 kHz con modulación en amplitud del 80 %.

– Inmunidad electromagnética conducida. Normativa aplicable: Norma UNE-EN 61000-4-6. «Compatibilidad electromagnética (CEM). Parte 4-6: Técnicas de ensayo y de medida. Inmunidad a las perturbaciones conducidas, inducidas por los campos de radiofrecuencia».

Consiste en exponer el cinemómetro a campos electromagnéticos conducidos en el rango de frecuencia de 0,15 MHz a 80 MHz; con un nivel de tensión de radiofrecuencia de 10 V, y una señal senoidal de 1 kHz con modulación en amplitud del 80 %.

2. Ensayos en tráfico real. Son los ensayos que se realizan con el cinemómetro instalado en su emplazamiento definitivo, en caso de cinemómetros fijos, o en circuitos representativos en otros casos, y que utilizan los propios vehículos de circulación para realizar las mediciones.

El cinemómetro se instalará y utilizará de acuerdo con las instrucciones que se indiquen en la documentación, en zonas despejadas, evitando cruces, pendientes pronunciadas y curvas, respetando los ángulos de apuntamiento, siguiendo las instrucciones del fabricante.

Se deben efectuar al menos 500 medidas en condiciones de tráfico real, a velocidades y densidades de tráfico variable, y a ser posible a diferentes temperaturas.

Si se realiza un número menor de medidas, deben considerarse como un muestreo que, por sus resultados, deben permitir estimar los errores del cinemómetro dentro de los mismos límites que las 500 medidas previstas.

Para la verificación de la distancia intervehícular se realizarán al menos 50 medidas y para la verificación de la distancia al objetivo que determina inequívocamente el carril de circulación, se requiere al menos realizar 30 observaciones, no resultando ninguna errónea.

Estos ensayos pueden realizarse in situ o mediante sistemas que permitan la conexión y medición remota.

Para la evaluación de los sistemas de control semafórico, se comprobará:

i. Su correcta instalación y condiciones funcionales,

ii. la correcta transmisión de imágenes así como la recepción, registro y protección de la información,

iii. el aseguramiento de la fecha y hora de la detección,

iv. los tiempos mínimos de activación y tiempos de cambio de fase,

v. la identificación del software,

vi. y se precintarán las cámaras de tal manera que se garantice la orientación y se impida el acceso a los parámetros relevantes.

B) Conformidad con el tipo basada en la verificación del producto (módulo F).

El módulo F aplicado a los cinemómetros deberá llevarse a cabo de acuerdo con lo que se determina en el artículo 13, del anexo I del Real Decreto 244/2016, de 3 de junio, y se realizará en dos fases:

1. Primera fase, llamada «Verificación de producto parcial». Consistirá en la comprobación de la conformidad del cinemómetro con el tipo, así como en la superación de los ensayos indicados en los puntos 1.1, 1.2 y 1.3 del apartado A de este apéndice, en las condiciones nominales.

2. Segunda fase, llamada «Verificación de producto después de la instalación». Consistirá en comprobar la correcta instalación y ajuste del cinemómetro, así como la superación de al menos 50 medidas realizadas en condiciones de tráfico real y 5 observaciones en caso de verificación de distancia al objetivo. Para los cinemómetros de tramo, descritos en el punto 3.7. del apéndice I de este anexo, se exigirán al menos 5 medidas en tráfico real, pudiendo realizarse las restantes hasta 50, en otros escenarios representativos del tráfico real, en cuanto a la distancia a medir se realizarán al menos 3 medidas.

En caso de cinemómetros de tramo, cuyas cámaras sincronizadas actúen como simples sensores de captación de imágenes y registro de la hora, y que envían la información a un centro de control para su tratamiento y posterior cálculo de la velocidad, se medirá in-situ la distancia entre los puntos referenciados y se verificará que los relojes de las cámaras que conforman el cinemómetro están sincronizados y cumplen con los requisitos establecidos en este anexo.

> _Nota BOE: Se modifica el párrafo tercero del apartado A) por el art. único.14 de la Orden ITU/1475/2024, de 17 de diciembre. Ref. BOE-A-2024-27147_

<!-- bloque ai-36 · versión publicada 20200224 · vigente desde 20201024 -->

APÉNDICE III

Procedimiento técnico de ensayos para la verificación después de reparación o modificación de cinemómetros

Los ensayos para la verificación después de reparación o modificación de cinemómetros, son los mismos que para la conformidad con el tipo basada en la verificación del producto, indicados en el apartado B del apéndice II de este anexo.

Los errores máximos permitidos (emp) para los cinemómetros, son los indicados en el punto 3.1.1. del apéndice I de este anexo, en la fase de evaluación de la conformidad.

El sistema de medida utilizado como referencia para la comparación de los resultados de los cinemómetros debe tener una incertidumbre inferior a 1/3 del error máximo permitido para el cinemómetro sometido a ensayo.

<!-- bloque ai-37 · versión publicada 20200224 · vigente desde 20201024 -->

APÉNDICE IV

Procedimiento técnico de ensayos para la verificación periódica de cinemómetros

Los ensayos para la verificación periódica de los cinemómetros, excepto para los denominados de tramo y en aeronaves, son los indicados en los puntos 1.1, 1.2 y 1.3 del apartado A del apéndice II de este anexo. En el caso de los cinemómetros fijos y estáticos, estos ensayos podrán ser sustituidos por, al menos, 30 medidas realizadas en condiciones de tráfico real y no será de aplicación el cumplimiento de los requisitos específicos que se establecen para las verificaciones; cada cuatro años y coincidiendo con el proceso de verificación periódica de los cinemómetros fijos se revisarán las cabinas que los alojan, utilizando métodos de medida distintos a los utilizados hasta entonces, a no ser que se detecten golpes o cambios en su orientación por causas accidentales o rotura de precintos, que exigiría una nueva verificación.

Los cinemómetros ubicados en vehículos en movimiento tendrán que superar también, al menos, 30 medidas realizadas en condiciones de tráfico real.

Los cinemómetros de tramo, tendrán que superar, al menos, 5 medidas realizadas en condiciones de tráfico real. En caso de cinemómetros de tramo cuyas cámaras sincronizadas actúen como simples sensores de captación de imágenes y registro de la hora, y que envían la información a un centro de control para su tratamiento y posterior cálculo de la velocidad, no será necesario la realización de estos ensayos, siempre que se garantice y asegure la distancia a medir y se verifique que los relojes de las cámaras que conforman el cinemómetro están sincronizados y cumplen los requisitos establecidos en este anexo. La garantía y aseguramiento de distancia y hora podrá realizarse por medios telemáticos.

Los cinemómetros ubicados en aeronaves, tendrán que superar, al menos, 30 medidas realizadas en condiciones de tráfico real.

Los errores máximos permitidos (emp) para los cinemómetros, son los indicados en el punto 3.1.2. del apéndice I de este anexo.

El sistema de medida utilizado como referencia para la comparación de los resultados de los cinemómetros debe tener una incertidumbre inferior a 1/3 del error máximo permitido para el cinemómetro sometido a ensayo.

## 5. Directriz 1/2022, de 19 de mayo, para la evaluación de las cabinas que alojan cinemómetros (BOE-A-2022-8355), anexo (selección)

> **Nota ggLaw:** la API del BOE no da fecha de vigencia para estos bloques (el comentario dice «vigente desde» en blanco). El apartado 7 fija su aplicabilidad «a los veinte días de su publicación». Es una directriz técnica del Consejo Superior de Metrología publicada por resolución; su valor normativo es dudoso (ver dudas).

<!-- bloque a1 · versión publicada 20220521 · vigente desde  -->

### Apartado 1. Objeto.

La presente directriz tiene por objeto establecer una sistemática a aplicar para la evaluación de las cabinas que influyan en las características metrológicas de los cinemómetros y para las comprobaciones in situ que, cada cuatro años, se realicen coincidiendo, siempre que sea posible, con la fase del control metrológico del Estado de verificación periódica de los cinemómetros.

<!-- bloque a2 · versión publicada 20220521 · vigente desde  -->

### Apartado 2. Cumplimiento de requisitos de las cabinas.

La Orden ICT/155/2020, de 7 de febrero, por la que se regula el control metrológico del Estado de determinados instrumentos de medida, establece, en el anexo XII, epígrafe I, subapartado 1.16, del apéndice I relativo a requisitos esenciales específicos para cinemómetros que, cuando la cabina influya en las características metrológicas del cinemómetro, deberá:

2.1 Incorporar una placa de características que, al menos, indique su modelo, su número de serie, los datos de identificación del fabricante, y la fecha de fabricación.

2.2 El diseño y la construcción de las cabinas y de sus anclajes al suelo o a la estructura en la que se ubique, así como a los elementos activos del cinemómetro, deberán tener la rigidez mecánica, aislamiento, seguridad y protección adecuados para su uso. A estos efectos, el fabricante deberá aportar la documentación acreditativa y la relación de las normas que satisface.

Considerando que todas las cabinas pueden influir en mayor o menor grado en las características metrológicas de los cinemómetros, los fabricantes deberán obtener un certificado de ensayos que habilite su utilización con determinados cinemómetros, para ello deben presentar la documentación técnica acreditativa y las normas que las mismas cumplen, junto con una solicitud de certificación de ensayo que avale el cumplimiento con los requisitos establecidos en este apartado. Este certificado cubrirá el diseño y la construcción de la cabina, sirviendo de referencia para la puesta en servicio.

La capacidad para la emisión del referido certificado de ensayos recae en la administración pública competente o en los organismos de control metrológico designados para el módulo B para cinemómetros.

Para la puesta en servicio de una cabina se realizarán los ensayos preceptivos con los modelos de cinemómetros legalmente en servicio que va a alojar con objeto de comprobar el cumplimiento de requisitos de las cabinas y, si el resultado es favorable, la administración pública competente o un organismo autorizado de verificación metrológica designado para cinemómetros, emitirá un certificado que se denominará certificado de revisión de cabina y procederá al precintado de las partes móviles, mediante precintos identificados y numerados.

<!-- bloque a3 · versión publicada 20220521 · vigente desde  -->

### Apartado 3. Revisión de la cabina.

La revisión de la cabina consistirá en comprobar que la misma no tiene influencia significativa en la medida. Se considera que la cabina no tiene influencia significativa cuando en la verificación de cinemómetros de los modelos que puede alojar y que están legalmente en servicio, se comprueba que estos son conformes con los errores máximos permitidos para la verificación periódica. Además, se deberán comprobar elementos activos, estructurales, así como sus anclajes al suelo.

La administración pública competente o los organismos autorizados de verificación metrológica para cinemómetros serán los encargados de realizar la revisión de las cabinas.

Superada la revisión se emitirá un certificado de revisión de la cabina en el que se indicará al menos la marca y el modelo de los cinemómetros que se hayan utilizado para la revisión, quedando estos incluidos en este certificado como cinemómetros en los que la cabina no tiene influencia significativa, y se adherirá a la misma una etiqueta de revisión de características similares a la establecida en el anexo III del Real Decreto 244/2016, de 3 de junio, por el que se desarrolla la Ley 32/2014, de 22 de diciembre, de Metrología, para la verificación periódica, donde se sustituye el texto «Resultado de la verificación» por «Resultado de la revisión».

Si en el momento de la revisión de la cabina se observa que se ha producido una rotura de precintos o anomalías como desplazamientos del terreno o el cinemómetro utilizado no cumple con los errores máximos permitidos en su verificación periódica, se adherirá una etiqueta de fuera de servicio de características similares a las establecidas en el anexo III del Real Decreto 244/2016, de 3 de junio, eliminando el término «Control Metrológico», hasta que se solventen los problemas detectados y se supere una nueva revisión.

En caso de que los precintos de la cabina no estén numerados se procederá a precintar con precintos numerados sin eliminar los anteriores. Así mismo en las cabinas en servicio con anterioridad a la Orden ITC/3123/2010, del 26 de noviembre, y/o cuyos precintos puedan considerarse insuficientes, será necesario solventar este hecho antes de emitir el certificado de revisión de la cabina por parte de un organismo autorizado de verificación metrológica.

<!-- bloque a4 · versión publicada 20220521 · vigente desde  -->

### Apartado 4. Plazos para la revisión de la cabina.

A partir del 25 de octubre de 2020 el plazo para la realización de las revisiones conjuntas de cabinas con los cinemómetros que alojan u otros del mismo modelo legalmente en servicio, se contabilizará de la siguiente forma:

4.1 Cuatro años desde la fecha del primer certificado de revisión de cabinas para las instaladas con posterioridad al 25 de octubre de 2020.

4.2 Para las cabinas legalmente en servicio antes del 25 de octubre de 2020, la primera revisión se realizará a fecha de vencimiento de su certificado en vigor y las subsiguientes cada cuatro años.

<!-- bloque a6 · versión publicada 20220521 · vigente desde  -->

### Apartado 6. Eficacia transitoria.

Las cabinas legalmente en servicio a la entrada en vigor de la Orden ICT/155/2020, de 7 de febrero, podrán continuar en servicio siempre y cuando superen las correspondientes revisiones.

<!-- bloque a7 · versión publicada 20220521 · vigente desde  -->

### Apartado 7. Aplicabilidad.

Lo establecido en esta directriz será exigible a los veinte días de su publicación en el «Boletín Oficial del Estado».

---

## Jurisprudencia

No se ha leído ninguna sentencia sobre cinemómetros. CENDOJ está bloqueado por CAPTCHA y
la página consolidada del BOE de estas cuatro normas no muestra panel de jurisprudencia
(comprobado el 2026-09-23). Ver dudas.

## Dudas abiertas

1. `TODO(juridico)`: **Descuento del error máximo permitido.** ¿Hay una norma que obligue a
   restar el emp de la tabla 2 a la velocidad medida antes de aplicar el anexo IV de la
   LSV? No está en la Ley 32/2014, el RD 244/2016 ni la Orden ICT/155/2020. Fuentes
   secundarias (prensa, despachos: pista no verificada) hablan de una práctica de la DGT
   y de jurisprudencia del TS. Fuente a consultar: instrucciones de la DGT (sede.dgt.gob.es,
   www.dgt.es) y jurisprudencia del TS sobre el art. 83.2 LSV (CENDOJ).
2. `TODO(juridico)`: **¿Qué emp se aplica al sancionar: el de la tabla 1 o el de la
   tabla 2?** La tabla 2 es la de «la verificación periódica», es decir, la tolerancia
   que el aparato debe cumplir en servicio. La Orden no dice cuál usar para encuadrar la
   infracción. Fuente: la misma que en la duda 1.
3. `TODO(juridico)`: **Carga de la prueba.** Si el denunciado no discute la verificación,
   ¿debe la Administración incorporar de oficio los certificados al expediente, o basta la
   presunción del art. 8.6 Ley 32/2014 y el valor probatorio de la denuncia (art. 88 LSV)?
   Fuente: jurisprudencia del TS y de los TSJ (CENDOJ); no consultada.
4. `TODO(juridico)`: **Hechos anteriores al 24/10/2020.** Para mediciones anteriores rige la
   Orden ITC/3123/2010 (BOE-A-2010-18556, derogada con efectos de 24/10/2020). No se ha
   transcrito. Hay que leer sus errores máximos y su periodicidad antes de aplicar una
   regla a hechos de esas fechas. Fuente: `scripts/boe_fetch.py BOE-A-2010-18556 --index`
   (la API conserva el texto de las normas derogadas).
5. `TODO(juridico)`: **Fecha de derogación de la orden de 2010: 24 o 25 de octubre de
   2020.** Los metadatos del BOE dan `fecha_derogacion: 20201024`, y la Orden ICT/155/2020
   entró en vigor el 24/10/2020 (página del BOE). La Directriz 1/2022 dice «A partir del 25
   de octubre de 2020, dicha orden queda derogada» (preámbulo del anexo, no transcrito) y
   cita por error la «Orden ICT/155/2021». Solo afecta a una medición del 24/10/2020.
6. `TODO(juridico)`: **Valor de la Directriz 1/2022.** Es una directriz técnica del Consejo
   Superior de Metrología (art. 16 Ley 32/2014, no transcrito) publicada por resolución
   de la Secretaría General de Industria. ¿Es vinculante o solo interpretativa? Si no lo
   es, la exigencia de revisión de cabina cada cuatro años descansa solo en el apéndice IV
   del anexo XII (que sí es norma). Fuente: Ley 32/2014 art. 16; RD 244/2016 art. 41.
7. `TODO(juridico)`: **Radares de tramo y en aeronave.** Tienen reglas propias (apéndice I,
   3.7 y 3.8; verificación periódica con 5 o 30 medidas; emp de la tabla 1). ggLaw no
   debería mezclarlos con los radares fijos o móviles.
8. `TODO(juridico)`: **Etilómetros.** El art. 83.2 LSV también afecta a los etilómetros
   (anexo XIII de la Orden ICT/155/2020, no transcrito). Pendiente para una regla futura.
9. `TODO(juridico)`: **Radares municipales de Palma.** Qué cinemómetros usa la Policía
   Local de Palma, quién es su titular a efectos del art. 19 RD 244/2016 y dónde se
   publican sus certificados. Fuente: Ajuntament de Palma (sede bloqueada desde el entorno
   de trabajo); www.cem.es (Registro de Control Metrológico) como apoyo.
