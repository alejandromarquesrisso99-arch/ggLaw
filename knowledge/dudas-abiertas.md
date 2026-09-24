# ggLaw: propuesta de respuesta a las dudas abiertas del sancionador de tráfico

> Borrador del subagente `investigador-normativa` (dudas 1-8: 2026-09-23; dudas 9-21:
> 2026-09-23 y 2026-09-24). **No es asesoramiento jurídico.** Todo requiere validación de
> Alex o de un abogado antes de pasar a `rules/` o a `core/plazos.py`.

**Certeza.** `A`: lo dice el texto literal. `B`: interpretación con apoyo en fuente
primaria. `C`: no resoluble con las fuentes accesibles (se indica qué falta).

**Abreviaturas y fuentes** (consultadas el 2026-09-23 y el 2026-09-24 con
`scripts/boe_fetch.py`, versión consolidada vigente):

- **LSV**: RDL 6/2015, BOE-A-2015-11722, <https://www.boe.es/buscar/act.php?id=BOE-A-2015-11722>
  (fichero: `knowledge/rdl-6-2015-procedimiento-sancionador.md`).
- **LPAC**: Ley 39/2015, BOE-A-2015-10565, <https://www.boe.es/buscar/act.php?id=BOE-A-2015-10565>
  (fichero: `knowledge/ley-39-2015-notificaciones-recursos.md`).
- **LRJSP**: Ley 40/2015, BOE-A-2015-10566, <https://www.boe.es/buscar/act.php?id=BOE-A-2015-10566>
  (fichero: `knowledge/ley-40-2015-potestad-sancionadora.md`).
- **RPST**: RD 320/1994, BOE-A-1994-8985, <https://www.boe.es/buscar/act.php?id=BOE-A-1994-8985>
  (fichero: `knowledge/rd-320-1994-reglamento-sancionador-trafico.md`).
- **CC**: Código Civil, art. 5, BOE-A-1889-4763, <https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763>
  (leído, no transcrito en `knowledge/`).
- **Ley 18/2009**: BOE-A-2009-18732, <https://www.boe.es/buscar/act.php?id=BOE-A-2009-18732> (art. único, DD única, DF 5ª y DF 7ª leídos).
- **LBRL**: Ley 7/1985, BOE-A-1985-5392, <https://www.boe.es/buscar/act.php?id=BOE-A-1985-5392>
  (fichero: `knowledge/lbrl-7-1985-regimen-local.md`).
- **LJCA**: Ley 29/1998, BOE-A-1998-16718, <https://www.boe.es/buscar/act.php?id=BOE-A-1998-16718>
  (fichero: `knowledge/ljca-29-1998-recurso-contencioso.md`).
- **LOPJ**: LO 6/1985, BOE-A-1985-12666, y **LO 1/2025**, BOE-A-2025-76
  (fichero: `knowledge/lopj-6-1985-tribunales-instancia.md`).
- **Orden TESTRA**: Orden INT/3022/2010, BOE-A-2010-18102, <https://www.boe.es/buscar/act.php?id=BOE-A-2010-18102>
  (fichero: `knowledge/orden-int-3022-2010-testra.md`).
- Leídas con `scripts/boe_fetch.py` y no transcritas en `knowledge/`: Ley 15/2014
  (BOE-A-2014-9467), art. 25; Ley 6/2014 (BOE-A-2014-3715), art. único; RD 181/2008
  (BOE-A-2008-2389), arts. 7 y 8; Ley 57/2003 (BOE-A-2003-23103), DT 1ª y DF 3ª. Leído en el
  diario oficial: RD 1748/2003 (BOE-A-2003-23404), cifras de población de 2003.

**Jurisprudencia.** CENDOJ no se puede usar desde el entorno de trabajo: el buscador
devuelve 403 y la descarga de sentencias pide un CAPTCHA, que no se ha intentado saltar.
hj.tribunalconstitucional.es sí es accesible (comprobado el 2026-09-23 y el 2026-09-24), y
los ECLI del TC citados están verificados en sus fichas. Del TS solo se han leído los fallos
que fijan doctrina legal publicados en el BOE. El panel «Jurisprudencia» de boe.es
(selección del CENDOJ) no vincula ninguna sentencia a los arts. 30 y 31 LPAC ni a los arts.
90, 95, 96 y 112 LSV. Para el art. 30 LRJSP vincula la STS 603/2021 (25/02/2021), no leída.
Todo lo demás son **pistas no verificadas**, halladas en fuentes secundarias.

---

## Dudas 1-8: supletoriedad y cómputo de plazos

### Duda 1. Qué preceptos de la Ley 39/2015 se aplican al sancionador de tráfico

**Respuesta propuesta.** Se aplica primero la LSV (y el RPST en lo que no la contradiga,
ver duda 3). La LPAC solo se aplica **cuando la LSV no regula la cuestión**, nunca
cuando la regula de otro modo. Reparto operativo para ggLaw:
- **Rige la LSV (no la LPAC):** plazos de alegaciones y pago (93-95), lugares y forma de
  notificación, DEV, rechazo, BOE y TESTRA (89-92), recurso (96: reposición potestativa de
  un mes, silencio al mes), caducidad de un año y prescripción (112), ejecución (108-110).
- **Rige la LPAC como supletoria (la LSV calla):** cómputo de plazos (30: día inicial,
  meses, días inhábiles, prórroga; 31: registros), lugares de presentación (16.4, además
  de los del 93.4 LSV), contenido y requisitos de la notificación y del intento acreditado
  (40-41; 42.2 en lo que el 90.3 LSV no diga, ver duda 6), invalidez (47-48), derechos del
  interesado (53), efectos de la caducidad (95.3), recursos en lo no regulado (112-120,
  123-124 en lo que no contradiga el 96 LSV) y recurso extraordinario de revisión (125-126).
- **No se aplican:** plazo máximo de 3 o 6 meses (21.2-21.3 LPAC: la LSV fija un año),
  alzada (121-122: la resolución pone fin a la vía, 96.1 LSV), reducciones del 85.3 LPAC
  (la LSV fija la suya en el 94) y ejecutividad del 90.3 LPAC (la LSV la regula en 95.5 y 96.1).

**Fundamento.**
- LSV 83.1: «procedimiento instruido con arreglo a lo dispuesto en este capítulo y,
  supletoriamente, en la normativa de procedimiento administrativo común».
- LPAC DA 1ª.2.c): «Las actuaciones y procedimientos sancionadores […] en materia de
  tráfico y seguridad vial» se regirán «por su normativa específica y supletoriamente por lo
  dispuesto en esta Ley».
- LPAC DA 1ª.1: los procedimientos de leyes especiales «que no exijan alguno de los
  trámites previstos en esta Ley o regulen trámites adicionales o distintos se regirán,
  respecto a éstos, por lo dispuesto en dichas leyes especiales».
- LRJSP 25.1: potestad sancionadora ejercida «de acuerdo con lo establecido en esta Ley y
  en la Ley de Procedimiento Administrativo Común».

**Fuente.** LSV art. 83; LPAC DA 1ª; LRJSP art. 25 (URLs arriba). Consultado 2026-09-23.

**Certeza.** `A` para la regla general (supletoriedad: la LSV primero, la LPAC en lo no
regulado). `B` para el reparto concreto de artículos. Es interpretación propia y el
riesgo está en los casos frontera en que la LSV regula algo **en parte** (p. ej. 90.3
frente a 42.2, o 112.3 frente a 40.4 y 95.3 LPAC). En esos casos no está claro si la
regulación parcial excluye el resto del precepto general.

**Qué queda pendiente.** Que Alex o un abogado confirmen la tabla precepto a precepto,
sobre todo 40.4, 42.2, 64.2 y 95.3 LPAC en tráfico. Buscar en CENDOJ doctrina del TS
sobre supletoriedad de la LPAC en tráfico (no localizada en boe.es).

---

### Duda 2. Aplicación supletoria del art. 30 de la Ley 40/2015 a la prescripción en tráfico

**Respuesta propuesta.** Los **plazos** de prescripción son los del art. 112 LSV (el 30.1
LRJSP remite a «las leyes que las establezcan»). Lo que la LSV sí regula (interrupción,
reanudación, día inicial) prevalece sobre la LRJSP. El art. 30 LRJSP **completa** tres
lagunas:
1. **Infracciones continuadas o permanentes** (30.2): el día inicial es el fin de la
   conducta. El 112.1 LSV no las contempla.
2. **Prescripción de la sanción cuando el recurso no se resuelve** (30.3, párr. 3): el
   texto habla solo de **alzada**, y en tráfico el recurso es la **reposición** (96.2 LSV).
   Hay una pista no verificada de que el TS lo extiende a la reposición. Si fuera así, la
   prescripción de la multa (4 años, 112.4 LSV) empezaría el día siguiente al mes del
   96.5 LSV, aunque el recurso siga sin resolverse. Esto superaría, en ese punto, la
   doctrina legal de la STS de 22/09/2008 (BOE-A-2008-18350).
3. **Día inicial de la prescripción de la sanción** (30.3, párr. 1): «sea ejecutable […] o
   haya transcurrido el plazo para recurrirla». Choca con el 112.4 LSV («adquiera
   firmeza»), así que no se aplica directamente. Solo aporta criterio si se discute qué es
   «firmeza».
Para ggLaw: **no implementar** la regla de prescripción de la sanción con reposición
pendiente hasta que se valide.

**Fundamento.**
- LRJSP 30.1: «Las infracciones y sanciones prescribirán según lo dispuesto en las leyes
  que las establezcan».
- LRJSP 30.2: «En el caso de infracciones continuadas o permanentes, el plazo comenzará a
  correr desde que finalizó la conducta infractora».
- LRJSP 30.3, párr. 3: «En el caso de desestimación presunta del recurso de alzada […] el
  plazo de prescripción de la sanción comenzará a contarse desde el día siguiente a aquel
  en que finalice el plazo legalmente previsto para la resolución de dicho recurso».
- LSV 112.4: «computados desde el día siguiente a aquel en que adquiera firmeza la sanción
  en vía administrativa». LSV 96.5: la reposición «se entenderá desestimado si no recae
  resolución expresa en el plazo de un mes».
- LRJSP 26.2: retroactividad favorable también en «sus plazos de prescripción».
- Carácter básico: LRJSP DF 14ª.1 (art. 149.1.18.ª CE). El capítulo III no está entre los
  preceptos no básicos de la DF 14ª.2.

**Fuente.** LRJSP arts. 25-31 y DF 14ª; LSV arts. 96 y 112. Jurisprudencia vinculada por
boe.es al art. 30 LRJSP: STS 603/2021 (25/02/2021), «Prescripción de sanciones. Día inicial
de cómputo en supuestos de desestimación presunta del recurso de alzada. Aplicación
retroactiva de la Ley 40/2015» (ECLI deducido ECLI:ES:TS:2021:603, no leída).
**Pistas no verificadas:** STS de 15/10/2020 (rec. cas. 7337/2019), que extendería el
30.3, párr. 3, a la reposición, y STS 333/2023, de 15/03/2023 (retroactividad).
Consultado 2026-09-23.

**Certeza.** `A` en que los plazos son los del 112 LSV y en el texto de 30.2 y 30.3.
`B` en la aplicación supletoria de 30.2 a tráfico: el 112.1 LSV fija el día inicial en «el
mismo día en que los hechos se hubieran cometido», y cabe sostener que eso excluye la
regla de las infracciones permanentes. `C` en la extensión a la reposición: depende de
jurisprudencia que no se ha podido leer.

**Qué queda pendiente.** Leer en CENDOJ la STS 603/2021 y la STS de 15/10/2020
(rec. 7337/2019), y confirmar ECLI y doctrina. Decidir si la regla de las infracciones
permanentes (30.2) se aplica a infracciones de tráfico concretas (seguro, ITV,
estacionamiento). Actualizar la duda 11 del fichero de la Ley 39/2015 (la STS 2008 puede
estar superada).

**Recomendación para ggLaw.** Mientras no se valide, tratar la prescripción de la sanción
con reposición no resuelta como «motivo posible, a verificar», nunca como motivo cierto.

---

### Duda 3. Vigencia y preceptos aplicables del RD 320/1994

**Respuesta propuesta.** El RPST está **formalmente vigente**: ninguna norma lo deroga
expresamente y el RDL 6/2015 no lo menciona. Pero todo lo que contradice la LSV está
desplazado: 15 días de alegaciones, alzada, prescripción de 1 año para muy graves y
sanciones, 15 días hábiles para pagar. Para ggLaw: **no usar ningún plazo del RPST** en
`core/`. Solo puede servir como complemento en lo que la LSV calla, por ejemplo el período
de prueba de 10 a 30 días (13.1 RPST), y siempre con `TODO(juridico)`. Su remisión al
RD 1398/1993 (art. 1) debe leerse hoy como remisión a la LPAC.

**Fundamento.**
- Metadatos API BOE: `estatus_derogacion: N`, `estatus_anulacion: N`, `vigencia_agotada: N`.
  La página consolidada dice «Última actualización publicada el 24/01/2005». El análisis BOE
  registra solo modificaciones (RD 116/1998, RD 137/2000, RD 318/2003) y la nulidad del
  art. 12.2, párr. 2, por STS de 27/10/2004 (BOE-A-2005-1214). No hay derogaciones.
- LSV DD única: deroga el RDL 339/1990 «así como las leyes que lo han modificado». No cita
  reglamentos. LSV DA 1ª: las referencias al texto de 1990 «se entenderán efectuadas a los
  preceptos correspondientes del texto refundido».
