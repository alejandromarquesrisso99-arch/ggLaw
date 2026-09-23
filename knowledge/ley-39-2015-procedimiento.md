---
norma: Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas
articulos: [14, 16, 21, 24, 25, 32, 35, 40, 41, 42, 44, 47, 48, 53, 64, 66, 68, 76, 77, 85, 89, 90, 95, 112, 115, 118, 121, 122, 123, 124]
fuente: https://www.boe.es/buscar/act.php?id=BOE-A-2015-10565
version_consolidada: 2024-11-06
consultado: 2026-09-23
estado: revisado
---

# Ley 39/2015 (LPACAP): procedimiento, notificaciones, procedimiento sancionador y recursos

## Nota sobre la fuente

- Transcripción literal de la versión vigente de cada artículo, obtenida de la API de datos
  abiertos del BOE (legislación consolidada), consultada el 2026-09-23. Bajo cada artículo se
  indican sus versiones y, si las hay, las notas del BOE sobre la norma que lo modificó. Las
  redacciones anteriores no se copian.
- `version_consolidada` es la fecha de actualización más reciente del índice del texto
  consolidado. La `fecha_actualizacion` de los metadatos es la del registro, no la del texto,
  y puede ser posterior.
- Los arts. 30, 31 y 43 y la DA 1.ª están en knowledge/ley-39-2015.md.

## Notas para ggLaw (no forman parte del texto legal)

En tráfico esta ley solo se aplica de forma supletoria (DA 1.ª.2.c; art. 83.1 RDL 6/2015).
Donde el RDL 6/2015 regula algo, prevalece. Varios artículos de aquí quedan desplazados y
alegarlos en una multa de tráfico sería un motivo que no procede:

- **Caducidad:** en tráfico es de un año desde la iniciación (art. 112.3 RDL 6/2015), no el
  plazo general de tres meses (arts. 21.3 y 25.1.b de esta ley).
- **Reducción por pago:** en tráfico es la del 50 % del art. 94 del RDL 6/2015, no las del
  art. 85 de esta ley.
- **Contenido de la denuncia y propuesta de resolución:** los regulan los arts. 87 y 95 del
  RDL 6/2015. TODO(juridico): confirmar si los requisitos de los arts. 64.2 y 89 de esta ley
  (p. ej. identidad del instructor, traslado de la propuesta) se exigen además en tráfico o si
  el RDL los desplaza, y cómo se aplica el art. 53.2.a) (derecho a conocer la identidad del
  instructor). Fuente: jurisprudencia sobre el art. 95 RDL 6/2015.
- **Notificaciones:** en tráfico la práctica de la notificación la regulan los arts. 89-92 del
  RDL 6/2015. Su art. 90.3 permite que la recoja cualquier persona que esté en el domicilio
  (el art. 42.2 exige mayor de catorce años) y repetir el intento dentro de los tres días
  siguientes, sin las reglas horarias del art. 42.2. La notificación infructuosa va al BOE
  (art. 91, veinte días naturales) y al TESTRA (art. 92), no por el art. 44. TODO(juridico):
  ¿se exigen en tráfico, de forma supletoria, las reglas horarias del segundo intento del art.
  42.2? Fuente: jurisprudencia del TS sobre notificaciones en tráfico.
- **Prueba y propuesta:** el art. 95.2-3 del RDL regula el informe del agente y el traslado de
  nuevas alegaciones; los arts. 77.2 y 90.2 de esta ley son, como mucho, supletorios.
- **Recursos:** la resolución sancionadora de tráfico pone fin a la vía administrativa (art.
  96.1 RDL 6/2015), así que no cabe recurso de alzada (arts. 121-122). El recurso de reposición
  es el del art. 96 del RDL (un mes, potestativo); los arts. 123-124 de esta ley son supletorios.

Para qué sirve cada bloque:

- Arts. 14 y 16: canal de presentación (electrónico o no), del que depende qué calendario de
  días inhábiles se usa (arts. 30.6 y 31.3; ver el TODO abierto sobre el alcance del art. 31.3
  en knowledge/ley-39-2015.md).
- Arts. 21, 24 y 25: obligación de resolver, silencio y caducidad (supletorios en tráfico).
- Art. 32: el apartado 5 (ampliación por ciberincidente) lo añadió el Real Decreto-ley 6/2022.
  core/plazos.py no modela ampliaciones de plazo: si la Administración acuerda una, el
  vencimiento calculado deja de valer.
- Art. 35: motivación, base de defectos de la resolución sancionadora.
- Arts. 40-42 y 44: requisitos y práctica de las notificaciones (defectos de notificación).
- Arts. 47 y 48: nulidad y anulabilidad, que fundamentan los recursos (art. 112.1). Por el
  art. 48.2, un defecto de forma solo anula si el acto carece de los requisitos formales
  indispensables para alcanzar su fin o causa indefensión: una regla de defecto formal debe
  comprobarlo para no alegar motivos que no proceden.
- Art. 53: derechos del interesado en el procedimiento.
- Arts. 64, 76, 77, 85, 89, 90 y 95: procedimiento sancionador general (supletorio). El art.
  77 tiene un apartado 3 bis añadido por la Ley 15/2022 (ver la nota del BOE bajo el artículo).
- Arts. 66 y 68: contenido mínimo de las solicitudes y subsanación (plantillas de la tarea 6).
- Arts. 112, 115, 118, 121-124: recursos.
- TODO(juridico): la Ley 40/2015 (principios de la potestad sancionadora, arts. 25-31,
  incluida la prescripción del art. 30) no está transcrita; hará falta para reglas que no
  regule el RDL 6/2015.

## Artículo 14. Derecho y obligación de relacionarse electrónicamente con las Administraciones Públicas.

_Versión vigente desde 2016-10-02. Versiones en el BOE: 2016-10-02._

1. Las personas físicas podrán elegir en todo momento si se comunican con las Administraciones Públicas para el ejercicio de sus derechos y obligaciones a través de medios electrónicos o no, salvo que estén obligadas a relacionarse a través de medios electrónicos con las Administraciones Públicas. El medio elegido por la persona para comunicarse con las Administraciones Públicas podrá ser modificado por aquella en cualquier momento.

2. En todo caso, estarán obligados a relacionarse a través de medios electrónicos con las Administraciones Públicas para la realización de cualquier trámite de un procedimiento administrativo, al menos, los siguientes sujetos:

a) Las personas jurídicas.

b) Las entidades sin personalidad jurídica.

c) Quienes ejerzan una actividad profesional para la que se requiera colegiación obligatoria, para los trámites y actuaciones que realicen con las Administraciones Públicas en ejercicio de dicha actividad profesional. En todo caso, dentro de este colectivo se entenderán incluidos los notarios y registradores de la propiedad y mercantiles.

d) Quienes representen a un interesado que esté obligado a relacionarse electrónicamente con la Administración.

e) Los empleados de las Administraciones Públicas para los trámites y actuaciones que realicen con ellas por razón de su condición de empleado público, en la forma en que se determine reglamentariamente por cada Administración.

3. Reglamentariamente, las Administraciones podrán establecer la obligación de relacionarse con ellas a través de medios electrónicos para determinados procedimientos y para ciertos colectivos de personas físicas que por razón de su capacidad económica, técnica, dedicación profesional u otros motivos quede acreditado que tienen acceso y disponibilidad de los medios electrónicos necesarios.

## Artículo 16. Registros.

_Versión vigente desde 2016-10-02. Versiones en el BOE: 2016-10-02._

