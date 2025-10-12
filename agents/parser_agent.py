from services.pdf_parser import parse_pdf
from services.docx_parser import parse_docx
from services.mistral_ocr import MistralOCR
from services.resume_parser import parse_resume_to_json


def parse_resume(file_path, file_type):
    """
    Parse a resume file into structured JSON.
    Supports PDF, DOCX, and OCR for scanned PDFs.
    """
    try:
        if file_type == "pdf":
            text = parse_pdf(file_path)
        elif file_type == "docx":
            text = parse_docx(file_path)
        else:
            raise ValueError("Unsupported file type")

        # If text is empty, try OCR via the configured OCR backend
        if not text.strip():
            try:
                ocr = MistralOCR()
                text = ocr.extract_text(file_path) or ""
            except Exception as e:
                print(f"OCR fallback failed: {e}")
                text = ""

        parsed_resume = parse_resume_to_json(text)
        return parsed_resume
    except Exception as e:
        print(f"Parser agent failed: {e}")
        return {"skills": [], "education": [], "experience": [], "raw_text": ""}
