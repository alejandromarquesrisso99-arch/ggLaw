# ggLaw

Asistente de código abierto para **defenderte por ti mismo** en trámites
administrativos en España: entender una notificación, calcular plazos y preparar
un escrito listo para presentar en tu propio nombre.

> [!WARNING]
> **AVISO LEGAL:** ggLaw no presta asesoramiento jurídico ni sustituye a un abogado.
> Te ayuda a preparar tus propios escritos: revisa todo lo que genere, comprueba
> los plazos en la norma aplicable y presenta cualquier escrito bajo tu
> responsabilidad.

## Estado

**Fase inicial.** Todavía no analiza notificaciones ni genera escritos. Solo existe
el esqueleto del proyecto.

El primer caso de uso serán las **multas de tráfico**, empezando por Palma
(Illes Balears). Después vendrán la plusvalía municipal, las reclamaciones a
suministradoras y las sanciones tributarias sencillas.

## Qué es y qué no es

- **Es** una herramienta local: se ejecuta en tu equipo. No hay servidor central y
  tus datos no salen de tu máquina, salvo que elijas un proveedor de IA en la nube.
- **Es** transparente: todo contenido jurídico cita la norma, el artículo, la
  versión consolidada del BOE y la fecha de consulta.
- **No es** un despacho ni un servicio profesional, y no garantiza ningún resultado.
- **No decide con IA** lo importante: los plazos, la prescripción, la caducidad y
  si un motivo de defensa procede se calculan con reglas deterministas y probadas.
  La IA solo extrae datos del documento, explica en lenguaje llano y adapta
  plantillas ya revisadas.

## Instalación (desarrollo)

Necesitas [uv](https://docs.astral.sh/uv/). uv descarga Python 3.12 si no lo tienes.

```bash
git clone https://github.com/alejandromarquesrisso99-arch/ggLaw.git
cd ggLaw
uv sync
uv run gglaw --help
```

## Desarrollo

```bash
uv run pytest                # tests
uv run ruff check . --fix    # lint
uv run ruff format .         # formato
uv run mypy                  # tipos (modo estricto)
```

Cada push y cada pull request pasan estas mismas comprobaciones en GitHub Actions.

Las convenciones del proyecto (formato del contenido jurídico, reglas, plantillas y
commits) están en [`CLAUDE.md`](CLAUDE.md).

## Privacidad

Nunca subas datos personales al repositorio: nombres, DNI/NIE, matrículas,
direcciones, números de expediente ni firmas.

- Guarda tus expedientes reales en `mis_casos/`, que git ignora.
- Git ignora también los PDF y las imágenes.
- Los casos de prueba se anonimizan siempre antes de añadirse a `tests/casos/`.

## Contribuir

Las contribuciones son bienvenidas, sobre todo las revisiones de juristas. Todo
contenido jurídico nuevo entra como `borrador` y debe citar su fuente oficial. Si
tienes una duda jurídica, no la resuelvas por intuición: déjala anotada como
`TODO(juridico)`.

## Licencia

[GNU Affero General Public License v3.0 o posterior](LICENSE)
(`AGPL-3.0-or-later`).