1. Cada Administración dispondrá de un Registro Electrónico General, en el que se hará el correspondiente asiento de todo documento que sea presentado o que se reciba en cualquier órgano administrativo, Organismo público o Entidad vinculado o dependiente a éstos. También se podrán anotar en el mismo, la salida de los documentos oficiales dirigidos a otros órganos o particulares.

Los Organismos públicos vinculados o dependientes de cada Administración podrán disponer de su propio registro electrónico plenamente interoperable e interconectado con el Registro Electrónico General de la Administración de la que depende.

El Registro Electrónico General de cada Administración funcionará como un portal que facilitará el acceso a los registros electrónicos de cada Organismo. Tanto el Registro Electrónico General de cada Administración como los registros electrónicos de cada Organismo cumplirán con las garantías y medidas de seguridad previstas en la legislación en materia de protección de datos de carácter personal.

Las disposiciones de creación de los registros electrónicos se publicarán en el diario oficial correspondiente y su texto íntegro deberá estar disponible para consulta en la sede electrónica de acceso al registro. En todo caso, las disposiciones de creación de registros electrónicos especificarán el órgano o unidad responsable de su gestión, así como la fecha y hora oficial y los días declarados como inhábiles.

En la sede electrónica de acceso a cada registro figurará la relación actualizada de trámites que pueden iniciarse en el mismo.

2. Los asientos se anotarán respetando el orden temporal de recepción o salida de los documentos, e indicarán la fecha del día en que se produzcan. Concluido el trámite de registro, los documentos serán cursados sin dilación a sus destinatarios y a las unidades administrativas correspondientes desde el registro en que hubieran sido recibidas.

3. El registro electrónico de cada Administración u Organismo garantizará la constancia, en cada asiento que se practique, de un número, epígrafe expresivo de su naturaleza, fecha y hora de su presentación, identificación del interesado, órgano administrativo remitente, si procede, y persona u órgano administrativo al que se envía, y, en su caso, referencia al contenido del documento que se registra. Para ello, se emitirá automáticamente un recibo consistente en una copia autenticada del documento de que se trate, incluyendo la fecha y hora de presentación y el número de entrada de registro, así como un recibo acreditativo de otros documentos que, en su caso, lo acompañen, que garantice la integridad y el no repudio de los mismos.

4. Los documentos que los interesados dirijan a los órganos de las Administraciones Públicas podrán presentarse:

a) En el registro electrónico de la Administración u Organismo al que se dirijan, así como en los restantes registros electrónicos de cualquiera de los sujetos a los que se refiere el artículo 2.1.

b) En las oficinas de Correos, en la forma que reglamentariamente se establezca.

c) En las representaciones diplomáticas u oficinas consulares de España en el extranjero.

d) En las oficinas de asistencia en materia de registros.

e) En cualquier otro que establezcan las disposiciones vigentes.

Los registros electrónicos de todas y cada una de las Administraciones, deberán ser plenamente interoperables, de modo que se garantice su compatibilidad informática e interconexión, así como la transmisión telemática de los asientos registrales y de los documentos que se presenten en cualquiera de los registros.

5. Los documentos presentados de manera presencial ante las Administraciones Públicas, deberán ser digitalizados, de acuerdo con lo previsto en el artículo 27 y demás normativa aplicable, por la oficina de asistencia en materia de registros en la que hayan sido presentados para su incorporación al expediente administrativo electrónico, devolviéndose los originales al interesado, sin perjuicio de aquellos supuestos en que la norma determine la custodia por la Administración de los documentos presentados o resulte obligatoria la presentación de objetos o de documentos en un soporte específico no susceptibles de digitalización.

Reglamentariamente, las Administraciones podrán establecer la obligación de presentar determinados documentos por medios electrónicos para ciertos procedimientos y colectivos de personas físicas que, por razón de su capacidad económica, técnica, dedicación profesional u otros motivos quede acreditado que tienen acceso y disponibilidad de los medios electrónicos necesarios.

6. Podrán hacerse efectivos mediante transferencia dirigida a la oficina pública correspondiente cualesquiera cantidades que haya que satisfacer en el momento de la presentación de documentos a las Administraciones Públicas, sin perjuicio de la posibilidad de su abono por otros medios.

7. Las Administraciones Públicas deberán hacer pública y mantener actualizada una relación de las oficinas en las que se prestará asistencia para la presentación electrónica de documentos.

8. No se tendrán por presentados en el registro aquellos documentos e información cuyo régimen especial establezca otra forma de presentación.

## Artículo 21. Obligación de resolver.

_Versión vigente desde 2016-10-02. Versiones en el BOE: 2016-10-02._

1. La Administración está obligada a dictar resolución expresa y a notificarla en todos los procedimientos cualquiera que sea su forma de iniciación.

En los casos de prescripción, renuncia del derecho, caducidad del procedimiento o desistimiento de la solicitud, así como de desaparición sobrevenida del objeto del procedimiento, la resolución consistirá en la declaración de la circunstancia que concurra en cada caso, con indicación de los hechos producidos y las normas aplicables.

Se exceptúan de la obligación a que se refiere el párrafo primero, los supuestos de terminación del procedimiento por pacto o convenio, así como los procedimientos relativos al ejercicio de derechos sometidos únicamente al deber de declaración responsable o comunicación a la Administración.

2. El plazo máximo en el que debe notificarse la resolución expresa será el fijado por la norma reguladora del correspondiente procedimiento.

Este plazo no podrá exceder de seis meses salvo que una norma con rango de Ley establezca uno mayor o así venga previsto en el Derecho de la Unión Europea.

3. Cuando las normas reguladoras de los procedimientos no fijen el plazo máximo, éste será de tres meses. Este plazo y los previstos en el apartado anterior se contarán:

a) En los procedimientos iniciados de oficio, desde la fecha del acuerdo de iniciación.

b) En los iniciados a solicitud del interesado, desde la fecha en que la solicitud haya tenido entrada en el registro electrónico de la Administración u Organismo competente para su tramitación.

4. Las Administraciones Públicas deben publicar y mantener actualizadas en el portal web, a efectos informativos, las relaciones de procedimientos de su competencia, con indicación de los plazos máximos de duración de los mismos, así como de los efectos que produzca el silencio administrativo.

En todo caso, las Administraciones Públicas informarán a los interesados del plazo máximo establecido para la resolución de los procedimientos y para la notificación de los actos que les pongan término, así como de los efectos que pueda producir el silencio administrativo. Dicha mención se incluirá en la notificación o publicación del acuerdo de iniciación de oficio, o en la comunicación que se dirigirá al efecto al interesado dentro de los diez días siguientes a la recepción de la solicitud iniciadora del procedimiento en el registro electrónico de la Administración u Organismo competente para su tramitación. En este último caso, la comunicación indicará además la fecha en que la solicitud ha sido recibida por el órgano competente.

5. Cuando el número de las solicitudes formuladas o las personas afectadas pudieran suponer un incumplimiento del plazo máximo de resolución, el órgano competente para resolver, a propuesta razonada del órgano instructor, o el superior jerárquico del órgano competente para resolver, a propuesta de éste, podrán habilitar los medios personales y materiales para cumplir con el despacho adecuado y en plazo.

6. El personal al servicio de las Administraciones Públicas que tenga a su cargo el despacho de los asuntos, así como los titulares de los órganos administrativos competentes para instruir y resolver son directamente responsables, en el ámbito de sus competencias, del cumplimiento de la obligación legal de dictar resolución expresa en plazo.

