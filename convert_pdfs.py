#!/usr/bin/env python3.14
"""
Drop PDFs into ~/PDFs-for-Claude, then run this script.
Each PDF gets converted to a .md file in the same folder.
Already-converted PDFs are skipped automatically.
"""

import subprocess
from pathlib import Path

folder = Path.home() / "PDFs-for-Claude"
pdfs = list(folder.glob("*.pdf"))

if not pdfs:
    print("No PDFs found in ~/PDFs-for-Claude — add some and try again.")
else:
    new_pdfs = [pdf for pdf in pdfs if not pdf.with_suffix(".md").exists()]
    already_done = [pdf for pdf in pdfs if pdf.with_suffix(".md").exists()]

    if already_done:
        print(f"Skipping {len(already_done)} already-converted PDF(s):")
        for pdf in already_done:
            print(f"  ↷ {pdf.name}")
        print()

    if not new_pdfs:
        print("No new PDFs to convert — all are already done.")
        print("(Delete the .md file if you want to re-convert a PDF.)\n")
    else:
        print(f"Converting {len(new_pdfs)} new PDF(s)...\n")
        for pdf in new_pdfs:
            md_file = pdf.with_suffix(".md")
            print(f"Converting: {pdf.name} → {md_file.name}")
            with open(md_file, "w") as out:
                result = subprocess.run(
                    ["python3.14", "-m", "markitdown", str(pdf)],
                    stdout=out,
                    stderr=subprocess.PIPE,
                    text=True
                )
            if result.returncode == 0:
                print(f"  ✓ Done — {md_file.name}\n")
            else:
                print(f"  ✗ Error: {result.stderr.strip()}\n")

    print("All done! Your .md files are in ~/PDFs-for-Claude")

    # Copy only new conversions to clipboard; if nothing new, copy all
    copy_pdfs = new_pdfs if new_pdfs else pdfs
    combined = ""
    for pdf in copy_pdfs:
        md_file = pdf.with_suffix(".md")
        if md_file.exists():
            combined += md_file.read_text() + "\n\n---\n\n"

    copy = subprocess.run(["pbcopy"], input=combined, text=True)
    if copy.returncode == 0:
        print("\n📋 Copied to clipboard — just Cmd+V into Claude chat!")
