from typer.testing import CliRunner

from gglaw import __version__
from gglaw.disclaimer import DISCLAIMER
from gglaw.interfaces.cli.main import app

runner = CliRunner()


def _normalize(text: str) -> str:
    """Colapsa espacios y saltos de línea que introduce el formato de la ayuda."""
    return " ".join(text.split())


def test_help_shows_disclaimer() -> None:
    result = runner.invoke(app, ["--help"])

    assert result.exit_code == 0
    assert _normalize(DISCLAIMER) in _normalize(result.output)


def test_version_prints_installed_version() -> None:
    result = runner.invoke(app, ["version"])

    assert result.exit_code == 0
    assert result.output.strip() == f"ggLaw {__version__}"