El incumplimiento de dicha obligación dará lugar a la exigencia de responsabilidad disciplinaria, sin perjuicio de la que hubiere lugar de acuerdo con la normativa aplicable.

## Artículo 24. Silencio administrativo en procedimientos iniciados a solicitud del interesado.

_Versión vigente desde 2016-10-02. Versiones en el BOE: 2016-10-02._

1. En los procedimientos iniciados a solicitud del interesado, sin perjuicio de la resolución que la Administración debe dictar en la forma prevista en el apartado 3 de este artículo, el vencimiento del plazo máximo sin haberse notificado resolución expresa, legitima al interesado o interesados para entenderla estimada por silencio administrativo, excepto en los supuestos en los que una norma con rango de ley o una norma de Derecho de la Unión Europea o de Derecho internacional aplicable en España establezcan lo contrario. Cuando el procedimiento tenga por objeto el acceso a actividades o su ejercicio, la ley que disponga el carácter desestimatorio del silencio deberá fundarse en la concurrencia de razones imperiosas de interés general.

El silencio tendrá efecto desestimatorio en los procedimientos relativos al ejercicio del derecho de petición, a que se refiere el artículo 29 de la Constitución, aquellos cuya estimación tuviera como consecuencia que se transfirieran al solicitante o a terceros facultades relativas al dominio público o al servicio público, impliquen el ejercicio de actividades que puedan dañar el medio ambiente y en los procedimientos de responsabilidad patrimonial de las Administraciones Públicas.

El sentido del silencio también será desestimatorio en los procedimientos de impugnación de actos y disposiciones y en los de revisión de oficio iniciados a solicitud de los interesados. No obstante, cuando el recurso de alzada se haya interpuesto contra la desestimación por silencio administrativo de una solicitud por el transcurso del plazo, se entenderá estimado el mismo si, llegado el plazo de resolución, el órgano administrativo competente no dictase y notificase resolución expresa, siempre que no se refiera a las materias enumeradas en el párrafo anterior de este apartado.

2. La estimación por silencio administrativo tiene a todos los efectos la consideración de acto administrativo finalizador del procedimiento. La desestimación por silencio administrativo tiene los solos efectos de permitir a los interesados la interposición del recurso administrativo o contencioso-administrativo que resulte procedente.

3. La obligación de dictar resolución expresa a que se refiere el apartado primero del artículo 21 se sujetará al siguiente régimen:

a) En los casos de estimación por silencio administrativo, la resolución expresa posterior a la producción del acto sólo podrá dictarse de ser confirmatoria del mismo.

b) En los casos de desestimación por silencio administrativo, la resolución expresa posterior al vencimiento del plazo se adoptará por la Administración sin vinculación alguna al sentido del silencio.

4. Los actos administrativos producidos por silencio administrativo se podrán hacer valer tanto ante la Administración como ante cualquier persona física o jurídica, pública o privada. Los mismos producen efectos desde el vencimiento del plazo máximo en el que debe dictarse y notificarse la resolución expresa sin que la misma se haya expedido, y su existencia puede ser acreditada por cualquier medio de prueba admitido en Derecho, incluido el certificado acreditativo del silencio producido. Este certificado se expedirá de oficio por el órgano competente para resolver en el plazo de quince días desde que expire el plazo máximo para resolver el procedimiento. Sin perjuicio de lo anterior, el interesado podrá pedirlo en cualquier momento, computándose el plazo indicado anteriormente desde el día siguiente a aquél en que la petición tuviese entrada en el registro electrónico de la Administración u Organismo competente para resolver.

## Artículo 25. Falta de resolución expresa en procedimientos iniciados de oficio.

_Versión vigente desde 2016-10-02. Versiones en el BOE: 2016-10-02._

1. En los procedimientos iniciados de oficio, el vencimiento del plazo máximo establecido sin que se haya dictado y notificado resolución expresa no exime a la Administración del cumplimiento de la obligación legal de resolver, produciendo los siguientes efectos:

a) En el caso de procedimientos de los que pudiera derivarse el reconocimiento o, en su caso, la constitución de derechos u otras situaciones jurídicas favorables, los interesados que hubieren comparecido podrán entender desestimadas sus pretensiones por silencio administrativo.

b) En los procedimientos en que la Administración ejercite potestades sancionadoras o, en general, de intervención, susceptibles de producir efectos desfavorables o de gravamen, se producirá la caducidad. En estos casos, la resolución que declare la caducidad ordenará el archivo de las actuaciones, con los efectos previstos en el artículo 95.

2. En los supuestos en los que el procedimiento se hubiera paralizado por causa imputable al interesado, se interrumpirá el cómputo del plazo para resolver y notificar la resolución.

## Artículo 32. Ampliación.

_Versión vigente desde 2022-03-31. Versiones en el BOE: 2016-10-02, 2022-03-31._

_Nota del BOE: Se añade el apartado 5 por la disposición final 21 del Real Decreto-ley 6/2022, de 29 de marzo. Ref. BOE-A-2022-4972#df-21_

1. La Administración, salvo precepto en contrario, podrá conceder de oficio o a petición de los interesados, una ampliación de los plazos establecidos, que no exceda de la mitad de los mismos, si las circunstancias lo aconsejan y con ello no se perjudican derechos de tercero. El acuerdo de ampliación deberá ser notificado a los interesados.

2. La ampliación de los plazos por el tiempo máximo permitido se aplicará en todo caso a los procedimientos tramitados por las misiones diplomáticas y oficinas consulares, así como a aquellos que, sustanciándose en el interior, exijan cumplimentar algún trámite en el extranjero o en los que intervengan interesados residentes fuera de España.

3. Tanto la petición de los interesados como la decisión sobre la ampliación deberán producirse, en todo caso, antes del vencimiento del plazo de que se trate. En ningún caso podrá ser objeto de ampliación un plazo ya vencido. Los acuerdos sobre ampliación de plazos o sobre su denegación no serán susceptibles de recurso, sin perjuicio del procedente contra la resolución que ponga fin al procedimiento.

4. Cuando una incidencia técnica haya imposibilitado el funcionamiento ordinario del sistema o aplicación que corresponda, y hasta que se solucione el problema, la Administración podrá determinar una ampliación de los plazos no vencidos, debiendo publicar en la sede electrónica tanto la incidencia técnica acontecida como la ampliación concreta del plazo no vencido.

5. Cuando como consecuencia de un ciberincidente se hayan visto gravemente afectados los servicios y sistemas utilizados para la tramitación de los procedimientos y el ejercicio de los derechos de los interesados que prevé la normativa vigente, la Administración podrá acordar la ampliación general de plazos de los procedimientos administrativos.

## Artículo 35. Motivación.

_Versión vigente desde 2016-10-02. Versiones en el BOE: 2016-10-02._

1. Serán motivados, con sucinta referencia de hechos y fundamentos de derecho:

a) Los actos que limiten derechos subjetivos o intereses legítimos.

b) Los actos que resuelvan procedimientos de revisión de oficio de disposiciones o actos administrativos, recursos administrativos y procedimientos de arbitraje y los que declaren su inadmisión.

c) Los actos que se separen del criterio seguido en actuaciones precedentes o del dictamen de órganos consultivos.

d) Los acuerdos de suspensión de actos, cualquiera que sea el motivo de ésta, así como la adopción de medidas provisionales previstas en el artículo 56.

