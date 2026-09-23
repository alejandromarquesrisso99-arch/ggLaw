# CLAUDE.md — ggLaw

## Qué es este proyecto

ggLaw es un asistente open source (AGPL-3.0-or-later) que ayuda a ciudadanos en España a
**defenderse por sí mismos** en trámites administrativos: recurrir multas, entender
notificaciones, calcular plazos y generar escritos listos para presentar.

- No es un producto comercial. Es para uso personal y de allegados, abierto a la comunidad.
- No sustituye a un abogado. Ayuda al usuario a redactar y presentar **su propio** escrito.
- Primer vertical: **multas de tráfico** (empezando por Palma / Illes Balears).
  Siguientes: plusvalía municipal, reclamaciones a suministradoras, sanciones tributarias
  sencillas. Herencias, al final y como guía paso a paso.

## Principios no negociables

1. **Lo crítico es determinista.** Cálculo de plazos, prescripción, caducidad y
   procedencia de un motivo de defensa se implementan en código y reglas con tests.
   El LLM **nunca** decide un plazo ni si un motivo aplica.
2. **El LLM solo:** extrae datos de documentos, explica en lenguaje llano y adapta
   plantillas ya revisadas. Toda salida del LLM se valida contra un esquema (pydantic).
3. **Todo contenido jurídico cita su fuente:** norma, artículo, versión consolidada del
   BOE y fecha de consulta. Sin fuente, no entra.
4. **Local primero.** La herramienta se ejecuta en el equipo del usuario. No hay servidor
   central ni se guardan datos personales fuera de la máquina del usuario.
5. **Privacidad en el repo.** Nunca se commitean datos personales: nombres, DNI/NIE,
   matrículas, direcciones, números de expediente, firmas. Los casos de prueba se
   anonimizan siempre con `scripts/anonymize.py` antes de añadirse.
6. **Aviso legal visible** en el README, la CLI y cada escrito generado: no es
   asesoramiento jurídico; el usuario revisa, verifica plazos y presenta bajo su
   responsabilidad.

## Stack

- Python 3.12, gestionado con `uv`
- `pydantic` para modelos y validación; `typer` para la CLI
- `jinja2` para plantillas de escritos
- `pyyaml` para reglas y calendarios
- `pytest` para tests; `ruff` para lint y formato; `mypy` en modo estricto en todo `gglaw/`
- Adaptador LLM intercambiable: API (Anthropic, OpenAI) o local (Ollama)
- OCR/extracción de PDF: por decidir (evaluar `pymupdf` + LLM con visión)

## Comandos

```bash
uv sync                    # instalar dependencias
uv run pytest              # tests
uv run ruff check . --fix  # lint
uv run ruff format .       # formato
uv run mypy                # tipos (rutas en pyproject.toml)
uv run gglaw --help        # CLI
```

## Estructura

```
ggLaw/
├── gglaw/                  # Paquete Python: todo el código
│   ├── core/               # Lógica determinista (sin dependencias de LLM)
│   │   ├── plazos.py       # Cómputo de plazos (días hábiles/naturales/meses)
│   │   ├── calendario.py   # Carga de festivos por ámbito
│   │   └── expediente.py   # Máquina de estados del expediente
│   ├── llm/                # Adaptadores y prompts (extracción, explicación, redacción)
│   ├── interfaces/cli/     # CLI (typer)
│   └── disclaimer.py       # Aviso legal común (CLI y escritos)
├── rules/                  # Motivos de defensa en YAML (uno por fichero)
├── knowledge/              # Normativa en Markdown con frontmatter de fuente
├── templates/              # Plantillas Jinja2 de escritos
├── calendars/              # Festivos: nacional, autonómico (IB), local (Palma)
├── scripts/                # anonymize.py, utilidades
├── tests/
│   └── casos/              # Casos reales ANONIMIZADOS con resultado esperado
├── .github/workflows/      # CI: ruff, mypy y pytest en cada push y PR
└── .claude/agents/         # Subagentes para Claude Code
```

El código vive dentro del paquete `gglaw/` (`from gglaw.core.plazos import ...`), para
no instalar paquetes con nombres genéricos como `core`. Los datos (reglas, normativa,
plantillas, calendarios) quedan en la raíz, fuera del paquete.

Identificadores de código en inglés; contenido jurídico, plantillas y mensajes al
usuario en español.

## Formato de contenido jurídico

### Normativa (`knowledge/*.md`)

