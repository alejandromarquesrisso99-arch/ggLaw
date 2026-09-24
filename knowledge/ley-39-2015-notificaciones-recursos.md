---
norma: Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas
identificador: BOE-A-2015-10565
articulos: [14, 16, 21, 22, 24, 25, 29, 30, 31, 32, 40, 41, 42, 43, 44, 45, 46, 47, 48, 53, 63, 64, 66, 68, 85, 89, 90, 95, 98, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126]
disposiciones: [adicional primera, derogatoria única, final séptima]
fuente: https://www.boe.es/buscar/act.php?id=BOE-A-2015-10565
version_consolidada: 2024-11-06
consultado: 2026-09-23
estado: borrador
---

# Ley 39/2015 (LPAC): notificaciones, plazos, sancionador y recursos

> **Aviso:** esto es material de referencia para ggLaw, no asesoramiento jurídico.
> Contenido en `estado: borrador`, pendiente de revisión por Alex o por un abogado.

**Cómo se ha obtenido el texto.** Los artículos de las secciones 1 a 8 se han transcrito
literalmente de la versión consolidada vigente, descargada con `scripts/boe_fetch.py`
(API de datos abiertos del BOE) el 2026-09-23. Se han comparado bloque a bloque con la
página HTML consolidada (`act.php?id=BOE-A-2015-10565`) y el texto coincide. Solo cambian
los espacios que deja el marcado HTML y los sufijos `#df-…` de las referencias. Cada
bloque lleva un comentario `<!-- bloque … -->` con la fecha de publicación y de vigencia
de la redacción transcrita. Las notas editoriales del BOE aparecen como `> _Nota BOE: …_`
y no son texto normativo. El art. 98 y la disposición derogatoria única se añadieron el
2026-09-24 con el mismo método (necesarios para las dudas 11 y 13 de `dudas-abiertas.md`).

**Fecha de la versión consolidada.** La API de metadatos devuelve
`fecha_actualizacion: 20260923T065942Z`, pero esa fecha es la de actualización del
registro, no la del texto. La página consolidada del BOE indica «Última actualización
publicada el 06/11/2024», que coincide con la fecha más reciente del índice de bloques
(disposición adicional novena). Por eso se usa `version_consolidada: 2024-11-06`. De los
bloques transcritos, solo han cambiado desde el texto original el **art. 32** (nuevo
apartado 5, RDL 6/2022, vigente desde 2022-03-31) y la **DF 7ª**. Todos los demás
conservan la redacción original, vigente desde el 2016-10-02. El BOE no incluye notas de
sentencias del TC en ninguno de ellos.

**Aplicación a tráfico.** Según la DA 1ª.2.c), los procedimientos sancionadores de tráfico
y seguridad vial se rigen «por su normativa específica» (RDL 6/2015, BOE-A-2015-11722) y
solo **supletoriamente** por esta Ley. Todo lo que aparece aquí debe contrastarse con el
RDL 6/2015 antes de usarlo en una regla (ver «Dudas abiertas»).

---

## Plazos clave (literal)

«Tipo de cómputo» indica lo que dice el propio texto. Cuando un plazo se expresa en
«días» sin más precisión, el art. 30.2 los considera hábiles, salvo que una ley o el
Derecho de la UE digan otra cosa. Los plazos en meses o años se cuentan de fecha a fecha
(art. 30.4). En todos los casos se aplica el art. 30.5: si el último día es inhábil, el
plazo se prorroga al primer día hábil siguiente.

| Plazo | Texto literal | Tipo de cómputo | Art. |
|---|---|---|---|
| Recurso de reposición (acto expreso) | "El plazo para la interposición del recurso de reposición será de un mes, si el acto fuera expreso" | meses (30.4) | 124.1 |
| Recurso de reposición (acto presunto) | "en cualquier momento a partir del día siguiente a aquel en que, de acuerdo con su normativa específica, se produzca el acto presunto" | sin plazo | 124.1 |
| Resolver la reposición | "El plazo máximo para dictar y notificar la resolución del recurso será de un mes" | meses | 124.2 |
| Recurso de alzada (acto expreso) | "El plazo para la interposición del recurso de alzada será de un mes, si el acto fuera expreso" | meses | 122.1 |
| Resolver la alzada | "El plazo máximo para dictar y notificar la resolución será de tres meses" y después "se podrá entender desestimado el recurso, salvo en el supuesto previsto en el artículo 24.1, tercer párrafo" | meses | 122.2 |
| Recurso extraordinario de revisión, causa a) | "dentro del plazo de cuatro años siguientes a la fecha de la notificación de la resolución impugnada" | años | 125.2 |
| Recurso extraordinario de revisión, otras causas | "el plazo será de tres meses a contar desde el conocimiento de los documentos o desde que la sentencia judicial quedó firme" | meses | 125.2 |
| Resolver el recurso de revisión | "Transcurrido el plazo de tres meses desde la interposición del recurso extraordinario de revisión sin haberse dictado y notificado la resolución, se entenderá desestimado" | meses | 126.3 |
| Acceder a una notificación electrónica | "se entenderá rechazada cuando hayan transcurrido diez días naturales desde la puesta a disposición de la notificación sin que se acceda a su contenido" (solo si es obligatoria o la eligió el interesado) | **días naturales** (literal) | 43.2 |
| Segundo intento de notificación en papel | "intento que se repetirá por una sola vez y en una hora distinta dentro de los tres días siguientes" | no lo precisa (ver dudas) | 42.2 |
| Separación entre los dos intentos | "En caso de que el primer intento de notificación se haya realizado antes de las quince horas, el segundo intento deberá realizarse después de las quince horas y viceversa, dejando en todo caso al menos un margen de diferencia de tres horas entre ambos intentos de notificación" | horas | 42.2 |
| Notificación infructuosa | "la notificación se hará por medio de un anuncio publicado en el" BOE | — | 44 |
| Envío de la notificación por la Administración | "Toda notificación deberá ser cursada dentro del plazo de diez días a partir de la fecha en que el acto haya sido dictado" | días | 40.2 |
| Subsanar una solicitud | "en un plazo de diez días", ampliable "hasta cinco días" | días | 68.1, 68.2 |
| Alegar si la resolución sancionadora agrava la calificación | "en el plazo de quince días" | días | 90.2 |
| Audiencia en el recurso por hechos o documentos nuevos | "en un plazo no inferior a diez días ni superior a quince" | días | 118.1 |
| Suspensión automática de la ejecución | "si transcurrido un mes desde que la solicitud de suspensión haya tenido entrada en el registro electrónico" sin resolución expresa | meses | 117.3 |
| Plazo máximo para resolver (regla general) | "Este plazo no podrá exceder de seis meses salvo que una norma con rango de Ley establezca uno mayor" | meses | 21.2 |
| Plazo máximo cuando la norma no lo fija | "Cuando las normas reguladoras de los procedimientos no fijen el plazo máximo, éste será de tres meses" (de oficio: "desde la fecha del acuerdo de iniciación") | meses | 21.3 |
| Suspensión por informe preceptivo | "Este plazo de suspensión no podrá exceder en ningún caso de tres meses" | meses | 22.1.d |
| Certificado de silencio | "en el plazo de quince días desde que expire el plazo máximo para resolver el procedimiento" | días | 24.4 |
| Caducidad por paralización (procedimientos a solicitud) | "transcurridos tres meses, se producirá la caducidad del procedimiento" | meses | 95.1 |
| Ampliación de plazos | "que no exceda de la mitad de los mismos"; "En ningún caso podrá ser objeto de ampliación un plazo ya vencido" | — | 32.1, 32.3 |
| Plazos por horas | "no podrán tener una duración superior a veinticuatro horas, en cuyo caso se expresarán en días" | horas hábiles | 30.1 |
| Reducción por reconocimiento o pago voluntario | "reducciones de, al menos, el 20 % sobre el importe de la sanción propuesta" | — | 85.3 |

---

## Índice temático (qué regula cada artículo y por qué se incluye)

### A. Ámbito: relación con la normativa de tráfico

| Art. | Regula | Contenido relevante | Por qué se incluye |
|---|---|---|---|
| DA 1ª | Especialidades por razón de materia | 2.c): "Las actuaciones y procedimientos sancionadores en materia tributaria y aduanera, en el orden social, en materia de tráfico y seguridad vial y en materia de extranjería" se rigen "por su normativa específica y supletoriamente por lo dispuesto en esta Ley" | Es la norma de enlace. Decide cuándo se aplica la LPAC a las multas de tráfico. |
| DD única | Derogación normativa | 2.a): deroga la "Ley 30/1992, de 26 de noviembre". 3: las referencias a lo derogado "deberán entenderse efectuadas a las disposiciones de esta Ley que regulan la misma materia" | Explica por qué la DA 21ª de la Ley 30/1992 (anuncios en el BOE) ya no existe como tal y su regla está hoy en el art. 44 (duda 13). |

### B. Relación electrónica y presentación de escritos

| Art. | Regula | Contenido relevante | Por qué se incluye |
|---|---|---|---|
| 14 | Derecho y obligación de relacionarse electrónicamente | 14.1: las personas físicas "podrán elegir en todo momento" el medio, "salvo que estén obligadas". 14.2: enumera a los obligados (personas jurídicas, etc.). 14.3: la obligación puede ampliarse reglamentariamente a colectivos de personas físicas | Determina si el usuario puede presentar y recibir en papel. |
| 16 | Registros y lugares de presentación | 16.4: registro electrónico, "En las oficinas de Correos, en la forma que reglamentariamente se establezca", representaciones diplomáticas y "En las oficinas de asistencia en materia de registros" | Indica dónde se puede presentar el escrito generado. |
| 66 | Contenido de las solicitudes | 66.1 a)-f): identificación, medio de notificación, "Hechos, razones y petición", lugar y fecha, firma, órgano y código de identificación | Estructura mínima de los escritos, que CLAUDE.md usa como base de las plantillas. |
| 68 | Subsanación y mejora | Plazo de diez días (ampliable cinco) con apercibimiento de desistimiento. 68.4: los obligados del art. 14 que presenten en papel deben subsanar electrónicamente | Respuesta a un requerimiento de subsanación. |
| DF 7ª | Entrada en vigor | Registro electrónico, apoderamientos, punto de acceso general, etc. "producirán efectos a partir del día 2 de abril de 2021" | Contexto: el régimen de registro electrónico está plenamente en vigor. |

### C. Términos y plazos

| Art. | Regula | Contenido relevante | Por qué se incluye |
|---|---|---|---|
| 29 | Obligatoriedad de términos y plazos | Los plazos obligan a la Administración y a los interesados | Fundamento general. |
| 30 | Cómputo de plazos | Días: "se entiende que éstos son hábiles, excluyéndose del cómputo los sábados, los domingos y los declarados festivos". Días naturales solo si lo declara una ley o el Derecho de la UE, y "se hará constar esta circunstancia en las correspondientes notificaciones". Inicio del cómputo: "a partir del día siguiente a aquel en que tenga lugar la notificación o publicación del acto de que se trate". Meses: "El plazo concluirá el mismo día en que se produjo la notificación, publicación o silencio administrativo en el mes o el año de vencimiento", y si no hay día equivalente, "se entenderá que el plazo expira el último día del mes". 30.5: "Cuando el último día del plazo sea inhábil, se entenderá prorrogado al primer día hábil siguiente". 30.6: un día hábil en el lugar de residencia e inhábil en la sede del órgano, o a la inversa, "se considerará inhábil en todo caso" | Núcleo de `core/plazos.py` y `core/calendario.py`. |
| 31 | Cómputo de plazos en los registros | El registro electrónico admite presentaciones "todos los días del año durante las veinticuatro horas". En plazos de días hábiles, lo presentado en día inhábil "se entenderá realizada en la primera hora del primer día hábil siguiente". 31.3: se aplica el calendario de la sede, "sin que resulte de aplicación a los mismos lo dispuesto en el artículo 30.6" | Presentación electrónica en fin de semana o festivo. |
| 32 | Ampliación | Ampliación de hasta la mitad del plazo, pedida y acordada antes del vencimiento, y no recurrible. Apdo. 5 (ciberincidentes) añadido por el RDL 6/2022 | Permite pedir más plazo. Es el único artículo incluido que se ha modificado después de 2015. |