e) Los acuerdos de aplicación de la tramitación de urgencia, de ampliación de plazos y de realización de actuaciones complementarias.

f) Los actos que rechacen pruebas propuestas por los interesados.

g) Los actos que acuerden la terminación del procedimiento por la imposibilidad material de continuarlo por causas sobrevenidas, así como los que acuerden el desistimiento por la Administración en procedimientos iniciados de oficio.

h) Las propuestas de resolución en los procedimientos de carácter sancionador, así como los actos que resuelvan procedimientos de carácter sancionador o de responsabilidad patrimonial.

i) Los actos que se dicten en el ejercicio de potestades discrecionales, así como los que deban serlo en virtud de disposición legal o reglamentaria expresa.

2. La motivación de los actos que pongan fin a los procedimientos selectivos y de concurrencia competitiva se realizará de conformidad con lo que dispongan las normas que regulen sus convocatorias, debiendo, en todo caso, quedar acreditados en el procedimiento los fundamentos de la resolución que se adopte.

## Artículo 40. Notificación.

_Versión vigente desde 2016-10-02. Versiones en el BOE: 2016-10-02._

1. El órgano que dicte las resoluciones y actos administrativos los notificará a los interesados cuyos derechos e intereses sean afectados por aquéllos, en los términos previstos en los artículos siguientes.

2. Toda notificación deberá ser cursada dentro del plazo de diez días a partir de la fecha en que el acto haya sido dictado, y deberá contener el texto íntegro de la resolución, con indicación de si pone fin o no a la vía administrativa, la expresión de los recursos que procedan, en su caso, en vía administrativa y judicial, el órgano ante el que hubieran de presentarse y el plazo para interponerlos, sin perjuicio de que los interesados puedan ejercitar, en su caso, cualquier otro que estimen procedente.

3. Las notificaciones que, conteniendo el texto íntegro del acto, omitiesen alguno de los demás requisitos previstos en el apartado anterior, surtirán efecto a partir de la fecha en que el interesado realice actuaciones que supongan el conocimiento del contenido y alcance de la resolución o acto objeto de la notificación, o interponga cualquier recurso que proceda.

4. Sin perjuicio de lo establecido en el apartado anterior, y a los solos efectos de entender cumplida la obligación de notificar dentro del plazo máximo de duración de los procedimientos, será suficiente la notificación que contenga, cuando menos, el texto íntegro de la resolución, así como el intento de notificación debidamente acreditado.

5. Las Administraciones Públicas podrán adoptar las medidas que consideren necesarias para la protección de los datos personales que consten en las resoluciones y actos administrativos, cuando éstos tengan por destinatarios a más de un interesado.

## Artículo 41. Condiciones generales para la práctica de las notificaciones.

_Versión vigente desde 2016-10-02. Versiones en el BOE: 2016-10-02._

1. Las notificaciones se practicarán preferentemente por medios electrónicos y, en todo caso, cuando el interesado resulte obligado a recibirlas por esta vía.

No obstante lo anterior, las Administraciones podrán practicar las notificaciones por medios no electrónicos en los siguientes supuestos:

a) Cuando la notificación se realice con ocasión de la comparecencia espontánea del interesado o su representante en las oficinas de asistencia en materia de registro y solicite la comunicación o notificación personal en ese momento.

b) Cuando para asegurar la eficacia de la actuación administrativa resulte necesario practicar la notificación por entrega directa de un empleado público de la Administración notificante.

Con independencia del medio utilizado, las notificaciones serán válidas siempre que permitan tener constancia de su envío o puesta a disposición, de la recepción o acceso por el interesado o su representante, de sus fechas y horas, del contenido íntegro, y de la identidad fidedigna del remitente y destinatario de la misma. La acreditación de la notificación efectuada se incorporará al expediente.

Los interesados que no estén obligados a recibir notificaciones electrónicas, podrán decidir y comunicar en cualquier momento a la Administración Pública, mediante los modelos normalizados que se establezcan al efecto, que las notificaciones sucesivas se practiquen o dejen de practicarse por medios electrónicos.

Reglamentariamente, las Administraciones podrán establecer la obligación de practicar electrónicamente las notificaciones para determinados procedimientos y para ciertos colectivos de personas físicas que por razón de su capacidad económica, técnica, dedicación profesional u otros motivos quede acreditado que tienen acceso y disponibilidad de los medios electrónicos necesarios.

Adicionalmente, el interesado podrá identificar un dispositivo electrónico y/o una dirección de correo electrónico que servirán para el envío de los avisos regulados en este artículo, pero no para la práctica de notificaciones.

2. En ningún caso se efectuarán por medios electrónicos las siguientes notificaciones:

a) Aquellas en las que el acto a notificar vaya acompañado de elementos que no sean susceptibles de conversión en formato electrónico.

b) Las que contengan medios de pago a favor de los obligados, tales como cheques.

3. En los procedimientos iniciados a solicitud del interesado, la notificación se practicará por el medio señalado al efecto por aquel. Esta notificación será electrónica en los casos en los que exista obligación de relacionarse de esta forma con la Administración.

Cuando no fuera posible realizar la notificación de acuerdo con lo señalado en la solicitud, se practicará en cualquier lugar adecuado a tal fin, y por cualquier medio que permita tener constancia de la recepción por el interesado o su representante, así como de la fecha, la identidad y el contenido del acto notificado.

4. En los procedimientos iniciados de oficio, a los solos efectos de su iniciación, las Administraciones Públicas podrán recabar, mediante consulta a las bases de datos del Instituto Nacional de Estadística, los datos sobre el domicilio del interesado recogidos en el Padrón Municipal, remitidos por las Entidades Locales en aplicación de lo previsto en la Ley 7/1985, de 2 de abril, reguladora de las Bases del Régimen Local.

5. Cuando el interesado o su representante rechace la notificación de una actuación administrativa, se hará constar en el expediente, especificándose las circunstancias del intento de notificación y el medio, dando por efectuado el trámite y siguiéndose el procedimiento.

6. Con independencia de que la notificación se realice en papel o por medios electrónicos, las Administraciones Públicas enviarán un aviso al dispositivo electrónico y/o a la dirección de correo electrónico del interesado que éste haya comunicado, informándole de la puesta a disposición de una notificación en la sede electrónica de la Administración u Organismo correspondiente o en la dirección electrónica habilitada única. La falta de práctica de este aviso no impedirá que la notificación sea considerada plenamente válida.

7. Cuando el interesado fuera notificado por distintos cauces, se tomará como fecha de notificación la de aquélla que se hubiera producido en primer lugar.

## Artículo 42. Práctica de las notificaciones en papel.

_Versión vigente desde 2016-10-02. Versiones en el BOE: 2016-10-02._

1. Todas las notificaciones que se practiquen en papel deberán ser puestas a disposición del interesado en la sede electrónica de la Administración u Organismo actuante para que pueda acceder al contenido de las mismas de forma voluntaria.

2. Cuando la notificación se practique en el domicilio del interesado, de no hallarse presente éste en el momento de entregarse la notificación, podrá hacerse cargo de la misma cualquier persona mayor de catorce años que se encuentre en el domicilio y haga constar su identidad. Si nadie se hiciera cargo de la notificación, se hará constar esta circunstancia en el expediente, junto con el día y la hora en que se intentó la notificación, intento que se repetirá por una sola vez y en una hora distinta dentro de los tres días siguientes. En caso de que el primer intento de notificación se haya realizado antes de las quince horas, el segundo intento deberá realizarse después de las quince horas y viceversa, dejando en todo caso al menos un margen de diferencia de tres horas entre ambos intentos de notificación. Si el segundo intento también resultara infructuoso, se procederá en la forma prevista en el artículo 44.

