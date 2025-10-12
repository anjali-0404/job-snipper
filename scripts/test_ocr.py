"""Small script to test OCR backends (Tesseract or Google Vision).

Usage:
  python scripts/test_ocr.py /path/to/image_or_pdf

It uses the same `MistralOCR` compatibility wrapper so results should match
what the app would produce.
"""

import sys
from services.mistral_ocr import MistralOCR


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/test_ocr.py /path/to/image_or_pdf")
        return

    path = sys.argv[1]
    ocr = MistralOCR()
    txt = ocr.extract_text(path)
    print("----- OCR RESULT -----")
    print(txt[:500])


if __name__ == "__main__":
    main()
