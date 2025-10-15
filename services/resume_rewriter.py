from dotenv import load_dotenv
import os

# NOTE: This file uses Google's Generative AI (Gemini) via the
# `google-ai-generativelanguage` SDK (recommended option B).
# Install: pip install google-ai-generativelanguage
# Set your API key in the environment variable GOOGLE_API_KEY (or configure
# application default credentials).

# Load env
load_dotenv()
# Support both GOOGLE_API_KEY and GEMINI_API_KEY
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
# Model is set in-code by default. Change this value to use a different Gemini model.
# If you still want environment override, set `GENAI_MODEL` and uncomment the line below.
MODEL = "models/gemini-2.5-flash"
# GENAI_MODEL = os.getenv("GENAI_MODEL", MODEL)  # optional override

try:
    # Newer GenAI client
    from google.ai import generativelanguage as genai
    from google.ai.generativelanguage import types as gl_types
    from google.ai.generativelanguage.services import text_service
    from google.api_core.client_options import ClientOptions

    # Initialize client; if GOOGLE_API_KEY is set, we pass it via client_options
    client_opts = None
    if GOOGLE_API_KEY:
        client_opts = ClientOptions(api_key=GOOGLE_API_KEY)

    _GENAI_CLIENT = text_service.TextServiceClient(client_options=client_opts)
    _HAS_GEMINI = True
except Exception as _e:
    # If the Gemini SDK isn't installed or fails to import, we'll keep a graceful fallback.
    print(
        "Warning: google-ai-generativelanguage SDK not available. Resume rewriter will use a noop fallback.\n",
        "Install with: pip install google-ai-generativelanguage",
    )
    _GENAI_CLIENT = None
    genai = None
    _HAS_GEMINI = False


def _call_gemini(
    prompt: str, model: str | None = None, temperature: float = 0.3
) -> str:
    """Call Gemini model and return the text output.

    Inputs:
      - prompt: the instruction + input text
      - model: Gemini model; default is the value of GENAI_MODEL
      - temperature: creativity control

    Returns: generated text (str) or raises on failure.
    """
    if not _HAS_GEMINI or _GENAI_CLIENT is None:
        raise RuntimeError("Gemini SDK not available")

    if model is None:
        model = MODEL

    # Build request using the newer client types
    request = gl_types.GenerateTextRequest(
        model=model,
        prompt=gl_types.TextPrompt(text=prompt),
        temperature=temperature,
    )

    resp = _GENAI_CLIENT.generate_text(request=request)

    # The response has `candidates` with `.output`
    if hasattr(resp, "candidates") and resp.candidates:
        return "\n".join([c.output for c in resp.candidates])
    return str(resp)


def rewrite_resume(resume_json: dict, instruction: str = None) -> dict:
    """Rewrite resume text with improved bullets and metrics using Gemini.

    Behavior:
      - Reads `raw_text` from the input dict
      - Produces `rewritten_text` on the returned dict
      - On failure, copies `raw_text` to `rewritten_text` and logs the error
      - Detects if AI returned the same content and marks it with metadata

    Args:
      - resume_json: Dictionary containing resume data with 'raw_text' key
      - instruction: Optional custom instruction for rewriting style/focus

    Returns:
      - Dictionary with 'rewritten_text' and metadata about changes
    """
    try:
        raw_text = resume_json.get("raw_text", "")

        # Build prompt with custom instruction if provided
        if instruction:
            prompt = (
                f"{instruction}\n\n"
                "Rewrite the following resume text to have impactful bullet points\n"
                "with measurable metrics wherever possible. Keep each bullet concise and action-oriented.\n"
                "If the resume is already well-written and optimized, you can make minor refinements "
                "or return it as-is if no improvements are needed.\n\n"
                f"Resume text:\n{raw_text}\n\n"
                "Output only the rewritten resume bullets."
            )
        else:
            prompt = (
                "Rewrite the following resume text to have impactful bullet points\n"
                "with measurable metrics wherever possible. Keep each bullet concise and action-oriented.\n"
                "If the resume is already well-written and optimized, you can make minor refinements "
                "or return it as-is if no improvements are needed.\n\n"
                f"Resume text:\n{raw_text}\n\n"
                "Output only the rewritten resume bullets."
            )

        if _HAS_GEMINI:
            # Use Gemini to generate text
            rewritten_text = _call_gemini(prompt, model=None, temperature=0.3)

            # Check if AI returned essentially the same content
            raw_clean = raw_text.strip().lower().replace(" ", "").replace("\n", "")
            rewritten_clean = (
                rewritten_text.strip().lower().replace(" ", "").replace("\n", "")
            )

            if raw_clean == rewritten_clean:
                print("✓ Resume was already optimized - AI returned same content")
                resume_json["no_changes_needed"] = True
                resume_json["change_reason"] = "Resume is already well-optimized"
            else:
                # Calculate similarity
                from difflib import SequenceMatcher

                similarity = SequenceMatcher(None, raw_clean, rewritten_clean).ratio()
                resume_json["no_changes_needed"] = False
                resume_json["similarity_percentage"] = round(similarity * 100, 1)

                if similarity > 0.9:
                    print(f"✓ Minor refinements made ({similarity * 100:.1f}% similar)")
                else:
                    print(
                        f"✓ Significant improvements made ({(1 - similarity) * 100:.1f}% different)"
                    )
        else:
            # Graceful fallback: return the original text unchanged
            print("⚠ Gemini not available; returning original text as rewritten_text")
            rewritten_text = raw_text
            resume_json["no_changes_needed"] = True
            resume_json["change_reason"] = (
                "AI service unavailable - fallback to original"
            )

        resume_json["rewritten_text"] = rewritten_text
        return resume_json
    except Exception as e:
        print(f"❌ Resume rewriting failed: {e}")
        resume_json["rewritten_text"] = resume_json.get("raw_text", "")
        resume_json["no_changes_needed"] = True
        resume_json["change_reason"] = f"Error occurred: {str(e)}"
        return resume_json


class ResumeRewriter:
    """Compatibility wrapper providing a class-based API expected by pages.

    Methods:
      - rewrite_resume(parsed_resume): returns rewritten text (string)
      - tailor_to_job(parsed_resume, job_description): tailor to JD
    """

    def __init__(self):
        pass

    def rewrite_resume(self, parsed_resume: dict) -> str:
        """Return rewritten resume text as a string."""
        result = rewrite_resume(parsed_resume)
        # Return rewritten text if available, otherwise fallback to raw_text
        return result.get("rewritten_text", parsed_resume.get("raw_text", ""))

    def tailor_to_job(self, parsed_resume: dict, job_description: str) -> str:
        """Tailor resume to a job description by passing instruction to the rewrite function."""
        instruction = f"Tailor the resume to the following job description:\n{job_description}"
        result = rewrite_resume(parsed_resume, instruction=instruction)
        return result.get("rewritten_text", parsed_resume.get("raw_text", ""))
