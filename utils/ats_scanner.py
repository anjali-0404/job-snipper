"""
ATS Scanner Simulator
Simulates how Applicant Tracking Systems parse and read resumes.
"""

import re
from typing import Dict, List, Any


class ATSScanner:
    """Simulate ATS resume parsing and identify potential issues."""

    def __init__(self):
        self.ats_friendly_sections = [
            "experience",
            "work experience",
            "professional experience",
            "education",
            "skills",
            "technical skills",
            "summary",
            "objective",
            "certifications",
            "projects",
            "achievements",
        ]

        self.ats_unfriendly_elements = [
            "tables",
            "columns",
            "text boxes",
            "headers",
            "footers",
            "images",
            "graphics",
            "charts",
            "special characters",
            "unusual fonts",
            "colored text",
            "background colors",
        ]

    def scan_resume(self, resume_text: str, file_format: str = "txt") -> Dict[str, Any]:
        """
        Perform comprehensive ATS scan on resume.

        Args:
            resume_text: Resume content
            file_format: File format (txt, pdf, docx)

        Returns:
            Dictionary with scan results
        """
        results = {
            "overall_score": 0,
            "format_score": 0,
            "content_score": 0,
            "keyword_score": 0,
            "issues": [],
            "warnings": [],
            "passed_checks": [],
            "parsing_preview": "",
            "recommendations": [],
        }

        # Run all checks
        format_check = self._check_format(resume_text, file_format)
        section_check = self._check_sections(resume_text)
        keyword_check = self._check_keywords(resume_text)
        contact_check = self._check_contact_info(resume_text)
        formatting_check = self._check_formatting_issues(resume_text)

        # Compile results
        results["issues"].extend(format_check["issues"])
        results["warnings"].extend(format_check["warnings"])
        results["passed_checks"].extend(format_check["passed"])

        results["issues"].extend(section_check["issues"])
        results["warnings"].extend(section_check["warnings"])
        results["passed_checks"].extend(section_check["passed"])

        results["issues"].extend(keyword_check["issues"])
        results["warnings"].extend(keyword_check["warnings"])
        results["passed_checks"].extend(keyword_check["passed"])

        results["issues"].extend(contact_check["issues"])
        results["warnings"].extend(contact_check["warnings"])
        results["passed_checks"].extend(contact_check["passed"])

        results["issues"].extend(formatting_check["issues"])
        results["warnings"].extend(formatting_check["warnings"])
        results["passed_checks"].extend(formatting_check["passed"])

        # Calculate scores
        total_checks = (
            len(results["issues"])
            + len(results["warnings"])
            + len(results["passed_checks"])
        )
        if total_checks > 0:
            passed_weight = len(results["passed_checks"])
            warning_weight = len(results["warnings"]) * 0.5
            results["overall_score"] = round(
                (passed_weight + warning_weight) / total_checks * 100, 1
            )

        results["format_score"] = self._calculate_subscore(format_check)
        results["content_score"] = self._calculate_subscore(section_check)
        results["keyword_score"] = self._calculate_subscore(keyword_check)

        # Generate parsing preview
        results["parsing_preview"] = self._generate_parsing_preview(resume_text)

        # Generate recommendations
        results["recommendations"] = self._generate_recommendations(results)

        return results

    def _check_format(self, resume_text: str, file_format: str) -> Dict[str, List[str]]:
        """Check file format compatibility."""
        issues = []
        warnings = []
        passed = []

        # File format check
        if file_format.lower() in ["txt", "docx", "pdf"]:
            passed.append(f"✅ {file_format.upper()} format is ATS-compatible")
        else:
            issues.append(
                f"❌ {file_format.upper()} format may not be ATS-compatible. Use TXT, DOCX, or PDF"
            )

        # Length check
        word_count = len(resume_text.split())
        if 300 <= word_count <= 1000:
            passed.append(f"✅ Resume length optimal ({word_count} words)")
        elif word_count < 300:
            warnings.append(
                f"⚠️ Resume is short ({word_count} words). Consider adding more detail"
            )
        else:
            warnings.append(
                f"⚠️ Resume is long ({word_count} words). Consider being more concise"
            )

        # Plain text check
        special_chars = re.findall(r"[^\w\s\n\-.,;:()@#$%&*+=/]", resume_text)
        if len(special_chars) < 10:
            passed.append("✅ Minimal special characters detected")
        else:
            warnings.append(
                f"⚠️ {len(special_chars)} special characters detected - may cause parsing issues"
            )

        return {"issues": issues, "warnings": warnings, "passed": passed}

    def _check_sections(self, resume_text: str) -> Dict[str, List[str]]:
        """Check for standard resume sections."""
        issues = []
        warnings = []
        passed = []

        text_lower = resume_text.lower()

        # Required sections
        required = {
            "Experience": [
                "experience",
                "work history",
                "employment",
                "professional experience",
            ],
            "Education": ["education", "academic", "degree"],
            "Skills": ["skills", "technical skills", "competencies", "expertise"],
        }

        for section_name, keywords in required.items():
            if any(kw in text_lower for kw in keywords):
                passed.append(f"✅ {section_name} section found")
            else:
                issues.append(f"❌ Missing {section_name} section - critical for ATS")

        # Optional but recommended
        optional = {
            "Summary/Objective": ["summary", "objective", "profile", "about"],
            "Contact Info": ["email", "phone", "@", "linkedin"],
        }

        for section_name, keywords in optional.items():
            if any(kw in text_lower for kw in keywords):
                passed.append(f"✅ {section_name} detected")
            else:
                warnings.append(f"⚠️ {section_name} not clearly identified")

        # Check for clear section headers
        section_headers = re.findall(
            r"^([A-Z][A-Z\s]{3,})\s*$", resume_text, re.MULTILINE
        )
        if len(section_headers) >= 3:
            passed.append(f"✅ Clear section headers found ({len(section_headers)})")
        else:
            warnings.append("⚠️ Section headers could be clearer - use ALL CAPS or bold")

        return {"issues": issues, "warnings": warnings, "passed": passed}

    def _check_keywords(self, resume_text: str) -> Dict[str, List[str]]:
        """Check for important keywords."""
        issues = []
        warnings = []
        passed = []

        text_lower = resume_text.lower()

        # Action verbs
        action_verbs = [
            "achieved",
            "managed",
            "led",
            "developed",
            "created",
            "implemented",
            "improved",
            "increased",
            "reduced",
            "designed",
            "built",
            "launched",
        ]
        found_verbs = sum(1 for verb in action_verbs if verb in text_lower)

        if found_verbs >= 5:
            passed.append(f"✅ Strong action verbs present ({found_verbs} found)")
        elif found_verbs >= 2:
            warnings.append(
                f"⚠️ Limited action verbs ({found_verbs} found). Add more impactful verbs"
            )
        else:
            issues.append(
                "❌ Very few action verbs - ATS looks for achievement-oriented language"
            )

        # Quantifiable metrics
        metrics = re.findall(
            r"\d+[%\+\-]|\d+\s*(?:years?|months?)|[\$€£]\d+|\d+\s*(?:people|team|users|customers|projects)",
            text_lower,
        )

        if len(metrics) >= 3:
            passed.append(
                f"✅ Quantifiable achievements present ({len(metrics)} found)"
            )
        elif len(metrics) >= 1:
            warnings.append(
                f"⚠️ Limited metrics ({len(metrics)} found). Add more numbers and percentages"
            )
        else:
            issues.append(
                "❌ No quantifiable metrics - add numbers to demonstrate impact"
            )

        # Technical terms (varies by industry)
        word_count = len(resume_text.split())
        unique_words = len(set(text_lower.split()))
        keyword_density = (unique_words / word_count * 100) if word_count > 0 else 0

        if keyword_density >= 40:
            passed.append(f"✅ Good keyword variety ({keyword_density:.0f}%)")
        else:
            warnings.append(
                f"⚠️ Limited keyword variety ({keyword_density:.0f}%). Add more industry terms"
            )

        return {"issues": issues, "warnings": warnings, "passed": passed}

    def _check_contact_info(self, resume_text: str) -> Dict[str, List[str]]:
        """Check for contact information."""
        issues = []
        warnings = []
        passed = []

        # Email
        emails = re.findall(
            r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", resume_text
        )
        if emails:
            passed.append(f"✅ Email address found: {emails[0]}")
        else:
            issues.append("❌ No email address detected - critical for contact")

        # Phone
        phones = re.findall(
            r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b|\(\d{3}\)\s*\d{3}[-.\s]?\d{4}",
            resume_text,
        )
        if phones:
            passed.append("✅ Phone number found")
        else:
            warnings.append("⚠️ No phone number detected")

        # LinkedIn
        if "linkedin" in resume_text.lower() or "linkedin.com" in resume_text.lower():
            passed.append("✅ LinkedIn profile included")
        else:
            warnings.append("⚠️ LinkedIn profile not found - recommended for networking")

        # Location
        location_keywords = ["location", "address", "city", "state", "country"]
        if any(kw in resume_text.lower() for kw in location_keywords) or re.search(
            r"\b[A-Z][a-z]+,\s*[A-Z]{2}\b", resume_text
        ):
            passed.append("✅ Location information found")
        else:
            warnings.append("⚠️ Location not clearly specified")

        return {"issues": issues, "warnings": warnings, "passed": passed}

    def _check_formatting_issues(self, resume_text: str) -> Dict[str, List[str]]:
        """Check for common formatting issues."""
        issues = []
        warnings = []
        passed = []

        # Line length check (very long lines suggest tables/columns)
        lines = resume_text.split("\n")
        long_lines = [line for line in lines if len(line) > 100]

        if len(long_lines) < len(lines) * 0.1:
            passed.append("✅ Line lengths are ATS-friendly")
        else:
            warnings.append(
                "⚠️ Some lines are very long - may indicate complex formatting"
            )

        # Multiple spaces (often from table formatting)
        multi_spaces = re.findall(r"  +", resume_text)
        if len(multi_spaces) < 10:
            passed.append("✅ Minimal spacing issues")
        else:
            warnings.append(
                f"⚠️ Multiple spaces detected ({len(multi_spaces)}) - check for table conversion issues"
            )

        # Bullet point consistency
        bullet_types = []
        if "•" in resume_text:
            bullet_types.append("•")
        if "◦" in resume_text:
            bullet_types.append("◦")
        if "▪" in resume_text:
            bullet_types.append("▪")
        if re.search(r"^\s*[-*]\s", resume_text, re.MULTILINE):
            bullet_types.append("-")

        if len(bullet_types) == 1:
            passed.append(f"✅ Consistent bullet style ({bullet_types[0]})")
        elif len(bullet_types) > 1:
            warnings.append(
                "⚠️ Mixed bullet styles detected - use consistent formatting"
            )
        else:
            warnings.append(
                "⚠️ No bullet points detected - consider using them for readability"
            )

        # All caps sections (good for ATS)
        caps_headers = re.findall(r"^([A-Z][A-Z\s]{3,})$", resume_text, re.MULTILINE)
        if caps_headers:
            passed.append(f"✅ Clear section headers ({len(caps_headers)} found)")
        else:
            warnings.append(
                "⚠️ Use ALL CAPS for section headers to help ATS identify sections"
            )

        return {"issues": issues, "warnings": warnings, "passed": passed}

    def _calculate_subscore(self, check_result: Dict[str, List[str]]) -> float:
        """Calculate sub-score for a specific check."""
        total = (
            len(check_result["issues"])
            + len(check_result["warnings"])
            + len(check_result["passed"])
        )
        if total == 0:
            return 100.0
        passed = len(check_result["passed"]) + (len(check_result["warnings"]) * 0.5)
        return round(passed / total * 100, 1)

    def _generate_parsing_preview(self, resume_text: str) -> str:
        """Generate what ATS sees when parsing resume."""
        # Simulate text extraction (strip extra formatting)
        parsed = resume_text

        # Remove multiple spaces
        parsed = re.sub(r"  +", " ", parsed)

        # Remove multiple newlines
        parsed = re.sub(r"\n\n+", "\n\n", parsed)

        # Truncate for preview
        lines = parsed.split("\n")
        preview_lines = lines[:30]  # First 30 lines

        preview = "\n".join(preview_lines)
        if len(lines) > 30:
            preview += f"\n\n... ({len(lines) - 30} more lines)"

        return preview

    def _generate_recommendations(self, results: Dict[str, Any]) -> List[str]:
        """Generate actionable recommendations based on scan results."""
        recommendations = []

        score = results["overall_score"]

        if score >= 90:
            recommendations.append("🎯 Excellent! Your resume is highly ATS-compatible")
        elif score >= 75:
            recommendations.append(
                "👍 Good ATS compatibility with minor improvements needed"
            )
        elif score >= 60:
            recommendations.append(
                "⚠️ Moderate issues - address warnings to improve ATS success"
            )
        else:
            recommendations.append(
                "❌ Significant issues detected - follow recommendations below"
            )

        # Priority fixes based on issues
        if results["issues"]:
            recommendations.append(
                f"\n🔴 CRITICAL: Fix {len(results['issues'])} issues:"
            )
            for issue in results["issues"][:5]:
                recommendations.append(f"  {issue}")

        if results["warnings"]:
            recommendations.append(
                f"\n🟡 IMPROVE: Address {len(results['warnings'])} warnings:"
            )
            for warning in results["warnings"][:5]:
                recommendations.append(f"  {warning}")

        # General recommendations
        recommendations.append("\n💡 ATS Best Practices:")
        recommendations.append(
            "  • Use standard section headers (EXPERIENCE, EDUCATION, SKILLS)"
        )
        recommendations.append("  • Include relevant keywords from job description")
        recommendations.append(
            "  • Use simple formatting (no tables, columns, or text boxes)"
        )
        recommendations.append("  • Save as .docx or .pdf for best compatibility")
        recommendations.append(
            "  • Use standard fonts (Arial, Calibri, Times New Roman)"
        )

        return recommendations

    def compare_formats(
        self, txt_version: str, pdf_version: str = None, docx_version: str = None
    ) -> Dict[str, Any]:
        """
        Compare how different formats parse in ATS.

        Args:
            txt_version: Plain text version
            pdf_version: PDF extracted text (optional)
            docx_version: DOCX extracted text (optional)

        Returns:
            Comparison results
        """
        results = {
            "txt_score": 0,
            "pdf_score": 0,
            "docx_score": 0,
            "best_format": "",
            "comparison": [],
        }

        # Scan TXT
        txt_scan = self.scan_resume(txt_version, "txt")
        results["txt_score"] = txt_scan["overall_score"]

        # Scan PDF if provided
        if pdf_version:
            pdf_scan = self.scan_resume(pdf_version, "pdf")
            results["pdf_score"] = pdf_scan["overall_score"]

            # Compare parsing
            if txt_version.strip() != pdf_version.strip():
                results["comparison"].append("⚠️ PDF version differs from original text")

        # Scan DOCX if provided
        if docx_version:
            docx_scan = self.scan_resume(docx_version, "docx")
            results["docx_score"] = docx_scan["overall_score"]

            if txt_version.strip() != docx_version.strip():
                results["comparison"].append(
                    "⚠️ DOCX version differs from original text"
                )

        # Determine best format
        scores = {
            "TXT": results["txt_score"],
            "PDF": results["pdf_score"],
            "DOCX": results["docx_score"],
        }
        results["best_format"] = max(scores, key=scores.get)

        return results

    def simulate_ats_systems(self, resume_text: str) -> Dict[str, Any]:
        """
        Simulate popular ATS systems (Workday, Taleo, Greenhouse, etc.)

        Args:
            resume_text: Resume content

        Returns:
            Results for different ATS systems
        """
        ats_systems = {
            "Workday": {"strictness": "high", "focus": "keywords"},
            "Taleo (Oracle)": {"strictness": "high", "focus": "formatting"},
            "Greenhouse": {"strictness": "medium", "focus": "structure"},
            "Lever": {"strictness": "medium", "focus": "content"},
            "iCIMS": {"strictness": "high", "focus": "sections"},
        }

        results = {}

        for ats_name, ats_config in ats_systems.items():
            scan = self.scan_resume(resume_text)

            # Adjust score based on ATS characteristics
            adjusted_score = scan["overall_score"]

            if ats_config["strictness"] == "high":
                # Stricter systems penalize more
                penalty = len(scan["issues"]) * 5 + len(scan["warnings"]) * 2
                adjusted_score = max(0, adjusted_score - penalty)

            results[ats_name] = {
                "score": round(adjusted_score, 1),
                "status": "Pass"
                if adjusted_score >= 70
                else "Review"
                if adjusted_score >= 50
                else "Reject",
                "focus_area": ats_config["focus"],
                "notes": f"Focuses on {ats_config['focus']} with {ats_config['strictness']} strictness",
            }

        return results