### D. Obligación de resolver, silencio y caducidad

| Art. | Regula | Contenido relevante | Por qué se incluye |
|---|---|---|---|
| 21 | Obligación de resolver y plazo máximo | Límite de seis meses salvo que una ley fije otro; tres meses por defecto, contados en los procedimientos de oficio desde el acuerdo de iniciación | Base supletoria para la caducidad del sancionador. |
| 22 | Suspensión del plazo máximo | Supuestos facultativos (22.1) y obligatorios (22.2) | Afectan al cómputo de la caducidad. |
| 24 | Silencio en procedimientos iniciados a solicitud del interesado | "El sentido del silencio también será desestimatorio en los procedimientos de impugnación de actos y disposiciones", con la excepción de la alzada contra una desestimación por silencio | Qué ocurre si no se resuelve un recurso. |
| 25 | Falta de resolución en procedimientos iniciados de oficio | 25.1.b): en los procedimientos sancionadores "se producirá la caducidad". 25.2: la paralización imputable al interesado interrumpe el cómputo | Fundamento general de la caducidad. |
| 95 | Caducidad: requisitos y efectos | 95.3: "los procedimientos caducados no interrumpirán el plazo de prescripción" y se puede iniciar un procedimiento nuevo si la infracción no ha prescrito | Efectos de la caducidad (regla `trafico.caducidad`). |

### E. Notificaciones

| Art. | Regula | Contenido relevante | Por qué se incluye |
|---|---|---|---|
| 40 | Notificación: plazo y contenido | Plazo de diez días para cursarla. Contenido obligatorio: texto íntegro, si pone fin a la vía administrativa, recursos, órgano y plazo. 40.3: la notificación defectuosa surte efecto cuando el interesado actúa o recurre. 40.4: para cumplir el plazo máximo basta "el intento de notificación debidamente acreditado" | Motivo de defensa por defectos de notificación y su relación con la caducidad. |
| 41 | Condiciones generales de la práctica | "Las notificaciones se practicarán preferentemente por medios electrónicos". 41.5: el rechazo da por efectuado el trámite. 41.6: si falta el aviso, la notificación sigue siendo válida. 41.7: si hay varios cauces, cuenta el primero | Validez de la notificación y fecha que se toma. |
| 42 | Notificación en papel | Puede recogerla "cualquier persona mayor de catorce años que se encuentre en el domicilio y haga constar su identidad". Dos intentos en franjas horarias distintas y, si fallan, se aplica el art. 44 | Comprobación de los dos intentos en papel. |
| 43 | Notificación electrónica | Se entiende practicada "en el momento en que se produzca el acceso a su contenido" y rechazada a los diez días naturales. 43.3: la puesta a disposición cumple el art. 40.4 | Plazo de diez días naturales para acceder. |
| 44 | Notificación infructuosa | Anuncio en el BOE (obligatorio) y, con carácter facultativo, en el boletín autonómico o provincial o en el tablón de edictos. La Ley no menciona el «Tablón Edictal Único» | Notificación edictal (ver jurisprudencia y dudas). |
| 45 | Publicación | Casos en que la publicación sustituye a la notificación. 45.4: la publicación en tablón se entiende cumplida con la del diario oficial | Diferenciar notificación y publicación. |
| 46 | Indicación de notificaciones y publicaciones | Somera indicación cuando la publicación lesione derechos | Complementa el art. 44. |

### F. Invalidez de los actos (motivos de los recursos)

| Art. | Regula | Contenido relevante | Por qué se incluye |
|---|---|---|---|
| 47 | Nulidad de pleno derecho | 47.1 a)-g). Por ejemplo, e): "Los dictados prescindiendo total y absolutamente del procedimiento legalmente establecido" | El art. 112.1 remite a los arts. 47 y 48 como motivos de recurso. |
| 48 | Anulabilidad | 48.2: el defecto de forma solo anula si "carezca de los requisitos formales indispensables para alcanzar su fin o dé lugar a la indefensión de los interesados". 48.3: una actuación fuera de plazo solo anula "cuando así lo imponga la naturaleza del término o plazo" | Límites al motivo «defecto de forma». |

### G. Especialidades del procedimiento sancionador

| Art. | Regula | Contenido relevante | Por qué se incluye |
|---|---|---|---|
| 53 | Derechos del interesado | 53.1.e): alegar y aportar documentos "en cualquier fase del procedimiento anterior al trámite de audiencia". 53.2: derecho a ser notificado de hechos, infracción y sanción y presunción de no responsabilidad | Garantías del presunto infractor. |
| 63 | Inicio del sancionador | Siempre de oficio y con separación entre instrucción y resolución: "En ningún caso se podrá imponer una sanción sin que se haya tramitado el oportuno procedimiento" | Fundamento de defensa. |
| 64 | Acuerdo de iniciación | Contenido mínimo (64.2 a-f). Si no se presentan alegaciones, el acuerdo "podrá ser considerado propuesta de resolución cuando contenga un pronunciamiento preciso acerca de la responsabilidad imputada" | Lista de comprobación del acto de inicio. |
| 85 | Terminación: reconocimiento y pago voluntario | Reducciones de al menos el 20 %, acumulables, condicionadas "al desistimiento o renuncia de cualquier acción o recurso en vía administrativa contra la sanción" | Consecuencia de pagar con descuento. |
| 89 | Propuesta de resolución | 89.1: archivo sin propuesta (hechos inexistentes o no acreditados, prescripción, etc.). 89.2: la propuesta se notifica y abre plazo de alegaciones | Fases del procedimiento. |
| 90 | Resolución sancionadora | 90.2: no puede basarse en hechos distintos. Si la infracción es más grave, alegaciones en quince días. 90.3: "será ejecutiva cuando no quepa contra ella ningún recurso ordinario en vía administrativa" | Momento en que la sanción es ejecutiva. |
| 98 | Ejecutoriedad | 98.1.b): no es inmediatamente ejecutiva la resolución sancionadora "contra la que quepa algún recurso en vía administrativa, incluido el potestativo de reposición", salvo que "Una disposición establezca lo contrario" (98.1.c) | En tráfico, la LSV lo establece: ejecutiva desde la notificación (96.1 y 96.3 LSV; duda 11). |

### H. Recursos administrativos

| Art. | Regula | Contenido relevante | Por qué se incluye |
|---|---|---|---|
| 112 | Objeto y clases | Alzada y reposición potestativa contra resoluciones y actos de trámite cualificados, por los motivos de los arts. 47 y 48 | Base de los recursos. |
| 113 | Recurso extraordinario de revisión | Contra actos firmes, solo por las causas del art. 125.1 | Vía excepcional. |
| 114 | Fin de la vía administrativa | 114.1 c): "Las resoluciones de los órganos administrativos que carezcan de superior jerárquico, salvo que una Ley establezca lo contrario" | Determina si procede alzada o reposición. |
| 115 | Interposición | Contenido del recurso. 115.2: "El error o la ausencia de la calificación del recurso por parte del recurrente no será obstáculo para su tramitación, siempre que se deduzca su verdadero carácter" | Plantilla del recurso. |
| 116 | Causas de inadmisión | d): "Haber transcurrido el plazo para la interposición del recurso" | Riesgo de extemporaneidad. |
| 117 | Suspensión de la ejecución | Por regla general el recurso no suspende. Suspensión si se pide y no se resuelve en un mes | Pedir la suspensión en el recurso. |
| 118 | Audiencia | Hechos o documentos nuevos: de diez a quince días | Trámite del recurso. |
| 119 | Resolución | "sin que en ningún caso pueda agravarse su situación inicial" | Prohibición de la *reformatio in peius*. |
| 120 | Pluralidad de recursos | Suspensión del plazo para resolver si hay un recurso judicial sobre el mismo acto | Completa la sección de disposiciones generales. Uso poco frecuente. |
| 121 | Alzada: objeto | Actos que no ponen fin a la vía administrativa, recurridos ante el superior jerárquico. Si se presenta ante el órgano autor, este lo remite "en el plazo de diez días" | Procedimiento de alzada. |
| 122 | Alzada: plazos | Ver «Plazos clave» | Plazo de interposición y silencio. |
| 123 | Reposición: objeto | Reposición potestativa contra actos que ponen fin a la vía administrativa. No cabe acudir al contencioso hasta que se resuelva o se desestime por silencio | Recurso típico contra la sanción. |
| 124 | Reposición: plazos | Ver «Plazos clave». 124.3: no cabe una segunda reposición | Plazo de interposición y silencio. |
| 125 | Revisión: objeto y plazos | Causas tasadas a)-d) y plazos de cuatro años o tres meses | Vía excepcional. |
| 126 | Revisión: resolución | Inadmisión y silencio desestimatorio a los tres meses | Vía excepcional. |

### Artículos revisados y no incluidos

Por ahora no se incluyen: el art. 33 (tramitación de urgencia), el 39 (eficacia de los
actos), los 9-10 (identificación y firma), el 73 (cumplimiento de trámites), los 76-77 y
82 (alegaciones, prueba y audiencia en el procedimiento común) y los
106-111 (revisión de oficio y rectificación de errores). Se pueden añadir si alguna regla
los necesita.

---

# Texto literal (versión consolidada BOE)

## 1. Ámbito: especialidades por razón de materia (tráfico)

<!-- bloque daprimera · versión publicada 20151002 · vigente desde 20161002 -->

### Disposición adicional primera. Especialidades por razón de materia.

1. Los procedimientos administrativos regulados en leyes especiales por razón de la materia que no exijan alguno de los trámites previstos en esta Ley o regulen trámites adicionales o distintos se regirán, respecto a éstos, por lo dispuesto en dichas leyes especiales.

2. Las siguientes actuaciones y procedimientos se regirán por su normativa específica y supletoriamente por lo dispuesto en esta Ley:

a) Las actuaciones y procedimientos de aplicación de los tributos en materia tributaria y aduanera, así como su revisión en vía administrativa.

b) Las actuaciones y procedimientos de gestión, inspección, liquidación, recaudación, impugnación y revisión en materia de Seguridad Social y Desempleo.

c) Las actuaciones y procedimientos sancionadores en materia tributaria y aduanera, en el orden social, en materia de tráfico y seguridad vial y en materia de extranjería.

d) Las actuaciones y procedimientos en materia de extranjería y asilo.

<!-- bloque ddunica · versión publicada 20151002 · vigente desde 20161002 -->

### Disposición derogatoria única. Derogación normativa.

1. Quedan derogadas todas las normas de igual o inferior rango en lo que contradigan o se opongan a lo dispuesto en la presente Ley.

2. Quedan derogadas expresamente las siguientes disposiciones:

a) Ley 30/1992, de 26 de noviembre, de Régimen Jurídico de las Administraciones Públicas y del Procedimiento Administrativo Común.

b) Ley 11/2007, de 22 de junio, de acceso electrónico de los ciudadanos a los Servicios Públicos.

c) Los artículos 4 a 7 de la Ley 2/2011, de 4 de marzo, de Economía Sostenible.

d) Real Decreto 429/1993, de 26 de marzo, por el que se aprueba el Reglamento de los procedimientos de las Administraciones Públicas en materia de responsabilidad patrimonial.

e) Real Decreto 1398/1993, de 4 de agosto, por el que se aprueba el Reglamento del Procedimiento para el Ejercicio de la Potestad Sancionadora.

