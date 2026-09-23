---
norma: Real Decreto Legislativo 6/2015, de 30 de octubre, por el que se aprueba el texto refundido de la Ley sobre Tráfico, Circulación de Vehículos a Motor y Seguridad Vial (procedimiento sancionador)
articulos: [7, 11, 60, 74, 77, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 107, 108, 109, 110, 111, 112, 113]
disposiciones: [DA quinta, DA undécima, DT segunda, DF tercera]
fuente: https://www.boe.es/buscar/act.php?id=BOE-A-2015-11722
# boe.es: "Última actualización publicada el 26/06/2026" (RD 518/2026, solo anexo I,
# con efectos 2026-10-01). El campo fecha_actualizacion de los metadatos de la API
# es 2026-07-31T08:26:22Z (fecha de actualización del registro, no de la versión).
version_consolidada: 2026-06-26
consultado: 2026-09-23
estado: borrador
---

# RDL 6/2015 (Ley sobre Tráfico): procedimiento sancionador

Texto refundido de la Ley sobre Tráfico, Circulación de Vehículos a Motor y Seguridad
Vial (en adelante, LSV), identificador BOE-A-2015-11722.

**Cómo leer este fichero**

- Los artículos se han obtenido con `scripts/boe_fetch.py` de la API de datos abiertos
  del BOE (legislación consolidada). Se ha comprobado que ninguna versión transcrita
  tiene fecha de vigencia posterior a la fecha de consulta.
- Todo lo que aparece bajo un encabezado `### Artículo …` o `### Disposición …` es
  **transcripción literal**. Los comentarios `<!-- bloque … -->` indican la versión de
  cada bloque (fecha de publicación de la norma modificadora y fecha de vigencia).
- Las líneas `> _Nota BOE: …_` son notas editoriales del BOE, no texto normativo.
  Las que empiezan por «Téngase en cuenta que esta actualización… entra en vigor el
  21 de marzo de 2022… Redacción anterior» son notas temporales que el BOE marca como
  caducadas desde el 2022-03-21 (atributo `caduca`). Se conservan, pero **el texto
  vigente es el del artículo**, no la «redacción anterior».
- Las marcas `[…]` y los bloques `> **Nota ggLaw …**` son de elaboración propia.
- El índice temático, la sección de jurisprudencia y las dudas son de elaboración
  propia. En el índice, los plazos se citan entre comillas **literalmente**.
- Ningún artículo del Título V se ha modificado después del 2023-06-30 (última versión
  de los arts. 76 y 77, RDL 5/2023). Las modificaciones de 2025 (Ley 9/2025) y 2026
  (RD 518/2026) no afectan a los artículos transcritos.

**Artículos no incluidos (a propósito):** arts. 75 y 76 (catálogo de infracciones leves
y graves) y art. 77 salvo la letra j); arts. 78-79 (seguro obligatorio y publicidad);
Capítulo V, arts. 97-102 (intercambio transfronterizo de información); arts. 103-106
(medidas provisionales, inmovilización, retirada y depósito, tratamiento residual del
vehículo); anexos (incluido el anexo IV, cuadro de sanciones por velocidad).

## Índice temático (elaboración propia)

Los plazos se transcriben literalmente, con el tipo de día **tal como lo dice el texto**.
Cuando el artículo no dice el tipo de día o el día inicial, se indica **No dice** o
**No fija** y hay una duda abierta al final. Ningún plazo de esta tabla debe usarse en `core/plazos.py`
sin revisar las dudas abiertas.

### Denuncia, iniciación y notificación

| Materia | Artículo | Texto literal clave | Día inicial / observaciones |
|---|---|---|---|
| Iniciación por denuncia notificada en el acto | 86.2 | «constituye el acto de iniciación del procedimiento sancionador, a todos los efectos» | Solo para la denuncia de agentes «notificada en el acto» |
| Contenido obligatorio de la denuncia | 87.2 y 87.3 | 87.3.d): «un plazo de veinte días naturales para efectuar el pago, con la reducción […] o para formular las alegaciones» | Contenido a comprobar en la regla de defectos de la denuncia |
| Valor probatorio de la denuncia del agente | 88 | «tendrán valor probatorio, salvo prueba en contrario» | — |
| Notificación en el acto y excepciones | 89 | «Las denuncias se notificarán en el acto al denunciado»; excepciones tasadas en 89.2 a)-d) | — |
| Orden de lugares de notificación | 90.1 | DEV; si no la tiene, domicilio indicado para el procedimiento; en su defecto, domicilio de los registros de la JCT | Art. 60.5: a la persona física solo se le asigna DEV «cuando lo solicite voluntariamente» |
| Notificación en DEV: rechazo presunto | 90.2 | «transcurrieran diez días naturales sin que se acceda a su contenido, se entenderá que aquélla ha sido rechazada» | **No fija** expresamente el día inicial (parte de que haya «constancia de la recepción»); efecto en plazos: duda |
| Notificación en domicilio: segundo intento | 90.3 | «se practicará de nuevo dentro de los tres días siguientes» | **No dice** el tipo de día |
| Notificación edictal en BOE | 91 | «Transcurrido el período de veinte días naturales desde que la notificación se hubiese publicado en el BOE se entenderá que ésta ha sido practicada» | — |
| TESTRA | 92 | «Con carácter previo y facultativo» | Ver DA undécima y DF tercera b) |

### Alegaciones, pago con reducción e identificación del conductor

| Materia | Artículo | Plazo literal | Día inicial / observaciones |
|---|---|---|---|
| Alegaciones y prueba (o pago con reducción) | 93.1 y 95.1 | «un plazo de veinte días naturales» | «Notificada la denuncia» (no dice «desde el día siguiente») |
| Pago con reducción del 50 % (procedimiento abreviado) | 94 | «dentro del plazo de veinte días naturales contados desde el día siguiente al de su notificación» | Reducción: «La reducción del 50 por ciento del importe de la sanción» (94.a) |
| Efectos del pago reducido | 94.b-g | Renuncia a alegaciones («se tendrán por no presentadas»); terminación «el día en que se realice el pago»; «agotamiento de la vía administrativa, siendo recurrible únicamente ante el orden jurisdiccional contencioso-administrativo» | Plazo contencioso: «se iniciará el día siguiente a aquel en que tenga lugar el pago» (94.e); la LSV no fija su duración |
| Infracciones sin procedimiento abreviado | 93.2 | «no será de aplicación a las infracciones previstas en el artículo 77.h), j), n), ñ), o), p), q), r), s) y t)» | Incluye 77.j (no identificar al conductor) |
| Identificación del conductor (sin detención del vehículo) | 93.1, párr. 2 | «un plazo de veinte días naturales para identificar al conductor responsable de la infracción» | **No dice** el día inicial. Por DEV, identificación «por medios telemáticos» |
| Contenido de la identificación | 11.1.a | «Los datos facilitados deben incluir el número del permiso o licencia de conducción» | Conductor habitual y arrendatario a largo plazo: 11.2-11.3 y 82.c-d |
| Infracción por no identificar | 77.j y 80.2.b | Muy grave; multa «el doble de la prevista para la infracción originaria que la motivó, si es infracción leve, y el triple, si es infracción grave o muy grave» | Sin procedimiento abreviado (93.2) |
| Responsables | 82 | Autor del hecho, con las reglas a)-g) | 82.g: titular responde de estacionamiento salvo conductor habitual o conductor indicado |

### Procedimiento ordinario, resolución y recursos

| Materia | Artículo | Plazo literal | Día inicial / observaciones |
|---|---|---|---|
| Informe del agente sobre las alegaciones | 95.2 | «para que informe en el plazo de quince días naturales» | Solo si hay datos nuevos y el instructor lo estima necesario |
| Traslado de la propuesta de resolución | 95.3 | «para que pueda formular nuevas alegaciones en el plazo de quince días naturales» | **Solo** si se tienen en cuenta hechos, alegaciones o pruebas distintos de los del interesado |
| Denuncia con efecto de acto resolutorio | 95.4 | Sin alegaciones ni pago «en el plazo de veinte días naturales siguientes al de la notificación de la denuncia» | Solo en los supuestos 95.4 a)-c) |
| Ejecución en ese caso | 95.4 y 95.5 | «podrá ejecutarse transcurridos treinta días naturales desde la notificación de la denuncia»; «se podrá ejecutar desde el día siguiente al transcurso de los treinta días antes indicados» | — |
| Resolución sancionadora | 96.1 | «pondrá fin a la vía administrativa y la sanción se podrá ejecutar desde el día siguiente a aquel en que se notifique al interesado» | — |
| Recurso de reposición | 96.2 | «con carácter potestativo, en el plazo de un mes contado desde el día siguiente al de su notificación» | Ante el órgano que dictó la resolución |
| Suspensión solicitada en reposición | 96.3 | «se entenderá denegada transcurrido el plazo de un mes desde la solicitud sin que se haya resuelto» | La reposición «no suspenderá la ejecución» |
| Hechos nuevos en reposición | 96.4 | «No se tendrán en cuenta […] hechos, documentos y alegaciones del recurrente que pudieran haber sido aportados en el procedimiento originario» | Importante para la estrategia de alegaciones |
| Silencio en reposición | 96.5 | «se entenderá desestimado si no recae resolución expresa en el plazo de un mes, quedando expedita la vía contencioso-administrativa» | — |
| Resoluciones de Alcaldes | 96.6 | «se estará a lo establecido en los anteriores apartados respetando la competencia sancionadora prevista en su normativa específica» | Ver duda sobre Palma |

### Prescripción, caducidad, firmeza y ejecución

