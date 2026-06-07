#!/usr/bin/env python3
"""Convert a Markdown report to PDF when local dependencies are available."""

from __future__ import annotations

import argparse
import pathlib
import sys


def convert_with_markdown_pdf(input_path: pathlib.Path, output_path: pathlib.Path) -> None:
    try:
        from markdown_pdf import MarkdownPdf, Section
    except ImportError as exc:
        raise RuntimeError(
            "Missing dependency: markdown-pdf. Install it or keep the Markdown report as the primary deliverable."
        ) from exc

    text = input_path.read_text(encoding="utf-8")
    pdf = MarkdownPdf(toc_level=2)
    pdf.add_section(Section(text, toc=True))
    pdf.save(str(output_path))


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert Markdown to PDF.")
    parser.add_argument("input", help="Input Markdown file")
    parser.add_argument("output", help="Output PDF file")
    args = parser.parse_args()

    input_path = pathlib.Path(args.input).resolve()
    output_path = pathlib.Path(args.output).resolve()

    if not input_path.exists():
        print(f"Input file does not exist: {input_path}", file=sys.stderr)
        return 2
    if input_path.suffix.lower() not in {".md", ".markdown"}:
        print(f"Input should be a Markdown file: {input_path}", file=sys.stderr)
        return 2

    output_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        convert_with_markdown_pdf(input_path, output_path)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    print(f"Wrote {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
