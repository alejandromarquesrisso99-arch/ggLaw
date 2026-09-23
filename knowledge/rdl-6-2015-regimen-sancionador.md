---
norma: Real Decreto Legislativo 6/2015, de 30 de octubre, por el que se aprueba el texto refundido de la Ley sobre Tráfico, Circulación de Vehículos a Motor y Seguridad Vial
articulos: [11, 74, 75, 76, 77, 80, 81, 82, 84, 85, 86, 88, 89, 92, 96, 108, 110, 112]
fuente: https://www.boe.es/buscar/act.php?id=BOE-A-2015-11722
version_consolidada: 2026-06-26
consultado: 2026-09-23
estado: revisado
---

# RDL 6/2015 (Ley sobre Tráfico): resto del régimen sancionador

## Nota sobre la fuente

- Transcripción literal de la versión vigente de cada artículo, obtenida de la API de datos
  abiertos del BOE (legislación consolidada), consultada el 2026-09-23. Bajo cada artículo se
  indican sus versiones y, si las hay, las notas del BOE sobre la norma que lo modificó. Las
  redacciones anteriores no se copian.
- `version_consolidada` es la fecha de actualización más reciente del índice del texto
  consolidado. La `fecha_actualizacion` de los metadatos es la del registro, no la del texto,
  y puede ser posterior.
- Junto con knowledge/rdl-6-2015.md (arts. 83, 87, 90, 91, 93, 94 y 95) completa el capítulo
  IV del título V (procedimiento sancionador, arts. 83-96).

## Notas para ggLaw (no forman parte del texto legal)

- **Gravedad (arts. 75, 76 y 77):** determina el plazo de prescripción del art. 112.1 (tres
  meses las leves; seis las graves y muy graves). El art. 77.j) tipifica como muy grave
  incumplir la obligación de identificar verazmente al conductor (art. 11).
- **Prescripción (art. 112.1):** corre «a partir del mismo día en que los hechos se hubieran
  cometido». `compute_deadline` no sirve para ella, porque cuenta desde el día siguiente.
  TODO(juridico): (1) ¿el plazo en meses se cuenta de fecha a fecha incluyendo el día de los
  hechos?; (2) ¿se aplica la prórroga del art. 30.5 de la Ley 39/2015 a un plazo de
  prescripción? Fuente: jurisprudencia sobre el art. 112 RDL 6/2015.
- **Interrupción de la prescripción (art. 112.2):** se interrumpe por «cualquier actuación
  administrativa de la que tenga conocimiento el denunciado o esté encaminada a averiguar su
  identidad o domicilio y se practique con otras administraciones, instituciones u
  organismos», y por las notificaciones de los arts. 89, 90 y 91; se reanuda si el
  procedimiento se paraliza más de un mes por causa no imputable al denunciado. Una regla que
  compare solo la fecha de los hechos con la de la notificación daría falsos positivos; una
  que trate cualquier averiguación interna como interruptiva daría falsos negativos.
  TODO(juridico): ¿la condición «y se practique con otras administraciones…» afecta solo a la
  averiguación de identidad o domicilio o también a la primera alternativa? Fuente:
  jurisprudencia sobre el art. 112.2 RDL 6/2015.
- **Caducidad (art. 112.3):** un año desde la iniciación del procedimiento sin que se haya
  producido la resolución sancionadora. Solo coincide con la fecha de la denuncia si se
  notificó en el acto (art. 86.2); si no, cuenta desde la incoación. El plazo se suspende
  mientras la jurisdicción penal conoce de los hechos (art. 112.3, párrafo segundo). La regla
  necesita la fecha de iniciación y la fecha de la resolución (o de su notificación).
  TODO(juridico): (1) ¿basta con dictar la resolución dentro del año o debe notificarse (arts.
  21.1, 25.1 y 40.4 de la Ley 39/2015, supletorios)?; (2) ¿se cuenta de fecha a fecha (art.
  30.4) y se aplica la prórroga del art. 30.5 a un plazo de la Administración?; (3) ¿se
  aplican las suspensiones del art. 22 y la interrupción del art. 25.2 de la Ley 39/2015?;
  (4) si la incoación no se notificó en el acto, ¿cuenta la fecha del acuerdo o la de su
  notificación? Fuente: jurisprudencia sobre el art. 112.3 RDL 6/2015.
- **Art. 96:** recurso de reposición potestativo en un mes contra la resolución sancionadora,
  que pone fin a la vía administrativa.