| Materia | Artículo | Plazo literal | Día inicial / observaciones |
|---|---|---|---|
| Prescripción de la infracción | 112.1 | «tres meses para las infracciones leves y de seis meses para las infracciones graves y muy graves» | «comenzará a contar a partir del mismo día en que los hechos se hubieran cometido» (ojo: el mismo día, no el siguiente) |
| Interrupción de la prescripción | 112.2 | Cualquier actuación administrativa conocida por el denunciado o dirigida a averiguar su identidad o domicilio; notificación según arts. 89, 90 y 91 | Se reanuda «si el procedimiento se paraliza durante más de un mes por causa no imputable al denunciado» |
| Caducidad del procedimiento | 112.3 | «Si no se hubiera producido la resolución sancionadora transcurrido un año desde la iniciación del procedimiento» | Suspensión si conoce la jurisdicción penal. Qué es la «iniciación»: ver duda |
| Prescripción de la sanción | 112.4 | Multa: «cuatro años»; suspensión del art. 80: «un año» | «computados desde el día siguiente a aquel en que adquiera firmeza la sanción en vía administrativa»; apremio: normativa tributaria |
| Firmeza tras pago reducido | 94.f | «La firmeza de la sanción en la vía administrativa desde el momento del pago, produciendo plenos efectos desde el día siguiente» | — |
| Ejecución | 108 | «Una vez firme la sanción en vía administrativa» | — |
| Pago voluntario tras firmeza | 110.1 | «un plazo final de quince días naturales para el pago de la multa» | «Una vez firme la sanción»; después, apremio |
| Responsables subsidiarios del pago | 111 | Titular, salvo supuestos a)-d) | Régimen tributario (111.2) |
| Bloqueo de trámites por impago | 107 | «cuatro sanciones firmes en vía administrativa por infracciones graves o muy graves» impagadas | — |
| Anotación en el Registro de Conductores e Infractores | 113.1 | «en el plazo de los quince días naturales siguientes a su firmeza en vía administrativa» | Cancelación: «una vez transcurridos tres años desde su total cumplimiento o prescripción» (113.4) |

### Competencia, garantías y medición

| Materia | Artículo | Texto literal clave | Observaciones |
|---|---|---|---|
| Supletoriedad | 83.1 | «supletoriamente, en la normativa de procedimiento administrativo común» | Ley 39/2015, DA primera.2.c) (ver dudas) |
| Control metrológico (cinemómetros, etilómetros…) | 83.2 | «estarán sometidos a control metrológico en los términos establecidos por la normativa de metrología» | Base de la regla de verificación del cinemómetro |
| Competencia en vías urbanas | 84.4 y 7.a | «corresponderá a los respectivos Alcaldes, los cuales podrán delegar esta competencia» | Excluidas las infracciones del título IV (84.4, párr. 2) |
| Competencia en vías interurbanas | 84.1 | «corresponde al Jefe de Tráfico de la provincia en que se haya cometido el hecho» | Delegación en el Director del Centro de Tratamiento de Denuncias Automatizadas (84.2) |
| Concurrencia con proceso penal | 85 | Suspensión de actuaciones; archivo si hay condena penal | Suspende la caducidad (112.3, párr. 2) |

### Mapa del procedimiento (resumen propio, no normativo)

1. **Denuncia** (86-89). Si se notifica en el acto, inicia el procedimiento (86.2). Si
   no, se notifica después en DEV, domicilio o BOE (90-92).
2. **20 días naturales** tras la notificación de la denuncia (93.1; el 94 los cuenta «desde el día siguiente al de su notificación»): pagar con reducción del 50 %
   (procedimiento abreviado, 94) **o** alegar y proponer prueba (procedimiento ordinario,
   95). Si no hubo detención del vehículo, el titular puede identificar al conductor en
   el mismo plazo (93.1, párr. 2).
3. **Abreviado:** el pago termina el procedimiento, agota la vía administrativa y solo
   cabe contencioso-administrativo (94).
4. **Ordinario sin alegaciones ni pago:** en los casos del 95.4, la denuncia vale como
   resolución y es ejecutable a los 30 días naturales de su notificación.
5. **Ordinario con alegaciones:** instrucción, en su caso informe del agente y traslado
   de la propuesta (95.2-95.3), y resolución sancionadora, que agota la vía administrativa
   (96.1). Recurso de reposición potestativo en un mes (96.2) o contencioso-administrativo.
6. **Límites temporales:** prescripción de la infracción (112.1-2), caducidad al año de la
   iniciación (112.3), prescripción de la sanción (112.4).
7. **Ejecución:** firme la sanción, 15 días naturales para pagar y después apremio (110).

---

## Título I (Ejercicio y coordinación de las competencias…), Capítulo I. Competencias — art. 7

<!-- bloque a7 · versión publicada 20151031 · vigente desde 20160131 -->

### Artículo 7. Competencias de los municipios.

Corresponde a los municipios:

a) La regulación, ordenación, gestión, vigilancia y disciplina, por medio de agentes propios, del tráfico en las vías urbanas de su titularidad, así como la denuncia de las infracciones que se cometan en dichas vías y la sanción de las mismas cuando no esté expresamente atribuida a otra Administración.

b) La regulación mediante ordenanza municipal de circulación, de los usos de las vías urbanas, haciendo compatible la equitativa distribución de los aparcamientos entre todos los usuarios con la necesaria fluidez del tráfico rodado y con el uso peatonal de las calles, así como el establecimiento de medidas de estacionamiento limitado, con el fin de garantizar la rotación de los aparcamientos, prestando especial atención a las necesidades de las personas con discapacidad que tienen reducida su movilidad y que utilizan vehículos, todo ello con el fin de favorecer su integración social.

c) La inmovilización de los vehículos en vías urbanas cuando no dispongan de título que habilite el estacionamiento en zonas limitadas en tiempo o excedan de la autorización concedida, hasta que se logre la identificación de su conductor.

La retirada de los vehículos de las vías urbanas y su posterior depósito cuando obstaculicen, dificulten o supongan un peligro para la circulación, o se encuentren incorrectamente aparcados en las zonas de estacionamiento restringido, en las condiciones previstas para la inmovilización en este mismo artículo. Las bicicletas sólo podrán ser retiradas y llevadas al correspondiente depósito si están abandonadas o si, estando amarradas, dificultan la circulación de vehículos o personas o dañan el mobiliario urbano.

Igualmente, la retirada de vehículos en las vías interurbanas y el posterior depósito de éstos, en los términos que reglamentariamente se determine.

d) La autorización de pruebas deportivas cuando discurran íntegra y exclusivamente por el casco urbano, exceptuadas las travesías.

e) La realización de las pruebas a que alude el artículo 5.o) en las vías urbanas, en los términos que reglamentariamente se determine.

f) El cierre de vías urbanas cuando sea necesario.

g) La restricción de la circulación a determinados vehículos en vías urbanas por motivos medioambientales.

## Título II (Normas de comportamiento en la circulación), Capítulo I — art. 11

<!-- bloque a11 · versión publicada 20151031 · vigente desde 20160131 -->

### Artículo 11. Obligaciones del titular del vehículo y del conductor habitual.

1. El titular de un vehículo tiene las siguientes obligaciones:

a) Facilitar a la Administración la identificación del conductor del vehículo en el momento de cometerse una infracción. Los datos facilitados deben incluir el número del permiso o licencia de conducción que permita la identificación en el Registro de Conductores e Infractores del organismo autónomo Jefatura Central de Tráfico.

Si el conductor no figura inscrito en el aludido Registro de Conductores e Infractores, el titular deberá disponer de copia de la autorización administrativa que le habilite a conducir en España y facilitarla a la Administración cuando le sea requerida. Si el titular fuese una empresa de alquiler de vehículos sin conductor, la copia de la autorización administrativa podrá sustituirse por la copia del contrato de arrendamiento.

b) Impedir que el vehículo sea conducido por quien nunca haya obtenido el permiso o la licencia de conducción correspondiente.

2. El titular del vehículo puede comunicar al Registro de Vehículos del organismo autónomo Jefatura Central de Tráfico la identidad del conductor habitual del mismo. En este supuesto, el titular queda exonerado de las obligaciones anteriores, que se trasladan al conductor habitual.

3. Las obligaciones establecidas en el apartado 1 y la comunicación descrita en el apartado anterior corresponden al arrendatario a largo plazo del vehículo, en el supuesto de que haya constancia de éste en el Registro de Vehículos del organismo autónomo Jefatura Central de Tráfico.

4. El titular del vehículo en régimen de arrendamiento a largo plazo debe comunicar al Registro de Vehículos del organismo autónomo Jefatura Central de Tráfico la identidad del arrendatario.

## Título IV (Autorizaciones administrativas), Capítulo I. Autorizaciones en general — art. 60

<!-- bloque a60 · versión publicada 20151031 · vigente desde 20160131 -->

### Artículo 60. Domicilio y Dirección Electrónica Vial (DEV).

1. El titular de un permiso o licencia de conducción o del permiso de circulación de un vehículo comunicará a los registros del organismo autónomo Jefatura Central de Tráfico su domicilio. Éste se utilizará para efectuar las notificaciones respecto de todas las autorizaciones de que disponga. A estos efectos, los ayuntamientos y la Agencia Estatal de Administración Tributaria podrán comunicar al organismo autónomo Jefatura Central de Tráfico los nuevos domicilios de que tengan constancia.

2. En el historial de cada vehículo podrá hacerse constar, además, un domicilio a los únicos efectos de gestión de los tributos relacionados con el mismo.

3. Sin perjuicio de lo dispuesto en el apartado 1, el organismo autónomo Jefatura Central de Tráfico asignará además a todo titular de un permiso o licencia de conducción o del permiso de circulación de un vehículo, y con carácter previo a su obtención, una Dirección Electrónica Vial (DEV). Esta dirección se asignará automáticamente a todas las autorizaciones de que disponga su titular en los Registros de Vehículos y de Conductores e Infractores del organismo autónomo Jefatura Central de Tráfico.

4. La asignación de la Dirección Electrónica Vial (DEV) se realizará también al arrendatario a largo plazo que conste en el Registro de Vehículos del organismo autónomo Jefatura Central de Tráfico, con carácter previo a su inclusión.

