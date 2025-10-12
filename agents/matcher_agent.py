from services.resume_matcher import match_resume_to_jd

def match_resume(parsed_resume, jd_text):
    """
    Match resume against job description
    """
    try:
        match_info = match_resume_to_jd(parsed_resume, jd_text)
        return {
            "match_score": match_info.get("match_score"),
            "matched_skills": match_info.get("matched_skills"),
            "missing_skills": match_info.get("missing_skills")
        }
    except Exception as e:
        print(f"Matcher agent failed: {e}")
        return {"match_score": 0, "matched_skills": [], "missing_skills": []}