- Arts. 74, 80-82, 108 y 110: infracciones, sanciones, responsables, ejecución y cobro.
- El anexo IV (sanciones por exceso de velocidad) tiene tablas y no se puede transcribir con el
  script de estos ficheros; necesita un tratamiento propio. Tampoco está transcrita la
  normativa de control metrológico de los cinemómetros. TODO(juridico): transcribir ambos
  antes de la regla de verificación metrológica del cinemómetro.
- Grafías que están así en el BOE (sic): el «.»» al final del art. 76.h), el punto que falta al
  final del art. 76.b) y «de acreditación los centros» en el art. 77.q).

## Artículo 11. Obligaciones del titular del vehículo y del conductor habitual.

_Versión vigente desde 2016-01-31. Versiones en el BOE: 2016-01-31._

1. El titular de un vehículo tiene las siguientes obligaciones:

a) Facilitar a la Administración la identificación del conductor del vehículo en el momento de cometerse una infracción. Los datos facilitados deben incluir el número del permiso o licencia de conducción que permita la identificación en el Registro de Conductores e Infractores del organismo autónomo Jefatura Central de Tráfico.

Si el conductor no figura inscrito en el aludido Registro de Conductores e Infractores, el titular deberá disponer de copia de la autorización administrativa que le habilite a conducir en España y facilitarla a la Administración cuando le sea requerida. Si el titular fuese una empresa de alquiler de vehículos sin conductor, la copia de la autorización administrativa podrá sustituirse por la copia del contrato de arrendamiento.

b) Impedir que el vehículo sea conducido por quien nunca haya obtenido el permiso o la licencia de conducción correspondiente.

2. El titular del vehículo puede comunicar al Registro de Vehículos del organismo autónomo Jefatura Central de Tráfico la identidad del conductor habitual del mismo. En este supuesto, el titular queda exonerado de las obligaciones anteriores, que se trasladan al conductor habitual.

3. Las obligaciones establecidas en el apartado 1 y la comunicación descrita en el apartado anterior corresponden al arrendatario a largo plazo del vehículo, en el supuesto de que haya constancia de éste en el Registro de Vehículos del organismo autónomo Jefatura Central de Tráfico.

4. El titular del vehículo en régimen de arrendamiento a largo plazo debe comunicar al Registro de Vehículos del organismo autónomo Jefatura Central de Tráfico la identidad del arrendatario.

## Artículo 74. Disposiciones generales.

_Versión vigente desde 2016-01-31. Versiones en el BOE: 2016-01-31._

1. Las acciones u omisiones contrarias a esta ley tendrán el carácter de infracciones administrativas y serán sancionadas en los términos previstos en la misma.

2. Cuando las acciones u omisiones puedan ser constitutivas de delitos tipificados en las leyes penales, se estará a lo dispuesto en el artículo 85.

3. Las infracciones se clasifican en leves, graves y muy graves.

## Artículo 75. Infracciones leves.

_Versión vigente desde 2021-12-22. Versiones en el BOE: 2016-01-31, 2021-12-22._

_Nota del BOE: Se añaden las letras b) bis y b) ter y se modifica la c) por el art. único.22 de la Ley 18/2021, de 20 de diciembre. Ref. BOE-A-2021-21006#au_

Son infracciones leves las conductas tipificadas en esta ley referidas a:

a) Circular en una bicicleta sin hacer uso del alumbrado reglamentario.

b) No hacer uso de los elementos y prendas reflectantes por parte de los usuarios de bicicletas.

b) bis. El impago de peaje, tasa o precio público, cuando estos fueran exigibles.

b) ter. Incumplir la obligación de los conductores de estar en todo momento en condiciones de controlar su vehículo.

c) Incumplir las normas contenidas en esta Ley que no se califiquen expresamente como infracciones graves o muy graves en los artículos siguientes, especialmente en el caso de los conductores de bicicletas siempre que no comprometan la seguridad de los usuarios de la vía.

## Artículo 76. Infracciones graves.

_Versión vigente desde 2023-06-30. Versiones en el BOE: 2016-01-31, 2022-03-02, 2022-03-21, 2023-06-30._

_Nota del BOE: Se modifica la letra w) por el art. 147.3 del Real Decreto-ley 5/2023, de 28 de junio. Ref. BOE-A-2023-15135#a1-59_

_Nota del BOE: Se modifica la letra n) por la disposición fnal 5 del Real Decreto-ley 3/2022, de 1 de marzo. Ref. BOE-A-2022-3290#df-5_

_Nota del BOE: Se modifican las letras d), g), h), j), s) y x) y se añaden las letras z1), z2) y z3), con efectos de 21 de marzo de 2022, por el art. único.23 de la Ley 18/2021, de 20 de diciembre. Ref. BOE-A-2021-21006#au_

Son infracciones graves, cuando no sean constitutivas de delito, las conductas tipificadas en esta ley referidas a:

