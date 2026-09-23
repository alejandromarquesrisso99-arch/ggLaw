"""Punto de entrada de la CLI `gglaw`."""

import typer

from gglaw import __version__
from gglaw.disclaimer import DISCLAIMER

app = typer.Typer(
    name="gglaw",
    epilog=DISCLAIMER,
    no_args_is_help=True,
)


@app.callback()
def main() -> None:
    """Asistente para defenderte por ti mismo en trámites administrativos en España."""


@app.command()
def version() -> None:
    """Muestra la versión instalada de ggLaw."""
    typer.echo(f"ggLaw {__version__}")
