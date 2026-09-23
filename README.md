# ggLaw

Asistente de código abierto para que cualquier persona en España pueda **defenderse por sí
misma** en trámites administrativos: recurrir multas, entender notificaciones, calcular plazos
y preparar escritos listos para presentar.

> [!WARNING]
> **Aviso legal.** ggLaw no presta asesoramiento jurídico ni sustituye a un abogado. Es una
> herramienta para que redactes y presentes **tu propio** escrito. Revisa siempre el
> resultado, comprueba los plazos en la notificación y en la norma, y preséntalo bajo tu
> responsabilidad. El proyecto no garantiza ningún resultado.

## Estado

En desarrollo; todavía no es utilizable como herramienta final. Primer ámbito: **multas de
tráfico** en Palma (Illes Balears).

Ya funciona:

- Cómputo de plazos según el art. 30 de la Ley 39/2015 (`core/plazos.py`): días hábiles y
  naturales, meses y años de fecha a fecha, prórroga si el último día es inhábil y fecha de
  las notificaciones electrónicas.
- Calendario de días inhábiles de 2026 para el Estado, Illes Balears y Palma
  (`calendars/`), con su fuente oficial. Los años sin calendario publicado no se calculan.

Siguiente: reglas de defensa en tráfico, plantillas de escritos y la CLI `gglaw analizar`.

## Principios

- **Lo crítico es determinista.** Plazos, prescripción, caducidad y procedencia de un motivo
  de defensa se calculan con código y reglas probadas. El LLM nunca los decide.
- **Todo contenido jurídico cita su fuente**: norma, artículo, versión consolidada del BOE y
  fecha de consulta.
- **Local primero.** Se ejecuta en tu equipo. No hay servidor central ni se guardan tus datos
  fuera de tu máquina.

## Uso para desarrollo

Requiere Python 3.12 y [uv](https://docs.astral.sh/uv/).

```bash
uv sync                    # instalar dependencias
uv run pytest --cov        # tests y cobertura
uv run ruff check .        # lint
uv run ruff format .       # formato
uv run mypy core/          # tipos
```

## Estructura

| Carpeta | Contenido |
|---|---|
| `core/` | Lógica determinista: plazos y calendarios. |
| `calendars/` | Días inhábiles por territorio y año, con su fuente. |
| `knowledge/` | Normativa transcrita del BOE y del BOIB. |
| `rules/` | Motivos de defensa en YAML. |
| `templates/` | Plantillas de escritos. |
| `llm/` | Adaptadores y prompts del LLM. |
| `interfaces/cli/` | Línea de comandos. |
| `scripts/` | Utilidades, como la anonimización de casos. |
| `tests/` | Tests y casos reales anonimizados. |

## Contribuir

Lee `CLAUDE.md`. En resumen: tests primero en `core/` y `rules/`, commits pequeños con
Conventional Commits en español y **nunca datos personales** en el repositorio (nombres,
DNI/NIE, matrículas, direcciones, números de expediente ni firmas).

## Licencia

[GNU Affero General Public License v3.0](LICENSE) o, a tu elección, cualquier versión
posterior publicada por la Free Software Foundation (`AGPL-3.0-or-later`).