f) Real Decreto 772/1999, de 7 de mayo, por el que se regula la presentación de solicitudes, escritos y comunicaciones ante la Administración General del Estado, la expedición de copias de documentos y devolución de originales y el régimen de las oficinas de registro.

g) Los artículos 2.3, 10, 13, 14, 15, 16, 26, 27, 28, 29.1.a), 29.1.d), 31, 32, 33, 35, 36, 39, 48, 50, los apartados 1, 2 y 4 de la disposición adicional primera, la disposición adicional tercera, la disposición transitoria primera, la disposición transitoria segunda, la disposición transitoria tercera y la disposición transitoria cuarta del Real Decreto 1671/2009, de 6 de noviembre, por el que se desarrolla parcialmente la Ley 11/2007, de 22 de junio, de acceso electrónico de los ciudadanos a los Servicios Públicos.

Hasta que, de acuerdo con lo dispuesto en la disposición final séptima, produzcan efectos las previsiones relativas al registro electrónico de apoderamientos, registro electrónico, punto de acceso general electrónico de la Administración y archivo único electrónico, se mantendrán en vigor los artículos de las normas previstas en las letras a), b) y g) relativos a las materias mencionadas.

3. Las referencias contenidas en normas vigentes a las disposiciones que se derogan expresamente deberán entenderse efectuadas a las disposiciones de esta Ley que regulan la misma materia que aquéllas.

## 2. Relación electrónica, registros y solicitudes

<!-- bloque a14 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 14. Derecho y obligación de relacionarse electrónicamente con las Administraciones Públicas.

1. Las personas físicas podrán elegir en todo momento si se comunican con las Administraciones Públicas para el ejercicio de sus derechos y obligaciones a través de medios electrónicos o no, salvo que estén obligadas a relacionarse a través de medios electrónicos con las Administraciones Públicas. El medio elegido por la persona para comunicarse con las Administraciones Públicas podrá ser modificado por aquella en cualquier momento.

2. En todo caso, estarán obligados a relacionarse a través de medios electrónicos con las Administraciones Públicas para la realización de cualquier trámite de un procedimiento administrativo, al menos, los siguientes sujetos:

a) Las personas jurídicas.

b) Las entidades sin personalidad jurídica.

c) Quienes ejerzan una actividad profesional para la que se requiera colegiación obligatoria, para los trámites y actuaciones que realicen con las Administraciones Públicas en ejercicio de dicha actividad profesional. En todo caso, dentro de este colectivo se entenderán incluidos los notarios y registradores de la propiedad y mercantiles.

d) Quienes representen a un interesado que esté obligado a relacionarse electrónicamente con la Administración.

e) Los empleados de las Administraciones Públicas para los trámites y actuaciones que realicen con ellas por razón de su condición de empleado público, en la forma en que se determine reglamentariamente por cada Administración.

3. Reglamentariamente, las Administraciones podrán establecer la obligación de relacionarse con ellas a través de medios electrónicos para determinados procedimientos y para ciertos colectivos de personas físicas que por razón de su capacidad económica, técnica, dedicación profesional u otros motivos quede acreditado que tienen acceso y disponibilidad de los medios electrónicos necesarios.

<!-- bloque a16 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 16. Registros.

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

<!-- bloque a66 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 66. Solicitudes de iniciación.

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

<!-- bloque a68 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 68. Subsanación y mejora de la solicitud.

1. Si la solicitud de iniciación no reúne los requisitos que señala el artículo 66, y, en su caso, los que señala el artículo 67 u otros exigidos por la legislación específica aplicable, se requerirá al interesado para que, en un plazo de diez días, subsane la falta o acompañe los documentos preceptivos, con indicación de que, si así no lo hiciera, se le tendrá por desistido de su petición, previa resolución que deberá ser dictada en los términos previstos en el artículo 21.

2. Siempre que no se trate de procedimientos selectivos o de concurrencia competitiva, este plazo podrá ser ampliado prudencialmente, hasta cinco días, a petición del interesado o a iniciativa del órgano, cuando la aportación de los documentos requeridos presente dificultades especiales.

3. En los procedimientos iniciados a solicitud de los interesados, el órgano competente podrá recabar del solicitante la modificación o mejora voluntarias de los términos de aquélla. De ello se levantará acta sucinta, que se incorporará al procedimiento.

4. Si alguno de los sujetos a los que hace referencia el artículo 14.2 y 14.3 presenta su solicitud presencialmente, las Administraciones Públicas requerirán al interesado para que la subsane a través de su presentación electrónica. A estos efectos, se considerará como fecha de presentación de la solicitud aquella en la que haya sido realizada la subsanación.

<!-- bloque dfseptima · versión publicada 20210710 · vigente desde 20210711 -->

### Disposición final séptima. Entrada en vigor.

La presente Ley entrará en vigor al año de su publicación en el “Boletín Oficial del Estado”.

No obstante, las previsiones relativas al registro electrónico de apoderamientos, registro electrónico, registro de empleados públicos habilitados, punto de acceso general electrónico de la Administración y archivo único electrónico producirán efectos a partir del día 2 de abril de 2021.

> _Nota BOE: Se modifica por la disposición final 9 de la Ley 10/2021, de 9 de julio. Ref. BOE-A-2021-11472#df-9 Se modifica por la disposición final 9 del Real Decreto-ley 28/2020, de 22 de septiembre. Ref. BOE-A-2020-11043#df-9 Se deja sin efecto la modificación por Resolución de 10 de septiembre de 2020, que publica el Acuerdo del Congreso de los Diputados por el que se deroga el Real Decreto-ley 27/2020, de 4 de agosto. Ref. BOE-A-2020-10491 Se modifica por la disposición final 6 del Real Decreto-ley 27/2020, de 4 de agosto. Ref. BOE-A-2020-9131#df-6 Se modifica por el art. 6 del Real Decreto-ley 11/2018, de 31 de agosto. Ref. BOE-A-2018-12131#as-2_

## 3. Términos y plazos (arts. 29-32)

<!-- bloque a29 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 29. Obligatoriedad de términos y plazos.

Los términos y plazos establecidos en ésta u otras leyes obligan a las autoridades y personal al servicio de las Administraciones Públicas competentes para la tramitación de los asuntos, así como a los interesados en los mismos.

<!-- bloque a30 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 30. Cómputo de plazos.

1. Salvo que por Ley o en el Derecho de la Unión Europea se disponga otro cómputo, cuando los plazos se señalen por horas, se entiende que éstas son hábiles. Son hábiles todas las horas del día que formen parte de un día hábil.

Los plazos expresados por horas se contarán de hora en hora y de minuto en minuto desde la hora y minuto en que tenga lugar la notificación o publicación del acto de que se trate y no podrán tener una duración superior a veinticuatro horas, en cuyo caso se expresarán en días.

2. Siempre que por Ley o en el Derecho de la Unión Europea no se exprese otro cómputo, cuando los plazos se señalen por días, se entiende que éstos son hábiles, excluyéndose del cómputo los sábados, los domingos y los declarados festivos.

Cuando los plazos se hayan señalado por días naturales por declararlo así una ley o por el Derecho de la Unión Europea, se hará constar esta circunstancia en las correspondientes notificaciones.

3. Los plazos expresados en días se contarán a partir del día siguiente a aquel en que tenga lugar la notificación o publicación del acto de que se trate, o desde el siguiente a aquel en que se produzca la estimación o la desestimación por silencio administrativo.

4. Si el plazo se fija en meses o años, éstos se computarán a partir del día siguiente a aquel en que tenga lugar la notificación o publicación del acto de que se trate, o desde el siguiente a aquel en que se produzca la estimación o desestimación por silencio administrativo.

El plazo concluirá el mismo día en que se produjo la notificación, publicación o silencio administrativo en el mes o el año de vencimiento. Si en el mes de vencimiento no hubiera día equivalente a aquel en que comienza el cómputo, se entenderá que el plazo expira el último día del mes.

5. Cuando el último día del plazo sea inhábil, se entenderá prorrogado al primer día hábil siguiente.

6. Cuando un día fuese hábil en el municipio o Comunidad Autónoma en que residiese el interesado, e inhábil en la sede del órgano administrativo, o a la inversa, se considerará inhábil en todo caso.

7. La Administración General del Estado y las Administraciones de las Comunidades Autónomas, con sujeción al calendario laboral oficial, fijarán, en su respectivo ámbito, el calendario de días inhábiles a efectos de cómputos de plazos. El calendario aprobado por las Comunidades Autónomas comprenderá los días inhábiles de las Entidades Locales correspondientes a su ámbito territorial, a las que será de aplicación.

Dicho calendario deberá publicarse antes del comienzo de cada año en el diario oficial que corresponda, así como en otros medios de difusión que garanticen su conocimiento generalizado.

8. La declaración de un día como hábil o inhábil a efectos de cómputo de plazos no determina por sí sola el funcionamiento de los centros de trabajo de las Administraciones Públicas, la organización del tiempo de trabajo o el régimen de jornada y horarios de las mismas.

<!-- bloque a31 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 31. Cómputo de plazos en los registros.

1. Cada Administración Pública publicará los días y el horario en el que deban permanecer abiertas las oficinas que prestarán asistencia para la presentación electrónica de documentos, garantizando el derecho de los interesados a ser asistidos en el uso de medios electrónicos.

2. El registro electrónico de cada Administración u Organismo se regirá a efectos de cómputo de los plazos, por la fecha y hora oficial de la sede electrónica de acceso, que deberá contar con las medidas de seguridad necesarias para garantizar su integridad y figurar de modo accesible y visible.

El funcionamiento del registro electrónico se regirá por las siguientes reglas:

a) Permitirá la presentación de documentos todos los días del año durante las veinticuatro horas.

b) A los efectos del cómputo de plazo fijado en días hábiles, y en lo que se refiere al cumplimiento de plazos por los interesados, la presentación en un día inhábil se entenderá realizada en la primera hora del primer día hábil siguiente salvo que una norma permita expresamente la recepción en día inhábil.

Los documentos se considerarán presentados por el orden de hora efectiva en el que lo fueron en el día inhábil. Los documentos presentados en el día inhábil se reputarán anteriores, según el mismo orden, a los que lo fueran el primer día hábil posterior.

c) El inicio del cómputo de los plazos que hayan de cumplir las Administraciones Públicas vendrá determinado por la fecha y hora de presentación en el registro electrónico de cada Administración u Organismo. En todo caso, la fecha y hora efectiva de inicio del cómputo de plazos deberá ser comunicada a quien presentó el documento.

3. La sede electrónica del registro de cada Administración Pública u Organismo, determinará, atendiendo al ámbito territorial en el que ejerce sus competencias el titular de aquélla y al calendario previsto en el artículo 30.7, los días que se considerarán inhábiles a los efectos previstos en este artículo. Este será el único calendario de días inhábiles que se aplicará a efectos del cómputo de plazos en los registros electrónicos, sin que resulte de aplicación a los mismos lo dispuesto en el artículo 30.6.

<!-- bloque a32 · versión publicada 20220330 · vigente desde 20220331 -->

### Artículo 32. Ampliación.

1. La Administración, salvo precepto en contrario, podrá conceder de oficio o a petición de los interesados, una ampliación de los plazos establecidos, que no exceda de la mitad de los mismos, si las circunstancias lo aconsejan y con ello no se perjudican derechos de tercero. El acuerdo de ampliación deberá ser notificado a los interesados.

2. La ampliación de los plazos por el tiempo máximo permitido se aplicará en todo caso a los procedimientos tramitados por las misiones diplomáticas y oficinas consulares, así como a aquellos que, sustanciándose en el interior, exijan cumplimentar algún trámite en el extranjero o en los que intervengan interesados residentes fuera de España.

3. Tanto la petición de los interesados como la decisión sobre la ampliación deberán producirse, en todo caso, antes del vencimiento del plazo de que se trate. En ningún caso podrá ser objeto de ampliación un plazo ya vencido. Los acuerdos sobre ampliación de plazos o sobre su denegación no serán susceptibles de recurso, sin perjuicio del procedente contra la resolución que ponga fin al procedimiento.

