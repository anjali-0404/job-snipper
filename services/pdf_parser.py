# Try to import PyMuPDF (fitz); fall back to pdfplumber if unavailable.
try:
    import fitz  # PyMuPDF
    HAS_FITZ = True
except Exception:
    fitz = None
    HAS_FITZ = False

try:
    import pdfplumber
    HAS_PDFPLUMBER = True
except Exception:
    pdfplumber = None
    HAS_PDFPLUMBER = False

def parse_pdf(file_path):
    """  Extract text from a pdf using PyMuPDF (preferred) or pdfplumber as fallback """
    if HAS_FITZ:
        try:
            doc = fitz.open(file_path)
            text = ""
            for page in doc:
                text += page.get_text()
            return text
        except Exception as e:
            print(f"PDF parsing with PyMuPDF failed: {e}")
            # fall through to try pdfplumber if available

    if HAS_PDFPLUMBER:
        try:
            pages = []
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    pages.append(page.extract_text() or "")
            return "\n".join(pages)
        except Exception as e:
            print(f"PDF parsing with pdfplumber failed: {e}")
            return ""

    print("No PDF parser available: install 'PyMuPDF' (fitz) or 'pdfplumber'.")
    return ""
    