5. No obstante lo dispuesto en los apartados anteriores, si el titular de la autorización es una persona física sólo se le asignará una Dirección Electrónica Vial (DEV) cuando lo solicite voluntariamente. En este caso, todas las notificaciones se practicarán en la Dirección Electrónica Vial conforme se establece en el artículo 90, sin perjuicio de lo previsto en la normativa sobre acceso electrónico de los ciudadanos a los servicios públicos.

6. En la Dirección Electrónica Vial (DEV) además se practicarán los avisos e incidencias relacionados con las autorizaciones administrativas recogidas en esta ley.

## Título V. Régimen sancionador — Capítulo I. Infracciones (selección)

<!-- bloque a74 · versión publicada 20151031 · vigente desde 20160131 -->

### Artículo 74. Disposiciones generales.

1. Las acciones u omisiones contrarias a esta ley tendrán el carácter de infracciones administrativas y serán sancionadas en los términos previstos en la misma.

2. Cuando las acciones u omisiones puedan ser constitutivas de delitos tipificados en las leyes penales, se estará a lo dispuesto en el artículo 85.

3. Las infracciones se clasifican en leves, graves y muy graves.

<!-- bloque a77 · versión publicada 20230629 · vigente desde 20230630 -->

### Artículo 77. Infracciones muy graves.

Son infracciones muy graves, cuando no sean constitutivas de delito, las conductas tipificadas en esta ley referidas a:

[…]

j) Incumplir el titular o el arrendatario del vehículo con el que se haya cometido la infracción la obligación de identificar verazmente al conductor responsable de dicha infracción, cuando sean debidamente requeridos para ello en el plazo establecido. En el supuesto de las empresas de alquiler de vehículos sin conductor la obligación de identificar se ajustará a las previsiones al respecto del artículo 11.

[…]

> **Nota ggLaw (no es texto legal):** extracto. Se omiten las letras a) a i) y k) a x). Las notas del BOE de este artículo se refieren a las letras q) y s) a x); la letra j) tiene la misma redacción en las tres versiones del bloque `a77` (2015, Ley 18/2021 y RDL 5/2023), comprobado en la API del BOE.

## Título V — Capítulo II. Sanciones

<!-- bloque a80 · versión publicada 20211221 · vigente desde 20220321 -->

### Artículo 80. Tipos.

1. Las infracciones leves serán sancionadas con multa de hasta 100 euros; las graves, con multa de 200 euros, y las muy graves, con multa de 500 euros. No obstante, las infracciones consistentes en no respetar los límites de velocidad se sancionarán en la cuantía prevista en el anexo IV.

2. Sin perjuicio de lo dispuesto anteriormente, en la imposición de sanciones deberá tenerse en cuenta que:

a) Las infracciones previstas en el artículo 77. c) y d) serán sancionadas con multa de 1.000 euros. En el supuesto de conducción con tasas de alcohol superiores a las que reglamentariamente se establezcan, esta sanción únicamente se impondrá al conductor que ya hubiera sido sancionado en el año inmediatamente anterior por exceder la tasa de alcohol permitida, así como al que circule con una tasa que supere el doble de la permitida.

b) La multa por la infracción prevista en el artículo 77. j) será el doble de la prevista para la infracción originaria que la motivó, si es infracción leve, y el triple, si es infracción grave o muy grave.

c) La infracción recogida en el artículo 77. h) se sancionará con multa de 6.000 euros.

d) Las infracciones recogidas en el artículo 77.n), ñ), o), p), q), r), s) y t) se sancionarán con multa de entre 3.000 y 20.000 euros.

3. En el supuesto de la infracción recogida en el artículo 77. q) se podrá imponer la sanción de suspensión de la correspondiente autorización por el período de hasta un año. Durante el tiempo que dure la suspensión su titular no podrá obtener otra autorización para las mismas actividades.

La realización de actividades durante el tiempo de suspensión de la autorización llevará aparejada además una nueva suspensión por un período de seis meses al cometerse el primer quebrantamiento, y de un año si se produjese un segundo o sucesivos quebrantamientos.

4. En el caso de la infracción recogida en el artículo 77.u), el aspirante no podrá presentarse a las pruebas para la obtención o recuperación del permiso o licencia de conducción u otra autorización administrativa para conducir en el plazo de seis meses.

> _Nota BOE: Téngase en cuenta que esta actualización de la letra d) del apartado 2 y el nuevo apartado 4, establecidos por el art. único.25 de la Ley 18/2021, de 20 de diciembre, Ref. BOE-A-2021-21006#au, entran en vigor el 21 de marzo de 2022, según determina su disposición final cuarta. Redacción anterior: "d) Las infracciones recogidas en el artículo 77. n), ñ), o), p), q) y r) se sancionarán con multa de entre 3.000 y 20.000 euros."_

> _Nota BOE: Se modifica la letra d) del apartado 2 y se añade el apartado 4, con efectos de 21 de marzo de 2022, por el art. único.25 de la Ley 18/2021, de 20 de diciembre. Ref. BOE-A-2021-21006#au_

<!-- bloque a81 · versión publicada 20211221 · vigente desde 20220321 -->

### Artículo 81. Graduación.

La cuantía de las multas establecidas en el artículo 80.1 y en el anexo IV podrá incrementarse en un 30 por ciento, en atención a la gravedad y trascendencia del hecho, los antecedentes del infractor y a su condición de reincidente, el peligro potencial creado para él mismo y para los demás usuarios de la vía y al criterio de proporcionalidad.

Los criterios de graduación establecidos anteriormente serán asimismo de aplicación a las sanciones por las infracciones previstas en el artículo 77, párrafos n) a t), ambos incluidos.

> _Nota BOE: Téngase en cuenta que esta actualización del segundo párrafo, establecida por el art. único.26 de la Ley 18/2021, de 20 de diciembre, Ref. BOE-A-2021-21006#au, entra en vigor el 21 de marzo de 2022, según determina su disposición final cuarta. Redacción anterior: "Los criterios de graduación establecidos anteriormente serán asimismo de aplicación a las sanciones por las infracciones previstas en el artículo 77, párrafos n) a r), ambos incluidos."_

> _Nota BOE: Se modifica el segundo párrafo, con efectos de 21 de marzo de 2022, por el art. único.26 de la Ley 18/2021, de 20 de diciembre. Ref. BOE-A-2021-21006#au_

## Título V — Capítulo III. Responsabilidad

<!-- bloque a82 · versión publicada 20151031 · vigente desde 20160131 -->

### Artículo 82. Responsables.

La responsabilidad por las infracciones a lo dispuesto en esta ley recaerá directamente en el autor del hecho en que consista la infracción. No obstante:

a) El conductor de cualquier vehículo para el que se exija el uso de casco por conductor y pasajero será responsable por la no utilización del casco de protección por el pasajero, así como por transportar pasajeros que no cuenten con la edad mínima exigida.

Asimismo, el conductor del vehículo será responsable por la no utilización de los sistemas de retención infantil, con la excepción prevista en el artículo 13.4 cuando se trate de conductores profesionales.

b) Cuando la autoría de los hechos cometidos corresponda a un menor de dieciocho años, responderán solidariamente con él de la multa impuesta sus padres, tutores, acogedores y guardadores legales o de hecho, por este orden, en razón al incumplimiento de la obligación impuesta a éstos que conlleva un deber de prevenir la infracción administrativa que se impute a los menores.

c) En los supuestos en que no tenga lugar la detención del vehículo y éste tuviese designado un conductor habitual, la responsabilidad recaerá en éste, salvo que acredite que era otro el conductor o la sustracción del vehículo.

d) En los supuestos en que no tenga lugar la detención del vehículo y éste no tuviese designado un conductor habitual, será responsable el conductor identificado por el titular o el arrendatario a largo plazo, de acuerdo con las obligaciones impuestas en el artículo 11.

e) En las empresas de arrendamiento de vehículos a corto plazo será responsable el arrendatario del vehículo. En caso de que éste manifestara no ser el conductor, o fuese persona jurídica, le corresponderán las obligaciones que para el titular establece el artículo 11. La misma responsabilidad corresponderá a los titulares de los talleres mecánicos o establecimientos de compraventa de vehículos por las infracciones cometidas con los vehículos mientras se encuentren allí depositados.

f) El titular, o el arrendatario a largo plazo, en el supuesto de que constase en el Registro de Vehículos del organismo autónomo Jefatura Central de Tráfico, será en todo caso responsable de las infracciones relativas a la documentación del vehículo, a los reconocimientos periódicos y a su estado de conservación, cuando las deficiencias afecten a las condiciones de seguridad del vehículo.

g) El titular o el arrendatario, en el supuesto de que constase en el Registro de Vehículos del organismo autónomo Jefatura Central de Tráfico, será responsable de las infracciones por estacionamiento o por impago de los peajes de las vías que lo tengan regulado, salvo en los supuestos en que el vehículo tuviese designado un conductor habitual o se indique un conductor responsable del hecho.

## Título V — Capítulo IV. Procedimiento sancionador

<!-- bloque a83 · versión publicada 20151031 · vigente desde 20160131 -->

### Artículo 83. Garantías procedimentales.

1. No se podrá imponer sanción alguna por las infracciones tipificadas en esta ley sino en virtud de procedimiento instruido con arreglo a lo dispuesto en este capítulo y, supletoriamente, en la normativa de procedimiento administrativo común.

2. Los instrumentos, aparatos o medios y sistemas de medida que sean utilizados para la formulación de denuncias por infracciones a la normativa de tráfico, seguridad vial y circulación de vehículos a motor estarán sometidos a control metrológico en los términos establecidos por la normativa de metrología.

<!-- bloque a84 · versión publicada 20151031 · vigente desde 20160131 -->

### Artículo 84. Competencia.

