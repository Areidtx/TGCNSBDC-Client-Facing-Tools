---
name: tgcnsbdc-branded-documents
description: Create or format Texas Gulf Coast Network SBDC documents with the supplied network logo at the upper left and www.sbdc.uh.edu in the footer. Use when Amy requests TGCNSBDC branded documents, network letterhead, or an SBDC branded report, handout, agenda, guide, or other Word or PDF document. Apply alongside the relevant document creation skill.
---

# TGCNSBDC Branded Documents

## Required branding

- Use the original bundled logo at `assets/tgcnsbdc-logo.png`. Do not redraw, recolor, crop, stretch, or substitute it. Do not ask for another upload when the bundled asset is available.
- Place the logo at the upper left in the page header, aligned with the left body margin. Repeat it on every page, including the first page, unless the user specifies otherwise.
- Display exactly `www.sbdc.uh.edu` in the footer on every page. Center it by default. Link the text to `https://www.sbdc.uh.edu` where supported.
- Keep header and footer content clear of body text and tables. Preserve the logo proportions and legibility. Use approximately 1.5 inches of logo width as a starting point; avoid enlarging the supplied raster image unnecessarily.
- Treat logo placement and the website as user requirements. Treat size, footer alignment, font, margins, and repeating placement as adjustable defaults rather than an official brand manual. Honor later user instructions.

## Workflow

1. Determine the document purpose and requested content from the current request. Use Word DOCX by default. Produce PDF when requested, preferably by exporting the verified Word document. Do not create both formats unless requested.
2. Read and follow the available documents skill for Word authoring and rendering, or the PDF skill for a PDF-only workflow. Use this skill for branding and the format skill for construction and verification.
3. For a new Word document, use `scripts/create_branded_docx.py` to create the branded shell, or import `new_branded_document()` from that script and add content before saving. Resolve all asset paths relative to this skill directory, including after installation changes its directory name.
4. Use US Letter portrait, readable black text, Arial 11 pt, 1-inch side margins, a 1.6-inch top margin, and a 0.7-inch bottom margin as starting defaults. Adapt the layout for the requested content. Keep headings clear and professional and leave whitespace below the logo.
5. For an existing document, preserve its content, tables, page orientation, section breaks, and useful layout. Edit branding in a copy. Inspect existing headers and footers before changing them; retain required notices, page numbers, and other necessary content. Replace obsolete logos only when the requested rebranding authorizes it. Do not use the new-document helper to overwrite an existing document.
6. Inspect every section and any active first-page or even-page header/footer variants. Ensure the logo and website repeat through section transitions without duplicates. Set adequate space for the header rather than letting it overlap the body.
7. Write in a direct, professional small business advising tone. Avoid contractions. Do not add unrequested slogans, contact information, funding statements, or claims of approval.
8. Render the completed document and inspect every page. Verify that the logo retains its colors and proportions, both branding elements are legible, no content overlaps them, and no unexpected blank pages appear. For a PDF, verify the final PDF pages as well.
9. Save requested user-facing documents through the Library workflow and provide the final file link. Keep internal test documents and render images out of the deliverables unless requested.

## Reusable Word helper

Run with the available document runtime Python:

```bash
"$CODEX_PRIMARY_RUNTIME_PYTHON" /absolute/path/to/this-skill/scripts/create_branded_docx.py --output /absolute/path/to/new-document.docx
```

The helper creates a new branded Word shell and refuses to overwrite an existing file. Add the requested content using the documents skill, then render and inspect the completed result. For direct authoring, import `new_branded_document()` and save the returned `python-docx` document after adding content. Keep the image embedded in the document so recipients do not need the original asset file.