- Ley 18/2009 DD única: «cuantas disposiciones de igual o inferior rango se opongan a lo
  dispuesto en esta Ley». Esa Ley introdujo los «veinte días naturales», el procedimiento
  abreviado, la DEV y la prescripción de la multa a «cuatro años» (comprobado en su texto).
  DF 5ª: «El Gobierno procederá a adaptar todas aquellas normas que se vean afectadas».
  No consta la adaptación.
- LPAC DD única 2.e) deroga el RD 1398/1993, y la DD única.3 dice: «Las referencias […] a
  las disposiciones que se derogan expresamente deberán entenderse efectuadas a las
  disposiciones de esta Ley».
- Contradicciones literales: RPST 10.1 y 12.1 «quince días» frente a LSV 93.1 y 95.1
  «veinte días naturales». RPST 18.1 «un año» (muy graves) frente a LSV 112.1 «seis
  meses». RPST 18.2 «un año» frente a LSV 112.4 «cuatro años». RPST 21.1 «quince días
  hábiles» frente a LSV 110.1 «quince días naturales». RPST 17.1 (alzada) frente a
  LSV 96 (reposición).

**Fuente.** <https://www.boe.es/buscar/act.php?id=BOE-A-1994-8985>;
<https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1994-8985/analisis>;
BOE-A-2005-1214; LSV DD única y DA 1ª; Ley 18/2009 DD única y DF 5ª. Consultado 2026-09-23.

**Certeza.** `A` en la vigencia formal y en la ausencia de derogación expresa. `B` en el
desplazamiento de los preceptos contrarios. Es el efecto de la DD de la Ley 18/2009 y de
la jerarquía normativa; el riesgo es bajo en los preceptos contrarios y alto en los
«complementarios» (13.1, 15.1 «habrá de notificarse en el plazo de un año», 16 con su
supuesto adicional de suspensión).

**Qué queda pendiente.** Jurisprudencia del TS (CENDOJ) sobre qué preceptos del RPST se
aplican tras 2010. Decidir si el 15.1 RPST («notificarse») pesa en la interpretación del
112.3 LSV («producido la resolución»); está enlazado con la duda 11 del fichero del RDL.

---

### Duda 4. Prórroga de un plazo en días naturales cuyo último día es inhábil; presentación electrónica en sábado

**Respuesta propuesta.**
- **Prórroga.** El art. 30.5 LPAC no distingue entre días hábiles y naturales y la LSV no
  tiene una regla propia. Por supletoriedad, un plazo de 20 días naturales (93.1, 95.1 y
  94 LSV) cuyo último día es sábado, domingo o festivo **se prorroga al primer día hábil
  siguiente**.
- **Sábado en plazo natural.** La regla del 31.2.b) LPAC (presentar en día inhábil cuenta
  como la primera hora del siguiente hábil) se limita al «cómputo de plazo fijado en días
  hábiles». En un plazo en días naturales, un escrito presentado en el registro
  electrónico en sábado **cuenta como presentado ese sábado**. El registro admite
  presentaciones «todos los días del año durante las veinticuatro horas» (31.2.a).
- Para `core/plazos.py`: `vencimiento = inicio + 20 días naturales` y, si ese día es
  inhábil según el calendario aplicable (duda 8), se desplaza al siguiente hábil. La fecha
  de presentación es la fecha real de registro, sin desplazarla.

**Fundamento.**
- LPAC 30.5: «Cuando el último día del plazo sea inhábil, se entenderá prorrogado al
  primer día hábil siguiente».
- LPAC 30.2: «excluyéndose del cómputo los sábados, los domingos y los declarados
  festivos». Por tanto, el sábado es inhábil.
- LPAC 31.2.a): «Permitirá la presentación de documentos todos los días del año durante
  las veinticuatro horas». LPAC 31.2.b): «A los efectos del cómputo de plazo fijado en
  días hábiles […] la presentación en un día inhábil se entenderá realizada en la primera
  hora del primer día hábil siguiente».
- LSV 83.1 (supletoriedad) y LSV 93.1, 94, 95.1 («veinte días naturales»).

**Fuente.** LPAC arts. 30 y 31; LSV arts. 83, 93-95. Consultado 2026-09-23.

**Certeza.** `B` en la prórroga: es la lectura literal del 30.5 y el precepto no
distingue, pero ninguna sentencia se ha leído. Riesgo: una línea jurisprudencial
(pista no verificada, STS de 17/04/2024, ECLI:ES:TS:2024:2017 según una reseña)
distinguiría plazos procedimentales (con prórroga) de plazos sustantivos (sin prórroga).
Los 20 días de alegaciones son procedimentales, así que el riesgo para ellos es bajo.
`A` en la presentación en sábado: el 31.2.b) se limita literalmente a los plazos en días
hábiles.

**Qué queda pendiente.** Confirmar en CENDOJ que el TS aplica el 30.5 a plazos en días
naturales de la LSV. Decidir si la prórroga se aplica también a los plazos en días
naturales que no son para el interesado (90.2 LSV, 10 días del rechazo en DEV; 91 LSV,
20 días desde la publicación en el BOE). Hay una pista secundaria de un criterio del TEAC
que no aplica el 30.5 al plazo de 10 días de las notificaciones electrónicas (art. 43.2
LPAC). **No aplicar la prórroga a esos plazos** hasta validarlo.

**Recomendación para ggLaw.** Mostrar al usuario como fecha límite **el día 20 natural
sin prórroga** («presenta como tarde el …») y, si ese día es inhábil, añadir como
información que la ley probablemente lo prorroga al día X. Así el usuario no depende de
una interpretación.

---

### Duda 5. Día inicial de los 20 días naturales (arts. 93.1 y 95.1 LSV)

**Respuesta propuesta.** Todos los plazos de 20 días naturales empiezan **el día
siguiente al de la notificación** de la denuncia. El día de la notificación no cuenta.
Ejemplo: notificada el 1 de marzo, el día 1 del plazo es el 2 de marzo y el día 20 es el
21 de marzo, con la prórroga de la duda 4 si procede. Para el pago con reducción (94) y
para el efecto resolutorio (95.4) lo dice la propia LSV. Para alegaciones e
identificación del conductor (93.1 y 95.1) lo completa el 30.3 LPAC. Y es el mismo plazo,
porque el 93.1 regula pago y alegaciones en un único «plazo de veinte días naturales».

**Fundamento.**
- LSV 94: «dentro del plazo de veinte días naturales contados desde el día siguiente al de
  su notificación».
- LSV 95.4: «en el plazo de veinte días naturales siguientes al de la notificación de la
  denuncia».
- LSV 93.1: «Notificada la denuncia […] dispondrá de un plazo de veinte días naturales para
  realizar el pago voluntario con reducción […] o para formular las alegaciones».
- LPAC 30.3: «Los plazos expresados en días se contarán a partir del día siguiente a aquel
  en que tenga lugar la notificación o publicación del acto».
- Concordante: CC 5.1 («quedará éste excluido del cómputo, el cual deberá empezar en el
  día siguiente»).

**Fuente.** LSV arts. 93-95; LPAC art. 30.3; CC art. 5. Consultado 2026-09-23.

**Certeza.** `A` para el pago con reducción (94) y el efecto resolutorio (95.4). `B` para
alegaciones (93.1 y 95.1) e identificación del conductor (93.1, párr. 2): no lo dice la
LSV, pero lo dicen la LPAC supletoria y el CC, y el 93.1 trata pago y alegaciones como
un solo plazo. Riesgo muy bajo: la lectura contraria (contar el propio día de
notificación) acortaría el plazo un día y no tiene apoyo textual.

**Qué queda pendiente.** El **momento** de la notificación en DEV (acceso al contenido o
rechazo a los 10 días naturales, 90.2 LSV) y en BOE (se entiende practicada
«transcurrido el período de veinte días naturales» desde la publicación, 91 LSV). Son
dudas distintas (17 y 18 del fichero del RDL): esta respuesta solo fija el día inicial
**una vez conocida la fecha de notificación**.

**Recomendación para ggLaw.** Si la fecha de notificación es dudosa (acuse ilegible, DEV
sin fecha de acceso), usar la fecha más temprana posible.

---

### Duda 6. «Dentro de los tres días siguientes» del segundo intento (90.3 LSV, 42.2 LPAC): ¿hábiles o naturales?

**Respuesta propuesta.** Ni la LSV ni la LPAC dicen el tipo de día. La regla general
supletoria (30.2 LPAC) los hace **hábiles**. ggLaw debe usarlo solo para **detectar
defectos de notificación**, con dos niveles:
- Segundo intento **después del 3.er día hábil** siguiente al primero: «posible defecto
  de notificación» (motivo sólido, pendiente de validar).
- Segundo intento después del 3.er día natural pero **dentro del 3.er día hábil**: no
  alegar como defecto, o solo como «discutible».
Además, el 90.3 LSV **no exige** la hora distinta ni la regla de «antes/después de las
quince horas» con tres horas de margen del 42.2 LPAC. Si esas exigencias se aplican
supletoriamente a tráfico es dudoso: se aplicarían por completar una laguna, pero cabe
sostener que el 90.3 regula el segundo intento de forma completa.

**Fundamento.**
- LSV 90.3: «se dejará constancia de esta circunstancia en el procedimiento sancionador,
  junto con el día y la hora en que se intentó, y se practicará de nuevo dentro de los
  tres días siguientes».
- LPAC 42.2: «intento que se repetirá por una sola vez y en una hora distinta dentro de los
  tres días siguientes. En caso de que el primer intento de notificación se haya realizado
  antes de las quince horas, el segundo intento deberá realizarse después de las quince
  horas y viceversa, dejando en todo caso al menos un margen de diferencia de tres horas».
- LPAC 30.2: «Siempre que por Ley […] no se exprese otro cómputo, cuando los plazos se
  señalen por días, se entiende que éstos son hábiles».
- LSV 83.1 (supletoriedad).

**Fuente.** LSV art. 90; LPAC arts. 30.2 y 42.2. Consultado 2026-09-23. boe.es no vincula
jurisprudencia del TS al art. 90 LSV y, al art. 42 LPAC, ninguna sobre esta cuestión.

**Certeza.** `B` en «hábiles». Es la regla legal por defecto, pero no se ha podido
contrastar con jurisprudencia, y cabe objetar que el 30.2 regula plazos para actuar y no
el tiempo entre dos actuaciones materiales del notificador. `C` en si la franja horaria
del 42.2 LPAC se exige en tráfico. Falta jurisprudencia del TS o de los TSJ en CENDOJ
(pista no verificada: STS de 12/12/2025, rec. 2922/2023, sobre uno o dos intentos y
caducidad; no consta que trate el tipo de día).

**Qué queda pendiente.** Buscar en CENDOJ: «tres días siguientes» con «hábiles» y
«segundo intento», y el art. 90.3 LSV o el 59.2 de la Ley 30/1992 (precedente con la
misma expresión). Que Alex o un abogado decidan si la franja horaria del 42.2 se aplica a
tráfico.

**Recomendación para ggLaw.** Solo marcar el defecto cuando el segundo intento falla
**con ambos cómputos** (fuera de los 3 días hábiles). Si el problema es solo la franja
horaria del 42.2, presentarlo como argumento subsidiario.

---

### Duda 7. Cómputo en meses (30.4 LPAC) y el «mismo día» del art. 112.1 LSV

**Respuesta propuesta.**
- **Plazos en meses del procedimiento** (reposición, 96.2 LSV; silencio y suspensión,
  96.3 y 96.5): se cuentan **de fecha a fecha**. Empiezan el día siguiente a la
  notificación, pero **vencen el mismo número de día** en el mes de vencimiento. Si ese
  día no existe, vencen el último día del mes. Después se aplica la prórroga del 30.5 si
  el último día es inhábil. Ejemplos: notificación el 15/03, vence el 15/04; notificación
  el 31/01, vence el 28/02 (29/02 en bisiesto).
- **Prescripción de la infracción (112.1 LSV)**: es un plazo **sustantivo**, no de
  procedimiento, y la LSV fija un día inicial propio: «el mismo día» de los hechos, que
  **se incluye** en el cómputo. Aplicando el CC 5.1 («fecha a fecha»), el último día hábil
  para interrumpir es el **día anterior** al del mismo número en el mes de vencimiento.
  Ejemplo: hechos el 15/01, leve (3 meses): el plazo cubre del 15/01 al 14/04 y la
  infracción está prescrita si la primera actuación interruptiva es del 15/04 o posterior.
  Con el cómputo general (desde el día siguiente) el último día sería el 15/04. La
  diferencia es de un día.
- **Prórroga en la prescripción**: según el CC 5.2 los días inhábiles no se excluyen en el
  cómputo civil. Aplicar el 30.5 LPAC a la prescripción es dudoso: hay una pista no
  verificada de una STS de 2024 que no lo aplicaría a un plazo sustantivo de 4 años.

**Fundamento.**
- LPAC 30.4: «Si el plazo se fija en meses o años, éstos se computarán a partir del día
  siguiente a aquel en que tenga lugar la notificación […]. El plazo concluirá el mismo día
  en que se produjo la notificación, publicación o silencio administrativo en el mes o el
  año de vencimiento. Si en el mes de vencimiento no hubiera día equivalente […] el plazo
  expira el último día del mes».
- LSV 96.2: «en el plazo de un mes contado desde el día siguiente al de su notificación».
- LSV 112.1: «tres meses para las infracciones leves y de seis meses para las infracciones
  graves y muy graves. El plazo de prescripción comenzará a contar a partir del mismo día
  en que los hechos se hubieran cometido».
