import re


def parse_resume_to_json(raw_text):
    """
    Extract structured data from resume text:
    - Skills
    - Education
    - Experience
    """
    try:
        skills_pattern = r"(Python|Java|C\+\+|SQL|Machine Learning|AI|Deep Learning|Data Analysis|TensorFlow|PyTorch)"
        education_pattern = r"(B\.Sc|M\.Sc|B\.Tech|M\.Tech|PhD|MBA)"
        experience_pattern = r"(\d+ years|internship|project|worked at|experience)"

        skills = re.findall(skills_pattern, raw_text, re.I)
        education = re.findall(education_pattern, raw_text, re.I)
        experience = re.findall(experience_pattern, raw_text, re.I)

        return {
            "skills": list(set(skills)),
            "education": list(set(education)),
            "experience": list(set(experience)),
            "raw_text": raw_text,
        }
    except Exception as e:
        print(f"Resume parsing failed: {e}")
        return {"skills": [], "education": [], "experience": [], "raw_text": raw_text}


class ResumeParser:
    """Compatibility wrapper providing a class-based API expected by pages.

    Provides parse_resume(raw_text) which returns the same structure as
    parse_resume_to_json.
    """

    def __init__(self):
        pass

    def parse_resume(self, raw_text: str):
        """Parse resume text and return structured JSON-like dict."""
        return parse_resume_to_json(raw_text)
