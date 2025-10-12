from dotenv import load_dotenv
import os

# This file now uses Google Gemini via the `google-ai-generativelanguage` SDK.
# It exposes a thin wrapper compatible with the previous `llm.call(prompt)` usage.
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL = os.getenv("GENAI_MODEL", "models/gemini-2.5-flash")

try:
    from google.ai import generativelanguage as genai
    from google.ai.generativelanguage import types as gl_types
    from google.ai.generativelanguage.services import text_service
    from google.api_core.client_options import ClientOptions

    client_opts = None
    if GOOGLE_API_KEY:
        client_opts = ClientOptions(api_key=GOOGLE_API_KEY)

    _GENAI_CLIENT = text_service.TextServiceClient(client_options=client_opts)
    _HAS_GEMINI = True
except Exception:
    genai = None
    _GENAI_CLIENT = None
    _HAS_GEMINI = False


class GeminiWrapper:
    """Thin wrapper that exposes .call(prompt) to match previous usage."""

    def __init__(self, model: str = MODEL, temperature: float = 0.3):
        self.model = model
        self.temperature = temperature

    def call(self, prompt: str) -> str:
        if not _HAS_GEMINI or _GENAI_CLIENT is None:
            raise RuntimeError("Gemini SDK not available")

        request = gl_types.GenerateTextRequest(
            model=self.model,
            prompt=gl_types.TextPrompt(text=prompt),
            temperature=self.temperature,
        )

        resp = _GENAI_CLIENT.generate_text(request=request)
        if hasattr(resp, "candidates") and resp.candidates:
            return "\n".join([c.output for c in resp.candidates])
        return str(resp)


# Create default wrapper instance
llm = GeminiWrapper()


def generate_cover_letter(resume_json, jd_text, tone="formal"):
    """
    Generate a tailored cover letter
    """
    try:
        rewritten_resume = resume_json.get(
            "rewritten_text", resume_json.get("raw_text", "")
        )
        prompt = f"""
        Generate a {tone} cover letter for the following job description:

        Job Description:
        {jd_text}

        Candidate Resume:
        {rewritten_resume}
        """
        cover_letter = llm.call(prompt)
        return cover_letter
    except Exception as e:
        print(f"Cover letter generation failed: {e}")
        return ""