1. La competencia para sancionar las infracciones cometidas en vías interurbanas y travesías corresponde al Jefe de Tráfico de la provincia en que se haya cometido el hecho. Si se trata de infracciones cometidas en el territorio de más de una provincia, la competencia para su sanción corresponde, en su caso, al Jefe de Tráfico de la provincia en que la infracción hubiera sido primeramente denunciada.

2. Los Jefes Provinciales podrán delegar esta competencia en la medida y extensión que estimen conveniente. En particular podrán delegar en el Director del Centro de Tratamiento de Denuncias Automatizadas la de las infracciones que hayan sido detectadas a través de medios de captación y reproducción de imágenes que permitan la identificación del vehículo.

Los órganos de las diferentes Administraciones Públicas podrán delegar el ejercicio de sus competencias sancionadoras mediante convenios o encomiendas de gestión, o a través de cualesquiera otros instrumentos de colaboración previstos en la normativa de procedimiento administrativo común.

3. En las comunidades autónomas que hayan recibido el traspaso de funciones y servicios en materia de tráfico y circulación de vehículos a motor serán competentes para sancionar los órganos previstos en la normativa autonómica.

4. La sanción por infracción a normas de circulación cometidas en vías urbanas corresponderá a los respectivos Alcaldes, los cuales podrán delegar esta competencia de acuerdo con la normativa aplicable.

Quedan excluidas de la competencia sancionadora municipal las infracciones a los preceptos del título IV, incluyendo las relativas a las condiciones técnicas de los vehículos y al seguro obligatorio.

Los Jefes Provinciales de Tráfico y los órganos competentes que correspondan, en caso de comunidades autónomas que hayan recibido el traspaso de funciones y servicios en materia de tráfico y circulación de vehículos a motor, asumirán la competencia de los Alcaldes cuando, por razones justificadas o por insuficiencia de los servicios municipales, no pueda ser ejercida por éstos.

5. La competencia para sancionar las infracciones a que se refiere el artículo 52 corresponderá, en todo caso, al Director General de Tráfico o al órgano que tenga atribuida la competencia en las comunidades autónomas que hayan recibido el traspaso de funciones y servicios en materia de tráfico y circulación de vehículos a motor, limitada al ámbito territorial de la comunidad autónoma.

6. En las ciudades de Ceuta y Melilla las competencias que en los apartados anteriores se atribuyen a los Jefes Provinciales de Tráfico, corresponderán a los Jefes Locales de Tráfico.

<!-- bloque a85 · versión publicada 20220914 · vigente desde 20220915 -->

### Artículo 85. Actuaciones administrativas y jurisdiccionales penales.

1. Cuando en un procedimiento sancionador se ponga de manifiesto un hecho que ofrezca indicios de delito perseguible de oficio, la autoridad administrativa lo pondrá en conocimiento del Ministerio Fiscal, por si procede el ejercicio de la acción penal, y acordará la suspensión de las actuaciones.

En todo caso, cuando se produzca un accidente de tráfico con resultado de lesión o muerte, la autoridad administrativa lo pondrá en conocimiento de la autoridad judicial, acompañando la comunicación del oportuno atestado.

2. Concluido el proceso penal con sentencia condenatoria, se archivará el procedimiento sancionador sin declaración de responsabilidad.

3. Si la sentencia es absolutoria o el procedimiento penal finaliza con otra resolución que le ponga fin sin declaración de responsabilidad, y siempre que la misma no esté fundada en la inexistencia del hecho, se podrá iniciar o continuar el procedimiento sancionador contra quien no haya sido condenado en vía penal.

La resolución que se dicte deberá respetar, en todo caso, la declaración de hechos probados en dicho procedimiento penal.

> _Nota BOE: Se modifica el apartado 1 por la disposición final 1 de la Ley Orgánica 11/2022, de 13 de septiembre. Ref. BOE-A-2022-14965#df_

<!-- bloque a86 · versión publicada 20151031 · vigente desde 20160131 -->

### Artículo 86. Incoación.

1. El procedimiento sancionador se incoará de oficio por la autoridad competente que tenga noticia de los hechos que puedan constituir infracciones tipificadas en esta ley, por iniciativa propia o mediante denuncia de los agentes de la autoridad encargados de la vigilancia del tráfico en el ejercicio de las funciones que tienen encomendadas o de cualquier persona que tenga conocimiento de los hechos.

2. No obstante, la denuncia formulada por los agentes de la autoridad encargados de la vigilancia del tráfico en el ejercicio de las funciones que tienen encomendadas, y notificada en el acto al denunciado, constituye el acto de iniciación del procedimiento sancionador, a todos los efectos.

<!-- bloque a87 · versión publicada 20211221 · vigente desde 20220321 -->

### Artículo 87. Denuncias.

1. Los agentes de la autoridad encargados de la vigilancia del tráfico en el ejercicio de las funciones que tienen encomendadas deberán denunciar las infracciones que observen cuando ejerzan funciones de esa naturaleza.

2. En las denuncias por hechos de circulación deberá constar, en todo caso:

a) La identificación del vehículo con el que se haya cometido la presunta infracción.

b) La identidad del denunciado, si se conoce.

c) Una descripción sucinta del hecho, con expresión del lugar o tramo, fecha y hora.

d) El nombre, apellidos y domicilio del denunciante o, si es un agente de la autoridad o un empleado que sin tener esa condición realiza tareas de control de zonas de estacionamiento regulado, su número de identificación profesional aportado por la administración competente.

> _Nota BOE: Téngase en cuenta que esta actualización de la letra d) del apartado 2, establecida por el art. único.27 de la Ley 18/2021, de 20 de diciembre, Ref. BOE-A-2021-21006#au, entra en vigor el 21 de marzo de 2022, según determina su disposición final cuarta. Redacción anterior: "d) El nombre, apellidos y domicilio del denunciante o, si es un agente de la autoridad, su número de identificación profesional."_

3. En las denuncias que los agentes de la autoridad notifiquen en el acto al denunciado deberá constar, además, a efectos de lo dispuesto en el artículo 86.1:

a) La infracción presuntamente cometida, la sanción que pueda corresponder y el número de puntos cuya pérdida lleve aparejada la infracción.

b) El órgano competente para imponer la sanción y la norma que le atribuye tal competencia.

c) Si el denunciado procede al abono de la sanción en el acto deberá señalarse, además, la cantidad abonada y las consecuencias derivadas del pago de la sanción previstas en el artículo 94.

d) En el caso de que no se proceda al abono en el acto de la sanción, deberá indicarse que dicha denuncia inicia el procedimiento sancionador y que dispone de un plazo de veinte días naturales para efectuar el pago, con la reducción y las consecuencias establecidas en el artículo 94, o para formular las alegaciones y proponer las pruebas que estime convenientes. En este caso, se indicarán los lugares, oficinas o dependencias donde puede presentarlas.

e) Si en el plazo señalado en el párrafo anterior no se han formulado alegaciones o no se ha abonado la multa, se indicará que el procedimiento se tendrá por concluido el día siguiente a la finalización de dicho plazo, conforme se establece en el artículo 95.4.

f) El domicilio que, en su caso, indique el interesado a efectos de notificaciones. Este domicilio no se tendrá en cuenta si el denunciado tiene asignada una Dirección Electrónica Vial (DEV), ello sin perjuicio de lo previsto en la normativa sobre acceso electrónico de los ciudadanos a los servicios públicos.

4. En el supuesto de infracciones que impliquen detracción de puntos, el agente denunciante tomará nota de los datos del permiso o de la licencia de conducción y los remitirá al órgano sancionador competente que, cuando la sanción sea firme en vía administrativa, los comunicará juntamente con la sanción y la detracción de puntos correspondiente al Registro de Conductores e Infractores del organismo autónomo Jefatura Central de Tráfico.

5. Cuando el infractor no acredite su residencia legal en territorio español, el agente denunciante fijará provisionalmente la cuantía de la multa y, de no depositarse su importe, el conductor deberá trasladar el vehículo e inmovilizarlo en el lugar indicado por el agente denunciante. El depósito podrá efectuarse mediante tarjeta de crédito, o en metálico en euros y, en todo caso, se tendrá en cuenta lo previsto en el artículo 94 respecto a la posibilidad de reducción del 50 por ciento de la multa inicialmente fijada.

6. En las denuncias por hechos ajenos a la circulación se especificarán todos los datos necesarios para su descripción.

> _Nota BOE: Se modifica la letra d) del apartado 2, con efectos de 21 de marzo de 2022, por el art. único.27 de la Ley 18/2021, de 20 de diciembre. Ref. BOE-A-2021-21006#au_

<!-- bloque a88 · versión publicada 20151031 · vigente desde 20160131 -->

### Artículo 88. Valor probatorio de las denuncias de los agentes de la autoridad encargados de la vigilancia del tráfico, en el ejercicio de las funciones que tienen encomendadas.

Las denuncias formuladas por los agentes de la autoridad encargados de la vigilancia del tráfico en el ejercicio de las funciones que tienen encomendadas tendrán valor probatorio, salvo prueba en contrario, de los hechos denunciados, de la identidad de quienes los hubieran cometido y, en su caso, de la notificación de la denuncia, sin perjuicio del deber de aquéllos de aportar todos los elementos probatorios que sean posibles sobre el hecho denunciado.

<!-- bloque a89 · versión publicada 20151031 · vigente desde 20160131 -->

### Artículo 89. Notificación de la denuncia.

1. Las denuncias se notificarán en el acto al denunciado.

2. No obstante, la notificación podrá efectuarse en un momento posterior siempre que se dé alguna de las siguientes circunstancias:

a) Que la denuncia se formule en circunstancias en que la detención del vehículo pueda originar un riesgo para la circulación. En este caso, el agente deberá indicar los motivos concretos que la impiden.

b) Que la denuncia se formule estando el vehículo estacionado, cuando el conductor no esté presente.

c) Que se haya tenido conocimiento de la infracción a través de medios de captación y reproducción de imágenes que permitan la identificación del vehículo.

