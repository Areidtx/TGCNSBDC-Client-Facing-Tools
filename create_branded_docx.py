"""Create a new TGCNSBDC Word document with embedded header and footer branding."""

import argparse
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.shared import Inches, Pt, RGBColor


def new_branded_document():
    """Return a new document ready for content; do not use to replace existing files."""
    logo = Path(__file__).resolve().parent.parent / "assets" / "tgcnsbdc-logo.png"
    if not logo.is_file():
        raise FileNotFoundError(f"Bundled network logo is missing: {logo}")
    document = Document()
    section = document.sections[0]
    section.page_width = Inches(8.5)
    section.page_height = Inches(11)
    section.top_margin = Inches(1.6)
    section.bottom_margin = Inches(0.7)
    section.left_margin = section.right_margin = Inches(1)
    section.header_distance = Inches(0.35)
    section.footer_distance = Inches(0.35)
    section.different_first_page_header_footer = False
    document.settings.odd_and_even_pages_header_footer = False

    for name in ("Normal", "Title", "Subtitle", "Heading 1", "Heading 2", "Heading 3"):
        style = document.styles[name]
        style.font.name = "Arial"
        style.font.color.rgb = RGBColor(0, 0, 0)
        for border in list(style.element.iter(qn("w:pBdr"))):
            border.getparent().remove(border)
    document.styles["Normal"].font.size = Pt(11)
    document.styles["Normal"].paragraph_format.space_after = Pt(6)

    header = section.header.paragraphs[0]
    header.alignment = WD_ALIGN_PARAGRAPH.LEFT
    header.paragraph_format.space_before = Pt(0)
    header.paragraph_format.space_after = Pt(0)
    header.paragraph_format.line_spacing = 1
    shape = header.add_run().add_picture(str(logo), width=Inches(1.5))
    shape._inline.docPr.set("descr", "America's SBDC Texas Gulf Coast Network logo")

    footer = section.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    footer.paragraph_format.space_before = Pt(0)
    footer.paragraph_format.space_after = Pt(0)
    relation = footer.part.relate_to("https://www.sbdc.uh.edu", RT.HYPERLINK, is_external=True)
    link = OxmlElement("w:hyperlink")
    link.set(qn("r:id"), relation)
    run = OxmlElement("w:r")
    properties = OxmlElement("w:rPr")
    for tag, value in (("w:color", "000000"), ("w:sz", "20")):
        element = OxmlElement(tag)
        element.set(qn("w:val"), value)
        properties.append(element)
    fonts = OxmlElement("w:rFonts")
    fonts.set(qn("w:ascii"), "Arial")
    fonts.set(qn("w:hAnsi"), "Arial")
    properties.append(fonts)
    run.append(properties)
    text = OxmlElement("w:t")
    text.text = "www.sbdc.uh.edu"
    run.append(text)
    link.append(run)
    footer._p.append(link)
    return document


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.suffix.lower() != ".docx":
        parser.error("Output must have a .docx extension.")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    document = new_branded_document()
    with args.output.open("xb") as target:
        document.save(target)
    print(f"Created branded Word document: {args.output}")


if __name__ == "__main__":
    main()