4. Cuando una incidencia técnica haya imposibilitado el funcionamiento ordinario del sistema o aplicación que corresponda, y hasta que se solucione el problema, la Administración podrá determinar una ampliación de los plazos no vencidos, debiendo publicar en la sede electrónica tanto la incidencia técnica acontecida como la ampliación concreta del plazo no vencido.

5. Cuando como consecuencia de un ciberincidente se hayan visto gravemente afectados los servicios y sistemas utilizados para la tramitación de los procedimientos y el ejercicio de los derechos de los interesados que prevé la normativa vigente, la Administración podrá acordar la ampliación general de plazos de los procedimientos administrativos.

> _Nota BOE: Se añade el apartado 5 por la disposición final 21 del Real Decreto-ley 6/2022, de 29 de marzo. Ref. BOE-A-2022-4972#df-21_

## 4. Obligación de resolver, silencio y caducidad

<!-- bloque a21 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 21. Obligación de resolver.

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

<!-- bloque a22 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 22. Suspensión del plazo máximo para resolver.

1. El transcurso del plazo máximo legal para resolver un procedimiento y notificar la resolución se podrá suspender en los siguientes casos:

a) Cuando deba requerirse a cualquier interesado para la subsanación de deficiencias o la aportación de documentos y otros elementos de juicio necesarios, por el tiempo que medie entre la notificación del requerimiento y su efectivo cumplimiento por el destinatario, o, en su defecto, por el del plazo concedido, todo ello sin perjuicio de lo previsto en el artículo 68 de la presente Ley.

b) Cuando deba obtenerse un pronunciamiento previo y preceptivo de un órgano de la Unión Europea, por el tiempo que medie entre la petición, que habrá de comunicarse a los interesados, y la notificación del pronunciamiento a la Administración instructora, que también deberá serles comunicada.

c) Cuando exista un procedimiento no finalizado en el ámbito de la Unión Europea que condicione directamente el contenido de la resolución de que se trate, desde que se tenga constancia de su existencia, lo que deberá ser comunicado a los interesados, hasta que se resuelva, lo que también habrá de ser notificado.

d) Cuando se soliciten informes preceptivos a un órgano de la misma o distinta Administración, por el tiempo que medie entre la petición, que deberá comunicarse a los interesados, y la recepción del informe, que igualmente deberá ser comunicada a los mismos. Este plazo de suspensión no podrá exceder en ningún caso de tres meses. En caso de no recibirse el informe en el plazo indicado, proseguirá el procedimiento.

e) Cuando deban realizarse pruebas técnicas o análisis contradictorios o dirimentes propuestos por los interesados, durante el tiempo necesario para la incorporación de los resultados al expediente.

f) Cuando se inicien negociaciones con vistas a la conclusión de un pacto o convenio en los términos previstos en el artículo 86 de esta Ley, desde la declaración formal al respecto y hasta la conclusión sin efecto, en su caso, de las referidas negociaciones, que se constatará mediante declaración formulada por la Administración o los interesados.

g) Cuando para la resolución del procedimiento sea indispensable la obtención de un previo pronunciamiento por parte de un órgano jurisdiccional, desde el momento en que se solicita, lo que habrá de comunicarse a los interesados, hasta que la Administración tenga constancia del mismo, lo que también deberá serles comunicado.

2. El transcurso del plazo máximo legal para resolver un procedimiento y notificar la resolución se suspenderá en los siguientes casos:

a) Cuando una Administración Pública requiera a otra para que anule o revise un acto que entienda que es ilegal y que constituya la base para el que la primera haya de dictar en el ámbito de sus competencias, en el supuesto al que se refiere el apartado 5 del artículo 39 de esta Ley, desde que se realiza el requerimiento hasta que se atienda o, en su caso, se resuelva el recurso interpuesto ante la jurisdicción contencioso administrativa. Deberá ser comunicado a los interesados tanto la realización del requerimiento, como su cumplimiento o, en su caso, la resolución del correspondiente recurso contencioso-administrativo.

b) Cuando el órgano competente para resolver decida realizar alguna actuación complementaria de las previstas en el artículo 87, desde el momento en que se notifique a los interesados el acuerdo motivado del inicio de las actuaciones hasta que se produzca su terminación.

c) Cuando los interesados promuevan la recusación en cualquier momento de la tramitación de un procedimiento, desde que ésta se plantee hasta que sea resuelta por el superior jerárquico del recusado.

<!-- bloque a24 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 24. Silencio administrativo en procedimientos iniciados a solicitud del interesado.

1. En los procedimientos iniciados a solicitud del interesado, sin perjuicio de la resolución que la Administración debe dictar en la forma prevista en el apartado 3 de este artículo, el vencimiento del plazo máximo sin haberse notificado resolución expresa, legitima al interesado o interesados para entenderla estimada por silencio administrativo, excepto en los supuestos en los que una norma con rango de ley o una norma de Derecho de la Unión Europea o de Derecho internacional aplicable en España establezcan lo contrario. Cuando el procedimiento tenga por objeto el acceso a actividades o su ejercicio, la ley que disponga el carácter desestimatorio del silencio deberá fundarse en la concurrencia de razones imperiosas de interés general.

El silencio tendrá efecto desestimatorio en los procedimientos relativos al ejercicio del derecho de petición, a que se refiere el artículo 29 de la Constitución, aquellos cuya estimación tuviera como consecuencia que se transfirieran al solicitante o a terceros facultades relativas al dominio público o al servicio público, impliquen el ejercicio de actividades que puedan dañar el medio ambiente y en los procedimientos de responsabilidad patrimonial de las Administraciones Públicas.

El sentido del silencio también será desestimatorio en los procedimientos de impugnación de actos y disposiciones y en los de revisión de oficio iniciados a solicitud de los interesados. No obstante, cuando el recurso de alzada se haya interpuesto contra la desestimación por silencio administrativo de una solicitud por el transcurso del plazo, se entenderá estimado el mismo si, llegado el plazo de resolución, el órgano administrativo competente no dictase y notificase resolución expresa, siempre que no se refiera a las materias enumeradas en el párrafo anterior de este apartado.

2. La estimación por silencio administrativo tiene a todos los efectos la consideración de acto administrativo finalizador del procedimiento. La desestimación por silencio administrativo tiene los solos efectos de permitir a los interesados la interposición del recurso administrativo o contencioso-administrativo que resulte procedente.

3. La obligación de dictar resolución expresa a que se refiere el apartado primero del artículo 21 se sujetará al siguiente régimen:

a) En los casos de estimación por silencio administrativo, la resolución expresa posterior a la producción del acto sólo podrá dictarse de ser confirmatoria del mismo.

b) En los casos de desestimación por silencio administrativo, la resolución expresa posterior al vencimiento del plazo se adoptará por la Administración sin vinculación alguna al sentido del silencio.

4. Los actos administrativos producidos por silencio administrativo se podrán hacer valer tanto ante la Administración como ante cualquier persona física o jurídica, pública o privada. Los mismos producen efectos desde el vencimiento del plazo máximo en el que debe dictarse y notificarse la resolución expresa sin que la misma se haya expedido, y su existencia puede ser acreditada por cualquier medio de prueba admitido en Derecho, incluido el certificado acreditativo del silencio producido. Este certificado se expedirá de oficio por el órgano competente para resolver en el plazo de quince días desde que expire el plazo máximo para resolver el procedimiento. Sin perjuicio de lo anterior, el interesado podrá pedirlo en cualquier momento, computándose el plazo indicado anteriormente desde el día siguiente a aquél en que la petición tuviese entrada en el registro electrónico de la Administración u Organismo competente para resolver.

<!-- bloque a25 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 25. Falta de resolución expresa en procedimientos iniciados de oficio.

1. En los procedimientos iniciados de oficio, el vencimiento del plazo máximo establecido sin que se haya dictado y notificado resolución expresa no exime a la Administración del cumplimiento de la obligación legal de resolver, produciendo los siguientes efectos:

a) En el caso de procedimientos de los que pudiera derivarse el reconocimiento o, en su caso, la constitución de derechos u otras situaciones jurídicas favorables, los interesados que hubieren comparecido podrán entender desestimadas sus pretensiones por silencio administrativo.

b) En los procedimientos en que la Administración ejercite potestades sancionadoras o, en general, de intervención, susceptibles de producir efectos desfavorables o de gravamen, se producirá la caducidad. En estos casos, la resolución que declare la caducidad ordenará el archivo de las actuaciones, con los efectos previstos en el artículo 95.

2. En los supuestos en los que el procedimiento se hubiera paralizado por causa imputable al interesado, se interrumpirá el cómputo del plazo para resolver y notificar la resolución.

<!-- bloque a95 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 95. Requisitos y efectos.

1. En los procedimientos iniciados a solicitud del interesado, cuando se produzca su paralización por causa imputable al mismo, la Administración le advertirá que, transcurridos tres meses, se producirá la caducidad del procedimiento. Consumido este plazo sin que el particular requerido realice las actividades necesarias para reanudar la tramitación, la Administración acordará el archivo de las actuaciones, notificándoselo al interesado. Contra la resolución que declare la caducidad procederán los recursos pertinentes.

2. No podrá acordarse la caducidad por la simple inactividad del interesado en la cumplimentación de trámites, siempre que no sean indispensables para dictar resolución. Dicha inactividad no tendrá otro efecto que la pérdida de su derecho al referido trámite.

3. La caducidad no producirá por sí sola la prescripción de las acciones del particular o de la Administración, pero los procedimientos caducados no interrumpirán el plazo de prescripción.

En los casos en los que sea posible la iniciación de un nuevo procedimiento por no haberse producido la prescripción, podrán incorporarse a éste los actos y trámites cuyo contenido se hubiera mantenido igual de no haberse producido la caducidad. En todo caso, en el nuevo procedimiento deberán cumplimentarse los trámites de alegaciones, proposición de prueba y audiencia al interesado.

4. Podrá no ser aplicable la caducidad en el supuesto de que la cuestión suscitada afecte al interés general, o fuera conveniente sustanciarla para su definición y esclarecimiento.

## 5. Notificaciones (arts. 40-46)

<!-- bloque a40 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 40. Notificación.

1. El órgano que dicte las resoluciones y actos administrativos los notificará a los interesados cuyos derechos e intereses sean afectados por aquéllos, en los términos previstos en los artículos siguientes.

2. Toda notificación deberá ser cursada dentro del plazo de diez días a partir de la fecha en que el acto haya sido dictado, y deberá contener el texto íntegro de la resolución, con indicación de si pone fin o no a la vía administrativa, la expresión de los recursos que procedan, en su caso, en vía administrativa y judicial, el órgano ante el que hubieran de presentarse y el plazo para interponerlos, sin perjuicio de que los interesados puedan ejercitar, en su caso, cualquier otro que estimen procedente.

3. Las notificaciones que, conteniendo el texto íntegro del acto, omitiesen alguno de los demás requisitos previstos en el apartado anterior, surtirán efecto a partir de la fecha en que el interesado realice actuaciones que supongan el conocimiento del contenido y alcance de la resolución o acto objeto de la notificación, o interponga cualquier recurso que proceda.

4. Sin perjuicio de lo establecido en el apartado anterior, y a los solos efectos de entender cumplida la obligación de notificar dentro del plazo máximo de duración de los procedimientos, será suficiente la notificación que contenga, cuando menos, el texto íntegro de la resolución, así como el intento de notificación debidamente acreditado.

5. Las Administraciones Públicas podrán adoptar las medidas que consideren necesarias para la protección de los datos personales que consten en las resoluciones y actos administrativos, cuando éstos tengan por destinatarios a más de un interesado.

<!-- bloque a41 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 41. Condiciones generales para la práctica de las notificaciones.

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