d) Que el agente denunciante se encuentre realizando labores de vigilancia, control, regulación o disciplina del tráfico y carezca de medios para proceder al seguimiento del vehículo.

<!-- bloque a90 · versión publicada 20151031 · vigente desde 20160131 -->

### Artículo 90. Práctica de la notificación de las denuncias.

1. Las Administraciones con competencias sancionadoras en materia de tráfico notificarán las denuncias que no se entreguen en el acto y las demás notificaciones a que dé lugar el procedimiento sancionador en la Dirección Electrónica Vial (DEV).

En el caso de que el denunciado no la tuviese, la notificación se efectuará en el domicilio que expresamente hubiese indicado para el procedimiento, y en su defecto, en el domicilio que figure en los registros del organismo autónomo Jefatura Central de Tráfico.

2. La notificación en la Dirección Electrónica Vial (DEV) permitirá acreditar la fecha y hora en que se produzca la puesta a disposición del denunciado del acto objeto de notificación, así como el acceso a su contenido, momento a partir del cual la notificación se entenderá practicada a todos los efectos legales.

Si existiendo constancia de la recepción de la notificación en la Dirección Electrónica Vial (DEV), transcurrieran diez días naturales sin que se acceda a su contenido, se entenderá que aquélla ha sido rechazada, salvo que de oficio o a instancia del destinatario se compruebe la imposibilidad técnica o material del acceso. El rechazo se hará constar en el procedimiento sancionador, especificándose las circunstancias del intento de notificación, y se tendrá por efectuado el trámite, continuándose el procedimiento.

3. Cuando la notificación se practique en el domicilio del interesado, de no hallarse presente éste en el momento de entregarse, podrá hacerse cargo de la misma cualquier persona que se encuentre en el domicilio y haga constar su identidad.

Si nadie se hiciera cargo de la notificación, se dejará constancia de esta circunstancia en el procedimiento sancionador, junto con el día y la hora en que se intentó, y se practicará de nuevo dentro de los tres días siguientes. Si tampoco fuera posible la entrega, se dará por cumplido el trámite, procediéndose a la publicación en el Boletín Oficial del Estado.

Si estando el interesado en el domicilio rechazase la notificación, se hará constar en el procedimiento sancionador, especificándose las circunstancias del intento de notificación, teniéndose por efectuado el trámite y continuándose el procedimiento.

<!-- bloque a91 · versión publicada 20151031 · vigente desde 20160131 -->

### Artículo 91. Notificaciones en el «Boletín Oficial del Estado» (BOE).

Las notificaciones que no puedan efectuarse en la Dirección Electrónica Vial (DEV) y, en caso de no disponer de la misma, en el domicilio expresamente indicado para el procedimiento o, de no haber indicado ninguno, en el domicilio que figure en los registros del organismo autónomo Jefatura Central de Tráfico, se practicarán en el «Boletín Oficial del Estado» (BOE). Transcurrido el período de veinte días naturales desde que la notificación se hubiese publicado en el BOE se entenderá que ésta ha sido practicada, dándose por cumplido dicho trámite.

<!-- bloque a92 · versión publicada 20151031 · vigente desde 20160131 -->

### Artículo 92. Tablón Edictal de Sanciones de Tráfico (TESTRA).

1. Con carácter previo y facultativo, las notificaciones a que se refiere el artículo anterior podrán practicarse también en el Tablón Edictal de Sanciones de Tráfico (TESTRA), que será gestionado por el organismo autónomo Jefatura Central de Tráfico.

2. El funcionamiento, la gestión y la publicación en el TESTRA se hará conforme a lo dispuesto en la normativa de protección de datos de carácter personal y en la de acceso electrónico de los ciudadanos a los servicios públicos.

<!-- bloque a93 · versión publicada 20211221 · vigente desde 20220321 -->

### Artículo 93. Clases de procedimientos sancionadores.

1. Notificada la denuncia, ya sea en el acto o en un momento posterior, el denunciado dispondrá de un plazo de veinte días naturales para realizar el pago voluntario con reducción de la sanción de multa, o para formular las alegaciones y proponer o aportar las pruebas que estime oportunas.

En el supuesto de que no se haya producido la detención del vehículo, el titular, el arrendatario a largo plazo o el conductor habitual, en su caso, dispondrán de un plazo de veinte días naturales para identificar al conductor responsable de la infracción, contra el que se iniciará el procedimiento sancionador. Esta identificación se efectuará por medios telemáticos si la notificación se hubiese realizado a través de la Dirección Electrónica Vial (DEV).

Si se efectúa el pago de la multa en las condiciones indicadas en el párrafo primero, se seguirá el procedimiento sancionador abreviado, y en caso de no hacerlo, el procedimiento sancionador ordinario.

2. El procedimiento sancionador abreviado no será de aplicación a las infracciones previstas en el artículo 77.h), j), n), ñ), o), p), q), r), s) y t).

> _Nota BOE: Téngase en cuenta que esta actualización del apartado 2, establecida por el art. único.28 de la Ley 18/2021, de 20 de diciembre, Ref. BOE-A-2021-21006#au, entra en vigor el 21 de marzo de 2022, según determina su disposición final cuarta. Redacción anterior: "2. El procedimiento sancionador abreviado no será de aplicación a las infracciones previstas en el artículo 77. h), j), n), ñ), o), p), q) y r)."_

3. El incumplimiento de la obligación de asegurar el vehículo que se establece en la normativa sobre responsabilidad civil y seguro en la circulación de vehículos a motor, podrá sancionarse conforme a uno de los dos procedimientos sancionadores que se establecen en esta ley.

4. Además de en los registros, oficinas y dependencias previstos en la normativa de procedimiento administrativo común, las alegaciones, escritos y recursos que se deriven de los procedimientos sancionadores en materia de tráfico podrán presentarse en los registros, oficinas y dependencias expresamente designados en la correspondiente denuncia o resolución sancionadora.

Cuando se presenten en los registros, oficinas o dependencias no designados expresamente, éstos los remitirán a los órganos competentes en materia de tráfico a la mayor brevedad posible.

> _Nota BOE: Se modifica el apartado 2, con efectos de 21 de marzo de 2022, por el art. único.28 de la Ley 18/2021, de 20 de diciembre. Ref. BOE-A-2021-21006#au_

<!-- bloque a94 · versión publicada 20151031 · vigente desde 20160131 -->

### Artículo 94. Procedimiento sancionador abreviado.

Una vez realizado el pago voluntario de la multa, ya sea en el acto de entrega de la denuncia o dentro del plazo de veinte días naturales contados desde el día siguiente al de su notificación, concluirá el procedimiento sancionador con las siguientes consecuencias:

a) La reducción del 50 por ciento del importe de la sanción.

b) La renuncia a formular alegaciones. En el caso de que se formulen se tendrán por no presentadas.

c) La terminación del procedimiento, sin necesidad de dictar resolución expresa, el día en que se realice el pago.

d) El agotamiento de la vía administrativa, siendo recurrible únicamente ante el orden jurisdiccional contencioso-administrativo.

e) El plazo para interponer el recurso contencioso-administrativo se iniciará el día siguiente a aquel en que tenga lugar el pago.

f) La firmeza de la sanción en la vía administrativa desde el momento del pago, produciendo plenos efectos desde el día siguiente.

g) La sanción no computará como antecedente en el Registro de Conductores e Infractores del organismo autónomo Jefatura Central de Tráfico, siempre que se trate de infracciones graves que no lleven aparejada pérdida de puntos.

<!-- bloque a95 · versión publicada 20211221 · vigente desde 20220321 -->

### Artículo 95. Procedimiento sancionador ordinario.

1. Notificada la denuncia, el interesado dispondrá de un plazo de veinte días naturales para formular las alegaciones que tenga por conveniente y proponer o aportar las pruebas que estime oportunas.

2. Si las alegaciones formuladas aportan datos nuevos o distintos de los constatados por el agente denunciante, y siempre que se estime necesario por el instructor, se dará traslado de aquéllas al agente para que informe en el plazo de quince días naturales.

En todo caso, el instructor podrá acordar que se practiquen las pruebas que estime pertinentes para la averiguación y calificación de los hechos y para la determinación de las posibles responsabilidades. La denegación de la práctica de las pruebas deberá ser motivada, dejando constancia en el procedimiento sancionador.

3. Concluida la instrucción del procedimiento sancionador, el órgano instructor elevará propuesta de resolución al órgano competente para sancionar para que dicte la resolución que proceda. Únicamente se dará traslado de la propuesta al interesado, para que pueda formular nuevas alegaciones en el plazo de quince días naturales, si figuran en el procedimiento sancionador o se han tenido en cuenta en la resolución otros hechos u otras alegaciones y pruebas diferentes a las aducidas por el interesado.

4. Si el denunciado no formula alegaciones ni abona el importe de la multa en el plazo de veinte días naturales siguientes al de la notificación de la denuncia, ésta surtirá el efecto de acto resolutorio del procedimiento sancionador en los siguientes casos:

a) Infracciones leves en todos los casos.

b) Infracciones graves que no supongan la detracción de puntos cuya notificación no se haya podido efectuar en el acto de la denuncia.

c) Infracciones graves y muy graves cuya notificación se efectuase en el acto de la denuncia, supongan o no la detracción de puntos.

En estos supuestos, la sanción podrá ejecutarse transcurridos treinta días naturales desde la notificación de la denuncia.

> _Nota BOE: Téngase en cuenta que esta actualización del apartado 4, establecida por el art. único.29 de la Ley 18/2021, de 20 de diciembre, Ref. BOE-A-2021-21006#au, entra en vigor el 21 de marzo de 2022, según determina su disposición final cuarta. Redacción anterior: "4. Cuando se trate de infracciones leves, de infracciones graves que no supongan la detracción de puntos, o de infracciones muy graves y graves cuya notificación se efectuase en el acto de la denuncia, si el denunciado no formula alegaciones ni abona el importe de la multa en el plazo de veinte días naturales siguientes al de la notificación de la denuncia, ésta surtirá el efecto de acto resolutorio del procedimiento sancionador. En este supuesto, la sanción podrá ejecutarse transcurridos treinta días naturales desde la notificación de la denuncia."_

