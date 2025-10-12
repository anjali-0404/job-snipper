from typing import Dict, Any, List

def compute_subscores(parsed_resume: Dict[str, Any]) -> Dict[str, float]:
    """
    Compute basic subscores for:
      - structure (presence of sections)
      - content (length, bullets, metrics tokens heuristics)
      - skills (count, relevance)
      Returns dict of normalized subscores [0..100].
    """
    # Structure: presence of contact, education, experience, skills
    structure_fields = ["raw_text", "education", "experience", "skills"]
    structure_count = sum(1 for f in structure_fields if parsed_resume.get(f))
    structure_score = (structure_count / len(structure_fields)) * 100

    # Skills score: number of unique skills (cap at 20)
    skills = parsed_resume.get("skills", [])
    skills_score = min(len(set(skills)) / 20.0, 1.0) * 100

    # Content score heuristics: presence of numeric tokens (metrics), number of lines/bullets
    raw = parsed_resume.get("raw_text", "") or ""
    lines = [line for line in raw.splitlines() if line.strip()]
    bullets = sum(1 for line in lines if line.strip().startswith(("-", "*", "•")))
    numeric_tokens = sum(1 for token in raw.split() if any(ch.isdigit() for ch in token))
    # scale bullets and numeric tokens
    bullets_score = min(bullets / 6.0, 1.0) * 50  # weight partial
    numeric_score = min(numeric_tokens / 5.0, 1.0) * 50
    content_score = (bullets_score * 0.6) + (numeric_score * 0.4)  # combine

    # normalize content_score to 0..100
    content_score = min(content_score, 100)

    return {
        "structure": round(structure_score, 2),
        "skills": round(skills_score, 2),
        "content": round(content_score, 2)
    }

def combine_scores(subscores: Dict[str, float], weights: Dict[str, float] = None) -> Dict[str, Any]:
    """
    Combine subscores into overall score with optional weights.
    Returns {"overall": xx, "breakdown": {...}}
    """
    if weights is None:
        weights = {"structure": 0.3, "skills": 0.35, "content": 0.35}
    overall = 0.0
    for k,w in weights.items():
        overall += subscores.get(k, 0.0) * w
    overall = round(overall, 2)
    return {"overall": overall, "breakdown": subscores}

def explain_score(parsed_resume: Dict[str, Any], subscores: Dict[str, float]) -> List[str]:
    """
    Produce short human-friendly explanation bullets for each subscore.
    """
    bullets = []
    # structure
    s = subscores.get("structure", 0)
    if s < 50:
        bullets.append("Resume structure incomplete: consider adding or reorganizing Education/Experience/Skills sections.")
    else:
        bullets.append("Resume structure looks good. Sections detected.")

    # skills
    sk = subscores.get("skills", 0)
    if sk < 30:
        bullets.append("Few skills detected — add a focused Skills section with technical keywords relevant to your target roles.")
    else:
        bullets.append("Skills section present; ensure keywords align to target job descriptions.")

    # content
    c = subscores.get("content", 0)
    if c < 40:
        bullets.append("Lacks measurable metrics or bullet-style impact statements — add numbers (e.g., % increase, reduced time by X).")
    else:
        bullets.append("Content contains impact statements or numeric metrics — good!")

    return bullets