3. Cuando el interesado accediera al contenido de la notificación en sede electrónica, se le ofrecerá la posibilidad de que el resto de notificaciones se puedan realizar a través de medios electrónicos.

## Artículo 44. Notificación infructuosa.

_Versión vigente desde 2016-10-02. Versiones en el BOE: 2016-10-02._

Cuando los interesados en un procedimiento sean desconocidos, se ignore el lugar de la notificación o bien, intentada ésta, no se hubiese podido practicar, la notificación se hará por medio de un anuncio publicado en el «Boletín Oficial del Estado».

Asimismo, previamente y con carácter facultativo, las Administraciones podrán publicar un anuncio en el boletín oficial de la Comunidad Autónoma o de la Provincia, en el tablón de edictos del Ayuntamiento del último domicilio del interesado o del Consulado o Sección Consular de la Embajada correspondiente.

Las Administraciones Públicas podrán establecer otras formas de notificación complementarias a través de los restantes medios de difusión, que no excluirán la obligación de publicar el correspondiente anuncio en el «Boletín Oficial del Estado».

## Artículo 47. Nulidad de pleno derecho.

_Versión vigente desde 2016-10-02. Versiones en el BOE: 2016-10-02._

1. Los actos de las Administraciones Públicas son nulos de pleno derecho en los casos siguientes:

a) Los que lesionen los derechos y libertades susceptibles de amparo constitucional.

b) Los dictados por órgano manifiestamente incompetente por razón de la materia o del territorio.

c) Los que tengan un contenido imposible.

d) Los que sean constitutivos de infracción penal o se dicten como consecuencia de ésta.

e) Los dictados prescindiendo total y absolutamente del procedimiento legalmente establecido o de las normas que contienen las reglas esenciales para la formación de la voluntad de los órganos colegiados.

f) Los actos expresos o presuntos contrarios al ordenamiento jurídico por los que se adquieren facultades o derechos cuando se carezca de los requisitos esenciales para su adquisición.

g) Cualquier otro que se establezca expresamente en una disposición con rango de Ley.

2. También serán nulas de pleno derecho las disposiciones administrativas que vulneren la Constitución, las leyes u otras disposiciones administrativas de rango superior, las que regulen materias reservadas a la Ley, y las que establezcan la retroactividad de disposiciones sancionadoras no favorables o restrictivas de derechos individuales.

## Artículo 48. Anulabilidad.

_Versión vigente desde 2016-10-02. Versiones en el BOE: 2016-10-02._

1. Son anulables los actos de la Administración que incurran en cualquier infracción del ordenamiento jurídico, incluso la desviación de poder.

2. No obstante, el defecto de forma sólo determinará la anulabilidad cuando el acto carezca de los requisitos formales indispensables para alcanzar su fin o dé lugar a la indefensión de los interesados.

3. La realización de actuaciones administrativas fuera del tiempo establecido para ellas sólo implicará la anulabilidad del acto cuando así lo imponga la naturaleza del término o plazo.

## Artículo 53. Derechos del interesado en el procedimiento administrativo.

_Versión vigente desde 2016-10-02. Versiones en el BOE: 2016-10-02._

1. Además del resto de derechos previstos en esta Ley, los interesados en un procedimiento administrativo, tienen los siguientes derechos:

a) A conocer, en cualquier momento, el estado de la tramitación de los procedimientos en los que tengan la condición de interesados; el sentido del silencio administrativo que corresponda, en caso de que la Administración no dicte ni notifique resolución expresa en plazo; el órgano competente para su instrucción, en su caso, y resolución; y los actos de trámite dictados. Asimismo, también tendrán derecho a acceder y a obtener copia de los documentos contenidos en los citados procedimientos.

Quienes se relacionen con las Administraciones Públicas a través de medios electrónicos, tendrán derecho a consultar la información a la que se refiere el párrafo anterior, en el Punto de Acceso General electrónico de la Administración que funcionará como un portal de acceso. Se entenderá cumplida la obligación de la Administración de facilitar copias de los documentos contenidos en los procedimientos mediante la puesta a disposición de las mismas en el Punto de Acceso General electrónico de la Administración competente o en las sedes electrónicas que correspondan.

b) A identificar a las autoridades y al personal al servicio de las Administraciones Públicas bajo cuya responsabilidad se tramiten los procedimientos.

c) A no presentar documentos originales salvo que, de manera excepcional, la normativa reguladora aplicable establezca lo contrario. En caso de que, excepcionalmente, deban presentar un documento original, tendrán derecho a obtener una copia autenticada de éste.

d) A no presentar datos y documentos no exigidos por las normas aplicables al procedimiento de que se trate, que ya se encuentren en poder de las Administraciones Públicas o que hayan sido elaborados por éstas.

e) A formular alegaciones, utilizar los medios de defensa admitidos por el Ordenamiento Jurídico, y a aportar documentos en cualquier fase del procedimiento anterior al trámite de audiencia, que deberán ser tenidos en cuenta por el órgano competente al redactar la propuesta de resolución.

f) A obtener información y orientación acerca de los requisitos jurídicos o técnicos que las disposiciones vigentes impongan a los proyectos, actuaciones o solicitudes que se propongan realizar.

g) A actuar asistidos de asesor cuando lo consideren conveniente en defensa de sus intereses.

h) A cumplir las obligaciones de pago a través de los medios electrónicos previstos en el artículo 98.2.

i) Cualesquiera otros que les reconozcan la Constitución y las leyes.

2. Además de los derechos previstos en el apartado anterior, en el caso de procedimientos administrativos de naturaleza sancionadora, los presuntos responsables tendrán los siguientes derechos:

a) A ser notificado de los hechos que se le imputen, de las infracciones que tales hechos puedan constituir y de las sanciones que, en su caso, se les pudieran imponer, así como de la identidad del instructor, de la autoridad competente para imponer la sanción y de la norma que atribuya tal competencia.

b) A la presunción de no existencia de responsabilidad administrativa mientras no se demuestre lo contrario.

## Artículo 64. Acuerdo de iniciación en los procedimientos de naturaleza sancionadora.

_Versión vigente desde 2016-10-02. Versiones en el BOE: 2016-10-02._

1. El acuerdo de iniciación se comunicará al instructor del procedimiento, con traslado de cuantas actuaciones existan al respecto, y se notificará a los interesados, entendiendo en todo caso por tal al inculpado.

Asimismo, la incoación se comunicará al denunciante cuando las normas reguladoras del procedimiento así lo prevean.

2. El acuerdo de iniciación deberá contener al menos:

a) Identificación de la persona o personas presuntamente responsables.

b) Los hechos que motivan la incoación del procedimiento, su posible calificación y las sanciones que pudieran corresponder, sin perjuicio de lo que resulte de la instrucción.

c) Identificación del instructor y, en su caso, Secretario del procedimiento, con expresa indicación del régimen de recusación de los mismos.

d) Órgano competente para la resolución del procedimiento y norma que le atribuya tal competencia, indicando la posibilidad de que el presunto responsable pueda reconocer voluntariamente su responsabilidad, con los efectos previstos en el artículo 85.

e) Medidas de carácter provisional que se hayan acordado por el órgano competente para iniciar el procedimiento sancionador, sin perjuicio de las que se puedan adoptar durante el mismo de conformidad con el artículo 56.