- CC 5.1: «Siempre que no se establezca otra cosa, en los plazos señalados por días, a
  contar de uno determinado, quedará éste excluido del cómputo […]; y si los plazos
  estuviesen fijados por meses o años, se computarán de fecha a fecha». CC 5.2: «En el
  cómputo civil de los plazos no se excluyen los días inhábiles».
- LRJSP 30.2 (general): «desde el día en que la infracción se hubiera cometido».

**Fuente.** LPAC art. 30.4-30.5; LSV arts. 96 y 112; CC art. 5; LRJSP art. 30. Consultado
2026-09-23.

**Certeza.** `A` en los plazos en meses del procedimiento (30.4 es literal y el 96.2 LSV
repite el día inicial). `B` en la prescripción. «El mismo día» incluye literalmente el día
de los hechos, pero cómo se combina con el cómputo «de fecha a fecha» (vencer el día
anterior o el mismo número de día) no está resuelto en los textos. Tampoco lo está qué
pasa en fin de mes (hechos el 30/11, 3 meses) ni si hay prórroga al día hábil. El riesgo
es de un día en los casos límite.

**Qué queda pendiente.** Jurisprudencia del TS sobre el cómputo del 112.1 LSV y de su
precepto equivalente del RDL 339/1990 (CENDOJ; número de artículo por confirmar). Verificar la STS de 17/04/2024
(pista) sobre el 30.5 y los plazos sustantivos. Decidir qué hacer en los casos de fin de
mes.

**Recomendación para ggLaw.** Implementar la prescripción con **tres zonas**:
`no_prescrita` (interrupción el día 14/04 del ejemplo o antes), `dudosa` (en la ventana
entre el cómputo más corto y el más largo, incluida una posible prórroga al día hábil) y
`prescrita` (interrupción posterior al cómputo **más largo**). Solo en la última zona el
motivo se propone como sólido.

---

### Duda 8. Festivo local del domicilio frente al de la sede: 30.6 frente a 31.3 LPAC

**Respuesta propuesta.** El resultado depende del **canal de presentación**:
- **Registro electrónico** (sede de la Administración que sanciona): solo cuenta el
  **calendario de la sede**. Un festivo local del municipio del usuario **no** prorroga el
  plazo. Ejemplo: un vecino de otro municipio de Mallorca con festivo local el último día
  del plazo, que presenta electrónicamente ante el Ajuntament de Palma, **no** tiene
  prórroga por su festivo. Solo la tiene si el día es inhábil en el calendario de la sede.
- **Papel u oficina de registro**: se aplica el 30.6. El día es inhábil si lo es en el
  municipio o en la CA de residencia del interesado **o** en la sede del órgano, así que
  el festivo del domicilio **sí** prorroga el plazo.
- En `core/plazos.py`, `es_inhabil(fecha, canal)`: si el canal es `electronico`, usar el
  calendario de la sede; si es `presencial`, la unión de los calendarios del domicilio y
  de la sede. Los calendarios (nacional, IB, local) vienen del BOE y del BOIB (30.7).

**Fundamento.**
- LPAC 30.6: «Cuando un día fuese hábil en el municipio o Comunidad Autónoma en que
  residiese el interesado, e inhábil en la sede del órgano administrativo, o a la inversa,
  se considerará inhábil en todo caso».
- LPAC 31.3: la sede electrónica determinará los días inhábiles «atendiendo al ámbito
  territorial en el que ejerce sus competencias el titular de aquélla y al calendario
  previsto en el artículo 30.7 […]. Este será el único calendario de días inhábiles que se
  aplicará a efectos del cómputo de plazos en los registros electrónicos, sin que resulte
  de aplicación a los mismos lo dispuesto en el artículo 30.6».
- LPAC 30.7: el calendario autonómico «comprenderá los días inhábiles de las Entidades
  Locales correspondientes a su ámbito territorial».

**Fuente.** LPAC arts. 30.6, 30.7 y 31.3. Consultado 2026-09-23.

**Certeza.** `A` para el registro electrónico (lo dice literalmente el 31.3). `B` para el
papel. El 30.6 es literal, pero no está claro si se aplica igual cuando se presenta en una
oficina de otra Administración o en Correos (16.4 LPAC), ni cómo se cuenta en la práctica.
Falta además concretar qué calendario publica cada sede: el Ajuntament de Palma y la DGT
(sede estatal, cuyo ámbito territorial es todo el Estado).

**Qué queda pendiente.** Obtener el calendario de días inhábiles publicado en la sede
electrónica del Ajuntament de Palma y el de la AGE (resolución anual en el BOE) para
saber qué festivos locales o autonómicos incluye cada uno. palma.cat está bloqueado, y
hay que buscar en BOE y BOIB la publicación del calendario. Buscar en CENDOJ doctrina
del TS sobre el 31.3 frente al 30.6.

**Recomendación para ggLaw.** Recomendar siempre la presentación electrónica y calcular
el vencimiento **ignorando el festivo del domicilio**. Si el usuario solo puede presentar
en papel, mencionar que un festivo local de su domicilio podría prorrogar el plazo, sin
contar con ello para fijar la fecha límite.

---

## Dudas 9-16: caducidad, prescripción, firmeza, notificaciones, pago reducido y recursos

### Duda 9. Qué es la «iniciación» a efectos de la caducidad de un año (112.3 LSV) y qué hay que hacer dentro del año

**Respuesta propuesta.**
- **Denuncia notificada en el acto**: la iniciación es la propia denuncia (86.2 LSV). El año
  corre desde ese día.
- **Denuncia no notificada en el acto** (radar o captación por imagen, estacionamiento sin
  conductor, 89.2 LSV): la LSV no dice qué acto inicia. La doctrina legal del TS de 2000
  (sobre el art. 16 RPST) toma como fecha de iniciación la de la **incoación por el órgano
  competente una vez conocida la identidad del infractor**, y no la de la denuncia del agente.
  La LPAC supletoria apunta en la misma dirección: el plazo corre «desde la fecha del acuerdo
  de iniciación» (21.3.a). Si el expediente no tiene un acuerdo de incoación separado, la
  fecha más segura es la de la **notificación de la denuncia**, que hace de acuerdo de
  iniciación.
- **Identificación de otro conductor** (93.1, párr. 2): la LSV dice que contra el
  identificado «se iniciará el procedimiento sancionador». Es un procedimiento nuevo, y su año
  empieza con la incoación frente al identificado, no con la denuncia inicial al titular.
- **Qué debe ocurrir dentro del año.** El 112.3 LSV exige que se haya «producido» la
  resolución. El RPST (15.1) y la LPAC supletoria (21.2 y 25.1) exigen además que se
  **notifique**. Si se aplica la LPAC, basta un **intento de notificación acreditado** con el
  texto íntegro (40.4), o la puesta a disposición electrónica (43.3). El intento cuenta en la
  fecha en que se hizo, no cuando vuelve el envío (doctrina del TS de 2003, rectificada en
  2013). No hay jurisprudencia leída que diga cuál de las dos lecturas rige hoy en tráfico.
- **Caso del 95.4 LSV** (la denuncia vale como resolución si no se alega ni se paga): el
  procedimiento termina solo, al día siguiente del vencimiento de los 20 días naturales
  (87.3.e). La caducidad solo es posible si ese día llega más de un año después de la
  iniciación. Eso puede pasar cuando la incoación es muy anterior a la notificación de la
  denuncia (por ejemplo, una notificación por BOE tras intentos fallidos muy tardíos), o
  cuando la notificación de la denuncia fue defectuosa y el efecto del 95.4 nunca se produjo.

**Fundamento.**
- LSV 86.1: «El procedimiento sancionador se incoará de oficio por la autoridad competente
  que tenga noticia de los hechos». LSV 86.2: la denuncia del agente «notificada en el acto al
  denunciado, constituye el acto de iniciación del procedimiento sancionador, a todos los
  efectos».
- LSV 93.1, párr. 2: el titular debe identificar al conductor responsable, «contra el que se
  iniciará el procedimiento sancionador».
- LSV 112.3: «Si no se hubiera producido la resolución sancionadora transcurrido un año desde
  la iniciación del procedimiento, se producirá su caducidad y se procederá al archivo de las
  actuaciones».
- RPST 15.1: «La resolución habrá de notificarse en el plazo de un año desde que se inició el
  procedimiento». RPST 16: «Si no hubiera recaído resolución sancionadora transcurrido un año
  desde la iniciación del procedimiento».
- LPAC 21.2: «El plazo máximo en el que debe notificarse la resolución expresa será el fijado
  por la norma reguladora del correspondiente procedimiento». LPAC 21.3.a: «En los
  procedimientos iniciados de oficio, desde la fecha del acuerdo de iniciación». LPAC 25.1:
  caducidad por «el vencimiento del plazo máximo establecido sin que se haya dictado y
  notificado resolución expresa».
- LPAC 40.4: «será suficiente la notificación que contenga, cuando menos, el texto íntegro de
  la resolución, así como el intento de notificación debidamente acreditado». LPAC 43.3: se
  cumple el 40.4 «con la puesta a disposición de la notificación en la sede electrónica […] o
  en la dirección electrónica habilitada única».
- LSV 87.3.e: la denuncia notificada en el acto debe indicar «que el procedimiento se tendrá
  por concluido el día siguiente a la finalización de dicho plazo, conforme se establece en el
  artículo 95.4».
- Jurisprudencia leída en fuente primaria (fallos publicados en el BOE):
  - **STS (Sala Tercera, Sección Cuarta) de 15/11/2000**, recurso de casación en interés de
    la ley 4041/1999. BOE núm. 25, de 29/01/2001, BOE-A-2001-2011.
    <https://www.boe.es/buscar/doc.php?id=BOE-A-2001-2011>. ECLI: no figura en el BOE.
    *Resumen propio:* doctrina legal sobre el art. 16 RPST. Cuando el infractor no pudo ser
    notificado en el acto, la caducidad se cuenta desde la incoación por el órgano
    competente, una vez conocida su identidad. No se cuenta desde la fecha de la denuncia
    del agente.
  - **STS (Sala Tercera, Sección Cuarta) de 03/06/2008**, recurso de casación en interés de
    la ley 35/2007. BOE núm. 175, de 21/07/2008, BOE-A-2008-12489.
    <https://www.boe.es/buscar/doc.php?id=BOE-A-2008-12489>. ECLI: no figura en el BOE.
    *Resumen propio:* doctrina legal sobre el art. 81 del RDL 339/1990 (redacción de la
    Ley 19/2001). En tráfico hay caducidad si no ha recaído resolución sancionadora al año de
    la iniciación. El fallo publicado no aclara si hace falta notificarla en ese año.
  - SSTS de 17/11/2003 (BOE-A-2004-198) y de 03/12/2013 (BOE-A-2014-291), ya documentadas en
    `knowledge/ley-39-2015-notificaciones-recursos.md`. Para cumplir el plazo máximo basta un
    intento de notificación con garantías y acreditado. El intento culmina en la fecha en
    que se hizo.

**Fuente.** LSV arts. 86, 87, 89, 93, 95 y 112; RPST arts. 15 y 16; LPAC arts. 21, 25, 40 y
43 (URLs de las abreviaturas); BOE-A-2001-2011; BOE-A-2008-12489; BOE-A-2004-198;
BOE-A-2014-291. El panel «Jurisprudencia» de boe.es no vincula ninguna sentencia a los
arts. 86, 89 ni 112 LSV. El número del precedente (art. 92.3 del RDL 339/1990 en la redacción
de la Ley 18/2009) se ha comprobado en la Ley 18/2009, art. único (BOE-A-2009-18732).
Consultado 2026-09-23.

**Certeza.**
- `A`: la denuncia notificada en el acto inicia el procedimiento (86.2), y el identificado
  tiene su propio procedimiento (93.1).
- `B`: denuncia no notificada en el acto. La doctrina de 2000 interpreta el RPST, anterior a
  la LSV vigente; el 21.3.a LPAC la respalda.
- `C`: si basta con dictar la resolución dentro del año (lectura literal del 112.3) o hace
  falta notificarla o intentarlo (15.1 RPST, 21 y 25 LPAC). Falta la jurisprudencia del TS
  posterior a 2010 sobre el 112.3 LSV (o su precedente, el art. 92.3 del RDL 339/1990 tras
  la Ley 18/2009), que no se puede leer en CENDOJ.
- `B`: en el caso del 95.4, la caducidad solo es posible en los supuestos descritos.

**Qué queda pendiente.**
- TODO(juridico): ¿exige el TS, con la LSV vigente, que la resolución sancionadora se
  notifique (o se intente notificar) dentro del año del 112.3, o basta con dictarla? Fuente:
  CENDOJ (Sala Tercera; buscar «112.3», «caducidad», «producido la resolución», «tráfico»).
- TODO(juridico): en radar y estacionamiento sin conductor, si el expediente no tiene acuerdo
  de incoación separado, ¿cuenta la fecha de la denuncia del agente, la de la resolución de
  incoación o la de la notificación? ¿Sigue vigente la doctrina legal de 15/11/2000 con la
  LSV actual? Fuente: CENDOJ.
- TODO(juridico): ¿interrumpe o suspende el plazo de caducidad el tiempo que tarda el titular
  en identificar al conductor? El 112.3 solo prevé la suspensión por proceso penal.

