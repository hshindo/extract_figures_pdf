import sys
from pathlib import Path
import fitz


def main(path: str):
    out_path = Path(path) / "images"
    if not out_path.exists():
        out_path.mkdir()

    for pdf_file in Path(path).glob("*.pdf"):
        print(pdf_file)
        doc = fitz.open(str(pdf_file))
        for i, page in enumerate(doc):
            pix = page.get_pixmap()
            pix.save(f"{out_path}/{pdf_file.name}_{i:03}.png")


if __name__ == "__main__":
    path = sys.argv[1]
    main(path)
