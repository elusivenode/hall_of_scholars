#!/usr/bin/env python3
"""Extract page-tagged plain text from a PDF, for scripts/validate.py --schedules-text.

Needs the third-party package pypdf, which is NOT a repository dependency; use a throwaway
virtual environment:

    python3 -m venv /tmp/pdfenv && /tmp/pdfenv/bin/pip install pypdf
    /tmp/pdfenv/bin/python scripts/extract_pdf_text.py schedules.pdf schedules.txt

Output format: each page starts with a line "=====PAGE n=====". Text extraction flattens
superscripts and subscripts (for example R^3 appears as R3).
"""
import sys

from pypdf import PdfReader

if len(sys.argv) != 3:
    sys.exit(__doc__)
reader = PdfReader(sys.argv[1])
with open(sys.argv[2], "w", encoding="utf-8") as out:
    for n, page in enumerate(reader.pages, 1):
        out.write(f"\n=====PAGE {n}=====\n{page.extract_text() or ''}")
print(f"{len(reader.pages)} pages written to {sys.argv[2]}")