**Recomendación para ggLaw.** Calcular la caducidad en tres niveles:
`caducado` (la **resolución** se dictó más de un año después de la iniciación, según la
fecha más tardía posible de iniciación); `posible` (dictada dentro del año, pero notificada,
o intentada, después); `no_caducado`. Como fecha de iniciación usar la **más tardía** de las
que consten (incoación o notificación de la denuncia), para no proponer un motivo que la
Administración pueda rebatir con una fecha anterior. En el caso del 95.4, solo marcar
`posible` si hay más de un año entre la incoación y el vencimiento de los 20 días.

---

### Duda 10. Qué interrumpe la prescripción de la infracción (112.2 LSV) y qué pasa tras la caducidad

**Respuesta propuesta.**
- **Qué interrumpe** (112.2 LSV, lista propia que prevalece sobre la LRJSP):
  1. Cualquier actuación administrativa **de la que tenga conocimiento el denunciado**.
  2. Las actuaciones para averiguar su identidad o domicilio **hechas con otras
     administraciones, instituciones u organismos**. Estas interrumpen aunque el denunciado
     no lo sepa. Por ejemplo, una consulta del Ayuntamiento al registro de la DGT. Una
     consulta de la DGT a su propio registro no es «con otras administraciones».
  3. La **notificación efectuada** conforme a los arts. 89, 90 y 91: en el acto, en DEV, en
     el domicilio o en el BOE.
- **Intento fallido de notificación.** Por sí solo no es una «notificación efectuada» ni una
  actuación conocida por el denunciado. Hay dos excepciones:
  - El **rechazo**, en el domicilio (90.3, párr. 3) o en la DEV a los 10 días naturales
    (90.2). La LSV lo da por «efectuado» y, por tanto, interrumpe.
  - Tras dos intentos fallidos en el domicilio, la notificación se completa en el **BOE** y
    se entiende practicada a los 20 días naturales de la publicación (91). No está claro si
    la interrupción se produce en la fecha de publicación o al cumplirse esos 20 días.
- **Publicación solo en TESTRA** (sin BOE): **no interrumpe** como notificación. El 112.2 solo
  cita los arts. 89, 90 y 91, y el TESTRA está en el 92, que lo define como «previo y
  facultativo» (ver duda 13).
- **«se paraliza durante más de un mes»**: si el procedimiento está parado más de un mes por
  causa no imputable al denunciado, la prescripción vuelve a correr. El 112.2 dice «se
  reanudará», y la LRJSP 30.2 «reiniciándose». No está claro si el nuevo plazo se cuenta desde
  la última actuación o desde que se cumple el mes de parálisis.
- **Una vez notificada la resolución**, deja de correr la prescripción de la infracción. La
  vía de recurso ya no cuenta para ella (doctrina legal del TS de 15/12/2004). Desde ese
  momento lo relevante es la prescripción de la **sanción** (duda 11).
- **Después de la caducidad**: por la LPAC supletoria (95.3), la caducidad no extingue por sí
  sola la acción, así que **cabe un procedimiento nuevo** si la infracción no ha prescrito.
  Pero el procedimiento caducado **no interrumpe** la prescripción, y en él hay que repetir
  alegaciones, prueba y audiencia. Con plazos de 3 y 6 meses (112.1) y una caducidad de un
  año, lo normal es que al caducar el procedimiento la infracción ya haya prescrito.
  Literalmente, tampoco interrumpen las notificaciones hechas dentro del procedimiento
  caducado, porque es el procedimiento entero el que «no interrumpirá».

**Fundamento.**
- LSV 112.2: «La prescripción se interrumpe por cualquier actuación administrativa de la que
  tenga conocimiento el denunciado o esté encaminada a averiguar su identidad o domicilio y
  se practique con otras administraciones, instituciones u organismos. También se interrumpe
  por la notificación efectuada de acuerdo con los artículos 89, 90 y 91». Párr. 2: «El plazo
  de prescripción se reanudará si el procedimiento se paraliza durante más de un mes por
  causa no imputable al denunciado».
- LSV 90.2, párr. 2: tras diez días naturales sin acceso «se entenderá que aquélla ha sido
  rechazada» y «se tendrá por efectuado el trámite, continuándose el procedimiento». LSV 90.3:
  tras el segundo intento, «Si tampoco fuera posible la entrega, se dará por cumplido el
  trámite, procediéndose a la publicación en el Boletín Oficial del Estado». Si rechaza:
  «teniéndose por efectuado el trámite y continuándose el procedimiento».
- LSV 91: «Transcurrido el período de veinte días naturales desde que la notificación se
  hubiese publicado en el BOE se entenderá que ésta ha sido practicada, dándose por cumplido
  dicho trámite». LSV 92.1: TESTRA «Con carácter previo y facultativo».
- LRJSP 30.2, párr. 2 (general, supletoria): interrumpe «la iniciación, con conocimiento del
  interesado, de un procedimiento administrativo de naturaleza sancionadora, reiniciándose el
  plazo de prescripción si el expediente sancionador estuviera paralizado durante más de un
  mes por causa no imputable al presunto responsable».
- LPAC 95.3: «La caducidad no producirá por sí sola la prescripción de las acciones del
  particular o de la Administración, pero los procedimientos caducados no interrumpirán el
  plazo de prescripción». «En todo caso, en el nuevo procedimiento deberán cumplimentarse los
  trámites de alegaciones, proposición de prueba y audiencia al interesado». LPAC 25.1.b: la
  resolución que declare la caducidad ordenará el archivo «con los efectos previstos en el
  artículo 95».
- Jurisprudencia leída en fuente primaria: **STS (Sala Tercera, Sección Quinta) de
  15/12/2004**, recurso de casación en interés de la ley 97/2002. BOE núm. 98, de 25/04/2005,
  BOE-A-2005-6615. <https://www.boe.es/buscar/doc.php?id=BOE-A-2005-6615>. ECLI: no figura en
  el BOE. *Resumen propio:* doctrina legal general, no específica de tráfico. El límite para
  ejercer la potestad sancionadora, y para la prescripción de la infracción, termina con la
  resolución sancionadora y su notificación. No se extiende a la vía de recurso.

**Fuente.** LSV arts. 90-92 y 112; LRJSP art. 30; LPAC arts. 25 y 95; BOE-A-2005-6615. El
precedente del 112.2 LSV es el art. 92.2 del RDL 339/1990 en la redacción de la Ley 18/2009
(comprobado en BOE-A-2009-18732, art. único). Consultado 2026-09-23.

**Certeza.**
- `A`: la lista del 112.2, incluido que el TESTRA no está entre los arts. 89-91. También el
  texto del 95.3 LPAC.
- `B`: que el rechazo interrumpe; que un intento fallido aislado no interrumpe; que el 95.3
  LPAC se aplica en tráfico (la LSV no regula los efectos de la caducidad); y que la vía de
  recurso no cuenta para la prescripción de la infracción (doctrina de 2004, general).
- `C`: la fecha exacta de la interrupción por BOE (publicación o día 20) y el día de
  reanudación tras la parálisis. Falta jurisprudencia del TS sobre el 112.2 LSV.

**Qué queda pendiente.**
- TODO(juridico): en la notificación por BOE (91 LSV), ¿la prescripción se interrumpe en la
  fecha de publicación o al cumplirse los 20 días naturales? Fuente: CENDOJ.
- TODO(juridico): tras más de un mes de parálisis, ¿el nuevo plazo completo se cuenta desde la
  última actuación interruptiva o desde el día en que se cumple el mes? Fuente: CENDOJ
  (jurisprudencia sobre «se reanudará», 112.2 LSV y su precedente, el art. 92.2 del
  RDL 339/1990).
- TODO(juridico): ¿las actuaciones de averiguación del domicilio hechas **antes** de la
  incoación forman parte del «procedimiento caducado» a efectos del 95.3 LPAC? Fuente: CENDOJ.
- TODO(juridico): ¿cuenta como «otras administraciones» una consulta de un Ayuntamiento al
  Registro de Vehículos de la DGT o al Padrón (41.4 LPAC)? Fuente: CENDOJ.

**Recomendación para ggLaw.** Pedir al usuario la lista de actuaciones con fecha (denuncia,
intentos, publicaciones, requerimientos) y aplicar las tres zonas de la duda 7. Tratar como
**no interruptivos** el intento fallido aislado y la publicación solo en TESTRA, y como
`dudosa` la ventana entre la publicación en el BOE y el día 20. No proponer como motivo sólido
la prescripción por parálisis salvo que la haya con cualquiera de los dos cómputos.

---

### Duda 11. Firmeza frente a ejecutividad de la sanción; día inicial del 110.1 y del 112.4 LSV

**Respuesta propuesta.**
- La LSV separa dos cosas:
  - **Ejecutividad**: la sanción se puede ejecutar desde el día siguiente a la notificación
    de la resolución (96.1), o desde el día siguiente a los 30 días naturales en el caso del
    95.4 (95.5), aunque quepa reposición y aunque esta se interponga (96.3). Esta regla
    especial desplaza a la LPAC (90.3 y 98.1.b), que en los sancionadores retrasa la
    ejecutividad mientras quepa cualquier recurso administrativo, incluida la reposición. La
    propia LPAC admite la excepción: «Una disposición establezca lo contrario» (98.1.c).
  - **Firmeza en vía administrativa**: la exigen el 108 (para ejecutar), el 110.1 (15 días
    naturales para pagar), el 112.4 (inicio de los 4 años de prescripción de la multa) y el
    87.4 (puntos). La LSV no la define, salvo en el pago reducido (94.f: firme desde el pago).
- **¿Cuándo es firme una sanción recurrible en reposición?** Hay dos lecturas:
  - **(a) Al notificarse.** La resolución «pondrá fin a la vía administrativa» y produce
    «plenos efectos» desde el día siguiente (96.1). La reposición es potestativa, y el 94
    asocia agotamiento de la vía y firmeza. El Ayuntamiento de Palma aplica en la práctica
    los 15 días del 110.1 desde el día siguiente a la notificación de la resolución (ver
    Fuente).
  - **(b) Cuando ya no cabe recurso administrativo.** Es decir, al vencer el mes del 96.2 sin
    reposición o, si se interpuso, al resolverse de forma expresa o por silencio. Es la noción
    clásica de «firme», coherente con el 98.1.b LPAC y con la doctrina legal del TS de 2008
    (con alzada pendiente, la sanción no es firme ni ejecutiva).
- **Consecuencias**:
  - 15 días del 110.1: con (a), desde el día siguiente a la notificación de la resolución;
    con (b), desde el día siguiente a la firmeza.
  - 4 años del 112.4: con (a), desde el día siguiente a la notificación; con (b), desde el
    día siguiente al fin del mes para recurrir o a la resolución de la reposición.
- **Reposición interpuesta y no resuelta**: con la STS de 2008 (alzada), la sanción no sería
  firme y los 4 años no empezarían a correr mientras no se resuelva. El art. 30.3, párr. 3,
  LRJSP lo cambió para la **alzada**: el plazo corre desde el día siguiente al fin del plazo
  para resolver. **Lo que depende de la STS de 15/10/2020 (rec. 7337/2019)**, que no se ha
  podido verificar (duda 20), es si esa regla se extiende a la **reposición** de tráfico. Si se extiende,
  los 4 años del 112.4 empiezan el día siguiente al mes del 96.5. Si no, rige la doctrina de
  2008 y la prescripción no corre mientras la reposición esté sin resolver.

**Fundamento.**
- LSV 96.1: «La resolución sancionadora pondrá fin a la vía administrativa y la sanción se
  podrá ejecutar desde el día siguiente a aquel en que se notifique al interesado, produciendo
  plenos efectos, o, en su caso, una vez haya transcurrido el plazo indicado en el artículo
  95.4». LSV 96.3: «La interposición del recurso de reposición no suspenderá la ejecución del
  acto impugnado ni la de la sanción». LSV 96.5: la reposición «se entenderá desestimado si no
  recae resolución expresa en el plazo de un mes».
- LSV 95.5: «La terminación del procedimiento pone fin a la vía administrativa y la sanción se
  podrá ejecutar desde el día siguiente al transcurso de los treinta días antes indicados».
- LSV 94.f: «La firmeza de la sanción en la vía administrativa desde el momento del pago,
  produciendo plenos efectos desde el día siguiente».
- LSV 108: «Una vez firme la sanción en vía administrativa, se procederá a su ejecución
  conforme a lo previsto en esta ley». LSV 110.1: «Una vez firme la sanción, el interesado
  dispondrá de un plazo final de quince días naturales para el pago de la multa». LSV 112.4:
  «computados desde el día siguiente a aquel en que adquiera firmeza la sanción en vía
  administrativa». LSV 87.4: «cuando la sanción sea firme en vía administrativa».
- LPAC 90.3: «La resolución que ponga fin al procedimiento será ejecutiva cuando no quepa
  contra ella ningún recurso ordinario en vía administrativa». LPAC 98.1.b: no es
  inmediatamente ejecutiva la resolución sancionadora «contra la que quepa algún recurso en
  vía administrativa, incluido el potestativo de reposición»; 98.1.c: salvo que «Una
  disposición establezca lo contrario». LPAC 117.1: la interposición de cualquier recurso «no
  suspenderá la ejecución del acto impugnado». LPAC 124.1: pasado el mes, «únicamente podrá
  interponerse recurso contencioso-administrativo».
- LRJSP 30.3, párr. 1: la prescripción de la sanción corre «desde el día siguiente a aquel en
  que sea ejecutable la resolución por la que se impone la sanción o haya transcurrido el
  plazo para recurrirla». Párr. 3: «En el caso de desestimación presunta del recurso de alzada
  […] desde el día siguiente a aquel en que finalice el plazo legalmente previsto para la
  resolución de dicho recurso».