a) No respetar los límites de velocidad reglamentariamente establecidos o circular en un tramo a una velocidad media superior a la reglamentariamente establecida, de acuerdo con lo recogido en el anexo IV.

b) Realizar obras en la vía sin comunicarlas con anterioridad a su inicio a la autoridad responsable de la regulación, ordenación y gestión del tráfico, así como no seguir las instrucciones de dicha autoridad referentes a las obras

c) Incumplir las disposiciones de esta ley en materia de preferencia de paso, adelantamientos, cambios de dirección o sentido y marcha atrás, sentido de la circulación, utilización de carriles y arcenes y, en general, toda vulneración de las ordenaciones especiales de tráfico por razones de seguridad o fluidez de la circulación.

d) Parar o estacionar en el carril bus, en carriles o vías ciclistas, en curvas, cambios de rasante, zonas de estacionamiento para uso exclusivo de personas con discapacidad, túneles, pasos inferiores, intersecciones o en cualquier otro lugar peligroso o en el que se obstaculice gravemente la circulación o constituya un riesgo, especialmente para los peatones.

e) Circular sin hacer uso del alumbrado reglamentario.

f) Conducir utilizando cualquier tipo de casco de audio o auricular conectado a aparatos receptores o reproductores de sonido u otros dispositivos que disminuyan la atención permanente a la conducción.

g) Utilizar, sujetándolo con la mano, o manteniéndolo ajustado entre el casco y la cabeza del usuario, dispositivos de telefonía móvil mientras se conduce, conducir utilizando manualmente dispositivos de telefonía móvil en condiciones distintas a las anteriores, conducir utilizando manualmente navegadores o cualquier otro medio o sistema de comunicación, así como llevar en los vehículos mecanismos de detección de radares o cinemómetros.

h) No hacer uso, o no hacerlo de forma adecuada, del cinturón de seguridad, sistemas de retención infantil, casco y demás elementos de protección obligatorios.»

i) Circular con menores de doce años como pasajeros de ciclomotores o motocicletas, o con menores en los asientos delanteros o traseros, cuando no esté permitido.

j) No respetar las señales o las órdenes de la autoridad encargada de la regulación, ordenación, gestión, vigilancia y disciplina del tráfico, o de sus agentes.

k) No respetar la luz roja de un semáforo.

l) No respetar la señal de stop o la señal de ceda el paso.

ll) Conducir un vehículo siendo titular de una autorización que carece de validez por no haber cumplido los requisitos administrativos exigidos reglamentariamente en España.

m) Conducción negligente.

n) Arrojar a la vía o en sus inmediaciones objetos que puedan obstaculizar la libre circulación.

ñ) No mantener la distancia de seguridad con el vehículo precedente.

o) Circular con un vehículo que incumpla las condiciones técnicas reglamentariamente establecidas, salvo que sea calificada como muy grave, así como las infracciones relativas a las normas que regulan la inspección técnica de vehículos.

p) Incumplir la obligación de todo conductor de verificar que las placas de matrícula del vehículo no presentan obstáculos que impidan o dificulten su lectura e identificación.

q) No facilitar al agente de la autoridad encargado de la vigilancia del tráfico en el ejercicio de las funciones que tenga encomendadas su identidad, ni los datos del vehículo solicitados por los afectados en un accidente de circulación, estando implicado en el mismo.

r) Conducir vehículos con la carga mal acondicionada o con peligro de caída.

s) Conducir un vehículo teniendo el permiso de conducción suspendido como medida cautelar o teniendo prohibido su uso.

t) Circular con un vehículo cuyo permiso de circulación está suspendido.

u) La ocupación excesiva del vehículo que suponga aumentar en un 50 por ciento el número de plazas autorizadas, excluida la del conductor.

v) Incumplir la obligación de impedir que el vehículo sea conducido por quien nunca haya obtenido el permiso o la licencia de conducción correspondiente.

w) Incumplir las normas sobre el régimen de autorización y funcionamiento de los centros de enseñanza y formación, de los centros de sensibilización y reeducación vial, y de los centros de reconocimiento de conductores acreditados por el Ministerio del Interior o por los órganos competentes de las comunidades autónomas, salvo que puedan calificarse como infracciones muy graves.

x) Circular por autopistas, autovías, vías interurbanas, travesías o túneles urbanos con vehículos que lo tienen prohibido.

y) No instalar los dispositivos de alerta al conductor en los garajes o aparcamientos en los términos legal y reglamentariamente previstos.

z) Circular en posición paralela con vehículos que lo tienen prohibido.

