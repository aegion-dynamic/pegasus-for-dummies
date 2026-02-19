#!/usr/bin/env python3
"""
Extract images from "Electronic Lab Notebooks (ELNs) and AI in Life Sciences.pdf".
- Extracts embedded images via pypdf.
- Renders pages 2, 3, 4 as PNG (figures described in the guide) via PyMuPDF.
Output: src/images/eln-guide/
Run from repo root. Source PDF path is in README.
"""

import os
import sys

def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_dir = os.path.join(repo_root, "src", "images", "eln-guide")
    os.makedirs(out_dir, exist_ok=True)

    # Default path; override with env or argv
    pdf_path = os.environ.get(
        "ELN_GUIDE_PDF",
        os.path.join(os.path.expanduser("~/Downloads"), "Electronic Lab Notebooks (ELNs) and AI in Life Sciences.pdf")
    )
    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
    if not os.path.isfile(pdf_path):
        print(f"PDF not found: {pdf_path}", file=sys.stderr)
        sys.exit(1)

    # 1) Extract embedded images with pypdf
    try:
        from pypdf import PdfReader
        reader = PdfReader(pdf_path)
        count = 0
        for i, page in enumerate(reader.pages):
            for j, img in enumerate(page.images):
                name = f"embedded-p{i+1}-{j}.png"
                path = os.path.join(out_dir, name)
                try:
                    img.image.save(path)
                    count += 1
                except Exception as e:
                    print(f"Skip image {name}: {e}", file=sys.stderr)
        if count:
            print(f"Extracted {count} embedded image(s).")
    except Exception as e:
        print(f"pypdf extraction: {e}", file=sys.stderr)

    # 2) Render pages 2, 3, 4 as PNG with PyMuPDF
    try:
        import fitz
        doc = fitz.open(pdf_path)
        names = ["eln-page-sections", "eln-raw-data", "eln-protocol"]
        for i, page_idx in enumerate([1, 2, 3]):  # 0-based: pages 2, 3, 4
            if page_idx >= len(doc):
                break
            page = doc[page_idx]
            pix = page.get_pixmap(dpi=150)
            path = os.path.join(out_dir, f"{names[i]}.png")
            pix.save(path)
            print(f"Rendered {names[i]}.png (page {page_idx + 1}).")
        doc.close()
    except Exception as e:
        print(f"PyMuPDF render: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Done. Output: {out_dir}")

if __name__ == "__main__":
    main()
