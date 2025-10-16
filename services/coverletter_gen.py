from dotenv import load_dotenv
import os

# This file now uses Google Gemini via the `google-ai-generativelanguage` SDK.
# It exposes a thin wrapper compatible with the previous `llm.call(prompt)` usage.
load_dotenv()
# Support both GOOGLE_API_KEY and GEMINI_API_KEY
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GENAI_MODEL", "models/gemini-2.5-flash")

try:
    # Use importlib to import the generative language SDK modules dynamically. This avoids
    # static import paths that some linters or editors may not be able to resolve while
    # preserving runtime imports when the package is installed in the active environment.
    import importlib

    genai = importlib.import_module("google.ai.generativelanguage")
    gl_types = importlib.import_module("google.ai.generativelanguage.types")

    # Try to load the concrete TextServiceClient class from the SDK. Some SDK versions
    # expose this under services.text_service, so we attempt that first and fall back to
    # a module-level lookup if needed.
    TextServiceClient = None
    try:
        _text_svc_mod = importlib.import_module(
            "google.ai.generativelanguage.services.text_service"
        )
        TextServiceClient = getattr(_text_svc_mod, "TextServiceClient", None)
    except Exception:
        try:
            _svc_mod = importlib.import_module("google.ai.generativelanguage.services")
            TextServiceClient = getattr(_svc_mod, "TextServiceClient", None)
        except Exception:
            TextServiceClient = None

    # Import ClientOptions dynamically as well
    try:
        api_core_mod = importlib.import_module("google.api_core.client_options")
        ClientOptions = getattr(api_core_mod, "ClientOptions", None)
    except Exception:
        ClientOptions = None

    client_opts = None
    if GOOGLE_API_KEY and ClientOptions is not None:
        client_opts = ClientOptions(api_key=GOOGLE_API_KEY)

    # Create client if the class is available
    if TextServiceClient is not None:
        _GENAI_CLIENT = TextServiceClient(client_options=client_opts)
        _HAS_GEMINI = True
    else:
        _GENAI_CLIENT = None
        _HAS_GEMINI = False
except Exception:
    genai = None
    gl_types = None
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