z1) Incumplir la normativa sobre los cursos de conducción segura y eficiente cuya realización conlleve la recuperación o bonificación de puntos, salvo que puedan calificarse como muy graves.

z2) Incumplir las normas de actuación por los operadores cuya actividad esté vinculada con el ejercicio de las competencias del organismo autónomo Jefatura Central de Tráfico, salvo que puedan calificarse como muy graves.

z3) No respetar las restricciones de circulación derivadas de la aplicación de los protocolos ante episodios de contaminación y de las zonas de bajas emisiones.

## Artículo 77. Infracciones muy graves.

_Versión vigente desde 2023-06-30. Versiones en el BOE: 2016-01-31, 2022-03-21, 2023-06-30._

_Nota del BOE: Se modifica la letra q) por el art. 147.4 del Real Decreto-ley 5/2023, de 28 de junio. Ref. BOE-A-2023-15135#a1-59_

_Nota del BOE: Se modifica la letra q) y se añaden las letras s), t), u), v), w) y x), con efectos de 21 de marzo de 2022, por el art. único.24 de la Ley 18/2021, de 20 de diciembre. Ref. BOE-A-2021-21006#au_

Son infracciones muy graves, cuando no sean constitutivas de delito, las conductas tipificadas en esta ley referidas a:

a) No respetar los límites de velocidad reglamentariamente establecidos o circular en un tramo a una velocidad media superior a la reglamentariamente establecida, de acuerdo con lo recogido en el anexo IV.

b) Circular con un vehículo cuya carga ha caído a la vía, por su mal acondicionamiento, creando grave peligro para el resto de los usuarios.

c) Conducir con tasas de alcohol superiores a las que reglamentariamente se establezcan, o con presencia en el organismo de drogas.

d) Incumplir la obligación de todos los conductores de vehículos, y de los demás usuarios de la vía cuando se hallen implicados en algún accidente de tráfico o hayan cometido una infracción, de someterse a las pruebas que se establezcan para la detección de alcohol o de la presencia de drogas en el organismo.

e) Conducción temeraria.

f) Circular en sentido contrario al establecido.

g) Participar en competiciones y carreras de vehículos no autorizadas.

h) Conducir vehículos que tengan instalados inhibidores de radares o cinemómetros o cualesquiera otros mecanismos encaminados a interferir en el correcto funcionamiento de los sistemas de vigilancia del tráfico.

i) Aumentar en más del 50 por ciento los tiempos de conducción o minorar en más del 50 por ciento los tiempos de descanso establecidos en la legislación sobre transporte terrestre.

j) Incumplir el titular o el arrendatario del vehículo con el que se haya cometido la infracción la obligación de identificar verazmente al conductor responsable de dicha infracción, cuando sean debidamente requeridos para ello en el plazo establecido. En el supuesto de las empresas de alquiler de vehículos sin conductor la obligación de identificar se ajustará a las previsiones al respecto del artículo 11.

k) Conducir un vehículo careciendo del permiso o licencia de conducción correspondiente.

l) Circular con un vehículo que carezca de la autorización administrativa correspondiente, con una autorización que no sea válida por no cumplir los requisitos exigidos reglamentariamente, o incumpliendo las condiciones de la autorización administrativa que habilita su circulación.

ll) Circular con un vehículo que incumpla las condiciones técnicas que afecten gravemente a la seguridad vial.

m) Participar o colaborar en la colocación o puesta en funcionamiento de elementos que alteren el normal funcionamiento del uso del tacógrafo o del limitador de velocidad.

n) Realizar en la vía obras sin la autorización correspondiente, así como la retirada, ocultación, alteración o deterioro de la señalización permanente u ocasional.

ñ) No instalar la señalización de obras o hacerlo incumpliendo la normativa vigente, poniendo en grave riesgo la seguridad vial.

o) Incumplir las normas que regulan las actividades industriales que afectan de manera directa a la seguridad vial.

p) Instalar inhibidores de radares o cinemómetros en los vehículos o cualesquiera otros mecanismos encaminados a interferir en el correcto funcionamiento de los sistemas de vigilancia del tráfico.

q) Incumplir las normas sobre el régimen de autorización y funcionamiento de los centros de enseñanza y formación, de los centros de sensibilización y reeducación vial y de acreditación los centros de reconocimiento de conductores autorizados o acreditados por el Ministerio del Interior o por los órganos competentes de las comunidades autónomas, que afecten a la cualificación de los profesores o facultativos, al estado de los vehículos utilizados en la enseñanza, al cumplimiento del régimen lectivo, a elementos esenciales que incidan directamente en la seguridad vial, o que supongan un impedimento a las labores de control, inspección o auditoría.