5. La terminación del procedimiento pone fin a la vía administrativa y la sanción se podrá ejecutar desde el día siguiente al transcurso de los treinta días antes indicados.

> _Nota BOE: Se modifica el apartado 4, con efectos de 21 de marzo de 2022, por el art. único.29 de la Ley 18/2021, de 20 de diciembre. Ref. BOE-A-2021-21006#au_

<!-- bloque a96 · versión publicada 20151031 · vigente desde 20160131 -->

### Artículo 96. Recursos en el procedimiento sancionador ordinario.

1. La resolución sancionadora pondrá fin a la vía administrativa y la sanción se podrá ejecutar desde el día siguiente a aquel en que se notifique al interesado, produciendo plenos efectos, o, en su caso, una vez haya transcurrido el plazo indicado en el artículo 95.4.

2. Contra las resoluciones sancionadoras, podrá interponerse recurso de reposición, con carácter potestativo, en el plazo de un mes contado desde el día siguiente al de su notificación.

El recurso se interpondrá ante el órgano que dictó la resolución sancionadora, que será el competente para resolverlo.

3. La interposición del recurso de reposición no suspenderá la ejecución del acto impugnado ni la de la sanción. En el caso de que el recurrente solicite la suspensión de la ejecución, ésta se entenderá denegada transcurrido el plazo de un mes desde la solicitud sin que se haya resuelto.

4. No se tendrán en cuenta en la resolución del recurso hechos, documentos y alegaciones del recurrente que pudieran haber sido aportados en el procedimiento originario.

5. El recurso de reposición regulado en este artículo se entenderá desestimado si no recae resolución expresa en el plazo de un mes, quedando expedita la vía contencioso-administrativa.

6. Contra las resoluciones sancionadoras dictadas por los órganos competentes de las comunidades autónomas que hayan recibido el traspaso de funciones y servicios en materia de tráfico y circulación de vehículos a motor, así como por los Alcaldes, en el caso de las entidades locales, se estará a lo establecido en los anteriores apartados respetando la competencia sancionadora prevista en su normativa específica.

## Título V — Capítulo VI. Medidas provisionales y otras medidas (selección)

<!-- bloque a107 · versión publicada 20151031 · vigente desde 20160131 -->

### Artículo 107. Limitaciones de disposición en las autorizaciones administrativas.

1. El titular de un permiso o licencia de conducción no podrá efectuar ningún trámite relativo a los vehículos de los que fuese titular en el Registro de Vehículos del organismo autónomo Jefatura Central de Tráfico cuando figuren como impagadas en su historial de conductor cuatro sanciones firmes en vía administrativa por infracciones graves o muy graves.

2. El titular de un vehículo no podrá efectuar ningún trámite relativo al mismo cuando figuren como impagadas en el historial del vehículo cuatro sanciones firmes en vía administrativa por infracciones graves o muy graves.

3. Queda exceptuado de lo dispuesto en los apartados anteriores el trámite de baja temporal o definitiva de vehículos.

## Título V — Capítulo VII. Ejecución de las sanciones

<!-- bloque a108 · versión publicada 20151031 · vigente desde 20160131 -->

### Artículo 108. Ejecución.

Una vez firme la sanción en vía administrativa, se procederá a su ejecución conforme a lo previsto en esta ley.

<!-- bloque a109 · versión publicada 20151031 · vigente desde 20160131 -->

### Artículo 109. Ejecución de la sanción de suspensión de las autorizaciones.

El cumplimiento de la sanción de suspensión prevista en el artículo 80 se iniciará transcurrido un mes desde que haya adquirido firmeza en vía administrativa, y el período de suspensión de la misma se anotará en los correspondientes registros.

<!-- bloque a110 · versión publicada 20151031 · vigente desde 20160131 -->

### Artículo 110. Cobro de multas.

1. Una vez firme la sanción, el interesado dispondrá de un plazo final de quince días naturales para el pago de la multa. Finalizado el plazo establecido sin que se haya pagado la multa, se iniciará el procedimiento de apremio.

2. Los órganos y procedimientos de la recaudación ejecutiva serán los establecidos en la normativa tributaria que le sea de aplicación, según las autoridades que las hayan impuesto.

<!-- bloque a111 · versión publicada 20151031 · vigente desde 20160131 -->

### Artículo 111. Responsables subsidiarios del pago de multas.

1. Los titulares de los vehículos con los que se haya cometido una infracción serán responsables subsidiarios en caso de impago de la multa impuesta al conductor, salvo en los siguientes supuestos:

a) Robo, hurto o cualquier otro uso en el que quede acreditado que el vehículo fue utilizado en contra de su voluntad.

b) Cuando el titular sea una empresa de alquiler sin conductor.

c) Cuando el vehículo tenga designado un arrendatario a largo plazo en el momento de cometerse la infracción. En este caso, la responsabilidad recaerá en aquel.

d) Cuando el vehículo tenga designado un conductor habitual en el momento de cometerse la infracción. En este caso, la responsabilidad recaerá en aquel.

2. La declaración de responsabilidad subsidiaria y sus consecuencias, incluida la posibilidad de adoptar medidas cautelares, se regirán por lo dispuesto en la normativa tributaria.

3. El responsable que haya satisfecho la multa tiene derecho de reembolso contra el infractor por la totalidad de lo que haya satisfecho.

## Título V — Capítulo VIII. Prescripción, caducidad y cancelación de antecedentes

<!-- bloque a112 · versión publicada 20151031 · vigente desde 20160131 -->

### Artículo 112. Prescripción y caducidad.

1. El plazo de prescripción de las infracciones previstas en esta ley será de tres meses para las infracciones leves y de seis meses para las infracciones graves y muy graves.

El plazo de prescripción comenzará a contar a partir del mismo día en que los hechos se hubieran cometido.

2. La prescripción se interrumpe por cualquier actuación administrativa de la que tenga conocimiento el denunciado o esté encaminada a averiguar su identidad o domicilio y se practique con otras administraciones, instituciones u organismos. También se interrumpe por la notificación efectuada de acuerdo con los artículos 89, 90 y 91.

El plazo de prescripción se reanudará si el procedimiento se paraliza durante más de un mes por causa no imputable al denunciado.

3. Si no se hubiera producido la resolución sancionadora transcurrido un año desde la iniciación del procedimiento, se producirá su caducidad y se procederá al archivo de las actuaciones, a solicitud de cualquier interesado o de oficio por el órgano competente para dictar resolución.

Cuando la paralización del procedimiento se hubiera producido a causa del conocimiento de los hechos por la jurisdicción penal, el plazo de caducidad se suspenderá y, una vez haya adquirido firmeza la resolución judicial, se reanudará el cómputo del plazo de caducidad por el tiempo que restaba en el momento de acordar la suspensión.

4. El plazo de prescripción de las sanciones consistentes en multa será de cuatro años y el de la suspensión prevista en el artículo 80 será de un año, computados desde el día siguiente a aquel en que adquiera firmeza la sanción en vía administrativa.

El cómputo y la interrupción del plazo de prescripción del derecho de la Administración para exigir el pago de las sanciones en vía de apremio consistentes en multa se regirán por lo dispuesto en la normativa tributaria.

<!-- bloque a113 · versión publicada 20151031 · vigente desde 20160131 -->

### Artículo 113. Anotación y cancelación.

1. Las sanciones por infracciones graves y muy graves y la detracción de puntos deberán ser comunicadas al Registro de Conductores e Infractores del organismo autónomo Jefatura Central de Tráfico por la autoridad que la hubiera impuesto en el plazo de los quince días naturales siguientes a su firmeza en vía administrativa.

2. Las autoridades judiciales comunicarán al Registro de Conductores e Infractores del organismo autónomo Jefatura Central de Tráfico, en el plazo de los quince días naturales siguientes a su firmeza, las penas de privación del derecho a conducir vehículos a motor y ciclomotores que se impongan por la comisión de delitos contra la seguridad vial.

3. En el Registro de Vehículos del organismo autónomo Jefatura Central de Tráfico quedarán reflejadas las sanciones firmes por infracciones graves y muy graves en las que un vehículo tanto matriculado en España como en el extranjero estuviese implicado y el impago de las mismas, en su caso. Estas anotaciones formarán parte del historial del vehículo.

4. Las anotaciones se cancelarán de oficio, a efectos de antecedentes, una vez transcurridos tres años desde su total cumplimiento o prescripción.

## Disposiciones adicionales, transitorias y finales (notificaciones DEV/TESTRA)

<!-- bloque daquinta · versión publicada 20151031 · vigente desde 20160131 -->

### Disposición adicional quinta. Notificaciones en comunidades autónomas que hayan recibido el traspaso de funciones y servicios en materia de tráfico y circulación de vehículos a motor.

Las comunidades autónomas que hayan recibido el traspaso de funciones y servicios en materia de tráfico y circulación de vehículos a motor podrán sustituir las notificaciones en la Dirección Electrónica Vial por notificaciones a través de sus propias plataformas informáticas, para aquellos ciudadanos que opten por las mismas.

Las administraciones locales pertenecientes a los ámbitos territoriales de las comunidades autónomas que hayan recibido el traspaso de funciones y servicios en materia de tráfico y circulación de vehículos a motor podrán suscribir convenios de colaboración para efectuar las notificaciones telemáticas a través de las plataformas de notificación de la comunidad autónoma.

<!-- bloque daundecima · versión publicada 20151031 · vigente desde 20160131 -->

### Disposición adicional undécima. Integración y coordinación de notificaciones a través del Tablón Edictal de Sanciones de Tráfico (TESTRA) y de la Dirección Electrónica Vial (DEV).