<!-- bloque a42 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 42. Práctica de las notificaciones en papel.

1. Todas las notificaciones que se practiquen en papel deberán ser puestas a disposición del interesado en la sede electrónica de la Administración u Organismo actuante para que pueda acceder al contenido de las mismas de forma voluntaria.

2. Cuando la notificación se practique en el domicilio del interesado, de no hallarse presente éste en el momento de entregarse la notificación, podrá hacerse cargo de la misma cualquier persona mayor de catorce años que se encuentre en el domicilio y haga constar su identidad. Si nadie se hiciera cargo de la notificación, se hará constar esta circunstancia en el expediente, junto con el día y la hora en que se intentó la notificación, intento que se repetirá por una sola vez y en una hora distinta dentro de los tres días siguientes. En caso de que el primer intento de notificación se haya realizado antes de las quince horas, el segundo intento deberá realizarse después de las quince horas y viceversa, dejando en todo caso al menos un margen de diferencia de tres horas entre ambos intentos de notificación. Si el segundo intento también resultara infructuoso, se procederá en la forma prevista en el artículo 44.

3. Cuando el interesado accediera al contenido de la notificación en sede electrónica, se le ofrecerá la posibilidad de que el resto de notificaciones se puedan realizar a través de medios electrónicos.

<!-- bloque a43 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 43. Práctica de las notificaciones a través de medios electrónicos.

1. Las notificaciones por medios electrónicos se practicarán mediante comparecencia en la sede electrónica de la Administración u Organismo actuante, a través de la dirección electrónica habilitada única o mediante ambos sistemas, según disponga cada Administración u Organismo.

A los efectos previstos en este artículo, se entiende por comparecencia en la sede electrónica, el acceso por el interesado o su representante debidamente identificado al contenido de la notificación.

2. Las notificaciones por medios electrónicos se entenderán practicadas en el momento en que se produzca el acceso a su contenido.

Cuando la notificación por medios electrónicos sea de carácter obligatorio, o haya sido expresamente elegida por el interesado, se entenderá rechazada cuando hayan transcurrido diez días naturales desde la puesta a disposición de la notificación sin que se acceda a su contenido.

3. Se entenderá cumplida la obligación a la que se refiere el artículo 40.4 con la puesta a disposición de la notificación en la sede electrónica de la Administración u Organismo actuante o en la dirección electrónica habilitada única.

4. Los interesados podrán acceder a las notificaciones desde el Punto de Acceso General electrónico de la Administración, que funcionará como un portal de acceso.

<!-- bloque a44 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 44. Notificación infructuosa.

Cuando los interesados en un procedimiento sean desconocidos, se ignore el lugar de la notificación o bien, intentada ésta, no se hubiese podido practicar, la notificación se hará por medio de un anuncio publicado en el «Boletín Oficial del Estado».

Asimismo, previamente y con carácter facultativo, las Administraciones podrán publicar un anuncio en el boletín oficial de la Comunidad Autónoma o de la Provincia, en el tablón de edictos del Ayuntamiento del último domicilio del interesado o del Consulado o Sección Consular de la Embajada correspondiente.

Las Administraciones Públicas podrán establecer otras formas de notificación complementarias a través de los restantes medios de difusión, que no excluirán la obligación de publicar el correspondiente anuncio en el «Boletín Oficial del Estado».

<!-- bloque a45 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 45. Publicación.

1. Los actos administrativos serán objeto de publicación cuando así lo establezcan las normas reguladoras de cada procedimiento o cuando lo aconsejen razones de interés público apreciadas por el órgano competente.

En todo caso, los actos administrativos serán objeto de publicación, surtiendo ésta los efectos de la notificación, en los siguientes casos:

a) Cuando el acto tenga por destinatario a una pluralidad indeterminada de personas o cuando la Administración estime que la notificación efectuada a un solo interesado es insuficiente para garantizar la notificación a todos, siendo, en este último caso, adicional a la individualmente realizada.

b) Cuando se trate de actos integrantes de un procedimiento selectivo o de concurrencia competitiva de cualquier tipo. En este caso, la convocatoria del procedimiento deberá indicar el medio donde se efectuarán las sucesivas publicaciones, careciendo de validez las que se lleven a cabo en lugares distintos.

2. La publicación de un acto deberá contener los mismos elementos que el artículo 40.2 exige respecto de las notificaciones. Será también aplicable a la publicación lo establecido en el apartado 3 del mismo artículo.

En los supuestos de publicaciones de actos que contengan elementos comunes, podrán publicarse de forma conjunta los aspectos coincidentes, especificándose solamente los aspectos individuales de cada acto.

3. La publicación de los actos se realizará en el diario oficial que corresponda, según cual sea la Administración de la que proceda el acto a notificar.

4. Sin perjuicio de lo dispuesto en el artículo 44, la publicación de actos y comunicaciones que, por disposición legal o reglamentaria deba practicarse en tablón de anuncios o edictos, se entenderá cumplida por su publicación en el Diario oficial correspondiente.

<!-- bloque a46 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 46. Indicación de notificaciones y publicaciones.

Si el órgano competente apreciase que la notificación por medio de anuncios o la publicación de un acto lesiona derechos o intereses legítimos, se limitará a publicar en el Diario oficial que corresponda una somera indicación del contenido del acto y del lugar donde los interesados podrán comparecer, en el plazo que se establezca, para conocimiento del contenido íntegro del mencionado acto y constancia de tal conocimiento.

Adicionalmente y de manera facultativa, las Administraciones podrán establecer otras formas de notificación complementarias a través de los restantes medios de difusión que no excluirán la obligación de publicar en el correspondiente Diario oficial.

## 6. Nulidad y anulabilidad (motivos de recurso)

<!-- bloque a47 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 47. Nulidad de pleno derecho.

1. Los actos de las Administraciones Públicas son nulos de pleno derecho en los casos siguientes:

a) Los que lesionen los derechos y libertades susceptibles de amparo constitucional.

b) Los dictados por órgano manifiestamente incompetente por razón de la materia o del territorio.

c) Los que tengan un contenido imposible.

d) Los que sean constitutivos de infracción penal o se dicten como consecuencia de ésta.

e) Los dictados prescindiendo total y absolutamente del procedimiento legalmente establecido o de las normas que contienen las reglas esenciales para la formación de la voluntad de los órganos colegiados.

f) Los actos expresos o presuntos contrarios al ordenamiento jurídico por los que se adquieren facultades o derechos cuando se carezca de los requisitos esenciales para su adquisición.

g) Cualquier otro que se establezca expresamente en una disposición con rango de Ley.

2. También serán nulas de pleno derecho las disposiciones administrativas que vulneren la Constitución, las leyes u otras disposiciones administrativas de rango superior, las que regulen materias reservadas a la Ley, y las que establezcan la retroactividad de disposiciones sancionadoras no favorables o restrictivas de derechos individuales.

<!-- bloque a48 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 48. Anulabilidad.

1. Son anulables los actos de la Administración que incurran en cualquier infracción del ordenamiento jurídico, incluso la desviación de poder.

2. No obstante, el defecto de forma sólo determinará la anulabilidad cuando el acto carezca de los requisitos formales indispensables para alcanzar su fin o dé lugar a la indefensión de los interesados.

3. La realización de actuaciones administrativas fuera del tiempo establecido para ellas sólo implicará la anulabilidad del acto cuando así lo imponga la naturaleza del término o plazo.

## 7. Especialidades del procedimiento sancionador

<!-- bloque a53 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 53. Derechos del interesado en el procedimiento administrativo.

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

<!-- bloque a63 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 63. Especialidades en el inicio de los procedimientos de naturaleza sancionadora.

1. Los procedimientos de naturaleza sancionadora se iniciarán siempre de oficio por acuerdo del órgano competente y establecerán la debida separación entre la fase instructora y la sancionadora, que se encomendará a órganos distintos.

Se considerará que un órgano es competente para iniciar el procedimiento cuando así lo determinen las normas reguladoras del mismo.

2. En ningún caso se podrá imponer una sanción sin que se haya tramitado el oportuno procedimiento.

3. No se podrán iniciar nuevos procedimientos de carácter sancionador por hechos o conductas tipificadas como infracciones en cuya comisión el infractor persista de forma continuada, en tanto no haya recaído una primera resolución sancionadora, con carácter ejecutivo.

<!-- bloque a64 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 64. Acuerdo de iniciación en los procedimientos de naturaleza sancionadora.

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

<!-- bloque a85 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 85. Terminación en los procedimientos sancionadores.

1. Iniciado un procedimiento sancionador, si el infractor reconoce su responsabilidad, se podrá resolver el procedimiento con la imposición de la sanción que proceda.

2. Cuando la sanción tenga únicamente carácter pecuniario o bien quepa imponer una sanción pecuniaria y otra de carácter no pecuniario pero se ha justificado la improcedencia de la segunda, el pago voluntario por el presunto responsable, en cualquier momento anterior a la resolución, implicará la terminación del procedimiento, salvo en lo relativo a la reposición de la situación alterada o a la determinación de la indemnización por los daños y perjuicios causados por la comisión de la infracción.

3. En ambos casos, cuando la sanción tenga únicamente carácter pecuniario, el órgano competente para resolver el procedimiento aplicará reducciones de, al menos, el 20 % sobre el importe de la sanción propuesta, siendo éstos acumulables entre sí. Las citadas reducciones, deberán estar determinadas en la notificación de iniciación del procedimiento y su efectividad estará condicionada al desistimiento o renuncia de cualquier acción o recurso en vía administrativa contra la sanción.

El porcentaje de reducción previsto en este apartado podrá ser incrementado reglamentariamente.

<!-- bloque a89 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 89. Propuesta de resolución en los procedimientos de carácter sancionador.

1. El órgano instructor resolverá la finalización del procedimiento, con archivo de las actuaciones, sin que sea necesaria la formulación de la propuesta de resolución, cuando en la instrucción procedimiento se ponga de manifiesto que concurre alguna de las siguientes circunstancias:

a) La inexistencia de los hechos que pudieran constituir la infracción.

b) Cuando los hechos no resulten acreditados.

c) Cuando los hechos probados no constituyan, de modo manifiesto, infracción administrativa.

d) Cuando no exista o no se haya podido identificar a la persona o personas responsables o bien aparezcan exentos de responsabilidad.

e) Cuando se concluyera, en cualquier momento, que ha prescrito la infracción.

2. En el caso de procedimientos de carácter sancionador, una vez concluida la instrucción del procedimiento, el órgano instructor formulará una propuesta de resolución que deberá ser notificada a los interesados. La propuesta de resolución deberá indicar la puesta de manifiesto del procedimiento y el plazo para formular alegaciones y presentar los documentos e informaciones que se estimen pertinentes.

3. En la propuesta de resolución se fijarán de forma motivada los hechos que se consideren probados y su exacta calificación jurídica, se determinará la infracción que, en su caso, aquéllos constituyan, la persona o personas responsables y la sanción que se proponga, la valoración de las pruebas practicadas, en especial aquellas que constituyan los fundamentos básicos de la decisión, así como las medidas provisionales que, en su caso, se hubieran adoptado. Cuando la instrucción concluya la inexistencia de infracción o responsabilidad y no se haga uso de la facultad prevista en el apartado primero, la propuesta declarará esa circunstancia.

<!-- bloque a90 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 90. Especialidades de la resolución en los procedimientos sancionadores.

1. En el caso de procedimientos de carácter sancionador, además del contenido previsto en los dos artículos anteriores, la resolución incluirá la valoración de las pruebas practicadas, en especial aquellas que constituyan los fundamentos básicos de la decisión, fijarán los hechos y, en su caso, la persona o personas responsables, la infracción o infracciones cometidas y la sanción o sanciones que se imponen, o bien la declaración de no existencia de infracción o responsabilidad.