r) Causar daños a la infraestructura de la vía, o alteraciones a la circulación debidos a la masa o a las dimensiones del vehículo, cuando se carezca de la correspondiente autorización administrativa o se hayan incumplido las condiciones de la misma, con independencia de la obligación de la reparación del daño causado.

s) Incumplir las normas sobre los cursos de conducción segura y eficiente cuya realización conlleve la recuperación o bonificación de puntos, que afecten a la cualificación de los profesores o facultativos, al estado de los vehículos utilizados, a elementos esenciales que incidan directamente en la seguridad vial, o que supongan un impedimento a las labores de control, inspección o auditoría.

t) Incumplir las normas de actuación por los operadores cuya actividad esté vinculada con el ejercicio de las competencias del organismo autónomo Jefatura Central de Tráfico que sean reiteración de errores de tramitación administrativa, o que supongan un impedimento a las labores de control, inspección o auditoría.

u) Utilizar dispositivos de intercomunicación no autorizados reglamentariamente, en las pruebas para la obtención y recuperación de permisos o licencias de conducción u otras autorizaciones administrativas para conducir, o colaborar o asistir con la utilización de dichos dispositivos.

v) Incumplir las normas en materia de auxilio en vías públicas.

w) Incumplir las normas sobre el uso de los alcoholímetros antiarranque.

x) Arrojar a la vía o sus inmediaciones objetos que puedan producir incendios o accidentes.

## Artículo 80. Tipos.

_Versión vigente desde 2022-03-21. Versiones en el BOE: 2016-01-31, 2022-03-21._

_Nota del BOE: Se modifica la letra d) del apartado 2 y se añade el apartado 4, con efectos de 21 de marzo de 2022, por el art. único.25 de la Ley 18/2021, de 20 de diciembre. Ref. BOE-A-2021-21006#au_

1. Las infracciones leves serán sancionadas con multa de hasta 100 euros; las graves, con multa de 200 euros, y las muy graves, con multa de 500 euros. No obstante, las infracciones consistentes en no respetar los límites de velocidad se sancionarán en la cuantía prevista en el anexo IV.

2. Sin perjuicio de lo dispuesto anteriormente, en la imposición de sanciones deberá tenerse en cuenta que:

a) Las infracciones previstas en el artículo 77. c) y d) serán sancionadas con multa de 1.000 euros. En el supuesto de conducción con tasas de alcohol superiores a las que reglamentariamente se establezcan, esta sanción únicamente se impondrá al conductor que ya hubiera sido sancionado en el año inmediatamente anterior por exceder la tasa de alcohol permitida, así como al que circule con una tasa que supere el doble de la permitida.

b) La multa por la infracción prevista en el artículo 77. j) será el doble de la prevista para la infracción originaria que la motivó, si es infracción leve, y el triple, si es infracción grave o muy grave.

c) La infracción recogida en el artículo 77. h) se sancionará con multa de 6.000 euros.

d) Las infracciones recogidas en el artículo 77.n), ñ), o), p), q), r), s) y t) se sancionarán con multa de entre 3.000 y 20.000 euros.

3. En el supuesto de la infracción recogida en el artículo 77. q) se podrá imponer la sanción de suspensión de la correspondiente autorización por el período de hasta un año. Durante el tiempo que dure la suspensión su titular no podrá obtener otra autorización para las mismas actividades.

La realización de actividades durante el tiempo de suspensión de la autorización llevará aparejada además una nueva suspensión por un período de seis meses al cometerse el primer quebrantamiento, y de un año si se produjese un segundo o sucesivos quebrantamientos.

4. En el caso de la infracción recogida en el artículo 77.u), el aspirante no podrá presentarse a las pruebas para la obtención o recuperación del permiso o licencia de conducción u otra autorización administrativa para conducir en el plazo de seis meses.

## Artículo 81. Graduación.

_Versión vigente desde 2022-03-21. Versiones en el BOE: 2016-01-31, 2022-03-21._

_Nota del BOE: Se modifica el segundo párrafo, con efectos de 21 de marzo de 2022, por el art. único.26 de la Ley 18/2021, de 20 de diciembre. Ref. BOE-A-2021-21006#au_

La cuantía de las multas establecidas en el artículo 80.1 y en el anexo IV podrá incrementarse en un 30 por ciento, en atención a la gravedad y trascendencia del hecho, los antecedentes del infractor y a su condición de reincidente, el peligro potencial creado para él mismo y para los demás usuarios de la vía y al criterio de proporcionalidad.

Los criterios de graduación establecidos anteriormente serán asimismo de aplicación a las sanciones por las infracciones previstas en el artículo 77, párrafos n) a t), ambos incluidos.