f) Indicación del derecho a formular alegaciones y a la audiencia en el procedimiento y de los plazos para su ejercicio, así como indicación de que, en caso de no efectuar alegaciones en el plazo previsto sobre el contenido del acuerdo de iniciación, éste podrá ser considerado propuesta de resolución cuando contenga un pronunciamiento preciso acerca de la responsabilidad imputada.

3. Excepcionalmente, cuando en el momento de dictar el acuerdo de iniciación no existan elementos suficientes para la calificación inicial de los hechos que motivan la incoación del procedimiento, la citada calificación podrá realizarse en una fase posterior mediante la elaboración de un Pliego de cargos, que deberá ser notificado a los interesados.

## Artículo 66. Solicitudes de iniciación.

_Versión vigente desde 2016-10-02. Versiones en el BOE: 2016-10-02._

1. Las solicitudes que se formulen deberán contener:

a) Nombre y apellidos del interesado y, en su caso, de la persona que lo represente.

b) Identificación del medio electrónico, o en su defecto, lugar físico en que desea que se practique la notificación. Adicionalmente, los interesados podrán aportar su dirección de correo electrónico y/o dispositivo electrónico con el fin de que las Administraciones Públicas les avisen del envío o puesta a disposición de la notificación.

c) Hechos, razones y petición en que se concrete, con toda claridad, la solicitud.

d) Lugar y fecha.

e) Firma del solicitante o acreditación de la autenticidad de su voluntad expresada por cualquier medio.

f) Órgano, centro o unidad administrativa a la que se dirige y su correspondiente código de identificación.

Las oficinas de asistencia en materia de registros estarán obligadas a facilitar a los interesados el código de identificación si el interesado lo desconoce. Asimismo, las Administraciones Públicas deberán mantener y actualizar en la sede electrónica correspondiente un listado con los códigos de identificación vigentes.

2. Cuando las pretensiones correspondientes a una pluralidad de personas tengan un contenido y fundamento idéntico o sustancialmente similar, podrán ser formuladas en una única solicitud, salvo que las normas reguladoras de los procedimientos específicos dispongan otra cosa.

3. De las solicitudes, comunicaciones y escritos que presenten los interesados electrónicamente o en las oficinas de asistencia en materia de registros de la Administración, podrán éstos exigir el correspondiente recibo que acredite la fecha y hora de presentación.

4. Las Administraciones Públicas deberán establecer modelos y sistemas de presentación masiva que permitan a los interesados presentar simultáneamente varias solicitudes. Estos modelos, de uso voluntario, estarán a disposición de los interesados en las correspondientes sedes electrónicas y en las oficinas de asistencia en materia de registros de las Administraciones Públicas.

Los solicitantes podrán acompañar los elementos que estimen convenientes para precisar o completar los datos del modelo, los cuales deberán ser admitidos y tenidos en cuenta por el órgano al que se dirijan.

5. Los sistemas normalizados de solicitud podrán incluir comprobaciones automáticas de la información aportada respecto de datos almacenados en sistemas propios o pertenecientes a otras Administraciones u ofrecer el formulario cumplimentado, en todo o en parte, con objeto de que el interesado verifique la información y, en su caso, la modifique y complete.

6. Cuando la Administración en un procedimiento concreto establezca expresamente modelos específicos de presentación de solicitudes, éstos serán de uso obligatorio por los interesados.

## Artículo 68. Subsanación y mejora de la solicitud.

_Versión vigente desde 2016-10-02. Versiones en el BOE: 2016-10-02._

1. Si la solicitud de iniciación no reúne los requisitos que señala el artículo 66, y, en su caso, los que señala el artículo 67 u otros exigidos por la legislación específica aplicable, se requerirá al interesado para que, en un plazo de diez días, subsane la falta o acompañe los documentos preceptivos, con indicación de que, si así no lo hiciera, se le tendrá por desistido de su petición, previa resolución que deberá ser dictada en los términos previstos en el artículo 21.

2. Siempre que no se trate de procedimientos selectivos o de concurrencia competitiva, este plazo podrá ser ampliado prudencialmente, hasta cinco días, a petición del interesado o a iniciativa del órgano, cuando la aportación de los documentos requeridos presente dificultades especiales.

3. En los procedimientos iniciados a solicitud de los interesados, el órgano competente podrá recabar del solicitante la modificación o mejora voluntarias de los términos de aquélla. De ello se levantará acta sucinta, que se incorporará al procedimiento.

4. Si alguno de los sujetos a los que hace referencia el artículo 14.2 y 14.3 presenta su solicitud presencialmente, las Administraciones Públicas requerirán al interesado para que la subsane a través de su presentación electrónica. A estos efectos, se considerará como fecha de presentación de la solicitud aquella en la que haya sido realizada la subsanación.

## Artículo 76. Alegaciones.

_Versión vigente desde 2016-10-02. Versiones en el BOE: 2016-10-02._

1. Los interesados podrán, en cualquier momento del procedimiento anterior al trámite de audiencia, aducir alegaciones y aportar documentos u otros elementos de juicio.

Unos y otros serán tenidos en cuenta por el órgano competente al redactar la correspondiente propuesta de resolución.

2. En todo momento podrán los interesados alegar los defectos de tramitación y, en especial, los que supongan paralización, infracción de los plazos preceptivamente señalados o la omisión de trámites que pueden ser subsanados antes de la resolución definitiva del asunto. Dichas alegaciones podrán dar lugar, si hubiere razones para ello, a la exigencia de la correspondiente responsabilidad disciplinaria.

## Artículo 77. Medios y período de prueba.

_Versión vigente desde 2022-07-14. Versiones en el BOE: 2016-10-02, 2022-07-14._

_Nota del BOE: Se añade el apartado 3 bis por la disposición final 4 de la Ley 15/2022, de 12 de julio. Ref. BOE-A-2022-11589#df-4_

1. Los hechos relevantes para la decisión de un procedimiento podrán acreditarse por cualquier medio de prueba admisible en Derecho, cuya valoración se realizará de acuerdo con los criterios establecidos en la Ley 1/2000, de 7 de enero, de Enjuiciamiento Civil.

2. Cuando la Administración no tenga por ciertos los hechos alegados por los interesados o la naturaleza del procedimiento lo exija, el instructor del mismo acordará la apertura de un período de prueba por un plazo no superior a treinta días ni inferior a diez, a fin de que puedan practicarse cuantas juzgue pertinentes. Asimismo, cuando lo considere necesario, el instructor, a petición de los interesados, podrá decidir la apertura de un período extraordinario de prueba por un plazo no superior a diez días.

3. El instructor del procedimiento sólo podrá rechazar las pruebas propuestas por los interesados cuando sean manifiestamente improcedentes o innecesarias, mediante resolución motivada.

3 bis. Cuando el interesado alegue discriminación y aporte indicios fundados sobre su existencia, corresponderá a la persona a quien se impute la situación discriminatoria la aportación de una justificación objetiva y razonable, suficientemente probada, de las medidas adoptadas y de su proporcionalidad.

A los efectos de lo dispuesto en el párrafo anterior, el órgano administrativo podrá recabar informe de los organismos públicos competentes en materia de igualdad.

4. En los procedimientos de carácter sancionador, los hechos declarados probados por resoluciones judiciales penales firmes vincularán a las Administraciones Públicas respecto de los procedimientos sancionadores que substancien.