- RPST 20.1 (desplazado en lo que contradiga a la LSV): «No se podrá proceder a la ejecución
  de las sanciones […] que no hayan adquirido firmeza en vía administrativa».
- Jurisprudencia: **STS (Sala Tercera, Sección Quinta) de 22/09/2008**, recurso de casación en
  interés de la ley 69/2005, BOE-A-2008-18350, **leída en fuente primaria** (ya documentada en
  `knowledge/ley-39-2015-notificaciones-recursos.md`). **Pista no verificada**: STS de
  15/10/2020, rec. 7337/2019 (no verificable desde el entorno; ver duda 20 y la revisión de
  pistas al final de este fichero).
- Práctica administrativa (no normativa): anuncios del Servicio de Multas del Ayuntamiento de
  Palma en el Suplemento de Notificaciones del BOE núm. 235, de 23/09/2026. Resumen propio:
  la notificación de la resolución sancionadora informa de que se puede pagar en 15 días
  naturales desde el día siguiente a la notificación, de que la resolución pone fin a la vía
  administrativa y de que cabe reposición en un mes. (Esos anuncios contienen datos
  personales: no copiar nada de ellos al repositorio.)

**Fuente.** LSV arts. 87, 94-96, 108, 110 y 112; LPAC arts. 90, 98, 117 y 124 (el art. 98 se ha
añadido a `knowledge/ley-39-2015-notificaciones-recursos.md`); LRJSP art. 30; RPST art. 20;
BOE-A-2008-18350. Consultado 2026-09-23.

**Certeza.**
- `A`: el texto de cada precepto, y que la LSV hace ejecutiva la sanción desde la
  notificación aunque quepa reposición (96.1 y 96.3).
- `C`: qué significa «firme en vía administrativa» en el 108, el 110.1 y el 112.4 para una
  sanción recurrible en reposición. Hay dos lecturas razonables y no se ha podido leer
  jurisprudencia del TS sobre la LSV.
- `C`: la prescripción de la sanción con la reposición pendiente depende de la STS de
  15/10/2020, que no se ha podido leer (duda 20).

**Qué queda pendiente.**
- TODO(juridico): ¿cuándo adquiere firmeza en vía administrativa, a efectos de los arts. 108,
  110.1 y 112.4 LSV, una sanción de tráfico que pone fin a la vía (96.1) pero admite
  reposición potestativa (96.2)? Fuente: CENDOJ (Sala Tercera; «firmeza», «112.4», «110.1»,
  «tráfico»).
- TODO(juridico): ¿cómo encaja el 108 («Una vez firme […] se procederá a su ejecución») con el
  96.1, que permite ejecutar desde la notificación? ¿El apremio exige firmeza (lectura b) o
  basta la ejecutividad?
- TODO(juridico): leer la STS de 15/10/2020 (rec. 7337/2019) y decidir si su criterio se
  aplica a la reposición del 96 LSV (duda 20: no verificable desde el entorno).

**Recomendación para ggLaw.** Usar siempre la lectura **menos favorable al usuario** para
cada efecto. Para **pagar** (110.1 y evitar el apremio), avisar de que el plazo de 15 días
naturales puede empezar al día siguiente de la notificación de la resolución. Para
**alegar la prescripción de la sanción** (112.4), contar los 4 años desde la fecha más tardía
posible, y marcar `dudosa` toda sanción con reposición pendiente hasta que se valide la
STS de 2020.

---

### Duda 12. ¿Está obligada una persona física a la DEV? Efecto en los plazos; ¿notifica Palma por DEV?

**Respuesta propuesta.**
- **Persona física: no está obligada.** La LSV solo le asigna DEV «cuando lo solicite
  voluntariamente» (60.5). La regla general de la LPAC es la misma: la persona física elige
  (14.1), salvo que un reglamento la obligue para un colectivo concreto (14.3 y 41.1). No se
  ha encontrado ninguna norma que imponga la DEV a las personas físicas. Las personas
  jurídicas sí están obligadas a relacionarse electrónicamente (14.2.a LPAC). Por eso la DGT,
  según su sede, les asigna la DEV de oficio y desde el 01/11/2022 ya no les notifica en
  papel.
- **Norma específica de la DEV**: no se ha localizado en el BOE ninguna orden ministerial ni
  resolución que regule la DEV con carácter general. La búsqueda por título solo devuelve la
  Resolución de la DGT de 17/08/2023 (BOE-A-2023-19016), sobre colaboración social
  (actuación mediante representantes) en el ámbito de la DEV. La DF 3ª LSV habilita al Ministro del Interior para el TESTRA, no
  para la DEV. La sede de la DGT cita como normativa reguladora de la DEV solo la LSV y la
  LPAC.
- **Efecto en los plazos** (si el interesado tiene DEV):
  - Si **accede**, la notificación se practica en ese momento (90.2 LSV y 43.2 LPAC).
  - Si **no accede** en 10 días naturales, se entiende **rechazada** y «se tendrá por
    efectuado el trámite» (90.2 LSV). La LPAC dice lo mismo (43.2).
  - Los 20 días naturales del 93-95 empiezan el día siguiente al de la notificación
    (acceso o rechazo), por el 30.3 LPAC (duda 5). La DGT informa en su sede de que, cuando
    la notificación «caduca» a los 10 días, se inicia el plazo de 20 días (criterio
    administrativo, no normativo).
  - El 90.2 LSV tiene una salvedad que el 43.2 LPAC no tiene: no hay rechazo si se comprueba
    «la imposibilidad técnica o material del acceso».
- **Límite constitucional**: el TC ha anulado sanciones notificadas electrónicamente por
  rechazo presunto cuando el interesado no llegó a conocerlas (por ejemplo, porque no recibió
  el aviso) y la Administración, sabiendo que no se accedía, no intentó otra vía (STC 84/2022,
  sanción de transportes). Es un argumento de defensa posible frente a un rechazo tácito en
  DEV.
- **¿Notifica Palma por DEV?** **No se ha podido verificar.**
  - La lista oficial de emisores integrados en la DEV (sedeapl.dgt.gob.es) está bloqueada
    desde el entorno, y palma.cat también.
  - Hay indicios en fuente oficial de que Palma notifica en papel y, si falla, por edictos:
    se incorporó al TESTRA el 23/01/2013 (Resolución de la DGT de 19/02/2013) y hoy publica
    anuncios de notificación de denuncias y sanciones de tráfico en el Suplemento de
    Notificaciones del BOE (visto el 23/09/2026).
  - La DT 2ª LSV solo obligaba a los ayuntamientos a notificar en la DEV antes del
    25/05/2016 «siempre que lo permitan sus disponibilidades presupuestarias y sus medios
    técnicos».
  - Según la DGT, un ayuntamiento que ya es emisor en la DEV debe notificar solo por la DEV a
    quien la tenga. Es coherente con el 90.1 LSV.

**Fundamento.**
- LSV 60.3: la JCT asignará DEV «a todo titular de un permiso o licencia de conducción o del
  permiso de circulación de un vehículo». LSV 60.5: «si el titular de la autorización es una
  persona física sólo se le asignará una Dirección Electrónica Vial (DEV) cuando lo solicite
  voluntariamente. En este caso, todas las notificaciones se practicarán en la Dirección
  Electrónica Vial conforme se establece en el artículo 90».
- LSV 90.1: las Administraciones «notificarán las denuncias que no se entreguen en el acto y
  las demás notificaciones a que dé lugar el procedimiento sancionador en la Dirección
  Electrónica Vial (DEV)». «En el caso de que el denunciado no la tuviese, la notificación se
  efectuará en el domicilio que expresamente hubiese indicado para el procedimiento».
- LSV 90.2: acceso al contenido, «momento a partir del cual la notificación se entenderá
  practicada a todos los efectos legales». «Si existiendo constancia de la recepción de la
  notificación en la Dirección Electrónica Vial (DEV), transcurrieran diez días naturales sin
  que se acceda a su contenido, se entenderá que aquélla ha sido rechazada, salvo que de
  oficio o a instancia del destinatario se compruebe la imposibilidad técnica o material del
  acceso».
- LSV DT 2ª: «Las administraciones locales practicarán las notificaciones en la Dirección
  Electrónica Vial (DEV) antes del 25 de mayo de 2016, siempre que lo permitan sus
  disponibilidades presupuestarias y sus medios técnicos». LSV DA 11ª: la DEV «podrá
  integrarse o coordinarse con la Dirección Electrónica Habilitada (DEH)».
- LPAC 14.1: «Las personas físicas podrán elegir en todo momento si se comunican con las
  Administraciones Públicas […] a través de medios electrónicos o no, salvo que estén
  obligadas». LPAC 14.2.a: obligadas «Las personas jurídicas». LPAC 14.3: los reglamentos
  pueden imponer la obligación «para ciertos colectivos de personas físicas».
- LPAC 43.2: «Las notificaciones por medios electrónicos se entenderán practicadas en el
  momento en que se produzca el acceso a su contenido». «Cuando la notificación por medios
  electrónicos sea de carácter obligatorio, o haya sido expresamente elegida por el
  interesado, se entenderá rechazada cuando hayan transcurrido diez días naturales desde la
  puesta a disposición de la notificación sin que se acceda a su contenido».
- LPAC 41.6: el aviso al correo o al móvil es obligatorio, pero «La falta de práctica de este
  aviso no impedirá que la notificación sea considerada plenamente válida». LPAC 41.7: si se
  notifica por varios cauces, «se tomará como fecha de notificación la de aquélla que se
  hubiera producido en primer lugar».
- Jurisprudencia leída en fuente primaria (hj.tribunalconstitucional.es):
  - **STC 84/2022, de 27 de junio** (Sala Primera), recurso de amparo 83-2021.
    ECLI:ES:TC:2022:84. BOE núm. 181, de 29/07/2022, BOE-A-2022-12748.
    <https://hj.tribunalconstitucional.es/es/Resolucion/Show/29026>. *Resumen propio:*
    sanción de transportes. La notificación en la DEH se tuvo por rechazada a los diez días,
    pero el aviso se envió a un correo mal transcrito y el interesado no supo nada. El TC
    aprecia vulneración del art. 24.2 CE: ante comunicaciones electrónicas infructuosas, la
    Administración debía haber hecho algo más para que llegaran a su conocimiento. Anula la
    sanción.
  - **STC 147/2022, de 29 de noviembre** (Sala Primera), recurso de amparo 3209-2019.
    ECLI:ES:TC:2022:147. BOE núm. 5, de 06/01/2023, BOE-A-2023-460.
    <https://hj.tribunalconstitucional.es/es/Resolucion/Show/29153>. *Resumen propio:*
    liquidación tributaria a una sociedad obligada a la DEH. Las notificaciones electrónicas
    se tuvieron por rechazadas y la Agencia Tributaria sabía que no se accedía a ellas. El TC
    aplica la STC 84/2022, otorga el amparo (art. 24.1 CE) y retrotrae las actuaciones.
- Información oficial, no normativa: sede de la DGT, “Notificaciones electrónicas (Dirección
  Electrónica Vial)”, <https://sede.dgt.gob.es/es/multas/direccion-electronica-vial/>, y “Envío
  de notificaciones a través de la DEV”,
  <https://sede.dgt.gob.es/es/multas/tramites-para-administraciones/envio-de-notificaciones-a-la-dev/>.
  Resolución de la DGT de 19/02/2013, BOE-A-2013-2095 (Palma incorporada al TESTRA el
  23/01/2013).

**Fuente.** LSV arts. 60 y 90, DT 2ª, DA 11ª, DF 3ª; LPAC arts. 14, 41 y 43;
BOE-A-2023-19016; BOE-A-2013-2095; SSTC 84/2022 y 147/2022; sede de la DGT (URLs arriba).
Consultado 2026-09-23. No se ha podido consultar: la lista de emisores de la DEV
(sedeapl.dgt.gob.es, bloqueado por el proxy) ni la sede de Palma (palma.cat, palma.es y
sede.palma.cat, bloqueados).

**Certeza.**
- `A`: la persona física no está obligada (60.5 LSV y 14.1 LPAC). También el efecto del
  acceso y del rechazo a los 10 días naturales (90.2 LSV y 43.2 LPAC).
- `B`: que no existe una orden específica de la DEV (búsqueda solo por títulos en el BOE); y
  que el plazo de 20 días empieza el día siguiente al rechazo.
- `C`: el día exacto en que se entiende rechazada (si el día de la puesta a disposición
  cuenta o no) y si Palma notifica hoy por DEV.

**Qué queda pendiente.**
- TODO(juridico): ¿figura el Ajuntament de Palma (o la ATIB en su nombre) en la lista de
  emisores integrados en la DEV? Fuente: <https://sedeapl.dgt.gob.es/WEB_NTRA_CONSULTA_NO_CERT/busquedaEntidadesIdiomaPostback.faces?idioma=es>
  (consultarla desde un navegador fuera del entorno) o la sede de Palma.
- TODO(juridico): cómputo exacto de los 10 días naturales del 90.2 LSV: ¿desde el día
  siguiente a la puesta a disposición (30.3 LPAC) o de hora a hora? ¿Qué día se entiende
  practicada la notificación rechazada? Fuente: CENDOJ; criterios de la DGT.
- TODO(juridico): búsqueda de texto completo en el BOE (no solo por título) de una orden o
  resolución de desarrollo de la DEV posterior a 2010.