## Artículo 82. Responsables.

_Versión vigente desde 2016-01-31. Versiones en el BOE: 2016-01-31._

La responsabilidad por las infracciones a lo dispuesto en esta ley recaerá directamente en el autor del hecho en que consista la infracción. No obstante:

a) El conductor de cualquier vehículo para el que se exija el uso de casco por conductor y pasajero será responsable por la no utilización del casco de protección por el pasajero, así como por transportar pasajeros que no cuenten con la edad mínima exigida.

Asimismo, el conductor del vehículo será responsable por la no utilización de los sistemas de retención infantil, con la excepción prevista en el artículo 13.4 cuando se trate de conductores profesionales.

b) Cuando la autoría de los hechos cometidos corresponda a un menor de dieciocho años, responderán solidariamente con él de la multa impuesta sus padres, tutores, acogedores y guardadores legales o de hecho, por este orden, en razón al incumplimiento de la obligación impuesta a éstos que conlleva un deber de prevenir la infracción administrativa que se impute a los menores.

c) En los supuestos en que no tenga lugar la detención del vehículo y éste tuviese designado un conductor habitual, la responsabilidad recaerá en éste, salvo que acredite que era otro el conductor o la sustracción del vehículo.

d) En los supuestos en que no tenga lugar la detención del vehículo y éste no tuviese designado un conductor habitual, será responsable el conductor identificado por el titular o el arrendatario a largo plazo, de acuerdo con las obligaciones impuestas en el artículo 11.

e) En las empresas de arrendamiento de vehículos a corto plazo será responsable el arrendatario del vehículo. En caso de que éste manifestara no ser el conductor, o fuese persona jurídica, le corresponderán las obligaciones que para el titular establece el artículo 11. La misma responsabilidad corresponderá a los titulares de los talleres mecánicos o establecimientos de compraventa de vehículos por las infracciones cometidas con los vehículos mientras se encuentren allí depositados.

f) El titular, o el arrendatario a largo plazo, en el supuesto de que constase en el Registro de Vehículos del organismo autónomo Jefatura Central de Tráfico, será en todo caso responsable de las infracciones relativas a la documentación del vehículo, a los reconocimientos periódicos y a su estado de conservación, cuando las deficiencias afecten a las condiciones de seguridad del vehículo.

g) El titular o el arrendatario, en el supuesto de que constase en el Registro de Vehículos del organismo autónomo Jefatura Central de Tráfico, será responsable de las infracciones por estacionamiento o por impago de los peajes de las vías que lo tengan regulado, salvo en los supuestos en que el vehículo tuviese designado un conductor habitual o se indique un conductor responsable del hecho.

## Artículo 84. Competencia.

_Versión vigente desde 2016-01-31. Versiones en el BOE: 2016-01-31._

1. La competencia para sancionar las infracciones cometidas en vías interurbanas y travesías corresponde al Jefe de Tráfico de la provincia en que se haya cometido el hecho. Si se trata de infracciones cometidas en el territorio de más de una provincia, la competencia para su sanción corresponde, en su caso, al Jefe de Tráfico de la provincia en que la infracción hubiera sido primeramente denunciada.

2. Los Jefes Provinciales podrán delegar esta competencia en la medida y extensión que estimen conveniente. En particular podrán delegar en el Director del Centro de Tratamiento de Denuncias Automatizadas la de las infracciones que hayan sido detectadas a través de medios de captación y reproducción de imágenes que permitan la identificación del vehículo.

Los órganos de las diferentes Administraciones Públicas podrán delegar el ejercicio de sus competencias sancionadoras mediante convenios o encomiendas de gestión, o a través de cualesquiera otros instrumentos de colaboración previstos en la normativa de procedimiento administrativo común.

3. En las comunidades autónomas que hayan recibido el traspaso de funciones y servicios en materia de tráfico y circulación de vehículos a motor serán competentes para sancionar los órganos previstos en la normativa autonómica.

4. La sanción por infracción a normas de circulación cometidas en vías urbanas corresponderá a los respectivos Alcaldes, los cuales podrán delegar esta competencia de acuerdo con la normativa aplicable.

Quedan excluidas de la competencia sancionadora municipal las infracciones a los preceptos del título IV, incluyendo las relativas a las condiciones técnicas de los vehículos y al seguro obligatorio.

Los Jefes Provinciales de Tráfico y los órganos competentes que correspondan, en caso de comunidades autónomas que hayan recibido el traspaso de funciones y servicios en materia de tráfico y circulación de vehículos a motor, asumirán la competencia de los Alcaldes cuando, por razones justificadas o por insuficiencia de los servicios municipales, no pueda ser ejercida por éstos.

