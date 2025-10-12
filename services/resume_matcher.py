from difflib import SequenceMatcher
import re

def match_resume_to_jd(resume_data, job_description):
    """
    Match resume data against a job description.
    Returns a similarity score and matched keywords.
    """
    try:
        resume_text = " ".join(resume_data.get("skills", []) + 
                               resume_data.get("education", []) + 
                               resume_data.get("experience", []))
        
        # Simple similarity measure using SequenceMatcher
        similarity = SequenceMatcher(None, resume_text.lower(), job_description.lower()).ratio()
        
        # Extract keywords from job description for matching
        jd_keywords = set(re.findall(r"\b\w+\b", job_description.lower()))
        resume_keywords = set(re.findall(r"\b\w+\b", resume_text.lower()))
        
        matched_keywords = jd_keywords.intersection(resume_keywords)
        
        return {
            "similarity_score": similarity,
            "matched_keywords": list(matched_keywords)
        }
    except Exception as e:
        print(f"Resume matching failed: {e}")
        return {"similarity_score": 0.0, "matched_keywords": []}    
    