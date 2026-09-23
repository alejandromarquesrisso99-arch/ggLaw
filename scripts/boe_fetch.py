"""Descarga artículos de la versión consolidada del BOE y los emite en Markdown.

Usa la API de datos abiertos de legislación consolidada del BOE:
https://www.boe.es/datosabiertos/api/legislacion-consolidada/

Uso:
    python scripts/boe_fetch.py BOE-A-2015-11722 a112 a93 a95
    python scripts/boe_fetch.py BOE-A-2015-11722 --index

Para cada bloque se toma la última <version> (la vigente) y se transcriben sus
párrafos literalmente. Solo usa la biblioteca estándar.
"""

from __future__ import annotations

import argparse
import sys
import urllib.request
import xml.etree.ElementTree as ET

API = "https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/{id}"


def _get(url: str) -> ET.Element:
    req = urllib.request.Request(url, headers={"Accept": "application/xml"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return ET.fromstring(resp.read())


def _text(el: ET.Element) -> str:
    return " ".join("".join(el.itertext()).split())


def fetch_index(norma_id: str) -> list[tuple[str, str, str]]:
    root = _get(API.format(id=norma_id) + "/texto/indice")
    return [
        (
            b.findtext("id", ""),
            b.findtext("titulo", ""),
            b.findtext("fecha_actualizacion", ""),
        )
        for b in root.iter("bloque")
    ]


def fetch_metadata(norma_id: str) -> dict[str, str]:
    root = _get(API.format(id=norma_id) + "/metadatos")
    meta = root.find("data/metadatos")
    if meta is None:
        return {}
    return {child.tag: _text(child) for child in meta}


def fetch_block_markdown(norma_id: str, block_id: str) -> str:
    root = _get(API.format(id=norma_id) + f"/texto/bloque/{block_id}")
    bloque = root.find("data/bloque")
    if bloque is None:
        raise ValueError(f"Bloque no encontrado: {block_id}")
    versions = bloque.findall("version")
    if not versions:
        raise ValueError(f"Bloque sin versiones: {block_id}")
    version = versions[-1]
    lines: list[str] = []
    for p in version:
        text = _text(p)
        if not text:
            continue
        cls = p.get("class", "")
        if cls == "articulo":
            lines.append(f"### {text}")
        elif p.tag == "blockquote":
            # Notas editoriales del BOE (no son texto normativo).
            lines.append(f"> _Nota BOE: {text}_")
        elif p.tag == "table" or cls.startswith("cabecera"):
            lines.append(f"**{text}**")
        else:
            lines.append(text)
    header = (
        f"<!-- bloque {block_id} · versión publicada "
        f"{version.get('fecha_publicacion')} · vigente desde "
        f"{version.get('fecha_vigencia')} -->"
    )
    return header + "\n\n" + "\n\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("norma_id", help="Identificador BOE, p. ej. BOE-A-2015-11722")
    parser.add_argument("bloques", nargs="*", help="Ids de bloque, p. ej. a112")
    parser.add_argument("--index", action="store_true", help="Lista los bloques")
    parser.add_argument("--meta", action="store_true", help="Muestra metadatos")
    args = parser.parse_args(argv)

    if args.meta:
        for key, value in fetch_metadata(args.norma_id).items():
            print(f"{key}: {value}")
    if args.index:
        for block_id, titulo, fecha in fetch_index(args.norma_id):
            print(f"{block_id}\t{fecha}\t{titulo}")
    for block_id in args.bloques:
        print(fetch_block_markdown(args.norma_id, block_id))
    return 0


if __name__ == "__main__":
    sys.exit(main())
