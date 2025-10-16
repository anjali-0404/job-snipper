from dotenv import load_dotenv
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.llm_utils import generate_text

# Load env
load_dotenv()


def _call_llm(
    prompt: str, temperature: float = 0.3, max_tokens: int = 2048, preferred_provider: str = None
) -> str:
    """Call multi-model LLM and return the text output.

    Inputs:
      - prompt: the instruction + input text
      - temperature: creativity control
      - max_tokens: maximum tokens to generate
      - preferred_provider: preferred LLM provider (groq, gemini, openai, anthropic)

    Returns: generated text (str) or raises on failure.
    """
    try:
        return generate_text(prompt, temperature, max_tokens, preferred_provider)
    except Exception as e:
        raise RuntimeError(f"LLM generation failed: {e}")


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

        try:
            # Use multi-model LLM to generate text
            rewritten_text = _call_llm(prompt, temperature=0.3, max_tokens=2048)

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
        except Exception as llm_error:
            # Graceful fallback: return the original text unchanged
            print(f"⚠ LLM not available ({llm_error}); returning original text as rewritten_text")
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