2. En la resolución no se podrán aceptar hechos distintos de los determinados en el curso del procedimiento, con independencia de su diferente valoración jurídica. No obstante, cuando el órgano competente para resolver considere que la infracción o la sanción revisten mayor gravedad que la determinada en la propuesta de resolución, se notificará al inculpado para que aporte cuantas alegaciones estime convenientes en el plazo de quince días.

3. La resolución que ponga fin al procedimiento será ejecutiva cuando no quepa contra ella ningún recurso ordinario en vía administrativa, pudiendo adoptarse en la misma las disposiciones cautelares precisas para garantizar su eficacia en tanto no sea ejecutiva y que podrán consistir en el mantenimiento de las medidas provisionales que en su caso se hubieran adoptado.

Cuando la resolución sea ejecutiva, se podrá suspender cautelarmente, si el interesado manifiesta a la Administración su intención de interponer recurso contencioso-administrativo contra la resolución firme en vía administrativa. Dicha suspensión cautelar finalizará cuando:

a) Haya transcurrido el plazo legalmente previsto sin que el interesado haya interpuesto recurso contencioso-administrativo.

b) Habiendo el interesado interpuesto recurso contencioso-administrativo:

1.º No se haya solicitado en el mismo trámite la suspensión cautelar de la resolución impugnada.

2.º El órgano judicial se pronuncie sobre la suspensión cautelar solicitada, en los términos previstos en ella.

4. Cuando las conductas sancionadas hubieran causado daños o perjuicios a las Administraciones y la cuantía destinada a indemnizar estos daños no hubiera quedado determinada en el expediente, se fijará mediante un procedimiento complementario, cuya resolución será inmediatamente ejecutiva. Este procedimiento será susceptible de terminación convencional, pero ni ésta ni la aceptación por el infractor de la resolución que pudiera recaer implicarán el reconocimiento voluntario de su responsabilidad. La resolución del procedimiento pondrá fin a la vía administrativa.

<!-- bloque a98 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 98. Ejecutoriedad.

1. Los actos de las Administraciones Públicas sujetos al Derecho Administrativo serán inmediatamente ejecutivos, salvo que:

a) Se produzca la suspensión de la ejecución del acto.

b) Se trate de una resolución de un procedimiento de naturaleza sancionadora contra la que quepa algún recurso en vía administrativa, incluido el potestativo de reposición.

c) Una disposición establezca lo contrario.

d) Se necesite aprobación o autorización superior.

2. Cuando de una resolución administrativa, o de cualquier otra forma de finalización del procedimiento administrativo prevista en esta ley, nazca una obligación de pago derivada de una sanción pecuniaria, multa o cualquier otro derecho que haya de abonarse a la Hacienda pública, éste se efectuará preferentemente, salvo que se justifique la imposibilidad de hacerlo, utilizando alguno de los medios electrónicos siguientes:

a) Tarjeta de crédito y débito.

b) Transferencia bancaria.

c) Domiciliación bancaria.

d) Cualesquiera otros que se autoricen por el órgano competente en materia de Hacienda Pública.

## 8.1 Recursos administrativos: disposiciones generales (arts. 112-120)

<!-- bloque a112 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 112. Objeto y clases.

1. Contra las resoluciones y los actos de trámite, si estos últimos deciden directa o indirectamente el fondo del asunto, determinan la imposibilidad de continuar el procedimiento, producen indefensión o perjuicio irreparable a derechos e intereses legítimos, podrán interponerse por los interesados los recursos de alzada y potestativo de reposición, que cabrá fundar en cualquiera de los motivos de nulidad o anulabilidad previstos en los artículos 47 y 48 de esta Ley.

La oposición a los restantes actos de trámite podrá alegarse por los interesados para su consideración en la resolución que ponga fin al procedimiento.

2. Las leyes podrán sustituir el recurso de alzada, en supuestos o ámbitos sectoriales determinados, y cuando la especificidad de la materia así lo justifique, por otros procedimientos de impugnación, reclamación, conciliación, mediación y arbitraje, ante órganos colegiados o Comisiones específicas no sometidas a instrucciones jerárquicas, con respeto a los principios, garantías y plazos que la presente Ley reconoce a las personas y a los interesados en todo procedimiento administrativo.

En las mismas condiciones, el recurso de reposición podrá ser sustituido por los procedimientos a que se refiere el párrafo anterior, respetando su carácter potestativo para el interesado.

La aplicación de estos procedimientos en el ámbito de la Administración Local no podrá suponer el desconocimiento de las facultades resolutorias reconocidas a los órganos representativos electos establecidos por la Ley.

3. Contra las disposiciones administrativas de carácter general no cabrá recurso en vía administrativa.

Los recursos contra un acto administrativo que se funden únicamente en la nulidad de alguna disposición administrativa de carácter general podrán interponerse directamente ante el órgano que dictó dicha disposición.

4. Las reclamaciones económico-administrativas se ajustarán a los procedimientos establecidos por su legislación específica.

<!-- bloque a113 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 113. Recurso extraordinario de revisión.

Contra los actos firmes en vía administrativa, sólo procederá el recurso extraordinario de revisión cuando concurra alguna de las circunstancias previstas en el artículo 125.1.

<!-- bloque a114 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 114. Fin de la vía administrativa.

1. Ponen fin a la vía administrativa:

a) Las resoluciones de los recursos de alzada.

b) Las resoluciones de los procedimientos a que se refiere el artículo 112.2.

c) Las resoluciones de los órganos administrativos que carezcan de superior jerárquico, salvo que una Ley establezca lo contrario.

d) Los acuerdos, pactos, convenios o contratos que tengan la consideración de finalizadores del procedimiento.

e) La resolución administrativa de los procedimientos de responsabilidad patrimonial, cualquiera que fuese el tipo de relación, pública o privada, de que derive.

f) La resolución de los procedimientos complementarios en materia sancionadora a los que se refiere el artículo 90.4.

g) Las demás resoluciones de órganos administrativos cuando una disposición legal o reglamentaria así lo establezca.

2. Además de lo previsto en el apartado anterior, en el ámbito estatal ponen fin a la vía administrativa los actos y resoluciones siguientes:

a) Los actos administrativos de los miembros y órganos del Gobierno.

b) Los emanados de los Ministros y los Secretarios de Estado en el ejercicio de las competencias que tienen atribuidas los órganos de los que son titulares.

c) Los emanados de los órganos directivos con nivel de Director general o superior, en relación con las competencias que tengan atribuidas en materia de personal.

d) En los Organismos públicos y entidades de derecho público vinculados o dependientes de la Administración General del Estado, los emanados de los máximos órganos de dirección unipersonales o colegiados, de acuerdo con lo que establezcan sus estatutos, salvo que por ley se establezca otra cosa.

<!-- bloque a115 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 115. Interposición de recurso.

1. La interposición del recurso deberá expresar:

a) El nombre y apellidos del recurrente, así como la identificación personal del mismo.

b) El acto que se recurre y la razón de su impugnación.

c) Lugar, fecha, firma del recurrente, identificación del medio y, en su caso, del lugar que se señale a efectos de notificaciones.

d) Órgano, centro o unidad administrativa al que se dirige y su correspondiente código de identificación.

e) Las demás particularidades exigidas, en su caso, por las disposiciones específicas.

2. El error o la ausencia de la calificación del recurso por parte del recurrente no será obstáculo para su tramitación, siempre que se deduzca su verdadero carácter.

3. Los vicios y defectos que hagan anulable un acto no podrán ser alegados por quienes los hubieren causado.

<!-- bloque a116 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 116. Causas de inadmisión.

Serán causas de inadmisión las siguientes:

a) Ser incompetente el órgano administrativo, cuando el competente perteneciera a otra Administración Pública. El recurso deberá remitirse al órgano competente, de acuerdo con lo establecido en el artículo 14.1 de la Ley de Régimen Jurídico del Sector Público.

b) Carecer de legitimación el recurrente.

c) Tratarse de un acto no susceptible de recurso.

d) Haber transcurrido el plazo para la interposición del recurso.

e) Carecer el recurso manifiestamente de fundamento.

<!-- bloque a117 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 117. Suspensión de la ejecución.

1. La interposición de cualquier recurso, excepto en los casos en que una disposición establezca lo contrario, no suspenderá la ejecución del acto impugnado.

2. No obstante lo dispuesto en el apartado anterior, el órgano a quien competa resolver el recurso, previa ponderación, suficientemente razonada, entre el perjuicio que causaría al interés público o a terceros la suspensión y el ocasionado al recurrente como consecuencia de la eficacia inmediata del acto recurrido, podrá suspender, de oficio o a solicitud del recurrente, la ejecución del acto impugnado cuando concurran alguna de las siguientes circunstancias:

a) Que la ejecución pudiera causar perjuicios de imposible o difícil reparación.

b) Que la impugnación se fundamente en alguna de las causas de nulidad de pleno derecho previstas en el artículo 47.1 de esta Ley.

3. La ejecución del acto impugnado se entenderá suspendida si transcurrido un mes desde que la solicitud de suspensión haya tenido entrada en el registro electrónico de la Administración u Organismo competente para decidir sobre la misma, el órgano a quien competa resolver el recurso no ha dictado y notificado resolución expresa al respecto. En estos casos, no será de aplicación lo establecido en el artículo 21.4 segundo párrafo, de esta Ley.

4. Al dictar el acuerdo de suspensión podrán adoptarse las medidas cautelares que sean necesarias para asegurar la protección del interés público o de terceros y la eficacia de la resolución o el acto impugnado.

Cuando de la suspensión puedan derivarse perjuicios de cualquier naturaleza, aquélla sólo producirá efectos previa prestación de caución o garantía suficiente para responder de ellos, en los términos establecidos reglamentariamente.

La suspensión se prolongará después de agotada la vía administrativa cuando, habiéndolo solicitado previamente el interesado, exista medida cautelar y los efectos de ésta se extiendan a la vía contencioso-administrativa. Si el interesado interpusiera recurso contencioso-administrativo, solicitando la suspensión del acto objeto del proceso, se mantendrá la suspensión hasta que se produzca el correspondiente pronunciamiento judicial sobre la solicitud.

5. Cuando el recurso tenga por objeto la impugnación de un acto administrativo que afecte a una pluralidad indeterminada de personas, la suspensión de su eficacia habrá de ser publicada en el periódico oficial en que aquél se insertó.

<!-- bloque a118 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 118. Audiencia de los interesados.

1. Cuando hayan de tenerse en cuenta nuevos hechos o documentos no recogidos en el expediente originario, se pondrán de manifiesto a los interesados para que, en un plazo no inferior a diez días ni superior a quince, formulen las alegaciones y presenten los documentos y justificantes que estimen procedentes.

No se tendrán en cuenta en la resolución de los recursos, hechos, documentos o alegaciones del recurrente, cuando habiendo podido aportarlos en el trámite de alegaciones no lo haya hecho. Tampoco podrá solicitarse la práctica de pruebas cuando su falta de realización en el procedimiento en el que se dictó la resolución recurrida fuera imputable al interesado.

2. Si hubiera otros interesados se les dará, en todo caso, traslado del recurso para que en el plazo antes citado, aleguen cuanto estimen procedente.

3. El recurso, los informes y las propuestas no tienen el carácter de documentos nuevos a los efectos de este artículo. Tampoco lo tendrán los que los interesados hayan aportado al expediente antes de recaer la resolución impugnada.

<!-- bloque a119 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 119. Resolución.

1. La resolución del recurso estimará en todo o en parte o desestimará las pretensiones formuladas en el mismo o declarará su inadmisión.

2. Cuando existiendo vicio de forma no se estime procedente resolver sobre el fondo se ordenará la retroacción del procedimiento al momento en el que el vicio fue cometido, sin perjuicio de que eventualmente pueda acordarse la convalidación de actuaciones por el órgano competente para ello, de acuerdo con lo dispuesto en el artículo 52.