- TODO(juridico): ¿se aplica la doctrina de las SSTC 84/2022 y 147/2022 a una persona física
  que se dio de alta voluntariamente en la DEV y no accede? Fuente: hj.tribunalconstitucional.es.

**Recomendación para ggLaw.** Preguntar siempre al usuario si tiene DEV. Si la tiene y no
sabe si accedió ni cuándo, tomar como fecha de notificación la **más temprana posible**, que
es el día de la puesta a disposición (recomendación de la duda 5). Usar la fecha del rechazo
(puesta a disposición + 10 días naturales) solo si consta que no accedió. Si la
notificación se tuvo por rechazada y el usuario no recibió el aviso, proponer como motivo
«posible» la indefensión (SSTC 84/2022 y 147/2022), nunca como motivo cierto.

---

### Duda 13. TESTRA frente al BOE y al Tablón Edictal Único; orden del TESTRA; vigencia de la doctrina del TC sobre edictos

**Respuesta propuesta.**
- **Hoy la notificación edictal válida en tráfico es la del BOE** (Suplemento de
  Notificaciones, que es el «Tablón Edictal Único»). Se entiende practicada a los 20 días
  naturales de su publicación (91 LSV). El TESTRA es solo **previo y facultativo** (92.1 LSV).
  Una publicación **solo en TESTRA no notifica** ni interrumpe la prescripción (duda 10).
- **Evolución** (comprobada en el BOE):
  - La Ley 18/2009 creó el TESTRA como medio único que sustituía al BOE. La Orden
    INT/3022/2010 lo desarrolló, y la Ley 6/2014 aún lo mantenía como medio de notificación
    (art. 78.1 del RDL 339/1990).
  - La Ley 15/2014 añadió a la Ley 30/1992 la DA 21ª: en los procedimientos con normativa
    específica, la notificación edictal se hace «en todo caso» en el BOE, y la forma
    específica (aquí, el TESTRA) queda como previa y facultativa. Se aplica desde el
    01/06/2015.
  - El RDL 6/2015 (arts. 91 y 92) y la LPAC (art. 44) recogen ya esa regla.
  - La DA 21ª **no está en la LPAC** (la LPAC solo tiene DA 1ª a 9ª). Estaba en la Ley 30/1992,
    que la LPAC derogó (DD única 2.a). Hoy la regla está en el art. 44 LPAC y en los arts. 91 y
    92 LSV.
- **Orden del TESTRA**: Orden INT/3022/2010, de 23 de noviembre (BOE-A-2010-18102). Según la
  API del BOE, no está derogada (`estatus_derogacion: N`) ni tiene modificaciones registradas.
  Pero su premisa (el TESTRA como «medio oficial» que sustituye al BOE; notificación
  practicada a los 20 días en el TESTRA, art. 10.4) choca con el 91 LSV vigente, que tiene
  rango de ley. En ese punto la orden está desplazada. Transcrita en
  `knowledge/orden-int-3022-2010-testra.md`.
- **Práctica**: según la sede de la DGT, desde el 01/01/2022 el TESTRA ya no sirve de
  intermediario hacia el TEU y los emisores deben enviar los anuncios directamente al BOE.
  La DGT lo describe como un servicio a extinguir. Palma se incorporó al TESTRA el 23/01/2013
  y hoy publica en el Suplemento de Notificaciones del BOE citando el art. 44 LPAC.
- **Doctrina del TC sobre edictos**: **sigue vigente**. No se ha encontrado ninguna resolución
  posterior a 2019 que la cambie. El TC la ha aplicado de forma reiterada entre 2020 y 2025,
  aunque en procesos judiciales (desahucios, ejecuciones hipotecarias). En el ámbito
  administrativo, las SSTC 84/2022 y 147/2022 extienden la exigencia de diligencia a las
  notificaciones electrónicas fallidas (duda 12). No se ha encontrado ninguna STC posterior a
  2019 sobre tráfico, TESTRA o TEU. Se han verificado los ECLI de las SSTC 219/2007
  (ECLI:ES:TC:2007:219) y 128/2008 (ECLI:ES:TC:2008:128).

**Fundamento.**
- LSV 91: las notificaciones que no puedan hacerse en la DEV ni en el domicilio «se
  practicarán en el “Boletín Oficial del Estado” (BOE). Transcurrido el período de veinte días
  naturales desde que la notificación se hubiese publicado en el BOE se entenderá que ésta ha
  sido practicada». LSV 92.1: «Con carácter previo y facultativo, las notificaciones a que se
  refiere el artículo anterior podrán practicarse también en el Tablón Edictal de Sanciones de
  Tráfico (TESTRA)».
- LSV DA 11ª: el TESTRA «podrá integrarse en el Tablón Edictal Único cuando razones
  justificadas de eficiencia en la prestación del servicio así lo aconsejen». LSV DF 3ª.b:
  habilita al Ministro del Interior para determinar «las condiciones para practicar la
  notificación en el TESTRA».
- LPAC 44: «la notificación se hará por medio de un anuncio publicado en el “Boletín Oficial
  del Estado”». «Asimismo, previamente y con carácter facultativo, las Administraciones podrán
  publicar un anuncio en el boletín oficial de la Comunidad Autónoma o de la Provincia, en el
  tablón de edictos del Ayuntamiento». Otras formas complementarias «no excluirán la
  obligación de publicar el correspondiente anuncio en el “Boletín Oficial del Estado”».
  LPAC 41.4: para iniciar el procedimiento, la Administración puede consultar al INE «los datos
  sobre el domicilio del interesado recogidos en el Padrón Municipal».
- Ley 15/2014, art. 25.Dos (DA 21ª.2 de la Ley 30/1992): «En aquellos procedimientos
  administrativos que cuenten con normativa específica, de concurrir los supuestos previstos
  en el artículo 59.5 de esta Ley, la práctica de la notificación se hará, en todo caso,
  mediante un anuncio publicado en el “Boletín Oficial del Estado”, sin perjuicio de que
  previamente y con carácter facultativo pueda realizarse en la forma prevista por dicha
  normativa específica». Art. 25.Tres (DT 3ª de la Ley 30/1992): «resultará de aplicación a
  partir del 1 de junio de 2015». LPAC DD única 2.a: deroga la «Ley 30/1992, de 26 de
  noviembre».
- Ley 6/2014, art. único (art. 78.1 del RDL 339/1990, redacción de 2014, hoy derogado): las
  notificaciones fallidas «se practicarán en el Tablón Edictal de Sanciones de Tráfico
  (TESTRA)».
- RD 181/2008 (ordenación del BOE), art. 7.2.a: existe como suplemento independiente «El
  Suplemento de notificaciones». Art. 8.7: «En el Suplemento de notificaciones se insertarán
  los anuncios de notificación».
- Orden INT/3022/2010, art. 1.1: el TESTRA «como medio oficial de publicación a través de
  edictos». Art. 10.4: «Finalizado el plazo de publicación o el período de vigencia, la
  notificación se tendrá por practicada y podrá continuarse el procedimiento». DT única: los
  entes locales «vendrán obligadas a efectuar la publicación en el Tablón Edictal de Sanciones
  de Tráfico de dichas notificaciones a partir del 25 de mayo de 2012».
- Jurisprudencia del TC leída en fuente primaria: SSTC 219/2007, 128/2008 y 82/2019 (ya en
  `knowledge/`), y SSTC 84/2022 y 147/2022 (duda 12). Vistos solo el encabezamiento y el
  sumario del BOE, como muestra de que la doctrina se sigue aplicando en procesos judiciales:
  STC 62/2020 (ECLI:ES:TC:2020:62) y STC 145/2021 (ECLI:ES:TC:2021:145).
- Información oficial, no normativa: sede de la DGT, “Envío de edictos de sanciones a
  TESTRA/TEU” y “Consulta de sanciones publicadas en el tablón edictal del BOE (TEU)”
  (<https://sede.dgt.gob.es/es/multas/tramites-para-administraciones/envio-de-edictos-a-testra-teu/>,
  <https://sede.dgt.gob.es/es/multas/consulta-del-tablon-edictal-de-sanciones/>).
  Resolución de la DGT de 19/02/2013, BOE-A-2013-2095.

**Fuente.** LSV arts. 91 y 92, DA 11ª, DF 3ª; LPAC arts. 41, 44 y DD única; Ley 15/2014
(BOE-A-2014-9467) art. 25; Ley 6/2014 (BOE-A-2014-3715) art. único; RD 181/2008
(BOE-A-2008-2389) arts. 7 y 8; Orden INT/3022/2010 (BOE-A-2010-18102); BOE-A-2013-2095;
hj.tribunalconstitucional.es (SSTC citadas). Consultado 2026-09-23. La Ley 15/2014, la Ley 6/2014 y el
RD 181/2008 se han leído con `scripts/boe_fetch.py`, pero no se transcriben en `knowledge/`;
la Orden INT/3022/2010 está en `knowledge/orden-int-3022-2010-testra.md`.

**Certeza.**
- `A`: el BOE es obligatorio y el TESTRA facultativo (91 y 92 LSV, 44 LPAC); la LPAC no
  tiene DA 21ª; la Orden INT/3022/2010 consta como vigente en la API del BOE.
- `B`: que una publicación solo en TESTRA no notifica. Es la consecuencia del texto legal y de
  la jerarquía normativa, pero no se ha leído jurisprudencia sobre ello. También que la doctrina
  del TC sigue vigente: no se ha encontrado nada en contra, aunque la búsqueda en el buscador
  del TC no funcionó y se hizo por títulos del BOE y por búsqueda web.
- `C`: el efecto de una publicación hecha en TESTRA entre el 25/11/2010 y el 31/05/2015. Es
  derecho transitorio y solo afecta a sanciones antiguas.

**Qué queda pendiente.**
- TODO(juridico): **contradicción en fuentes oficiales.** La sede de la DGT dice que los
  organismos no incorporados al TEU seguirán notificando en boletines provinciales y
  tablones de edictos, y cita el art. 44 LPAC. Pero el art. 44 LPAC y el 91 LSV exigen el BOE
  y solo admiten los demás medios como previos y facultativos. Decidir si una notificación
  edictal de tráfico hecha solo en el BOIB o en el tablón municipal es nula. Fuente: CENDOJ.
- TODO(juridico): búsqueda completa (texto, no solo título) en hj.tribunalconstitucional.es de
  sentencias posteriores a 2019 sobre notificación edictal en sanciones de tráfico. El buscador
  del TC no respondió a consultas automáticas.
- TODO(juridico): ¿exige el TC o el TS, antes de publicar en el BOE, consultar el Padrón
  (41.4 LPAC) además del domicilio de la DGT (90.1 LSV)? Fuente: CENDOJ;
  hj.tribunalconstitucional.es.

**Recomendación para ggLaw.** Si el expediente solo muestra la publicación en TESTRA, en el
BOIB o en un tablón municipal, sin anuncio en el BOE, marcar `posible defecto de
notificación`. Si hubo BOE, contar los 20 días desde la publicación. Si el usuario acredita
un domicilio conocido por la Administración (Padrón, otros expedientes, el apremio notificado
en otro domicilio), proponer como motivo la doctrina de las SSTC 219/2007, 128/2008 y 82/2019.

---

### Duda 14. Pago con la reducción del 50 % y recurso posterior; pago tardío o parcial; importe graduado

**Respuesta propuesta.**
- **Reposición tras pagar: no cabe.** El pago reducido agota la vía administrativa y la
  sanción es recurrible **«únicamente»** ante lo contencioso-administrativo (94.d). Una
  reposición sería inadmisible por tratarse de un acto no susceptible de recurso (116.c LPAC).
  Además, las alegaciones presentadas después de pagar «se tendrán por no presentadas» (94.b).
- **Contencioso: sí cabe.** El plazo empieza el día siguiente al pago (94.e). La LSV no fija
  la duración, así que se aplican los **dos meses** del 46.1 LJCA contados desde ese día. El
  cómputo en meses y los días inhábiles procesales (agosto) están pendientes en el fichero de
  la LJCA. Hace falta abogado (23 LJCA; duda 1 del fichero de la LJCA).
- **Pago fuera de plazo**: si no se paga «en las condiciones indicadas» (dentro de los 20
  días naturales), se sigue el **procedimiento ordinario** (93.1, párr. 3). No hay reducción
  ni terminación por pago. La LSV no dice qué pasa con lo pagado tarde. El 85.2 LPAC (el pago
  voluntario antes de la resolución termina el procedimiento) podría aplicarse de forma
  supletoria, pero sin la reducción del 85.3, que la LSV desplaza.
- **Pago parcial**: el 94 exige el «pago voluntario de la multa» con la reducción. Un pago
  inferior al 50 % no parece cumplirlo y deja el asunto en el procedimiento ordinario.
- **Infracciones excluidas**: no hay pago reducido ni procedimiento abreviado para el
  77.h), j), n), ñ), o), p), q), r), s) y t) (93.2). Entre ellas, no identificar al conductor
  (77.j).
- **Importe graduado (81)**: la reducción se aplica al «importe de la sanción» (94.a). Como en
  el abreviado no hay resolución, ese importe es el de la sanción que figura en la denuncia
  (87.3.a: «la sanción que pueda corresponder»). Si la denuncia ya incluye el incremento de
  hasta el 30 % del art. 81, el 50 % se calcula sobre esa cifra. No consta ninguna norma que
  obligue a reducir sobre la cuantía sin graduar.
- **Relación con el 85 LPAC**: el 85.3 LPAC (reducciones de al menos el 20 %, condicionadas a
  renunciar a los recursos en vía administrativa) **no se aplica**, porque la LSV tiene su
  régimen propio (LPAC DA 1ª.2.c). La lógica es la misma: se renuncia a la vía administrativa,
  pero no a la judicial. En tráfico, el 94.d-e lo dice expresamente.