```markdown
---
norma: Real Decreto Legislativo 6/2015 (Ley sobre Tráfico)
articulos: [93, 94, 95, 112]
fuente: https://www.boe.es/buscar/act.php?id=BOE-A-2015-11722
version_consolidada: AAAA-MM-DD
consultado: AAAA-MM-DD
---
```

Se transcribe literalmente el texto legal (no tiene derechos de autor, art. 13 LPI).
La jurisprudencia se **referencia** (tribunal, número, fecha, ECLI, enlace), no se copia en masa.

### Reglas (`rules/*.yaml`)

```yaml
id: trafico.prescripcion_infraccion
titulo: Prescripción de la infracción
ambito: trafico
estado: borrador          # borrador | revisado | validado_abogado
fundamento:
  - norma: RDL 6/2015
    articulo: 112
condiciones:              # evaluadas por gglaw/core/, nunca por el LLM
  - ...
datos_necesarios: [fecha_hechos, fecha_notificacion_denuncia, gravedad]
parrafo_tipo: templates/parrafos/prescripcion.md.j2
notas: ""
```

### Plantillas (`templates/`)

- Redacción **original**, basada en la estructura exigida por la normativa
  (p. ej. art. 66 de la Ley 39/2015 para solicitudes).
- No copiar plantillas de despachos, gestorías u otras webs. Se pueden consultar como
  referencia de estructura, pero el texto debe ser propio.
- Cada plantilla lleva cabecera con `estado`, fuentes y variables requeridas.

## Plazos (el módulo más crítico)

- Implementar según la Ley 39/2015 (art. 30): días hábiles excluyen sábados, domingos y
  festivos; plazos en meses de fecha a fecha; si el último día es inhábil, se prorroga
  al siguiente hábil.
- Los plazos específicos (p. ej. alegaciones en tráfico en días naturales) vienen de la
  norma sectorial y se definen en datos, no incrustados en código.
- **Verificar cada plazo contra la versión consolidada del BOE** antes de marcar una
  regla como `revisado`. No fiarse de la memoria del modelo.
- Cobertura de tests alta en `gglaw/core/plazos.py`: casos límite de fin de mes, años
  bisiestos, festivos encadenados, notificaciones electrónicas.

## Flujo de un caso

1. Entrada: PDF o foto de la notificación → extracción estructurada (LLM + validación).
2. Clasificación: procedimiento y fase (denuncia, propuesta, resolución, apremio).
3. Plazos: `gglaw/core/plazos.py`.
4. Reglas: evaluación determinista de `rules/` aplicables.
5. Redacción: plantilla + párrafos de las reglas aplicables, adaptados por el LLM.
6. Salida: escrito, resumen en lenguaje llano, pasos de presentación y fechas clave.
7. Seguimiento: estado del expediente y siguiente paso cuando llegue la respuesta.

## Cómo trabajar en este repo

- Antes de implementar algo no trivial, propón un plan breve y espera confirmación.
- Tests primero en `gglaw/core/` y `rules/`.
- Cambios pequeños y commits atómicos (Conventional Commits en español:
  `feat(plazos): ...`, `fix(reglas): ...`, `docs(normativa): ...`).
- Todo contenido jurídico nuevo entra con `estado: borrador`. Solo Alex (o un abogado
  revisor) lo cambia a `revisado` / `validado_abogado`.
- Si hay duda jurídica, **no inventes**: deja un `TODO(juridico):` con la pregunta
  concreta y la fuente que habría que consultar.
- Para investigar normativa o redactar plantillas, usa los subagentes de `.claude/agents/`.

## Primeras tareas

1. Esqueleto del proyecto: `pyproject.toml`, estructura de carpetas, ruff/mypy/pytest,
   LICENSE (AGPL-3.0-or-later), README con aviso legal, CI. **Hecha.**
2. `gglaw/core/calendario.py` + `calendars/` con festivos nacionales, Illes Balears y Palma.
3. `gglaw/core/plazos.py` con tests exhaustivos.
4. `knowledge/`: Ley 39/2015 (arts. clave) y RDL 6/2015 (procedimiento sancionador).
5. Primeras reglas de tráfico: prescripción, caducidad del procedimiento, defectos de
   notificación, identificación del conductor, verificación metrológica del cinemómetro.
6. Plantillas: escrito de alegaciones y recurso de reposición.
7. `scripts/anonymize.py` y primer caso de prueba anonimizado.
8. CLI mínima: `gglaw analizar <notificacion.pdf>`.
