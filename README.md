# Pegasus for Dummies

Open source ecosystem contributor guide for [Pegasus](https://github.com/pegasus-eln/pegasus), an open standard Electronic Lab Notebook (ELN) system.

**Copyright © Aegion Dynamic. All rights reserved.** This repository and the book content are protected by copyright. Others are not permitted to reuse the name, materials, or derivatives without permission. See [COPYRIGHT](COPYRIGHT) and [LICENSE](LICENSE) for full terms and restrictions.

## Building the book

This is an [mdBook](https://rust-lang.github.io/mdBook/) project. To build and serve locally:

```bash
mdbook build    # output in book/
mdbook serve    # serve at http://localhost:3000
```

## Re-extracting images from the ELN guide PDF

Chapter 1 uses figures extracted from the PDF *"Electronic Lab Notebooks (ELNs) and AI in Life Sciences"*. To refresh those images after updating the PDF:

1. Put the PDF in `~/Downloads/` (or set `ELN_GUIDE_PDF` or pass the path as the first argument).
2. From the repo root, run:
   ```bash
   python3 scripts/extract_eln_guide_images.py
   ```
3. Output is written to `src/images/eln-guide/`. The script uses **pypdf** (embedded images) and **PyMuPDF** (full-page renders for pages 2–4). Install with: `pip install pypdf pymupdf`.