**Fundamento.**
- LSV 94: el pago dentro del plazo «de veinte días naturales contados desde el día siguiente al
  de su notificación» concluye el procedimiento con estas consecuencias: «a) La reducción del
  50 por ciento del importe de la sanción»; «b) La renuncia a formular alegaciones. En el caso
  de que se formulen se tendrán por no presentadas»; «c) La terminación del procedimiento, sin
  necesidad de dictar resolución expresa, el día en que se realice el pago»; «d) El
  agotamiento de la vía administrativa, siendo recurrible únicamente ante el orden
  jurisdiccional contencioso-administrativo»; «e) El plazo para interponer el recurso
  contencioso-administrativo se iniciará el día siguiente a aquel en que tenga lugar el pago»;
  «f) La firmeza de la sanción en la vía administrativa desde el momento del pago».
- LSV 93.1, párr. 3: «Si se efectúa el pago de la multa en las condiciones indicadas en el
  párrafo primero, se seguirá el procedimiento sancionador abreviado, y en caso de no hacerlo,
  el procedimiento sancionador ordinario». LSV 93.2: el abreviado «no será de aplicación a las
  infracciones previstas en el artículo 77.h), j), n), ñ), o), p), q), r), s) y t)».
- LSV 81: la cuantía de la multa «podrá incrementarse en un 30 por ciento». LSV 87.3.a: la
  denuncia notificada en el acto debe indicar «La infracción presuntamente cometida, la sanción
  que pueda corresponder».
- LPAC 116.c: causa de inadmisión «Tratarse de un acto no susceptible de recurso». LPAC 85.2:
  «el pago voluntario por el presunto responsable, en cualquier momento anterior a la
  resolución, implicará la terminación del procedimiento». LPAC 85.3: reducciones «de, al
  menos, el 20 %», cuya «efectividad estará condicionada al desistimiento o renuncia de
  cualquier acción o recurso en vía administrativa contra la sanción». LPAC DA 1ª.2.c.
- LJCA 46.1: «dos meses contados desde el día siguiente al de la publicación de la disposición
  impugnada o al de la notificación o publicación del acto que ponga fin a la vía
  administrativa, si fuera expreso».
- **Pista no verificada** (fuente secundaria): STS de 18/02/2021, rec. 2201/2020, que según
  reseñas admite el contencioso tras un pago reducido del 85 LPAC, aunque advierte de que el
  reconocimiento de responsabilidad dificulta ganarlo. No leída. En tráfico no es necesaria
  para admitir el contencioso, porque el 94.d-e lo dice expresamente.
- Práctica administrativa (no normativa): los anuncios de denuncias del Ayuntamiento de Palma
  en el Suplemento de Notificaciones del BOE (23/09/2026) informan de que el pago reducido
  implica la renuncia a alegar, el fin del procedimiento sin resolución, el agotamiento de la
  vía y la firmeza, y de que presentar alegaciones supone perder la reducción.

**Fuente.** LSV arts. 81, 87, 93 y 94; LPAC arts. 85, 116 y DA 1ª; LJCA art. 46. Consultado
2026-09-23.

**Certeza.**
- `A`: no cabe reposición (94.d: «únicamente»), cabe el contencioso con inicio el día
  siguiente al pago (94.e), el abreviado no se aplica a las infracciones del 93.2, y la
  reducción del 85.3 LPAC queda desplazada.
- `B`: la duración de dos meses (46.1 LJCA combinado con el 94.e); que el pago tardío o
  parcial lleva al procedimiento ordinario; que la reducción se calcula sobre el importe que
  figura en la denuncia.
- `C`: el destino del dinero pagado tarde o en parte (¿termina el procedimiento por el 85.2
  LPAC?, ¿se devuelve?, ¿se imputa a la sanción final?).

**Qué queda pendiente.**
- TODO(juridico): pago con reducción fuera de los 20 días naturales o por importe inferior:
  ¿se aplica el 85.2 LPAC (terminación sin reducción) o se sigue el ordinario del 93.1 LSV?
  ¿Qué pasa con lo pagado? Fuente: CENDOJ; criterios de la DGT y del Ajuntament de Palma.
- TODO(juridico): cómputo del plazo de dos meses del contencioso tras el pago (días inhábiles
  procesales, agosto). Ya abierto en el fichero de la LJCA, duda 2.
- TODO(juridico): ¿se puede pagar con reducción una denuncia cuyo importe ya está graduado al
  alza (81) sin haberse motivado la graduación? ¿Es motivo de impugnación en el contencioso?
  Fuente: CENDOJ.

**Recomendación para ggLaw.** Antes de ofrecer el pago reducido, avisar de forma clara y
visible de que **cierra la vía administrativa** y de que solo queda el contencioso, con
abogado. No generar nunca un recurso de reposición contra una multa pagada con reducción. Si
el usuario ya pagó, informar solo de la fecha límite del contencioso (día siguiente al pago +
2 meses, pendiente de validar) y recomendarle que consulte a un abogado.

---

### Duda 15. Multa del Ayuntamiento de Palma: ¿reposición o alzada? ¿Qué órgano judicial conoce del contencioso?

**Respuesta propuesta.**
- **Recurso administrativo: reposición potestativa, no alzada.** La resolución sancionadora de
  tráfico pone fin a la vía administrativa por mandato de la propia LSV (96.1), y el 96.6
  extiende ese régimen a las resoluciones de los Alcaldes. En el ámbito local lo confirma el
  52.2 LBRL: las resoluciones del Alcalde, y las de órganos inferiores que resuelven por
  delegación del Alcalde, agotan la vía. El plazo es de **un mes** desde el día siguiente a la
  notificación (96.2), y el silencio es desestimatorio al mes (96.5). Después queda el
  contencioso.
- **Órgano que sanciona en Palma.** La ley atribuye la sanción al Alcalde (84.4 LSV; art. 90.1
  de la Ley balear 23/2006 de capitalidad), que puede delegarla o desconcentrarla (90.2 de la
  Ley 23/2006). En los anuncios de 2026, el Ayuntamiento indica que sanciona el **Concejal del
  Área de Movilidad** y que la resolución pone fin a la vía y admite reposición. Según
  `knowledge/palma-competencia-sancionadora-trafico.md` (duda 17), la Resolución de
  Alcaldía 4833, de 6/03/2026 (BOIB núm. 32, de 12/03/2026),
  **delega** en el titular del Área de Movilidad la potestad sancionadora de tráfico, incluida
  la resolución de las reposiciones. Es, por tanto, el supuesto del 52.2.b LBRL. Aunque fuera
  una desconcentración, la resolución seguiría agotando la vía, porque lo dispone una ley
  (96.1 LSV; 114.1.g LPAC).
- **Palma es municipio de gran población** por el 121.1.a LBRL (más de 250.000 habitantes). El
  Título X entró en vigor el **01/01/2004** (Ley 57/2003, DF 3ª), con seis meses para adaptar
  la organización (DT 1ª). Palma ya superaba el umbral entonces: 367.277 habitantes a
  01/01/2003 (RD 1748/2003). Hoy tiene 434.786 (RD 1117/2025, ya en `knowledge/`). En el
  Título X la potestad sancionadora corresponde a la Junta de Gobierno «salvo que por ley esté
  atribuida a otro órgano» (127.1.l), y en tráfico la ley la atribuye al Alcalde. El Título X
  no crea una alzada para estas multas. La Ley 23/2006 (art. 148) permite crear comisiones que
  «informen» de los recursos de reposición y de alzada en materia de sanciones, pero no cambia
  el tipo de recurso.
- **Órgano judicial.** Conocen los **Juzgados de lo Contencioso-administrativo** de los actos
  de las entidades locales (8.1 LJCA), sin límite de cuantía. Tras la LO 1/2025, esos Juzgados
  se transformaron el **31/12/2025** en la **Sección de lo Contencioso-Administrativo del
  Tribunal de Instancia** con sede en la capital de la provincia (Palma) y jurisdicción en toda
  ella (93.1 LOPJ; LO 1/2025, DT 1ª.3.º y DA 1ª). Las leyes que hablan de «Juzgados de lo
  Contencioso-Administrativo» (como el art. 8 LJCA) se entienden referidas a esas Secciones.
  Territorialmente, en materia de sanciones el demandante puede elegir entre el órgano de su
  domicilio y el de la sede del órgano sancionador. Para actos locales, la elección se limita a
  la circunscripción del TSJ de la sede (14.1, regla 2ª, LJCA). Como las Illes Balears son una
  sola provincia, en la práctica es siempre la Sección de lo Contencioso-Administrativo del
  Tribunal de Instancia de Palma.
- **Corrección de la pregunta**: tras la LO 1/2025, el art. 90 LOPJ regula las Secciones de lo
  **Penal**. Las de lo Contencioso-Administrativo están en el art. 93 LOPJ.

**Fundamento.**
- LSV 96.1: «La resolución sancionadora pondrá fin a la vía administrativa». LSV 96.2: «podrá
  interponerse recurso de reposición, con carácter potestativo, en el plazo de un mes contado
  desde el día siguiente al de su notificación». LSV 96.6: contra las resoluciones de los
  Alcaldes «se estará a lo establecido en los anteriores apartados respetando la competencia
  sancionadora prevista en su normativa específica».
- LSV 84.4: la sanción en vías urbanas «corresponderá a los respectivos Alcaldes, los cuales
  podrán delegar esta competencia de acuerdo con la normativa aplicable».
- Ley 23/2006 (Illes Balears), art. 89.1: es competencia propia del Ayuntamiento de Palma «la
  ordenación del tráfico de personas y vehículos, incluyendo la vigilancia y sanción de
  infracciones por todas las vías urbanas». Art. 90.1: «La sanción por infracciones de normas
  de circulación cometidas en vías urbanas corresponde al alcalde o a la alcaldesa». Art. 90.2:
  «puede desconcentrar o delegar el ejercicio de dichas competencias en los términos de la
  legislación básica de régimen local y la presente Ley». Art. 148.1: comisiones «que conozcan
  de los recursos de reposición y de alzada e informen de ellos, en las materias de […]
  sanciones de competencia municipal».
- LBRL 52.1: contra los actos que pongan fin a la vía cabe acudir a la jurisdicción, «pudiendo
  no obstante interponer con carácter previo y potestativo recurso de reposición». LBRL 52.2:
  ponen fin a la vía las resoluciones de «los Alcaldes» (a) y «Las de autoridades y órganos
  inferiores en los casos que resuelvan por delegación del Alcalde» (b). LPAC 114.1.g: ponen
  fin a la vía «Las demás resoluciones de órganos administrativos cuando una disposición legal
  o reglamentaria así lo establezca».
- LBRL 121.1.a: el Título X se aplica «A los municipios cuya población supere los 250.000
  habitantes». LBRL 127.1.l: la Junta de Gobierno Local puede «Ejercer la potestad sancionadora
  salvo que por ley esté atribuida a otro órgano».
- Ley 57/2003, DF 3ª: «La presente ley entrará en vigor el 1 de enero de 2004». DT 1ª: los
  Plenos de los municipios del Título X «dispondrán de un plazo de seis meses desde su entrada
  en vigor para aprobar las normas orgánicas necesarias para la adaptación de su organización».
- LJCA 8.1: «Los Juzgados de lo Contencioso-administrativo conocerán, en única o primera
  instancia […] de los recursos que se deduzcan frente a los actos de las entidades locales».
  LJCA 14.1, regla 2ª: en sanciones será competente, «a elección del demandante, el juzgado o
  el tribunal en cuya circunscripción tenga aquél su domicilio o se halle la sede del órgano
  autor del acto originario impugnado». Para las entidades locales, esa elección «se entenderá
  limitada a la circunscripción del Tribunal Superior de Justicia en que tenga su sede el
  órgano que hubiere dictado el acto originario impugnado».
- LOPJ 84.1 (redacción de la LO 1/2025): «Habrá un Tribunal de Instancia en cada partido
  judicial, con sede en su capital». LOPJ 84.2.h: los Tribunales pueden tener una Sección «De
  lo Contencioso-Administrativo». LOPJ 93.1: «Con carácter general, en el Tribunal de Instancia
  con sede en la capital de cada provincia, y con jurisdicción en toda ella, existirá una
  Sección de lo Contencioso-Administrativo».
- LO 1/2025, DT 1ª: «El día 31 de diciembre de 2025, los restantes Juzgados, no comprendidos en
  los supuestos anteriores, se transformarán en las respectivas Secciones». DA 1ª: las
  referencias en las leyes a los Juzgados «de lo Contencioso-Administrativo» «se entenderán
  referidas a las Secciones del orden jurisdiccional correspondiente de los Tribunales de
  Instancia».
- Hechos comprobados en el BOE (texto del diario; el RD no está en la API de legislación
  consolidada): el RD 1748/2003 (BOE-A-2003-23404) fija para Palma de Mallorca 367.277
  habitantes a 01/01/2003. Existencia de los Juzgados de lo Contencioso-Administrativo de
  Palma de Mallorca antes de la transformación: anuncios en la sección IV del BOE (por ejemplo,
  BOE-B-2025-15235, de 26/04/2025; contenido no leído).
- Práctica administrativa (no normativa): anuncios del Servicio de Multas del Ayuntamiento de
  Palma en el Suplemento de Notificaciones del BOE núm. 235, de 23/09/2026. *Resumen propio:*
  la resolución la dicta el Concejal del Área de Movilidad y pone fin a la vía
  administrativa; cabe reposición en un mes o contencioso directo en dos meses, y la
  reposición no suspende la ejecución.