5. Los documentos formalizados por los funcionarios a los que se reconoce la condición de autoridad y en los que, observándose los requisitos legales correspondientes se recojan los hechos constatados por aquéllos harán prueba de éstos salvo que se acredite lo contrario.

6. Cuando la prueba consista en la emisión de un informe de un órgano administrativo, organismo público o Entidad de derecho público, se entenderá que éste tiene carácter preceptivo.

7. Cuando la valoración de las pruebas practicadas pueda constituir el fundamento básico de la decisión que se adopte en el procedimiento, por ser pieza imprescindible para la correcta evaluación de los hechos, deberá incluirse en la propuesta de resolución.

## Artículo 85. Terminación en los procedimientos sancionadores.

_Versión vigente desde 2016-10-02. Versiones en el BOE: 2016-10-02._

1. Iniciado un procedimiento sancionador, si el infractor reconoce su responsabilidad, se podrá resolver el procedimiento con la imposición de la sanción que proceda.

2. Cuando la sanción tenga únicamente carácter pecuniario o bien quepa imponer una sanción pecuniaria y otra de carácter no pecuniario pero se ha justificado la improcedencia de la segunda, el pago voluntario por el presunto responsable, en cualquier momento anterior a la resolución, implicará la terminación del procedimiento, salvo en lo relativo a la reposición de la situación alterada o a la determinación de la indemnización por los daños y perjuicios causados por la comisión de la infracción.

3. En ambos casos, cuando la sanción tenga únicamente carácter pecuniario, el órgano competente para resolver el procedimiento aplicará reducciones de, al menos, el 20 % sobre el importe de la sanción propuesta, siendo éstos acumulables entre sí. Las citadas reducciones, deberán estar determinadas en la notificación de iniciación del procedimiento y su efectividad estará condicionada al desistimiento o renuncia de cualquier acción o recurso en vía administrativa contra la sanción.

El porcentaje de reducción previsto en este apartado podrá ser incrementado reglamentariamente.

## Artículo 89. Propuesta de resolución en los procedimientos de carácter sancionador.

_Versión vigente desde 2016-10-02. Versiones en el BOE: 2016-10-02._

1. El órgano instructor resolverá la finalización del procedimiento, con archivo de las actuaciones, sin que sea necesaria la formulación de la propuesta de resolución, cuando en la instrucción procedimiento se ponga de manifiesto que concurre alguna de las siguientes circunstancias:

a) La inexistencia de los hechos que pudieran constituir la infracción.

b) Cuando los hechos no resulten acreditados.

c) Cuando los hechos probados no constituyan, de modo manifiesto, infracción administrativa.

d) Cuando no exista o no se haya podido identificar a la persona o personas responsables o bien aparezcan exentos de responsabilidad.

e) Cuando se concluyera, en cualquier momento, que ha prescrito la infracción.

2. En el caso de procedimientos de carácter sancionador, una vez concluida la instrucción del procedimiento, el órgano instructor formulará una propuesta de resolución que deberá ser notificada a los interesados. La propuesta de resolución deberá indicar la puesta de manifiesto del procedimiento y el plazo para formular alegaciones y presentar los documentos e informaciones que se estimen pertinentes.

3. En la propuesta de resolución se fijarán de forma motivada los hechos que se consideren probados y su exacta calificación jurídica, se determinará la infracción que, en su caso, aquéllos constituyan, la persona o personas responsables y la sanción que se proponga, la valoración de las pruebas practicadas, en especial aquellas que constituyan los fundamentos básicos de la decisión, así como las medidas provisionales que, en su caso, se hubieran adoptado. Cuando la instrucción concluya la inexistencia de infracción o responsabilidad y no se haga uso de la facultad prevista en el apartado primero, la propuesta declarará esa circunstancia.

## Artículo 90. Especialidades de la resolución en los procedimientos sancionadores.

_Versión vigente desde 2016-10-02. Versiones en el BOE: 2016-10-02._

1. En el caso de procedimientos de carácter sancionador, además del contenido previsto en los dos artículos anteriores, la resolución incluirá la valoración de las pruebas practicadas, en especial aquellas que constituyan los fundamentos básicos de la decisión, fijarán los hechos y, en su caso, la persona o personas responsables, la infracción o infracciones cometidas y la sanción o sanciones que se imponen, o bien la declaración de no existencia de infracción o responsabilidad.

2. En la resolución no se podrán aceptar hechos distintos de los determinados en el curso del procedimiento, con independencia de su diferente valoración jurídica. No obstante, cuando el órgano competente para resolver considere que la infracción o la sanción revisten mayor gravedad que la determinada en la propuesta de resolución, se notificará al inculpado para que aporte cuantas alegaciones estime convenientes en el plazo de quince días.

3. La resolución que ponga fin al procedimiento será ejecutiva cuando no quepa contra ella ningún recurso ordinario en vía administrativa, pudiendo adoptarse en la misma las disposiciones cautelares precisas para garantizar su eficacia en tanto no sea ejecutiva y que podrán consistir en el mantenimiento de las medidas provisionales que en su caso se hubieran adoptado.

Cuando la resolución sea ejecutiva, se podrá suspender cautelarmente, si el interesado manifiesta a la Administración su intención de interponer recurso contencioso-administrativo contra la resolución firme en vía administrativa. Dicha suspensión cautelar finalizará cuando:

a) Haya transcurrido el plazo legalmente previsto sin que el interesado haya interpuesto recurso contencioso-administrativo.

b) Habiendo el interesado interpuesto recurso contencioso-administrativo:

1.º No se haya solicitado en el mismo trámite la suspensión cautelar de la resolución impugnada.

2.º El órgano judicial se pronuncie sobre la suspensión cautelar solicitada, en los términos previstos en ella.

4. Cuando las conductas sancionadas hubieran causado daños o perjuicios a las Administraciones y la cuantía destinada a indemnizar estos daños no hubiera quedado determinada en el expediente, se fijará mediante un procedimiento complementario, cuya resolución será inmediatamente ejecutiva. Este procedimiento será susceptible de terminación convencional, pero ni ésta ni la aceptación por el infractor de la resolución que pudiera recaer implicarán el reconocimiento voluntario de su responsabilidad. La resolución del procedimiento pondrá fin a la vía administrativa.

## Artículo 95. Requisitos y efectos.

_Versión vigente desde 2016-10-02. Versiones en el BOE: 2016-10-02._

1. En los procedimientos iniciados a solicitud del interesado, cuando se produzca su paralización por causa imputable al mismo, la Administración le advertirá que, transcurridos tres meses, se producirá la caducidad del procedimiento. Consumido este plazo sin que el particular requerido realice las actividades necesarias para reanudar la tramitación, la Administración acordará el archivo de las actuaciones, notificándoselo al interesado. Contra la resolución que declare la caducidad procederán los recursos pertinentes.

2. No podrá acordarse la caducidad por la simple inactividad del interesado en la cumplimentación de trámites, siempre que no sean indispensables para dictar resolución. Dicha inactividad no tendrá otro efecto que la pérdida de su derecho al referido trámite.

3. La caducidad no producirá por sí sola la prescripción de las acciones del particular o de la Administración, pero los procedimientos caducados no interrumpirán el plazo de prescripción.

En los casos en los que sea posible la iniciación de un nuevo procedimiento por no haberse producido la prescripción, podrán incorporarse a éste los actos y trámites cuyo contenido se hubiera mantenido igual de no haberse producido la caducidad. En todo caso, en el nuevo procedimiento deberán cumplimentarse los trámites de alegaciones, proposición de prueba y audiencia al interesado.

