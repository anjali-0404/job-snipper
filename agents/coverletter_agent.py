from services.coverletter_gen import generate_cover_letter as _gen_cover_letter


def generate_cover_letter(parsed_resume, context):
    """
    Generate a personalized cover letter based on resume and job context

    Args:
        parsed_resume: Dictionary containing resume data
        context: Dictionary with keys:
            - company: Company name
            - position: Job title
            - job_description: Full job description text
            - tone: Tone style (professional, enthusiastic, formal, creative)
            - highlight_skills: List of skills to emphasize
    """
    try:
        # Extract context
        company = context.get("company", "")
        position = context.get("position", "")
        job_description = context.get("job_description", "")
        tone = context.get("tone", "professional")
        highlight_skills = context.get("highlight_skills", [])

        # Build comprehensive job description text
        jd_text = f"""
Company: {company}
Position: {position}

{job_description if job_description else f"Position: {position} at {company}"}

{f"Key skills to highlight: {', '.join(highlight_skills)}" if highlight_skills else ""}
        """.strip()

        # Call the service function
        cover_letter = _gen_cover_letter(parsed_resume, jd_text, tone)
        return cover_letter
    except Exception as e:
        print(f"Cover letter agent failed: {e}")
        return f"Error generating cover letter: {str(e)}"


def generate_coverletter(parsed_resume, jd_text, tone="formal"):
    """
    Legacy function for backward compatibility
    """
    return _gen_cover_letter(parsed_resume, jd_text, tone)