3. El órgano que resuelva el recurso decidirá cuantas cuestiones, tanto de forma como de fondo, plantee el procedimiento, hayan sido o no alegadas por los interesados. En este último caso se les oirá previamente. No obstante, la resolución será congruente con las peticiones formuladas por el recurrente, sin que en ningún caso pueda agravarse su situación inicial.

<!-- bloque a120 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 120. Pluralidad de recursos administrativos.

1. Cuando deban resolverse una pluralidad de recursos administrativos que traigan causa de un mismo acto administrativo y se hubiera interpuesto un recurso judicial contra una resolución administrativa o bien contra el correspondiente acto presunto desestimatorio, el órgano administrativo podrá acordar la suspensión del plazo para resolver hasta que recaiga pronunciamiento judicial.

2. El acuerdo de suspensión deberá ser notificado a los interesados, quienes podrán recurrirlo.

La interposición del correspondiente recurso por un interesado, no afectará a los restantes procedimientos de recurso que se encuentren suspendidos por traer causa del mismo acto administrativo.

3. Recaído el pronunciamiento judicial, será comunicado a los interesados y el órgano administrativo competente para resolver podrá dictar resolución sin necesidad de realizar ningún trámite adicional, salvo el de audiencia, cuando proceda.

## 8.2 Recurso de alzada (arts. 121-122)

<!-- bloque a121 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 121. Objeto.

1. Las resoluciones y actos a que se refiere el artículo 112.1, cuando no pongan fin a la vía administrativa, podrán ser recurridos en alzada ante el órgano superior jerárquico del que los dictó. A estos efectos, los Tribunales y órganos de selección del personal al servicio de las Administraciones Públicas y cualesquiera otros que, en el seno de éstas, actúen con autonomía funcional, se considerarán dependientes del órgano al que estén adscritos o, en su defecto, del que haya nombrado al presidente de los mismos.

2. El recurso podrá interponerse ante el órgano que dictó el acto que se impugna o ante el competente para resolverlo.

Si el recurso se hubiera interpuesto ante el órgano que dictó el acto impugnado, éste deberá remitirlo al competente en el plazo de diez días, con su informe y con una copia completa y ordenada del expediente.

El titular del órgano que dictó el acto recurrido será responsable directo del cumplimiento de lo previsto en el párrafo anterior.

<!-- bloque a122 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 122. Plazos.

1. El plazo para la interposición del recurso de alzada será de un mes, si el acto fuera expreso. Transcurrido dicho plazo sin haberse interpuesto el recurso, la resolución será firme a todos los efectos.

Si el acto no fuera expreso el solicitante y otros posibles interesados podrán interponer recurso de alzada en cualquier momento a partir del día siguiente a aquel en que, de acuerdo con su normativa específica, se produzcan los efectos del silencio administrativo.

2. El plazo máximo para dictar y notificar la resolución será de tres meses. Transcurrido este plazo sin que recaiga resolución, se podrá entender desestimado el recurso, salvo en el supuesto previsto en el artículo 24.1, tercer párrafo.

3. Contra la resolución de un recurso de alzada no cabrá ningún otro recurso administrativo, salvo el recurso extraordinario de revisión, en los casos establecidos en el artículo 125.1.

## 8.3 Recurso potestativo de reposición (arts. 123-124)

<!-- bloque a123 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 123. Objeto y naturaleza.

1. Los actos administrativos que pongan fin a la vía administrativa podrán ser recurridos potestativamente en reposición ante el mismo órgano que los hubiera dictado o ser impugnados directamente ante el orden jurisdiccional contencioso-administrativo.

2. No se podrá interponer recurso contencioso-administrativo hasta que sea resuelto expresamente o se haya producido la desestimación presunta del recurso de reposición interpuesto.

<!-- bloque a124 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 124. Plazos.

1. El plazo para la interposición del recurso de reposición será de un mes, si el acto fuera expreso. Transcurrido dicho plazo, únicamente podrá interponerse recurso contencioso-administrativo, sin perjuicio, en su caso, de la procedencia del recurso extraordinario de revisión.

Si el acto no fuera expreso, el solicitante y otros posibles interesados podrán interponer recurso de reposición en cualquier momento a partir del día siguiente a aquel en que, de acuerdo con su normativa específica, se produzca el acto presunto.

2. El plazo máximo para dictar y notificar la resolución del recurso será de un mes.

3. Contra la resolución de un recurso de reposición no podrá interponerse de nuevo dicho recurso.

## 8.4 Recurso extraordinario de revisión (arts. 125-126)

<!-- bloque a125 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 125. Objeto y plazos.

1. Contra los actos firmes en vía administrativa podrá interponerse el recurso extraordinario de revisión ante el órgano administrativo que los dictó, que también será el competente para su resolución, cuando concurra alguna de las circunstancias siguientes:

a) Que al dictarlos se hubiera incurrido en error de hecho, que resulte de los propios documentos incorporados al expediente.

b) Que aparezcan documentos de valor esencial para la resolución del asunto que, aunque sean posteriores, evidencien el error de la resolución recurrida.

c) Que en la resolución hayan influido esencialmente documentos o testimonios declarados falsos por sentencia judicial firme, anterior o posterior a aquella resolución.

d) Que la resolución se hubiese dictado como consecuencia de prevaricación, cohecho, violencia, maquinación fraudulenta u otra conducta punible y se haya declarado así en virtud de sentencia judicial firme.

2. El recurso extraordinario de revisión se interpondrá, cuando se trate de la causa a) del apartado anterior, dentro del plazo de cuatro años siguientes a la fecha de la notificación de la resolución impugnada. En los demás casos, el plazo será de tres meses a contar desde el conocimiento de los documentos o desde que la sentencia judicial quedó firme.

3. Lo establecido en el presente artículo no perjudica el derecho de los interesados a formular la solicitud y la instancia a que se refieren los artículos 106 y 109.2 de la presente Ley ni su derecho a que las mismas se sustancien y resuelvan.

<!-- bloque a126 · versión publicada 20151002 · vigente desde 20161002 -->

### Artículo 126. Resolución.

1. El órgano competente para la resolución del recurso podrá acordar motivadamente la inadmisión a trámite, sin necesidad de recabar dictamen del Consejo de Estado u órgano consultivo de la Comunidad Autónoma, cuando el mismo no se funde en alguna de las causas previstas en el apartado 1 del artículo anterior o en el supuesto de que se hubiesen desestimado en cuanto al fondo otros recursos sustancialmente iguales.

2. El órgano al que corresponde conocer del recurso extraordinario de revisión debe pronunciarse no sólo sobre la procedencia del recurso, sino también, en su caso, sobre el fondo de la cuestión resuelta por el acto recurrido.

3. Transcurrido el plazo de tres meses desde la interposición del recurso extraordinario de revisión sin haberse dictado y notificado la resolución, se entenderá desestimado, quedando expedita la vía jurisdiccional contencioso-administrativa.

---

## Jurisprudencia relevante

Aquí solo figuran resoluciones leídas en una fuente primaria, la publicación en el BOE,
el 2026-09-23. Los resúmenes son propios. Desde este entorno no se ha podido acceder a
CENDOJ (poderjudicial.es) ni a tribunalconstitucional.es (el proxy bloquea ambos
dominios). Por eso los ECLI que el BOE no publica se marcan como pendientes.

Todas las resoluciones son anteriores a la Ley 39/2015 o aplican normativa anterior: la
Ley 30/1992 y la ley de tráfico entonces vigente. La doctrina del TC deriva del art. 24 CE
y no depende de la ley de procedimiento aplicable. La del TS interpreta el art. 58.4 de la
Ley 30/1992, cuyo equivalente actual es el art. 40.4 de la Ley 39/2015.

### Tribunal Constitucional: notificación edictal en procedimientos sancionadores

- **STC 82/2019, de 17 de junio** (Sala Segunda, recurso de amparo 5533-2017).
  ECLI:ES:TC:2019:82. BOE núm. 177, de 25/07/2019, BOE-A-2019-10910.
  <https://www.boe.es/diario_boe/txt.php?id=BOE-A-2019-10910>
  *Resumen propio:* reúne la doctrina del TC sobre notificaciones edictales en los
  sancionadores. Los edictos son un remedio último y excepcional. Antes de usarlos, la
  Administración debe buscar el domicilio con diligencia, también en otros registros
  públicos, y no le basta un único intento en el domicilio del DNI. En el caso (sanción
  de juego) se anularon la sanción y la providencia de apremio.
  Relacionado con los arts. 42 y 44 LPAC y con el art. 24.2 CE.

- **STC 219/2007, de 8 de octubre** (Sala Segunda, recurso de amparo 2204-2005).
  BOE núm. 273, de 14/11/2007, BOE-T-2007-19598.
  <https://www.boe.es/diario_boe/txt.php?id=BOE-T-2007-19598>
  ECLI: la publicación del BOE no lo incluye. `TODO(juridico)`: confirmar en
  hj.tribunalconstitucional.es; por el formato habitual sería ECLI:ES:TC:2007:219.
  *Resumen propio:* multa municipal de tráfico. La denuncia se notificó en un domicilio
  erróneo y después por edictos, aunque el Ayuntamiento conocía el domicilio real por el
  censo electoral. El TC aprecia falta de diligencia, declara vulnerado el art. 24 CE y
  anula la sanción y la sentencia que la confirmó.

- **STC 54/2003, de 24 de marzo** (Sala Segunda, recurso de amparo 727-2000).
  BOE núm. 91, de 16/04/2003, BOE-T-2003-7855.
  <https://www.boe.es/diario_boe/txt.php?id=BOE-T-2003-7855>
  ECLI: la publicación del BOE no lo incluye. `TODO(juridico)`: confirmar; por formato
  sería ECLI:ES:TC:2003:54.
  *Resumen propio:* multa por no identificar al conductor. La empresa titular fue
  emplazada por edictos en su antiguo domicilio social, aunque el nuevo constaba en el
  Registro Mercantil y la Administración lo usó después para el apremio. Para el TC fue
  una sanción impuesta sin procedimiento contradictorio y declara vulnerado el art. 24 CE.

La STC 82/2019 cita además, en la misma línea, las SSTC 158/2007, 32/2008, 128/2008,
59/2014 y 93/2018. Se han visto solo como citas y no se han leído una a una.

### Tribunal Supremo: «intento de notificación debidamente acreditado» (art. 58.4 Ley 30/1992, hoy art. 40.4 LPAC)

- **STS (Sala Tercera, Sección Tercera) de 17 de noviembre de 2003**, recurso de
  casación en interés de la ley 128/2002. Doctrina legal publicada en el BOE núm. 4, de
  05/01/2004, BOE-A-2004-198. <https://www.boe.es/buscar/doc.php?id=BOE-A-2004-198>
  ECLI: el BOE no lo publica y queda pendiente de obtener en CENDOJ.
  *Resumen propio:* para cumplir el plazo máximo del procedimiento basta un intento de
  notificación personal hecho con las garantías legales y acreditado en el expediente,
  aunque no llegue a practicarse. En su redacción original situaba el final del intento
  por correo certificado en la recepción de la devolución (**rectificado en 2013**, ver
  la entrada siguiente).

- **STS (Sala Tercera, Pleno) de 3 de diciembre de 2013**, recurso
  contencioso-administrativo 557/2011. Rectificación de doctrina legal publicada en el
  BOE núm. 9, de 10/01/2014, BOE-A-2014-291.
  <https://www.boe.es/diario_boe/txt.php?id=BOE-A-2014-291>
  ECLI: pendiente (CENDOJ).
  *Resumen propio:* corrige la doctrina de 2003 en un único punto. A efectos del plazo
  máximo, el intento de notificación termina en la fecha en que se hizo, no cuando la
  Administración recibe el envío devuelto. Es relevante para calcular la caducidad cuando
  la resolución se intentó notificar cerca del final del plazo.