El Tablón Edictal de Sanciones de Tráfico (TESTRA) podrá integrarse en el Tablón Edictal Único cuando razones justificadas de eficiencia en la prestación del servicio así lo aconsejen para los anuncios de notificaciones edictales de los procedimientos sancionadores en materia de tráfico. Por estos mismos motivos, y cumpliendo las funciones que la ley recoge, la Dirección Electrónica Vial (DEV) podrá integrarse o coordinarse con la Dirección Electrónica Habilitada (DEH).

<!-- bloque dtsegunda · versión publicada 20151031 · vigente desde 20160131 -->

### Disposición transitoria segunda. Práctica de las notificaciones en la Dirección Electrónica Vial (DEV).

Las administraciones locales practicarán las notificaciones en la Dirección Electrónica Vial (DEV) antes del 25 de mayo de 2016, siempre que lo permitan sus disponibilidades presupuestarias y sus medios técnicos.

<!-- bloque dftercera · versión publicada 20211221 · vigente desde 20220321 -->

### Disposición final tercera. Habilitaciones al Ministro del Interior.

Se habilita al Ministro del Interior para determinar:

a) la duración, el contenido y los requisitos de los cursos de sensibilización y reeducación vial.

b) las condiciones para practicar la notificación en el TESTRA.

c) los términos en los que el titular o el arrendatario a largo plazo comunicarán al Registro de Vehículos la identidad del conductor habitual

d) los términos en los que el arrendatario a largo plazo comunicará al Registro de Vehículos la identidad del arrendatario.

e) los términos en que se comunicará al Registro Nacional de Víctimas de Accidentes de Tráfico la información referente a las víctimas de accidentes de tráfico.

f) la duración, el contenido y los requisitos de los cursos de conducción segura y eficiente, así como los mecanismos de certificación y control de los mismos.

> _Nota BOE: Téngase en cuenta que la letra f), añadida por el art. único.45 de la Ley 18/2021, de 20 de diciembre, Ref. BOE-A-2021-21006#au, entra en vigor el 21 de marzo de 2022, según determina su disposición final cuarta._

> _Nota BOE: Se añade la letra f), con efectos de 21 de marzo de 2022, por el art. único.45 de la Ley 18/2021, de 20 de diciembre. Ref. BOE-A-2021-21006#au_

---

## Jurisprudencia relevante

Solo se incluyen sentencias **verificadas en fuente primaria**: el texto íntegro de cada
una se ha consultado en el BOE (Suplemento del Tribunal Constitucional) el 2026-09-23.
Los resúmenes son propios. No se incluyen nombres de las partes.

No se ha podido verificar ninguna sentencia del Tribunal Supremo ni de tribunales
superiores: CENDOJ (poderjudicial.es) y tribunalconstitucional.es no son accesibles
desde el entorno de trabajo. Por el mismo motivo, **el ECLI de las sentencias siguientes
está pendiente de verificar** (el BOE no lo recoge en estas publicaciones).

Todas se dictaron sobre el texto articulado anterior (RDL 339/1990). Su aplicación al
régimen vigente del RDL 6/2015 (DEV, TESTRA, art. 11.1.a) está en las dudas abiertas.

### Identificación del conductor

- **STC 197/1995, de 21 de diciembre** (Pleno). Cuestiones de inconstitucionalidad
  acumuladas 2848/1993 y otras. BOE núm. 21, de 24/01/1996, ref. BOE-T-1996-1494.
  ECLI: pendiente de verificar.
  <https://www.boe.es/buscar/doc.php?id=BOE-T-1996-1494>
  Resumen: desestima la cuestión contra el antiguo art. 72.3 LSV. El deber del titular
  de comunicar quién conducía es un deber de colaboración que no obliga a declarar sobre
  la infracción ni a confesarla, por lo que no vulnera el derecho a no declarar contra sí
  mismo (art. 24.2 CE). La responsabilidad del identificado se decide después, en el
  procedimiento sancionador.

- **STC 111/2004, de 12 de julio** (Sala Primera). Recurso de amparo 6667-2000. BOE
  núm. 193, de 11/08/2004, ref. BOE-T-2004-14849. ECLI: pendiente de verificar.
  <https://www.boe.es/diario_boe/txt.php?id=BOE-T-2004-14849>
  Resumen: otorga el amparo (legalidad sancionadora, art. 25.1 CE) y anula la multa
  impuesta a una titular que identificó al conductor con nombre, apellidos y domicilio
  pero sin el número de permiso, porque la norma de entonces no exigía ese dato.
  **Ojo:** el art. 11.1.a vigente sí exige el número del permiso o licencia.

- **STC 29/2014, de 24 de febrero** (Sala Primera). Recurso de amparo 8363-2010. BOE
  núm. 73, de 25/03/2014, ref. BOE-A-2014-3239. ECLI: pendiente de verificar.
  <https://www.boe.es/diario_boe/txt.php?id=BOE-A-2014-3239>
  Resumen: deniega el amparo. Se puede sancionar al titular por una identificación que
  no es veraz cuando la Administración ha intentado dirigir el procedimiento contra la
  persona identificada y esta niega haber conducido. Aun así, esa negativa no hace
  responsable al titular de forma automática: hace falta un procedimiento con garantías.
  Distingue su caso del de la STC 111/2004 y posteriores.

### Notificación edictal de denuncias y sanciones de tráfico

- **STC 219/2007, de 8 de octubre** (Sala Segunda). Recurso de amparo 2204-2005. BOE
  núm. 273, de 14/11/2007, ref. BOE-T-2007-19598. ECLI: pendiente de verificar.
  <https://www.boe.es/diario_boe/txt.php?id=BOE-T-2007-19598>
  Resumen: otorga el amparo (art. 24.1 CE) frente a una multa municipal de tráfico
  notificada por edictos después de fallar la notificación en un domicilio erróneo. El
  Ayuntamiento podía conocer el domicilio real consultando sus propios archivos. No haberlo
  hecho antes de acudir a los edictos es falta de diligencia y deja al interesado sin
  defensa.

- **STC 128/2008, de 27 de octubre** (Sala Primera). Recurso de amparo 1292-2005. BOE
  núm. 281, de 21/11/2008, ref. BOE-T-2008-18801. ECLI: pendiente de verificar.
  <https://www.boe.es/diario_boe/txt.php?id=BOE-T-2008-18801>
  Resumen: otorga el amparo (art. 24.2 CE). Aunque se intentó notificar en el domicilio
  del Registro de Vehículos, la Administración no podía pasar a los edictos sin una mínima
  indagación en otros registros públicos, sobre todo cuando después notificó la providencia
  de apremio sin problema en otro domicilio. Anula la sanción y el apremio.

---

## Dudas abiertas

Formato: `TODO(juridico):` pregunta concreta, seguida de la fuente que habría que
consultar. Ninguna tiene respuesta en este fichero y no deben resolverse de memoria.

### Supletoriedad y cómputo de plazos

1. TODO(juridico): ¿Qué preceptos de la Ley 39/2015 se aplican de forma supletoria al
   procedimiento sancionador de tráfico? El art. 83.1 LSV remite «supletoriamente, en la
   normativa de procedimiento administrativo común», y la DA primera.2.c) de la Ley 39/2015
   dice que los procedimientos sancionadores «en materia de tráfico y seguridad vial» se
   rigen «por su normativa específica y supletoriamente por lo dispuesto en esta Ley».
   Hay que concretar qué pasa con los arts. 21, 25, 30, 40-46, 89-90 y 95 de la Ley 39/2015.
   Fuente: Ley 39/2015 consolidada (BOE-A-2015-10565) y jurisprudencia del TS sobre
   supletoriedad en tráfico (CENDOJ).
2. TODO(juridico): En los plazos de la LSV en «días naturales» (arts. 90.2, 91, 93.1,
   94, 95, 110.1, 113), ¿se aplica el art. 30.5 de la Ley 39/2015 (si el último día es
   inhábil, se prorroga al primer día hábil siguiente)? Y los plazos en días de la LSV que
   no dicen el tipo de día (p. ej. 90.3), ¿son hábiles por el art. 30.2 de la Ley 39/2015
   («Siempre que por Ley […] no se exprese otro cómputo, cuando los plazos se señalen por
   días, se entiende que éstos son hábiles»)? Fuente: Ley 39/2015, art. 30
   (BOE-A-2015-10565); doctrina del TS (CENDOJ).
3. TODO(juridico): Día inicial de los 20 días naturales. El art. 94 dice «contados desde
   el día siguiente al de su notificación», pero los arts. 93.1 y 95.1 solo dicen
   «Notificada la denuncia» y el 95.4 «siguientes al de la notificación de la denuncia».
   ¿Se cuentan todos desde el día siguiente a la notificación, como dice el art. 30.3 de la
   Ley 39/2015? Fuente: Ley 39/2015 art. 30; RD 320/1994 (si sigue aplicándose, duda 6).
4. TODO(juridico): ¿Cómo se computan los plazos en meses de la LSV: reposición «en el
   plazo de un mes contado desde el día siguiente al de su notificación» (96.2), silencio
   y suspensión de un mes (96.3 y 96.5), prescripción de tres y seis meses (112.1)? ¿Se
   cuentan de fecha a fecha (art. 30.4, párr. 2, Ley 39/2015: «El plazo concluirá el mismo
   día en que se produjo la notificación […] en el mes o el año de vencimiento»)? En la prescripción, ¿cómo encaja
   «comenzará a contar a partir del mismo día en que los hechos se hubieran cometido»
   (112.1) con el cómputo de fecha a fecha? ¿En qué fecha vence exactamente?
   Fuente: Ley 39/2015 art. 30.4; Código Civil art. 5; jurisprudencia del TS sobre
   el art. 112 LSV (CENDOJ).
5. TODO(juridico): Segundo intento de notificación en domicilio «dentro de los tres días
   siguientes» (90.3): ¿días hábiles o naturales? ¿Se aplican las reglas del art. 42.2 de
   la Ley 39/2015 (franja horaria distinta, etc.)? Fuente: Ley 39/2015 art. 42;
   jurisprudencia del TS sobre notificaciones en dos intentos (CENDOJ).