5. La competencia para sancionar las infracciones a que se refiere el artículo 52 corresponderá, en todo caso, al Director General de Tráfico o al órgano que tenga atribuida la competencia en las comunidades autónomas que hayan recibido el traspaso de funciones y servicios en materia de tráfico y circulación de vehículos a motor, limitada al ámbito territorial de la comunidad autónoma.

6. En las ciudades de Ceuta y Melilla las competencias que en los apartados anteriores se atribuyen a los Jefes Provinciales de Tráfico, corresponderán a los Jefes Locales de Tráfico.

## Artículo 85. Actuaciones administrativas y jurisdiccionales penales.

_Versión vigente desde 2022-09-15. Versiones en el BOE: 2016-01-31, 2022-09-15._

_Nota del BOE: Se modifica el apartado 1 por la disposición final 1 de la Ley Orgánica 11/2022, de 13 de septiembre. Ref. BOE-A-2022-14965#df_

1. Cuando en un procedimiento sancionador se ponga de manifiesto un hecho que ofrezca indicios de delito perseguible de oficio, la autoridad administrativa lo pondrá en conocimiento del Ministerio Fiscal, por si procede el ejercicio de la acción penal, y acordará la suspensión de las actuaciones.

En todo caso, cuando se produzca un accidente de tráfico con resultado de lesión o muerte, la autoridad administrativa lo pondrá en conocimiento de la autoridad judicial, acompañando la comunicación del oportuno atestado.

2. Concluido el proceso penal con sentencia condenatoria, se archivará el procedimiento sancionador sin declaración de responsabilidad.

3. Si la sentencia es absolutoria o el procedimiento penal finaliza con otra resolución que le ponga fin sin declaración de responsabilidad, y siempre que la misma no esté fundada en la inexistencia del hecho, se podrá iniciar o continuar el procedimiento sancionador contra quien no haya sido condenado en vía penal.

La resolución que se dicte deberá respetar, en todo caso, la declaración de hechos probados en dicho procedimiento penal.

## Artículo 86. Incoación.

_Versión vigente desde 2016-01-31. Versiones en el BOE: 2016-01-31._

1. El procedimiento sancionador se incoará de oficio por la autoridad competente que tenga noticia de los hechos que puedan constituir infracciones tipificadas en esta ley, por iniciativa propia o mediante denuncia de los agentes de la autoridad encargados de la vigilancia del tráfico en el ejercicio de las funciones que tienen encomendadas o de cualquier persona que tenga conocimiento de los hechos.

2. No obstante, la denuncia formulada por los agentes de la autoridad encargados de la vigilancia del tráfico en el ejercicio de las funciones que tienen encomendadas, y notificada en el acto al denunciado, constituye el acto de iniciación del procedimiento sancionador, a todos los efectos.

## Artículo 88. Valor probatorio de las denuncias de los agentes de la autoridad encargados de la vigilancia del tráfico, en el ejercicio de las funciones que tienen encomendadas.

_Versión vigente desde 2016-01-31. Versiones en el BOE: 2016-01-31._

Las denuncias formuladas por los agentes de la autoridad encargados de la vigilancia del tráfico en el ejercicio de las funciones que tienen encomendadas tendrán valor probatorio, salvo prueba en contrario, de los hechos denunciados, de la identidad de quienes los hubieran cometido y, en su caso, de la notificación de la denuncia, sin perjuicio del deber de aquéllos de aportar todos los elementos probatorios que sean posibles sobre el hecho denunciado.

## Artículo 89. Notificación de la denuncia.

_Versión vigente desde 2016-01-31. Versiones en el BOE: 2016-01-31._

1. Las denuncias se notificarán en el acto al denunciado.

2. No obstante, la notificación podrá efectuarse en un momento posterior siempre que se dé alguna de las siguientes circunstancias:

a) Que la denuncia se formule en circunstancias en que la detención del vehículo pueda originar un riesgo para la circulación. En este caso, el agente deberá indicar los motivos concretos que la impiden.

b) Que la denuncia se formule estando el vehículo estacionado, cuando el conductor no esté presente.

c) Que se haya tenido conocimiento de la infracción a través de medios de captación y reproducción de imágenes que permitan la identificación del vehículo.

d) Que el agente denunciante se encuentre realizando labores de vigilancia, control, regulación o disciplina del tráfico y carezca de medios para proceder al seguimiento del vehículo.

## Artículo 92. Tablón Edictal de Sanciones de Tráfico (TESTRA).

_Versión vigente desde 2016-01-31. Versiones en el BOE: 2016-01-31._