**Fuente.** LSV arts. 84 y 96; LBRL arts. 52, 121 y 127; LPAC art. 114; LJCA arts. 8 y 14;
Ley 23/2006 (BOE-A-2007-1896) arts. 89, 90 y 148, <https://www.boe.es/buscar/act.php?id=BOE-A-2007-1896>
(`knowledge/ley-23-2006-capitalidad-palma.md`); Ley 57/2003 (BOE-A-2003-23103) DT 1ª y
DF 3ª (leída con `scripts/boe_fetch.py`, no transcrita); LOPJ (BOE-A-1985-12666) arts. 84,
90 y 93 y LO 1/2025 (BOE-A-2025-76) DA 1ª y DT 1ª (`knowledge/lopj-6-1985-tribunales-instancia.md`);
RD 1748/2003 (BOE-A-2003-23404). Consultado 2026-09-23 y 2026-09-24.

**Certeza.**
- `A`: el recurso es la reposición potestativa de un mes (96.1, 96.2 y 96.6 LSV; 52 LBRL); el
  órgano judicial es la Sección de lo Contencioso-Administrativo del Tribunal de Instancia de
  Palma (8.1 LJCA; 93.1 LOPJ; DT 1ª y DA 1ª de la LO 1/2025); y Palma es municipio de gran
  población por su población.
- `B`: que Palma está en el Título X desde el 01/01/2004 (aplicación directa del 121.1.a; no se
  ha verificado la fecha de su reglamento orgánico). También que la resolución agota la vía
  aunque el Concejal actúe por desconcentración.
- `B`: que el Concejal del Área de Movilidad resuelve por delegación (Resolución de
  Alcaldía 4833/2026, BOIB; duda 17).
- `C`: la fecha efectiva de constitución del Tribunal de Instancia de Palma.

**Qué queda pendiente.**
- TODO(juridico): cerrar la duda 1 del fichero de la LBRL con la Resolución de Alcaldía
  4833/2026 (duda 17), y resolver antes la validez de delegar también la resolución de la
  reposición en el mismo órgano (art. 9.2.c LRJSP; duda 17).
- TODO(juridico): confirmar en el BOE o en el CGPJ la constitución efectiva del Tribunal de
  Instancia de Palma y el número de plazas de su Sección de lo Contencioso-Administrativo. Los
  anexos de la Ley 38/1988 no están consolidados en la API del BOE.
- TODO(juridico): ¿afecta a una multa de tráfico la reclamación económico-administrativa
  municipal (art. 137 LBRL) en la fase de apremio? Ya abierto en el fichero de la LBRL, duda 3.

**Recomendación para ggLaw.** Para Palma, generar solo el **recurso de reposición** (un mes,
dirigido al mismo órgano que dictó la resolución). Para el contencioso, limitarse a informar:
“Sección de lo Contencioso-Administrativo del Tribunal de Instancia de Palma, dos meses,
con abogado”.

---

### Duda 16. La denuncia que vale como resolución (95.4 LSV): plazo del recurso, reposición y requisitos de la denuncia

**Respuesta propuesta.**
- **Cuándo se produce el efecto.** Si en los 20 días naturales siguientes a la notificación de
  la denuncia no se alega ni se paga, la denuncia «surtirá el efecto de acto resolutorio» solo
  en tres casos (95.4):
  - a) infracciones leves;
  - b) graves **sin** puntos cuya notificación no se hizo en el acto;
  - c) graves y muy graves notificadas en el acto, con o sin puntos.

  **Quedan fuera**, cuando la denuncia **no** se notificó en el acto, las graves **con**
  detracción de puntos (por ejemplo, un radar con puntos) y **todas** las muy graves, tengan
  o no puntos. En ellas hace falta propuesta y resolución expresa (95.3). El procedimiento se tiene por concluido **el día siguiente al último de los
  20 días** (87.3.e). Desde ese día la sanción pone fin a la vía administrativa (95.5), y se
  puede ejecutar desde el día siguiente a los 30 días naturales desde la notificación de la
  denuncia (95.4, último párrafo, y 95.5).
- **¿Cabe reposición?** Sí. Es una terminación que «pone fin a la vía administrativa» (95.5), y
  contra esos actos cabe la reposición potestativa (96.2 LSV, 52.1 LBRL y 123.1 LPAC). Pero con
  un límite importante: en la reposición **no se tendrán en cuenta** hechos, documentos ni
  alegaciones que pudieron aportarse en el procedimiento originario (96.4). Quien no alegó en
  los 20 días apenas puede alegar hechos nuevos en la reposición. Le quedan sobre todo los
  motivos de derecho: prescripción, caducidad, notificación defectuosa, falta de competencia
  y nulidades.
- **¿Desde cuándo corre el plazo del recurso?** La LSV no lo dice: no hay una resolución
  distinta que notificar. Hay dos lecturas:
  - **(a)** El mes de reposición (96.2) y los dos meses del contencioso (46.1 LJCA) cuentan
    desde el día siguiente a aquel en que se produce el efecto resolutorio (día siguiente al
    fin de los 20 días).
  - **(b)** Cuentan desde el día siguiente a la notificación de la **denuncia**, que es el
    documento notificado que hace de resolución. Con esta lectura, el plazo de reposición se
    solaparía casi entero con el de alegaciones.

  Además, si la denuncia no indicó los recursos procedentes, el órgano y el plazo, el 40.3
  LPAC permite sostener que el plazo no empezó a correr hasta que el interesado actuó
  conociendo el acto, o recurrió.
- **Requisitos de la denuncia para que produzca el efecto.**
  1. Notificación válida (89-91 LSV; dudas 12 y 13).
  2. Infracción incluida en las letras a) a c) del 95.4.
  3. Ni alegaciones ni pago en los 20 días.
  4. **Contenido.** Si la denuncia se notificó **en el acto**, el 87.3 exige indicar la
     infracción, la sanción y los puntos (a); el órgano competente y su norma (b); que la
     denuncia inicia el procedimiento y el plazo de 20 días para pagar o alegar, con los
     lugares de presentación (d); y la **advertencia** de que, sin alegaciones ni pago, el
     procedimiento se tendrá por concluido conforme al 95.4 (e).

     Si se notificó **después** (radar, estacionamiento), la LSV no fija el contenido. Por
     supletoriedad se aplica el 64.2 LPAC (contenido mínimo del acuerdo de iniciación). Su
     letra f) exige advertir de que, sin alegaciones, el acuerdo «podrá ser considerado
     propuesta de resolución». En tráfico el efecto es más fuerte (resolución, no propuesta),
     así que con mayor razón debería advertirse.
  - El último párrafo del 95.4 no fija requisitos de contenido. Solo fija el momento de la
    ejecución (30 días naturales desde la notificación de la denuncia).
- Una denuncia sin la advertencia del 87.3.e o del 64.2.f no debería producir el efecto
  resolutorio. En ese caso el procedimiento necesitaría una resolución expresa dentro del
  año del 112.3 (duda 9). Es un motivo de defensa **posible**, no confirmado por
  jurisprudencia leída.

**Fundamento.**
- LSV 95.4: «Si el denunciado no formula alegaciones ni abona el importe de la multa en el
  plazo de veinte días naturales siguientes al de la notificación de la denuncia, ésta surtirá
  el efecto de acto resolutorio del procedimiento sancionador en los siguientes casos:
  a) Infracciones leves en todos los casos. b) Infracciones graves que no supongan la
  detracción de puntos cuya notificación no se haya podido efectuar en el acto de la denuncia.
  c) Infracciones graves y muy graves cuya notificación se efectuase en el acto de la
  denuncia, supongan o no la detracción de puntos». Último párrafo: «En estos supuestos, la
  sanción podrá ejecutarse transcurridos treinta días naturales desde la notificación de la
  denuncia».
- LSV 95.5: «La terminación del procedimiento pone fin a la vía administrativa y la sanción se
  podrá ejecutar desde el día siguiente al transcurso de los treinta días antes indicados».
- LSV 87.3: «En las denuncias que los agentes de la autoridad notifiquen en el acto al
  denunciado deberá constar, además». Letra d): se indicará «que dicha denuncia inicia el
  procedimiento sancionador y que dispone de un plazo de veinte días naturales para efectuar el
  pago, con la reducción y las consecuencias establecidas en el artículo 94, o para formular
  las alegaciones». Letra e): «Si en el plazo señalado en el párrafo anterior no se han
  formulado alegaciones o no se ha abonado la multa, se indicará que el procedimiento se tendrá
  por concluido el día siguiente a la finalización de dicho plazo, conforme se establece en el
  artículo 95.4».
- LSV 96.2: reposición «en el plazo de un mes contado desde el día siguiente al de su
  notificación». LSV 96.4: «No se tendrán en cuenta en la resolución del recurso hechos,
  documentos y alegaciones del recurrente que pudieran haber sido aportados en el procedimiento
  originario». LSV 96.1: la sanción se puede ejecutar «una vez haya transcurrido el plazo
  indicado en el artículo 95.4».
- LPAC 64.2.f: el acuerdo de iniciación debe contener la «indicación de que, en caso de no
  efectuar alegaciones en el plazo previsto sobre el contenido del acuerdo de iniciación, éste
  podrá ser considerado propuesta de resolución cuando contenga un pronunciamiento preciso
  acerca de la responsabilidad imputada».
- LPAC 40.2: la notificación debe contener el texto íntegro, «con indicación de si pone fin o
  no a la vía administrativa, la expresión de los recursos que procedan, en su caso, en vía
  administrativa y judicial, el órgano ante el que hubieran de presentarse y el plazo para
  interponerlos». LPAC 40.3: si falta alguno de esos requisitos, la notificación surte efecto
  «a partir de la fecha en que el interesado realice actuaciones que supongan el conocimiento
  del contenido y alcance de la resolución o acto objeto de la notificación, o interponga
  cualquier recurso que proceda».
- LBRL 52.1 y LPAC 123.1: reposición potestativa contra los actos que ponen fin a la vía.
  LJCA 46.1: dos meses desde el día siguiente a la notificación del acto que pone fin a la
  vía, «si fuera expreso».
- Práctica administrativa (no normativa): los anuncios de denuncias del Ayuntamiento de Palma
  en el Suplemento de Notificaciones del BOE (23/09/2026) advierten de que, en las denuncias
  por estacionamiento, si no se alega ni se paga en 20 días naturales, la notificación tendrá
  efectos de resolución sancionadora y se podrá ejecutar pasados 30 días naturales. También
  dicen que todos los plazos del expediente se cuentan desde el día siguiente a esa
  notificación. No indican cuándo empieza el plazo de reposición contra esa resolución.

**Fuente.** LSV arts. 87, 95 y 96; LPAC arts. 40, 64 y 123; LBRL art. 52; LJCA art. 46. El
panel «Jurisprudencia» de boe.es no vincula ninguna sentencia a los arts. 95 y 96 LSV. El
precedente del 95.4 es el art. 81.5 del RDL 339/1990 en la redacción de la Ley 18/2009, que
entonces daba quince días naturales (comprobado en BOE-A-2009-18732, art. único). Consultado
2026-09-23.

**Certeza.**
- `A`: los supuestos del 95.4 (y que, si la denuncia no se notificó en el acto, quedan fuera
  las graves con puntos y todas las muy graves), el día de conclusión (87.3.e), el fin de la vía (95.5), la ejecutividad a los
  30 días y el límite del 96.4 en la reposición.
- `B`: que cabe reposición contra la denuncia convertida en resolución, y que la advertencia
  del 87.3.e (o del 64.2.f por supletoriedad) es un requisito para que se produzca el efecto.
- `C`: el día inicial del mes de reposición y de los dos meses del contencioso en este caso.
  Falta jurisprudencia del TS o de los TSJ sobre el 95.4 LSV (o su precedente, el art. 81.5
  del RDL 339/1990 tras la Ley 18/2009).

**Qué queda pendiente.**
- TODO(juridico): en el supuesto del 95.4 LSV, ¿desde qué día corren el mes de reposición
  (96.2) y los dos meses del contencioso (46.1 LJCA): desde la notificación de la denuncia o
  desde el día siguiente a la conclusión del procedimiento? Fuente: CENDOJ.
- TODO(juridico): ¿impide el efecto resolutorio una denuncia notificada después (radar,
  estacionamiento) que no advierte de él? ¿Se aplica en tráfico el 64.2.f LPAC? Fuente:
  CENDOJ.
- TODO(juridico): ¿cómo se combinan los 30 días del 95.4 y 95.5 (ejecutividad) con los
  15 días naturales del 110.1 para el pago voluntario tras la firmeza (duda 11)? ¿Cuándo
  empieza el apremio?

**Recomendación para ggLaw.** No dejar nunca que el usuario llegue al 95.4 sin decidir.
Recordarle que **alegar dentro de los 20 días naturales** es la única vía para que se
valoren hechos y pruebas (96.4). Si ya pasaron los 20 días, calcular el plazo de reposición
con la **lectura más corta** (un mes desde el día siguiente a la notificación de la denuncia)
y, si ha vencido, estudiar los motivos de derecho que no dependen de ese plazo: notificación
defectuosa, falta de advertencia, prescripción y caducidad.

---

## Dudas 17-21: pendientes

TODO(juridico): en preparación (órgano sancionador de Palma, cinemómetros, identificación
del conductor, verificación de ECLI y control de modificaciones de las normas).