### Normativa de desarrollo y ámbito local (Palma)

6. TODO(juridico): Vigencia y aplicabilidad del RD 320/1994, de 25 de febrero, Reglamento
   de procedimiento sancionador en materia de tráfico (BOE-A-1994-8985). A 2026-09-23 la
   API del BOE lo marca como no derogado (`estatus_derogacion: N`). Su última modificación
   registrada es de 2003, y en 2005 el BOE recoge la nulidad del art. 12.2, párrafo 2, por
   STS de 27/10/2004. Es anterior a la reforma de la LSV y al RDL 6/2015. ¿Qué preceptos
   siguen aplicándose y cuáles han quedado desplazados por la LSV?
   Fuente: RD 320/1994 consolidado y su análisis en boe.es; jurisprudencia del TS (CENDOJ).
7. TODO(juridico): Competencia sancionadora en Palma. ¿Qué órgano sanciona en la práctica
   (Alcalde o concejal o órgano delegado, art. 84.4)? ¿Qué ordenanza municipal de
   circulación está vigente y dónde se publicó (BOIB)? ¿Tiene especialidades de
   procedimiento, órganos o lugares de presentación (art. 93.4)? ¿Existe un recurso o
   régimen específico para Palma como municipio de gran población (art. 96.6, «respetando
   la competencia sancionadora prevista en su normativa específica»)?
   Fuente: sede electrónica del Ajuntament de Palma, BOIB, Ley 7/1985 (Título X).
8. TODO(juridico): ¿Ha recibido la Comunitat Autònoma de les Illes Balears el traspaso de
   funciones y servicios en materia de tráfico (arts. 84.3 y 96.6, DA quinta)? Si no, en
   vías interurbanas de Mallorca sanciona la Jefatura Provincial de Tráfico (84.1). Hay que
   confirmarlo. Fuente: reales decretos de traspaso en BOE; Estatuto de Autonomía de las
   Illes Balears (LO 1/2007).
9. TODO(juridico): ¿Qué norma metrológica concreta aplica el art. 83.2 a cinemómetros y
   etilómetros (Ley 32/2014 de Metrología y la orden ministerial vigente de control
   metrológico)? ¿Qué debe acreditar la Administración en el expediente (certificado de
   verificación, fecha, vigencia)? Fuente: BOE (Ley 32/2014 y orden vigente, hay que
   buscarla); jurisprudencia del TS/TSJ (CENDOJ).

### Caducidad y prescripción

10. TODO(juridico): Caducidad de un año (112.3): ¿cuál es exactamente la «iniciación del
    procedimiento»? Si la denuncia se notifica en el acto, el art. 86.2 la hace acto de
    iniciación. Pero en radar, estacionamiento sin conductor o captación por imagen (89.2),
    ¿cuenta la fecha de la denuncia, la del acuerdo de incoación o la de la notificación?
    ¿Y cuando hay identificación de otro conductor (93.1, párr. 2)?
    Fuente: jurisprudencia del TS sobre el art. 112.3 LSV y su precedente en el
    RDL 339/1990 (CENDOJ); Ley 39/2015 arts. 21.3 y 25.
11. TODO(juridico): Para evitar la caducidad, ¿basta con que la resolución sancionadora
    se «produzca» (se dicte) antes del año, o debe notificarse, o intentarse notificar,
    en ese plazo (Ley 39/2015 art. 40.4)? En los casos del 95.4, en que la denuncia hace
    de acto resolutorio, ¿cómo juega la caducidad?
    Fuente: Ley 39/2015 arts. 25 y 40.4; jurisprudencia del TS (CENDOJ).
12. TODO(juridico): ¿Qué actuaciones interrumpen la prescripción (112.2)? En concreto:
    ¿interrumpe un intento de notificación fallido, o la publicación en TESTRA sin
    publicación en BOE? ¿Cuándo «se paraliza durante más de un mes por causa no imputable
    al denunciado» el procedimiento? Tras declararse la caducidad, ¿se puede iniciar un nuevo
    procedimiento si la infracción no ha prescrito? ¿Se aplica en tráfico la regla de que
    «los procedimientos caducados no interrumpirán el plazo de prescripción» (Ley 39/2015
    art. 95.3), también respecto de las notificaciones hechas en el procedimiento caducado?
    Fuente: jurisprudencia del TS (CENDOJ); Ley 39/2015 art. 95.
13. TODO(juridico): ¿Se aplica de forma supletoria el art. 30 de la Ley 40/2015
    (prescripción de infracciones y sanciones) en lo que el art. 112 LSV no regula? Por
    ejemplo, infracciones continuadas o permanentes, o el día inicial de la prescripción de
    la sanción cuando se desestima por silencio un recurso de reposición.
    Fuente: Ley 40/2015 (BOE-A-2015-10566) arts. 25-31; jurisprudencia del TS (CENDOJ).

### Reducción del 50 %, firmeza y recursos

14. TODO(juridico): Si se paga con reducción y luego se quiere impugnar: el art. 94
    dice que el pago supone renuncia a alegar y agota la vía administrativa, siendo la
    sanción «recurrible únicamente ante el orden jurisdiccional contencioso-administrativo».
    ¿Es inadmisible entonces un recurso de reposición? ¿Cuál es el plazo del contencioso
    (la LSV solo fija su inicio, 94.e)? ¿Qué pasa con un pago reducido fuera de plazo o
    parcial? ¿Se aplica la reducción al importe graduado según el art. 81?
    Fuente: Ley 29/1998 (LJCA) arts. 8 y 46; jurisprudencia (CENDOJ).
15. TODO(juridico): Firmeza y ejecutividad. El art. 96.1 permite ejecutar la resolución
    desde el día siguiente a su notificación, aunque quepa reposición potestativa. Los arts.
    108 y 110.1 hablan de sanción «firme en vía administrativa». ¿Cuándo es firme una
    sanción recurrible en reposición: al notificarse o al vencer el mes del 96.2? ¿Cómo
    encaja con el art. 90.3 de la Ley 39/2015 (ejecutividad cuando no quepa recurso
    ordinario en vía administrativa)? ¿Desde cuándo corren los 15 días naturales del
    art. 110.1 y los cuatro años del 112.4?
    Fuente: Ley 39/2015 arts. 90, 98 y 117; jurisprudencia del TS (CENDOJ).
16. TODO(juridico): Recurso de reposición frente a vía contencioso-administrativa. ¿Qué
    órgano judicial es competente (juzgados de lo contencioso, art. 8 LJCA) y en qué
    plazos, tras resolución expresa o silencio (96.5)? ¿Cabe recurso extraordinario de
    revisión (Ley 39/2015 art. 125) contra sanciones firmes? ¿Afecta el art. 96.4 (no se
    tienen en cuenta en la reposición documentos que pudieron aportarse antes) a la
    estrategia de alegaciones?
    Fuente: LJCA (BOE-A-1998-16718) arts. 8, 25 y 46; Ley 39/2015 arts. 123-126.

### Notificaciones (DEV, domicilio, BOE, TESTRA)

17. TODO(juridico): Efecto de la notificación en DEV sobre los plazos. Si se accede al
    contenido, la notificación se entiende practicada en ese momento (90.2). Si no se
    accede en diez días naturales, se entiende rechazada y «se tendrá por efectuado el
    trámite». ¿Desde qué día corren entonces los 20 días naturales? ¿Cómo encaja con el
    art. 43.2 de la Ley 39/2015 y con la posible integración de la DEV en la Dirección
    Electrónica Habilitada (DEH) (DA undécima)? ¿Notifica hoy el Ajuntament de Palma por DEV (DT segunda), por
    plataforma propia o solo en papel?
    Fuente: Ley 39/2015 arts. 41-43; normativa y sede de la DGT sobre DEV; Ajuntament
    de Palma.
18. TODO(juridico): TESTRA y BOE. El art. 91 hace producir efecto a la publicación en el
    BOE a los 20 días naturales. El art. 92 dice que TESTRA es «previo y facultativo». ¿Qué
    efecto jurídico tiene hoy una publicación solo en TESTRA? ¿Se ha integrado TESTRA en el
    Tablón Edictal Único del BOE (DA undécima; art. 44 Ley 39/2015)? ¿Qué orden ministerial
    regula las condiciones de TESTRA (DF tercera b)?
    Fuente: BOE (orden de TESTRA, hay que buscarla); Ley 39/2015 art. 44.
19. TODO(juridico): ¿Siguen aplicándose al régimen actual de DEV, domicilio de la DGT,
    BOE y TESTRA las SSTC 219/2007 y 128/2008, que exigen indagar el domicilio antes de
    notificar por edictos? ¿Hay doctrina posterior del TC o del TS sobre notificación
    edictal en tráfico con el RDL 6/2015? Fuente: hj.tribunalconstitucional.es; CENDOJ.
20. TODO(juridico): Identificación del conductor. ¿Desde qué día corren los 20 días
    naturales del art. 93.1, párr. 2 (el texto no lo dice)? ¿Qué requisitos debe cumplir
    el requerimiento para que sea «debidamente» hecho (77.j)? ¿Sigue valiendo la doctrina
    de la STC 111/2004 ahora que el art. 11.1.a exige el número del permiso? ¿Se puede
    pagar con reducción la sanción por no identificar (el art. 93.2 excluye el 77.j del
    procedimiento abreviado)?
    Fuente: jurisprudencia del TS y del TC posterior a 2005 (CENDOJ, hj.tribunalconstitucional.es).

### Verificación pendiente (no jurídica)

21. TODO(juridico): Verificar el ECLI de las SSTC 197/1995, 111/2004, 29/2014, 219/2007
    y 128/2008 en hj.tribunalconstitucional.es (no accesible desde el entorno de trabajo).
