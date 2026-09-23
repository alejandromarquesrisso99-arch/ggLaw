# ggLaw: propuesta de respuesta a las dudas 1-8 (supletoriedad y cómputo de plazos en tráfico)

> Borrador del subagente `investigador-normativa`, 2026-09-23. **No es asesoramiento
> jurídico.** Todo requiere validación de Alex o de un abogado antes de pasar a `rules/`
> o a `core/plazos.py`.

**Abreviaturas y fuentes** (todas consultadas el 2026-09-23 con `scripts/boe_fetch.py`,
versión consolidada vigente):

- **LSV**: RDL 6/2015, BOE-A-2015-11722, <https://www.boe.es/buscar/act.php?id=BOE-A-2015-11722>
  (fichero: `knowledge/rdl-6-2015-procedimiento-sancionador.md`).
- **LPAC**: Ley 39/2015, BOE-A-2015-10565, <https://www.boe.es/buscar/act.php?id=BOE-A-2015-10565>
  (fichero: `knowledge/ley-39-2015-notificaciones-recursos.md`).
- **LRJSP**: Ley 40/2015, BOE-A-2015-10566, <https://www.boe.es/buscar/act.php?id=BOE-A-2015-10566>
  (fichero nuevo: `knowledge/ley-40-2015-potestad-sancionadora.md`).
- **RPST**: RD 320/1994, BOE-A-1994-8985, <https://www.boe.es/buscar/act.php?id=BOE-A-1994-8985>
  (fichero nuevo: `knowledge/rd-320-1994-reglamento-sancionador-trafico.md`).
- **CC**: Código Civil, art. 5, BOE-A-1889-4763, <https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763>
  (leído, no transcrito en `knowledge/`).
- **Ley 18/2009**: BOE-A-2009-18732, <https://www.boe.es/buscar/act.php?id=BOE-A-2009-18732> (DD única y DF 5ª leídas).

**Jurisprudencia.** CENDOJ y tribunalconstitucional.es están bloqueados. El panel
«Jurisprudencia» de boe.es (selección del CENDOJ) no vincula ninguna sentencia a los arts.
30 y 31 LPAC ni a los arts. 90, 95, 96 y 112 LSV. Para el art. 30 LRJSP vincula la
STS 603/2021 (25/02/2021), no leída. Todo lo demás son **pistas no verificadas**, halladas
en fuentes secundarias.

---

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

## Dudas 9-21: pendientes

TODO(juridico): investigación interrumpida el 2026-09-23 por falta de acceso a CENDOJ, TC, DGT y Ayuntamiento de Palma. Ver la lista consolidada en el historial de la tarea 4 y en las secciones "Dudas abiertas" de los ficheros de `knowledge/`.