4. Podrá no ser aplicable la caducidad en el supuesto de que la cuestión suscitada afecte al interés general, o fuera conveniente sustanciarla para su definición y esclarecimiento.

## Artículo 112. Objeto y clases.

_Versión vigente desde 2016-10-02. Versiones en el BOE: 2016-10-02._

1. Contra las resoluciones y los actos de trámite, si estos últimos deciden directa o indirectamente el fondo del asunto, determinan la imposibilidad de continuar el procedimiento, producen indefensión o perjuicio irreparable a derechos e intereses legítimos, podrán interponerse por los interesados los recursos de alzada y potestativo de reposición, que cabrá fundar en cualquiera de los motivos de nulidad o anulabilidad previstos en los artículos 47 y 48 de esta Ley.

La oposición a los restantes actos de trámite podrá alegarse por los interesados para su consideración en la resolución que ponga fin al procedimiento.

2. Las leyes podrán sustituir el recurso de alzada, en supuestos o ámbitos sectoriales determinados, y cuando la especificidad de la materia así lo justifique, por otros procedimientos de impugnación, reclamación, conciliación, mediación y arbitraje, ante órganos colegiados o Comisiones específicas no sometidas a instrucciones jerárquicas, con respeto a los principios, garantías y plazos que la presente Ley reconoce a las personas y a los interesados en todo procedimiento administrativo.

En las mismas condiciones, el recurso de reposición podrá ser sustituido por los procedimientos a que se refiere el párrafo anterior, respetando su carácter potestativo para el interesado.

La aplicación de estos procedimientos en el ámbito de la Administración Local no podrá suponer el desconocimiento de las facultades resolutorias reconocidas a los órganos representativos electos establecidos por la Ley.

3. Contra las disposiciones administrativas de carácter general no cabrá recurso en vía administrativa.

Los recursos contra un acto administrativo que se funden únicamente en la nulidad de alguna disposición administrativa de carácter general podrán interponerse directamente ante el órgano que dictó dicha disposición.

4. Las reclamaciones económico-administrativas se ajustarán a los procedimientos establecidos por su legislación específica.

## Artículo 115. Interposición de recurso.

_Versión vigente desde 2016-10-02. Versiones en el BOE: 2016-10-02._

1. La interposición del recurso deberá expresar:

a) El nombre y apellidos del recurrente, así como la identificación personal del mismo.

b) El acto que se recurre y la razón de su impugnación.

c) Lugar, fecha, firma del recurrente, identificación del medio y, en su caso, del lugar que se señale a efectos de notificaciones.

d) Órgano, centro o unidad administrativa al que se dirige y su correspondiente código de identificación.

e) Las demás particularidades exigidas, en su caso, por las disposiciones específicas.

2. El error o la ausencia de la calificación del recurso por parte del recurrente no será obstáculo para su tramitación, siempre que se deduzca su verdadero carácter.

3. Los vicios y defectos que hagan anulable un acto no podrán ser alegados por quienes los hubieren causado.

## Artículo 118. Audiencia de los interesados.

_Versión vigente desde 2016-10-02. Versiones en el BOE: 2016-10-02._

1. Cuando hayan de tenerse en cuenta nuevos hechos o documentos no recogidos en el expediente originario, se pondrán de manifiesto a los interesados para que, en un plazo no inferior a diez días ni superior a quince, formulen las alegaciones y presenten los documentos y justificantes que estimen procedentes.

No se tendrán en cuenta en la resolución de los recursos, hechos, documentos o alegaciones del recurrente, cuando habiendo podido aportarlos en el trámite de alegaciones no lo haya hecho. Tampoco podrá solicitarse la práctica de pruebas cuando su falta de realización en el procedimiento en el que se dictó la resolución recurrida fuera imputable al interesado.

2. Si hubiera otros interesados se les dará, en todo caso, traslado del recurso para que en el plazo antes citado, aleguen cuanto estimen procedente.

3. El recurso, los informes y las propuestas no tienen el carácter de documentos nuevos a los efectos de este artículo. Tampoco lo tendrán los que los interesados hayan aportado al expediente antes de recaer la resolución impugnada.

## Artículo 121. Objeto.

_Versión vigente desde 2016-10-02. Versiones en el BOE: 2016-10-02._

1. Las resoluciones y actos a que se refiere el artículo 112.1, cuando no pongan fin a la vía administrativa, podrán ser recurridos en alzada ante el órgano superior jerárquico del que los dictó. A estos efectos, los Tribunales y órganos de selección del personal al servicio de las Administraciones Públicas y cualesquiera otros que, en el seno de éstas, actúen con autonomía funcional, se considerarán dependientes del órgano al que estén adscritos o, en su defecto, del que haya nombrado al presidente de los mismos.

2. El recurso podrá interponerse ante el órgano que dictó el acto que se impugna o ante el competente para resolverlo.

Si el recurso se hubiera interpuesto ante el órgano que dictó el acto impugnado, éste deberá remitirlo al competente en el plazo de diez días, con su informe y con una copia completa y ordenada del expediente.

El titular del órgano que dictó el acto recurrido será responsable directo del cumplimiento de lo previsto en el párrafo anterior.

## Artículo 122. Plazos.

_Versión vigente desde 2016-10-02. Versiones en el BOE: 2016-10-02._

1. El plazo para la interposición del recurso de alzada será de un mes, si el acto fuera expreso. Transcurrido dicho plazo sin haberse interpuesto el recurso, la resolución será firme a todos los efectos.

Si el acto no fuera expreso el solicitante y otros posibles interesados podrán interponer recurso de alzada en cualquier momento a partir del día siguiente a aquel en que, de acuerdo con su normativa específica, se produzcan los efectos del silencio administrativo.

2. El plazo máximo para dictar y notificar la resolución será de tres meses. Transcurrido este plazo sin que recaiga resolución, se podrá entender desestimado el recurso, salvo en el supuesto previsto en el artículo 24.1, tercer párrafo.

3. Contra la resolución de un recurso de alzada no cabrá ningún otro recurso administrativo, salvo el recurso extraordinario de revisión, en los casos establecidos en el artículo 125.1.

## Artículo 123. Objeto y naturaleza.

_Versión vigente desde 2016-10-02. Versiones en el BOE: 2016-10-02._

1. Los actos administrativos que pongan fin a la vía administrativa podrán ser recurridos potestativamente en reposición ante el mismo órgano que los hubiera dictado o ser impugnados directamente ante el orden jurisdiccional contencioso-administrativo.

2. No se podrá interponer recurso contencioso-administrativo hasta que sea resuelto expresamente o se haya producido la desestimación presunta del recurso de reposición interpuesto.

## Artículo 124. Plazos.

_Versión vigente desde 2016-10-02. Versiones en el BOE: 2016-10-02._

1. El plazo para la interposición del recurso de reposición será de un mes, si el acto fuera expreso. Transcurrido dicho plazo, únicamente podrá interponerse recurso contencioso-administrativo, sin perjuicio, en su caso, de la procedencia del recurso extraordinario de revisión.

Si el acto no fuera expreso, el solicitante y otros posibles interesados podrán interponer recurso de reposición en cualquier momento a partir del día siguiente a aquel en que, de acuerdo con su normativa específica, se produzca el acto presunto.

2. El plazo máximo para dictar y notificar la resolución del recurso será de un mes.

3. Contra la resolución de un recurso de reposición no podrá interponerse de nuevo dicho recurso.
