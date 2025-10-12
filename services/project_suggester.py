def suggest_projects(resume_json, missing_skills):
    """
    Suggest portfolio projects to fill skill gaps
    """
    try:
        suggestions = []
        for skill in missing_skills:
            suggestions.append(f"Build a portfolio project using {skill} to improve proficiency")
        return suggestions
    except Exception as e:
        print(f"Project suggestion failed: {e}")
        return []
