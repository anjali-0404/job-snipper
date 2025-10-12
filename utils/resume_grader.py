"""
Resume Grader
Comprehensive 50+ point checklist evaluation.
"""

from typing import Dict, List, Any
import re


class ResumeGrader:
    """Grade resume on comprehensive checklist."""

    def __init__(self):
        self.max_score = 100
        self.weight_distribution = {
            "content": 40,
            "formatting": 25,
            "impact": 20,
            "ats_compatibility": 15,
        }

    def grade_resume(
        self, resume_text: str, resume_format: str = "unknown"
    ) -> Dict[str, Any]:
        """Comprehensive resume grading."""

        content_score = self._grade_content(resume_text)
        formatting_score = self._grade_formatting(resume_text, resume_format)
        impact_score = self._grade_impact(resume_text)
        ats_score = self._grade_ats_compatibility(resume_text, resume_format)

        # Calculate weighted total
        total_score = (
            content_score["score"] * self.weight_distribution["content"] / 100
            + formatting_score["score"] * self.weight_distribution["formatting"] / 100
            + impact_score["score"] * self.weight_distribution["impact"] / 100
            + ats_score["score"] * self.weight_distribution["ats_compatibility"] / 100
        )

        grade_letter = self._calculate_grade(total_score)

        return {
            "total_score": round(total_score, 1),
            "grade": grade_letter,
            "content": content_score,
            "formatting": formatting_score,
            "impact": impact_score,
            "ats_compatibility": ats_score,
            "summary": self._generate_summary(total_score, grade_letter),
            "top_improvements": self._get_top_improvements(
                content_score, formatting_score, impact_score, ats_score
            ),
        }

    def _grade_content(self, text: str) -> Dict[str, Any]:
        """Grade content quality."""

        score = 0
        max_points = 100
        feedback = []

        # Check for required sections (25 points)
        required_sections = {
            "experience": r"(experience|work history|employment)",
            "education": r"(education|academic|degree)",
            "skills": r"(skills|technical skills|competencies)",
            "contact": r"(email|phone|linkedin)",
        }

        sections_found = 0
        for section_name, pattern in required_sections.items():
            if re.search(pattern, text, re.IGNORECASE):
                sections_found += 1
                score += 6.25
                feedback.append(f"✅ Has {section_name} section")
            else:
                feedback.append(f"❌ Missing {section_name} section")

        # Check word count (15 points)
        word_count = len(text.split())
        if 300 <= word_count <= 600:
            score += 15
            feedback.append(f"✅ Good length ({word_count} words)")
        elif word_count < 300:
            score += 7
            feedback.append(f"⚠️ Too short ({word_count} words) - add more details")
        else:
            score += 10
            feedback.append(f"⚠️ Too long ({word_count} words) - be more concise")

        # Check for summary/objective (10 points)
        if re.search(r"(summary|objective|about|profile)", text, re.IGNORECASE):
            score += 10
            feedback.append("✅ Has professional summary")
        else:
            feedback.append("❌ Missing professional summary")

        # Check for quantifiable achievements (20 points)
        numbers = re.findall(r"\b\d+%?|\$\d+[KkMmBb]?\b", text)
        if len(numbers) >= 5:
            score += 20
            feedback.append(f"✅ Good use of metrics ({len(numbers)} numbers found)")
        elif len(numbers) >= 3:
            score += 12
            feedback.append(f"⚠️ Use more metrics ({len(numbers)} found, aim for 5+)")
        else:
            feedback.append(
                f"❌ Insufficient metrics ({len(numbers)} found, aim for 5+)"
            )

        # Check for action verbs (15 points)
        action_verbs = [
            "achieved",
            "improved",
            "increased",
            "led",
            "managed",
            "developed",
            "created",
            "implemented",
            "designed",
            "built",
            "launched",
            "optimized",
        ]
        verbs_found = sum(1 for verb in action_verbs if verb in text.lower())

        if verbs_found >= 5:
            score += 15
            feedback.append(f"✅ Strong action verbs ({verbs_found} found)")
        elif verbs_found >= 3:
            score += 10
            feedback.append(f"⚠️ Use more action verbs ({verbs_found} found)")
        else:
            feedback.append(f"❌ Weak action verbs ({verbs_found} found)")

        # Check for buzzwords/clichés to avoid (15 points deduction potential)
        buzzwords = [
            "hardworking",
            "team player",
            "go-getter",
            "self-starter",
            "results-oriented",
            "detail-oriented",
            "dynamic",
        ]
        buzzwords_found = [word for word in buzzwords if word in text.lower()]

        if len(buzzwords_found) == 0:
            score += 15
            feedback.append("✅ Avoids clichés and buzzwords")
        elif len(buzzwords_found) <= 2:
            score += 8
            feedback.append(f"⚠️ Some buzzwords detected: {', '.join(buzzwords_found)}")
        else:
            feedback.append(f"❌ Too many buzzwords: {', '.join(buzzwords_found)}")

        return {
            "score": min(score, max_points),
            "max_points": max_points,
            "feedback": feedback,
            "sections_found": sections_found,
            "word_count": word_count,
        }

    def _grade_formatting(self, text: str, resume_format: str) -> Dict[str, Any]:
        """Grade formatting and structure."""

        score = 0
        max_points = 100
        feedback = []

        # Check format type (20 points)
        if resume_format.lower() in ["pdf", "docx"]:
            score += 20
            feedback.append(f"✅ Good format ({resume_format.upper()})")
        elif resume_format.lower() == "txt":
            score += 10
            feedback.append("⚠️ Plain text - consider PDF or DOCX")
        else:
            feedback.append("❌ Unknown format - use PDF or DOCX")

        # Check for consistent bullet points (20 points)
        bullet_patterns = [r"^\s*[-•●]\s", r"^\s*\*\s", r"^\s*\d+\.\s"]
        bullets_used = []
        for pattern in bullet_patterns:
            if re.search(pattern, text, re.MULTILINE):
                bullets_used.append(pattern)

        if len(bullets_used) == 1:
            score += 20
            feedback.append("✅ Consistent bullet style")
        elif len(bullets_used) > 1:
            score += 10
            feedback.append("⚠️ Mixed bullet styles - use one style consistently")
        else:
            feedback.append("❌ No bullets used - use bullets for achievements")

        # Check line length (15 points)
        lines = text.split("\n")
        long_lines = [line for line in lines if len(line) > 100]

        if len(long_lines) == 0:
            score += 15
            feedback.append("✅ Good line lengths")
        elif len(long_lines) <= 3:
            score += 10
            feedback.append(f"⚠️ Some long lines ({len(long_lines)} lines > 100 chars)")
        else:
            feedback.append(
                f"❌ Too many long lines ({len(long_lines)} lines > 100 chars)"
            )

        # Check for proper spacing (15 points)
        double_spaces = text.count("  ")
        if double_spaces <= 5:
            score += 15
            feedback.append("✅ Clean spacing")
        else:
            score += 8
            feedback.append(f"⚠️ Multiple spaces detected ({double_spaces} instances)")

        # Check for section headers (15 points)
        headers = re.findall(r"^[A-Z][A-Z\s]+$", text, re.MULTILINE)
        if len(headers) >= 3:
            score += 15
            feedback.append(f"✅ Clear section headers ({len(headers)} found)")
        elif len(headers) >= 2:
            score += 10
            feedback.append(f"⚠️ Add more section headers ({len(headers)} found)")
        else:
            feedback.append("❌ Missing clear section headers")

        # Check for date formatting consistency (15 points)
        date_patterns = [
            r"\d{4}[-/]\d{2}",  # 2020-01 or 2020/01
            r"\w+ \d{4}",  # January 2020
            r"\d{2}/\d{4}",  # 01/2020
        ]
        dates_found = []
        for pattern in date_patterns:
            dates_found.extend(re.findall(pattern, text))

        if len(dates_found) >= 2:
            score += 15
            feedback.append("✅ Has dates for experiences")
        else:
            feedback.append("⚠️ Missing dates for work experience")

        return {
            "score": min(score, max_points),
            "max_points": max_points,
            "feedback": feedback,
        }

    def _grade_impact(self, text: str) -> Dict[str, Any]:
        """Grade overall impact and effectiveness."""

        score = 0
        max_points = 100
        feedback = []

        # Check for leadership indicators (25 points)
        leadership_words = [
            "led",
            "managed",
            "supervised",
            "directed",
            "coordinated",
            "mentored",
            "trained",
            "guided",
        ]
        leadership_count = sum(1 for word in leadership_words if word in text.lower())

        if leadership_count >= 3:
            score += 25
            feedback.append(f"✅ Strong leadership indicators ({leadership_count})")
        elif leadership_count >= 1:
            score += 15
            feedback.append(f"⚠️ Some leadership shown ({leadership_count})")
        else:
            feedback.append("❌ No leadership indicators")

        # Check for impact/results focus (25 points)
        impact_words = [
            "increased",
            "decreased",
            "improved",
            "reduced",
            "saved",
            "generated",
            "grew",
            "exceeded",
        ]
        impact_count = sum(1 for word in impact_words if word in text.lower())

        if impact_count >= 4:
            score += 25
            feedback.append(f"✅ Results-focused ({impact_count} impact words)")
        elif impact_count >= 2:
            score += 15
            feedback.append(f"⚠️ Show more results ({impact_count} impact words)")
        else:
            feedback.append("❌ Lacks results/impact focus")

        # Check for industry-specific keywords (20 points)
        # This is a simplified check - would need customization per industry
        if len(text.split()) > 200:
            score += 20
            feedback.append("✅ Sufficient detail for context")
        else:
            score += 10
            feedback.append("⚠️ Add more specific details")

        # Check for progression/growth (15 points)
        progression_words = [
            "promoted",
            "advanced",
            "progressed",
            "grew from",
            "started as",
        ]
        if any(word in text.lower() for word in progression_words):
            score += 15
            feedback.append("✅ Shows career progression")
        else:
            feedback.append("⚠️ Consider highlighting career growth")

        # Check for technical depth (15 points)
        technical_indicators = [
            "developed",
            "built",
            "implemented",
            "designed",
            "architected",
            "engineered",
            "programmed",
        ]
        tech_count = sum(1 for word in technical_indicators if word in text.lower())

        if tech_count >= 3:
            score += 15
            feedback.append(f"✅ Shows technical expertise ({tech_count})")
        elif tech_count >= 1:
            score += 8
            feedback.append(f"⚠️ Add more technical details ({tech_count})")
        else:
            feedback.append("❌ Lacks technical depth")

        return {
            "score": min(score, max_points),
            "max_points": max_points,
            "feedback": feedback,
        }

    def _grade_ats_compatibility(self, text: str, resume_format: str) -> Dict[str, Any]:
        """Grade ATS compatibility."""

        score = 0
        max_points = 100
        feedback = []

        # Format compatibility (30 points)
        if resume_format.lower() in ["pdf", "docx", "txt"]:
            score += 30
            feedback.append(f"✅ ATS-friendly format ({resume_format.upper()})")
        else:
            feedback.append("❌ Use PDF, DOCX, or TXT for ATS")

        # Check for standard section names (25 points)
        standard_sections = ["experience", "education", "skills", "summary"]
        sections_found = sum(
            1 for section in standard_sections if section in text.lower()
        )

        if sections_found >= 3:
            score += 25
            feedback.append("✅ Standard section names used")
        elif sections_found >= 2:
            score += 15
            feedback.append("⚠️ Use standard section names")
        else:
            feedback.append("❌ Missing standard section names")

        # Check for keyword density (20 points)
        words = text.split()
        unique_words = set(word.lower() for word in words if len(word) > 3)
        keyword_density = len(unique_words) / len(words) if words else 0

        if 0.3 <= keyword_density <= 0.6:
            score += 20
            feedback.append("✅ Good keyword variety")
        else:
            score += 10
            feedback.append("⚠️ Adjust keyword density")

        # Check for contact information (25 points)
        has_email = bool(
            re.search(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
        )
        has_phone = bool(re.search(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}", text))

        if has_email and has_phone:
            score += 25
            feedback.append("✅ Complete contact information")
        elif has_email or has_phone:
            score += 15
            feedback.append("⚠️ Add missing contact info")
        else:
            feedback.append("❌ Missing contact information")

        return {
            "score": min(score, max_points),
            "max_points": max_points,
            "feedback": feedback,
        }

    def _calculate_grade(self, score: float) -> str:
        """Convert score to letter grade."""
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    def _generate_summary(self, score: float, grade: str) -> str:
        """Generate overall summary."""

        if score >= 90:
            return "Excellent! Your resume is highly competitive and ready to submit."
        elif score >= 80:
            return "Very good! Your resume is strong with minor improvements needed."
        elif score >= 70:
            return "Good foundation, but several areas need improvement."
        elif score >= 60:
            return "Needs work. Focus on the recommendations below."
        else:
            return "Significant improvements required. Consider major revisions."

    def _get_top_improvements(
        self, content: Dict, formatting: Dict, impact: Dict, ats: Dict
    ) -> List[str]:
        """Extract top 5 improvement recommendations."""

        all_feedback = (
            content["feedback"]
            + formatting["feedback"]
            + impact["feedback"]
            + ats["feedback"]
        )

        # Filter for issues (❌ and ⚠️)
        issues = [item for item in all_feedback if "❌" in item or "⚠️" in item]

        # Prioritize critical issues (❌) first
        critical = [item for item in issues if "❌" in item]
        warnings = [item for item in issues if "⚠️" in item]

        top_improvements = (critical + warnings)[:5]

        if not top_improvements:
            return ["Keep up the great work! No major improvements needed."]

        return top_improvements

    def simulate_6_second_scan(self, text: str) -> Dict[str, Any]:
        """Simulate what recruiter sees in 6-second scan."""

        # Extract key information
        lines = text.split("\n")
        first_20_lines = lines[:20]  # Roughly what fits on screen

        # What recruiters look for in 6 seconds
        checks = {
            "name_visible": False,
            "contact_visible": False,
            "current_title": False,
            "years_experience": False,
            "education": False,
            "key_skills": False,
        }

        first_screen = "\n".join(first_20_lines)

        # Name (usually at top)
        if re.search(r"^[A-Z][a-z]+ [A-Z][a-z]+", first_screen, re.MULTILINE):
            checks["name_visible"] = True

        # Contact
        if re.search(r"@", first_screen) or re.search(r"\d{3}", first_screen):
            checks["contact_visible"] = True

        # Current/recent title
        title_keywords = [
            "engineer",
            "manager",
            "developer",
            "analyst",
            "designer",
            "specialist",
            "consultant",
            "director",
        ]
        if any(keyword in first_screen.lower() for keyword in title_keywords):
            checks["current_title"] = True

        # Years of experience
        if re.search(r"\d+\s*years?", first_screen.lower()):
            checks["years_experience"] = True

        # Education
        if re.search(
            r"(education|degree|university|college|bachelor|master)",
            first_screen.lower(),
        ):
            checks["education"] = True

        # Key skills
        if re.search(r"(skills|technologies|technical)", first_screen.lower()):
            checks["key_skills"] = True

        score = sum(checks.values()) / len(checks) * 100

        return {
            "score": round(score, 1),
            "checks": checks,
            "first_screen_preview": first_screen[:500] + "...",
            "passes_scan": score >= 70,
            "feedback": self._generate_scan_feedback(checks),
        }

    def _generate_scan_feedback(self, checks: Dict[str, bool]) -> List[str]:
        """Generate feedback for 6-second scan."""

        feedback = []

        if not checks["name_visible"]:
            feedback.append("❌ Name not clearly visible at top")
        if not checks["contact_visible"]:
            feedback.append("❌ Contact info not visible in first screen")
        if not checks["current_title"]:
            feedback.append("❌ Current job title not immediately clear")
        if not checks["years_experience"]:
            feedback.append("⚠️ Years of experience not highlighted")
        if not checks["education"]:
            feedback.append("⚠️ Education not visible early")
        if not checks["key_skills"]:
            feedback.append("⚠️ Key skills section not prominent")

        if not feedback:
            feedback.append("✅ Passes the 6-second scan test!")

        return feedback