1. Con carácter previo y facultativo, las notificaciones a que se refiere el artículo anterior podrán practicarse también en el Tablón Edictal de Sanciones de Tráfico (TESTRA), que será gestionado por el organismo autónomo Jefatura Central de Tráfico.

2. El funcionamiento, la gestión y la publicación en el TESTRA se hará conforme a lo dispuesto en la normativa de protección de datos de carácter personal y en la de acceso electrónico de los ciudadanos a los servicios públicos.

## Artículo 96. Recursos en el procedimiento sancionador ordinario.

_Versión vigente desde 2016-01-31. Versiones en el BOE: 2016-01-31._

1. La resolución sancionadora pondrá fin a la vía administrativa y la sanción se podrá ejecutar desde el día siguiente a aquel en que se notifique al interesado, produciendo plenos efectos, o, en su caso, una vez haya transcurrido el plazo indicado en el artículo 95.4.

2. Contra las resoluciones sancionadoras, podrá interponerse recurso de reposición, con carácter potestativo, en el plazo de un mes contado desde el día siguiente al de su notificación.

El recurso se interpondrá ante el órgano que dictó la resolución sancionadora, que será el competente para resolverlo.

3. La interposición del recurso de reposición no suspenderá la ejecución del acto impugnado ni la de la sanción. En el caso de que el recurrente solicite la suspensión de la ejecución, ésta se entenderá denegada transcurrido el plazo de un mes desde la solicitud sin que se haya resuelto.

4. No se tendrán en cuenta en la resolución del recurso hechos, documentos y alegaciones del recurrente que pudieran haber sido aportados en el procedimiento originario.

5. El recurso de reposición regulado en este artículo se entenderá desestimado si no recae resolución expresa en el plazo de un mes, quedando expedita la vía contencioso-administrativa.

6. Contra las resoluciones sancionadoras dictadas por los órganos competentes de las comunidades autónomas que hayan recibido el traspaso de funciones y servicios en materia de tráfico y circulación de vehículos a motor, así como por los Alcaldes, en el caso de las entidades locales, se estará a lo establecido en los anteriores apartados respetando la competencia sancionadora prevista en su normativa específica.

## Artículo 108. Ejecución.

_Versión vigente desde 2016-01-31. Versiones en el BOE: 2016-01-31._

Una vez firme la sanción en vía administrativa, se procederá a su ejecución conforme a lo previsto en esta ley.

## Artículo 110. Cobro de multas.

_Versión vigente desde 2016-01-31. Versiones en el BOE: 2016-01-31._

1. Una vez firme la sanción, el interesado dispondrá de un plazo final de quince días naturales para el pago de la multa. Finalizado el plazo establecido sin que se haya pagado la multa, se iniciará el procedimiento de apremio.

2. Los órganos y procedimientos de la recaudación ejecutiva serán los establecidos en la normativa tributaria que le sea de aplicación, según las autoridades que las hayan impuesto.

## Artículo 112. Prescripción y caducidad.

_Versión vigente desde 2016-01-31. Versiones en el BOE: 2016-01-31._

1. El plazo de prescripción de las infracciones previstas en esta ley será de tres meses para las infracciones leves y de seis meses para las infracciones graves y muy graves.

El plazo de prescripción comenzará a contar a partir del mismo día en que los hechos se hubieran cometido.

2. La prescripción se interrumpe por cualquier actuación administrativa de la que tenga conocimiento el denunciado o esté encaminada a averiguar su identidad o domicilio y se practique con otras administraciones, instituciones u organismos. También se interrumpe por la notificación efectuada de acuerdo con los artículos 89, 90 y 91.

El plazo de prescripción se reanudará si el procedimiento se paraliza durante más de un mes por causa no imputable al denunciado.

3. Si no se hubiera producido la resolución sancionadora transcurrido un año desde la iniciación del procedimiento, se producirá su caducidad y se procederá al archivo de las actuaciones, a solicitud de cualquier interesado o de oficio por el órgano competente para dictar resolución.

Cuando la paralización del procedimiento se hubiera producido a causa del conocimiento de los hechos por la jurisdicción penal, el plazo de caducidad se suspenderá y, una vez haya adquirido firmeza la resolución judicial, se reanudará el cómputo del plazo de caducidad por el tiempo que restaba en el momento de acordar la suspensión.

4. El plazo de prescripción de las sanciones consistentes en multa será de cuatro años y el de la suspensión prevista en el artículo 80 será de un año, computados desde el día siguiente a aquel en que adquiera firmeza la sanción en vía administrativa.

El cómputo y la interrupción del plazo de prescripción del derecho de la Administración para exigir el pago de las sanciones en vía de apremio consistentes en multa se regirán por lo dispuesto en la normativa tributaria.
