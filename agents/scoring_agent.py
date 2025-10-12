def score_resume(parsed_resume):
    """
    Compute a basic resume score (0-100) based on completeness
    """
    try:
        skills_score = min(len(parsed_resume.get("skills", [])) * 10, 30)
        education_score = min(len(parsed_resume.get("education", [])) * 15, 30)
        experience_score = min(len(parsed_resume.get("experience", [])) * 10, 40)

        total_score = skills_score + education_score + experience_score
        return {"score": total_score}
    except Exception as e:
        print(f"Scoring agent failed: {e}")
        return {"score": 0}
