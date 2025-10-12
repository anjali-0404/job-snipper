"""
Job Description Matcher
Analyzes job descriptions and customizes resumes to match requirements.
"""

import re
from collections import Counter
from typing import Dict, List, Tuple, Any


class JobMatcher:
    """Match resume content to job descriptions and provide optimization suggestions."""

    def __init__(self):
        # Common job-related keywords categories
        self.skill_indicators = [
            "experience",
            "proficient",
            "knowledge",
            "familiar",
            "expertise",
            "skilled",
            "understanding",
            "background",
            "strong",
            "demonstrated",
        ]

        self.requirement_indicators = [
            "required",
            "must have",
            "essential",
            "mandatory",
            "necessary",
            "should have",
            "preferred",
            "desired",
            "ideal",
            "looking for",
        ]

    def extract_keywords(
        self, job_description: str, top_n: int = 30
    ) -> List[Dict[str, Any]]:
        """
        Extract key terms from job description.

        Args:
            job_description: The job posting text
            top_n: Number of top keywords to return

        Returns:
            List of dictionaries with keyword info
        """
        # Clean and tokenize
        text = job_description.lower()

        # Remove common words
        stop_words = {
            "the",
            "a",
            "an",
            "and",
            "or",
            "but",
            "in",
            "on",
            "at",
            "to",
            "for",
            "of",
            "with",
            "by",
            "from",
            "as",
            "is",
            "was",
            "are",
            "be",
            "been",
            "being",
            "have",
            "has",
            "had",
            "do",
            "does",
            "did",
            "will",
            "would",
            "should",
            "could",
            "may",
            "might",
            "must",
            "can",
            "this",
            "that",
            "these",
            "those",
            "i",
            "you",
            "he",
            "she",
            "it",
            "we",
            "they",
        }

        # Extract words (including compound words like "machine learning")
        words = re.findall(r"\b[a-z]+\b", text)

        # Get bigrams (two-word phrases)
        bigrams = [f"{words[i]} {words[i + 1]}" for i in range(len(words) - 1)]

        # Get trigrams (three-word phrases)
        trigrams = [
            f"{words[i]} {words[i + 1]} {words[i + 2]}" for i in range(len(words) - 2)
        ]

        # Combine all
        all_terms = words + bigrams + trigrams

        # Filter stop words and short terms
        filtered_terms = [
            term for term in all_terms if term not in stop_words and len(term) > 2
        ]

        # Count frequencies
        term_counts = Counter(filtered_terms)

        # Get top terms
        top_terms = term_counts.most_common(top_n)

        # Format results
        keywords = []
        for term, count in top_terms:
            keywords.append(
                {
                    "keyword": term,
                    "frequency": count,
                    "type": self._classify_keyword(term),
                }
            )

        return keywords

    def _classify_keyword(self, keyword: str) -> str:
        """Classify keyword type (skill, tool, soft skill, etc.)"""

        # Programming languages and frameworks
        tech_keywords = {
            "python",
            "java",
            "javascript",
            "react",
            "node",
            "angular",
            "vue",
            "typescript",
            "c++",
            "c#",
            "ruby",
            "go",
            "rust",
            "swift",
            "kotlin",
            "django",
            "flask",
            "spring",
            "express",
            "fastapi",
            "laravel",
            "tensorflow",
            "pytorch",
            "keras",
            "scikit",
            "pandas",
            "numpy",
        }

        # Tools and platforms
        tool_keywords = {
            "git",
            "docker",
            "kubernetes",
            "aws",
            "azure",
            "gcp",
            "jenkins",
            "jira",
            "confluence",
            "slack",
            "figma",
            "sketch",
            "photoshop",
            "excel",
            "powerpoint",
            "salesforce",
            "tableau",
            "power bi",
        }

        # Soft skills
        soft_skills = {
            "leadership",
            "communication",
            "teamwork",
            "problem solving",
            "analytical",
            "creative",
            "collaborative",
            "adaptable",
            "organized",
            "detail oriented",
            "time management",
            "critical thinking",
        }

        # Check classifications
        if any(tech in keyword for tech in tech_keywords):
            return "Technical Skill"
        elif any(tool in keyword for tool in tool_keywords):
            return "Tool/Platform"
        elif any(soft in keyword for soft in soft_skills):
            return "Soft Skill"
        elif any(ind in keyword for ind in self.requirement_indicators):
            return "Requirement"
        else:
            return "General"

    def calculate_match_score(
        self, resume_text: str, job_description: str
    ) -> Dict[str, Any]:
        """
        Calculate how well resume matches job description.

        Args:
            resume_text: Resume content
            job_description: Job posting text

        Returns:
            Dictionary with match score and details
        """
        # Extract keywords from job description
        job_keywords = self.extract_keywords(job_description, top_n=50)

        # Normalize texts
        resume_lower = resume_text.lower()

        # Calculate matches
        matched_keywords = []
        missing_keywords = []

        for kw_info in job_keywords:
            keyword = kw_info["keyword"]
            if keyword in resume_lower:
                matched_keywords.append(kw_info)
            else:
                missing_keywords.append(kw_info)

        # Calculate score (weighted by frequency)
        total_weight = sum(kw["frequency"] for kw in job_keywords)
        matched_weight = sum(kw["frequency"] for kw in matched_keywords)

        match_score = (matched_weight / total_weight * 100) if total_weight > 0 else 0

        # Extract required skills that are missing
        critical_missing = [
            kw
            for kw in missing_keywords
            if kw["type"] in ["Technical Skill", "Tool/Platform"]
            and kw["frequency"] >= 2
        ]

        return {
            "overall_score": round(match_score, 1),
            "matched_keywords": matched_keywords[:20],  # Top 20
            "missing_keywords": missing_keywords[:20],  # Top 20
            "critical_missing": critical_missing[:10],  # Top 10 critical
            "match_ratio": f"{len(matched_keywords)}/{len(job_keywords)}",
            "recommendations": self._generate_recommendations(
                missing_keywords, critical_missing
            ),
        }

    def _generate_recommendations(
        self, missing_keywords: List[Dict], critical_missing: List[Dict]
    ) -> List[str]:
        """Generate actionable recommendations."""

        recommendations = []

        if critical_missing:
            recommendations.append(
                f"⚠️ Add these {len(critical_missing)} critical skills to your resume: "
                f"{', '.join([kw['keyword'] for kw in critical_missing[:5]])}"
            )

        # Group by type
        missing_by_type = {}
        for kw in missing_keywords[:15]:
            kw_type = kw["type"]
            if kw_type not in missing_by_type:
                missing_by_type[kw_type] = []
            missing_by_type[kw_type].append(kw["keyword"])

        for kw_type, keywords in missing_by_type.items():
            if keywords:
                recommendations.append(
                    f"📌 Consider adding {kw_type.lower()}: {', '.join(keywords[:3])}"
                )

        if not recommendations:
            recommendations.append("✅ Your resume covers most key requirements!")

        return recommendations

    def identify_skill_gaps(
        self, resume_text: str, job_description: str
    ) -> Dict[str, List[str]]:
        """
        Identify specific skill gaps between resume and job.

        Args:
            resume_text: Resume content
            job_description: Job posting text

        Returns:
            Dictionary categorizing skill gaps
        """
        match_data = self.calculate_match_score(resume_text, job_description)

        gaps = {
            "technical_skills": [],
            "tools_platforms": [],
            "soft_skills": [],
            "certifications": [],
            "other": [],
        }

        for kw in match_data["missing_keywords"]:
            keyword = kw["keyword"]
            kw_type = kw["type"]

            if kw_type == "Technical Skill":
                gaps["technical_skills"].append(keyword)
            elif kw_type == "Tool/Platform":
                gaps["tools_platforms"].append(keyword)
            elif kw_type == "Soft Skill":
                gaps["soft_skills"].append(keyword)
            elif "certif" in keyword or "degree" in keyword:
                gaps["certifications"].append(keyword)
            else:
                gaps["other"].append(keyword)

        # Limit each category
        for category in gaps:
            gaps[category] = gaps[category][:10]

        return gaps

    def generate_tailored_suggestions(
        self, resume_text: str, job_description: str
    ) -> List[Dict[str, str]]:
        """
        Generate specific suggestions to tailor resume for job.

        Args:
            resume_text: Resume content
            job_description: Job posting text

        Returns:
            List of actionable suggestions
        """
        match_data = self.calculate_match_score(resume_text, job_description)
        job_keywords = self.extract_keywords(job_description, top_n=30)

        suggestions = []

        # Suggestion 1: Add critical keywords
        if match_data["critical_missing"]:
            critical_kw = [kw["keyword"] for kw in match_data["critical_missing"][:3]]
            suggestions.append(
                {
                    "priority": "High",
                    "category": "Keywords",
                    "suggestion": f"Add these critical keywords: {', '.join(critical_kw)}",
                    "action": f"Include '{critical_kw[0]}' in your experience or skills section",
                    "impact": "Significantly improves ATS match score",
                }
            )

        # Suggestion 2: Skill emphasis
        tech_missing = [
            kw["keyword"]
            for kw in match_data["missing_keywords"]
            if kw["type"] == "Technical Skill"
        ][:3]

        if tech_missing:
            suggestions.append(
                {
                    "priority": "High",
                    "category": "Technical Skills",
                    "suggestion": f"Highlight these technical skills: {', '.join(tech_missing)}",
                    "action": f"Add a 'Technical Skills' section or mention in experience",
                    "impact": "Matches job technical requirements",
                }
            )

        # Suggestion 3: Action verbs alignment
        job_lower = job_description.lower()
        action_verbs = [
            "led",
            "managed",
            "developed",
            "implemented",
            "designed",
            "created",
        ]
        found_verbs = [verb for verb in action_verbs if verb in job_lower]

        if found_verbs:
            suggestions.append(
                {
                    "priority": "Medium",
                    "category": "Language",
                    "suggestion": f"Use action verbs like: {', '.join(found_verbs[:3])}",
                    "action": "Rephrase experience bullets to start with these verbs",
                    "impact": "Aligns language with job description",
                }
            )

        # Suggestion 4: Quantifiable metrics
        if (
            "%" in job_description
            or "increase" in job_description
            or "improve" in job_description
        ):
            suggestions.append(
                {
                    "priority": "Medium",
                    "category": "Achievements",
                    "suggestion": "Add quantifiable metrics to your achievements",
                    "action": "Include percentages, numbers, dollar amounts in bullet points",
                    "impact": "Demonstrates measurable impact",
                }
            )

        # Suggestion 5: Section optimization
        sections_mentioned = []
        if "education" in job_description.lower():
            sections_mentioned.append("Education")
        if "project" in job_description.lower():
            sections_mentioned.append("Projects")
        if "certif" in job_description.lower():
            sections_mentioned.append("Certifications")

        if sections_mentioned:
            suggestions.append(
                {
                    "priority": "Low",
                    "category": "Structure",
                    "suggestion": f"Emphasize these sections: {', '.join(sections_mentioned)}",
                    "action": f"Ensure {sections_mentioned[0]} section is detailed and prominent",
                    "impact": "Matches expected resume structure",
                }
            )

        return suggestions

    def generate_customized_resume_prompt(
        self, resume_text: str, job_description: str
    ) -> str:
        """
        Generate an AI prompt to customize resume for specific job.

        Args:
            resume_text: Resume content
            job_description: Job posting text

        Returns:
            Prompt string for AI resume customization
        """
        match_data = self.calculate_match_score(resume_text, job_description)
        gaps = self.identify_skill_gaps(resume_text, job_description)

        # Build comprehensive prompt
        prompt = f"""Customize the following resume for this specific job description.

JOB DESCRIPTION:
{job_description[:1000]}...

CURRENT MATCH SCORE: {match_data["overall_score"]}%

CRITICAL KEYWORDS TO ADD:
{", ".join([kw["keyword"] for kw in match_data["critical_missing"][:10]])}

MISSING TECHNICAL SKILLS:
{", ".join(gaps["technical_skills"][:5])}

MISSING TOOLS/PLATFORMS:
{", ".join(gaps["tools_platforms"][:5])}

CUSTOMIZATION INSTRUCTIONS:
1. Incorporate the critical keywords naturally into experience bullets
2. Emphasize relevant technical skills and projects
3. Align language and action verbs with job description
4. Highlight transferable skills that match requirements
5. Reorder sections to prioritize most relevant experience
6. Add specific tools/technologies mentioned in job description
7. Maintain truthfulness - only add skills you actually have
8. Keep ATS-friendly formatting

ORIGINAL RESUME:
{resume_text}

Please rewrite the resume to better match this job while maintaining accuracy and professionalism."""

        return prompt

    def compare_resumes(
        self, original_resume: str, tailored_resume: str, job_description: str
    ) -> Dict[str, Any]:
        """
        Compare original vs tailored resume against job description.

        Args:
            original_resume: Original resume text
            tailored_resume: Customized resume text
            job_description: Job posting text

        Returns:
            Comparison metrics
        """
        original_match = self.calculate_match_score(original_resume, job_description)
        tailored_match = self.calculate_match_score(tailored_resume, job_description)

        improvement = tailored_match["overall_score"] - original_match["overall_score"]

        return {
            "original_score": original_match["overall_score"],
            "tailored_score": tailored_match["overall_score"],
            "improvement": round(improvement, 1),
            "improvement_percentage": round(
                (improvement / original_match["overall_score"] * 100)
                if original_match["overall_score"] > 0
                else 0,
                1,
            ),
            "keywords_added": len(tailored_match["matched_keywords"])
            - len(original_match["matched_keywords"]),
            "gaps_filled": len(original_match["missing_keywords"])
            - len(tailored_match["missing_keywords"]),
            "status": "Excellent"
            if tailored_match["overall_score"] >= 80
            else "Good"
            if tailored_match["overall_score"] >= 60
            else "Needs Work",
        }