### Tribunal Supremo: recurso de alzada y prescripción de la sanción

- **STS (Sala Tercera, Sección Quinta) de 22 de septiembre de 2008**, recurso de
  casación en interés de la ley 69/2005. Doctrina legal publicada en el BOE núm. 275, de
  14/11/2008, BOE-A-2008-18350.
  <https://www.boe.es/diario_boe/txt.php?id=BOE-A-2008-18350>
  ECLI: pendiente (CENDOJ).
  *Resumen propio:* aunque pasen los tres meses sin resolver la alzada contra una
  sanción, la sanción no es firme ni ejecutiva, así que no empieza a correr su plazo de
  prescripción. **Atención:** podría haber quedado superada por una ley posterior (ver la
  duda n.º 11). No debe usarse en una regla sin verificarlo.

---

## Dudas abiertas

1. `TODO(juridico)`: **Supletoriedad frente al RDL 6/2015.** La DA 1ª.2.c) remite los
   sancionadores de tráfico a «su normativa específica» y aplica la LPAC solo de forma
   supletoria. Hay que decidir, para cada regla de ggLaw, qué precepto rige: plazos de
   alegaciones, notificación, recursos, caducidad y prescripción. Fuente: RDL 6/2015
   (BOE-A-2015-11722, versión consolidada), arts. 87 (Denuncias), 89 (Notificación de la
   denuncia), 90 (Práctica de la notificación de las denuncias), 91 (Notificaciones en el
   BOE), 92 (TESTRA), 93-95 (clases de procedimiento, abreviado y ordinario),
   96 (Recursos en el procedimiento sancionador ordinario) y 112 (Prescripción y
   caducidad). Aquí solo se han comprobado sus rúbricas, no su contenido.

2. `TODO(juridico)`: **Plazo del recurso de reposición en tráfico.** El art. 124.1 LPAC
   fija «un mes» si el acto es expreso. Hay que comprobar si el art. 96 del RDL 6/2015 fija
   un plazo propio, cómo lo expresa (meses o días naturales), qué plazo tiene la
   Administración para resolver y qué efecto tiene su silencio (compararlo con el art.
   124.2 y el art. 24.1, tercer párrafo, LPAC). Fuente: RDL 6/2015, art. 96.

3. `TODO(juridico)`: **¿Reposición o alzada contra una multa del Ayuntamiento de Palma?**
   Depende de si la resolución pone fin a la vía administrativa (art. 114 LPAC). En el
   ámbito local, el art. 52.2 de la Ley 7/1985 (LBRL, BOE-A-1985-5392) enumera qué
   resoluciones ponen fin a la vía (comprobado que existe; no se ha transcrito). Falta
   verificar qué órgano sanciona en Palma, si actúa por delegación, si se aplica el
   Título X de la LBRL y lo que disponga el RDL 6/2015. Fuente: LBRL art. 52.2, RDL 6/2015,
   normas orgánicas del Ayuntamiento de Palma y ordenanza de circulación.

4. `TODO(juridico)`: **Obligación de relacionarse electrónicamente de las personas
   físicas.** El art. 14.1 les permite elegir, pero los arts. 14.3 y 41.1 permiten
   imponer la obligación a ciertos colectivos por reglamento. En tráfico existe la
   Dirección Electrónica Vial (DEV). Hay que comprobar quién está obligado a usarla, si
   para una persona física es voluntaria y si se aplica el rechazo a los diez días
   naturales del art. 43.2 LPAC o una regla propia. Fuente: RDL 6/2015, arts. 89-90, y
   RD 203/2021, Reglamento de actuación y funcionamiento del sector público por medios
   electrónicos (BOE-A-2021-5032).

5. `TODO(juridico)`: **Plazos en días naturales cuyo último día es inhábil.** El art.
   30.5 dice sin distinguir que «Cuando el último día del plazo sea inhábil, se entenderá
   prorrogado al primer día hábil siguiente». Hay que confirmar que se aplica, de forma
   supletoria, a los plazos en días naturales del RDL 6/2015 y que este no tiene una regla
   propia. Además, el art. 31.2.b) (presentación en día inhábil) se refiere solo al
   «cómputo de plazo fijado en días hábiles». ¿Cómo se trata una presentación electrónica
   en sábado dentro de un plazo en días naturales? Fuente: arts. 30.2, 30.5 y 31.2.b)
   LPAC, RDL 6/2015 y jurisprudencia del TS (buscar en CENDOJ).

6. `TODO(juridico)`: **Festivos locales del domicilio y de la sede (art. 30.6 frente al
   art. 31.3).** Según el art. 30.6, es inhábil el día que lo sea en el municipio o la
   comunidad autónoma de residencia del interesado o en la sede del órgano. Según el art.
   31.3, para los registros electrónicos solo cuenta el calendario de la sede, «sin que
   resulte de aplicación a los mismos lo dispuesto en el artículo 30.6». Pregunta concreta:
   un usuario de otro municipio de Mallorca, con festivo local el último día del plazo,
   ¿tiene prórroga si presenta electrónicamente ante el Ayuntamiento de Palma? ¿Y si
   presenta en papel en una oficina de registro? Hay que decidir cómo modela
   `core/plazos.py` el calendario según el canal de presentación. Fuente: arts. 30.6, 30.7
   y 31.3 LPAC, calendarios de días inhábiles (BOE para la AGE y BOIB para Illes Balears y
   sus entidades locales) y jurisprudencia del TS.

7. `TODO(juridico)`: **«dentro de los tres días siguientes» (art. 42.2).** El texto no
   dice si son días hábiles o naturales. Aplicar por defecto el art. 30.2 (hábiles) es
   una interpretación que hay que confirmar. También falta confirmar si un único intento
   dentro del plazo máximo basta para el art. 40.4. Algunas reseñas secundarias, no
   verificadas y que solo sirven de pista, mencionan sentencias recientes del TS en
   casación, entre ellas una STS de 12/12/2025 (rec. 2922/2023). Fuente: CENDOJ (Sala
   Tercera; buscar: artículo 42.2 Ley 39/2015 y segundo intento).

8. `TODO(juridico)`: **Vigencia de la doctrina 2003/2013 sobre el «intento de notificación debidamente
   acreditado».**
   Interpreta el art. 58.4 de la Ley 30/1992. Hay que confirmar en CENDOJ que el TS la
   aplica igual al art. 40.4 LPAC y a la caducidad del sancionador de tráfico, y obtener
   los ECLI.

9. `TODO(juridico)`: **Caducidad del sancionador de tráfico.** En la LPAC, los arts. 21.2
   y 21.3 (seis meses como máximo y tres meses por defecto) y el 25.1.b) son solo
   supletorios. Hay que verificar en el art. 112 del RDL 6/2015 el plazo, desde cuándo se
   cuenta, si admite suspensiones (aplicación del art. 22 LPAC) y sus efectos (art. 95.3
   LPAC). Fuente: RDL 6/2015, art. 112.

10. `TODO(juridico)`: **Reducción por pago frente al pronto pago de tráfico.** El art.
    85.3 LPAC prevé reducciones de «al menos, el 20 %» condicionadas a renunciar a los
    recursos. Hay que comprobar qué reducción y qué condiciones fija el RDL 6/2015
    (procedimiento abreviado, arts. 93-94) y si el art. 85 se aplica de algún modo.
    Fuente: RDL 6/2015, arts. 93-95.

11. `TODO(juridico)`: **Prescripción de la sanción si no se resuelve la alzada.** La
    doctrina legal de la STS de 22/09/2008 (BOE-A-2008-18350) puede haber quedado afectada
    por la regulación de la prescripción de sanciones en la Ley 40/2015 (BOE-A-2015-10566,
    art. 30). No se ha verificado en esta tarea y hay que leer el art. 30 de la Ley 40/2015
    antes de construir una regla. Fuente: Ley 40/2015, art. 30, y RDL 6/2015, art. 112.

12. `TODO(juridico)`: **Notificación edictal en tráfico: BOE, TEU y TESTRA.** El art. 44
    LPAC exige un anuncio en el BOE y no menciona el «Tablón Edictal Único» (se ha
    comprobado en el texto consolidado). El RDL 6/2015 tiene un art. 91 (Notificaciones en
    el BOE) y un art. 92 (Tablón Edictal de Sanciones de Tráfico, TESTRA). Hay que
    verificar el régimen vigente, si el TESTRA sigue operativo o se ha sustituido por el
    TEU del BOE, y qué diligencia previa de búsqueda del domicilio se exige (doctrina de la
    STC 82/2019). Fuente: RDL 6/2015, arts. 91-92, y normativa del BOE sobre el TEU.

13. `TODO(juridico)`: **La denuncia como acuerdo de iniciación (art. 64.2.f).** Hay que
    comprobar si, en tráfico, la denuncia notificada cumple la función del acuerdo de
    iniciación y si, sin alegaciones, se convierte en propuesta o en resolución. En ese
    caso, la checklist del art. 64.2 solo se aplicaría de forma supletoria. Fuente: RDL
    6/2015, arts. 93-95.

14. `TODO(juridico)`: **Jurisprudencia sobre plazos en meses.** No se ha localizado ni
    verificado jurisprudencia sobre el cómputo «de fecha a fecha», como el caso de una
    notificación el día 31 o el 29 de febrero. El art. 30.4 es literal y claro, pero
    conviene documentar la doctrina del TS para los casos límite. Fuente: CENDOJ.

15. `TODO(juridico)`: **Sentencias del TS seleccionadas por el BOE y no leídas.** El panel
    «Jurisprudencia» del texto consolidado (boe.es, en colaboración con CENDOJ) relaciona
    con estos artículos las siguientes STS. Su existencia, fecha y enlace se han
    comprobado en boe.es, pero **no se ha leído el texto** porque CENDOJ está bloqueado.
    Los ECLI indicados se deducen del ROJ y hay que confirmarlos.
    - STS 3150/2019 (15/10/2019), art. 42: sanción y notificación por BOE.
      <https://www.poderjudicial.es/search/openDocument/a4834ece81452fb2>. ECLI:ES:TS:2019:3150, pendiente de confirmar.
    - STS 2496/2019 (12/07/2019), arts. 123-124: reposición desistida y extemporaneidad
      del contencioso. <https://www.poderjudicial.es/search/openDocument/0f06db0c4c7e7dd9>. ECLI:ES:TS:2019:2496, pendiente de confirmar.
    - STS 2916/2020 (22/09/2020), art. 21: caducidad de tres meses cuando la norma no
      prevé un plazo. <https://www.poderjudicial.es/search/openDocument/97c967e37288dde0>. ECLI:ES:TS:2020:2916, pendiente de confirmar.
    - STS 2714/2022 (07/07/2022), arts. 66 y 68: falta de firma electrónica y subsanación.
      <https://www.poderjudicial.es/search/openDocument/22ac8862a296db32a0a8778d75e36f0d>. ECLI:ES:TS:2022:2714, pendiente de confirmar.
    - STS 4444/2021 (01/12/2021), arts. 66 y 68: presentaciones telemáticas no
      finalizadas y requerimiento de subsanación.
      <https://www.poderjudicial.es/search/openDocument/9e85a5c73275c7a9>. ECLI:ES:TS:2021:4444, pendiente de confirmar.

16. `TODO(juridico)`: **Seguimiento de modificaciones.** A fecha de consulta, de lo
    transcrito solo se han modificado desde 2015 el art. 32 (RDL 6/2022) y la DF 7ª
    (RDL 11/2018, RDL 28/2020 y Ley 10/2021). Antes de marcar como `revisado` cualquier
    regla que dependa de este fichero, hay que volver a ejecutar
    `scripts/boe_fetch.py BOE-A-2015-10565 --index` y comprobar que ningún bloque tiene
    una fecha posterior a 2024-11-06. También hay que revisar el desarrollo reglamentario
    de las notificaciones en el RD 203/2021.
