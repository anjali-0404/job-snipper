from services.resume_rewriter import rewrite_resume

def rewrite_resume_agent(parsed_resume):
    """
    Rewrite resume with stronger bullet points and metrics
    """
    try:
        rewritten = rewrite_resume(parsed_resume)
        return rewritten
    except Exception as e:
        print(f"Rewrite agent failed: {e}")
        return parsed_resume
