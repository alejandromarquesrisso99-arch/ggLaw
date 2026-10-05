"""Utilidades comunes de los evaluadores de reglas de tráfico."""

from datetime import date

from core.plazos import DateRange
from core.reglas import Check, CheckStatus


def fmt(day: date) -> str:
    return day.strftime("%d/%m/%Y")


def fmt_range(days: DateRange) -> str:
    if days.latest == days.earliest:
        return fmt(days.earliest)
    if days.latest is None:
        return f"{fmt(days.earliest)} o posterior (falta el calendario oficial para acotarlo)"
    return f"entre el {fmt(days.earliest)} y el {fmt(days.latest)}"


def missing(condition: str, *names: str) -> Check:
    return Check(
        condition=condition,
        status=CheckStatus.MISSING_DATA,
        detail=f"Faltan datos: {', '.join(names)}.",
        missing=names,
    )


def check(condition: str, status: CheckStatus, detail: str) -> Check:
    return Check(condition=condition, status=status, detail=detail)
