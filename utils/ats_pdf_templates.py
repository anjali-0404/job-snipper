"""
Professional ATS-Optimized PDF Resume Templates
Creates properly formatted, ATS-friendly PDF resumes with multiple template styles.
"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    HRFlowable,
    PageBreak,
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfgen import canvas
from io import BytesIO
import re


class ATSResumeTemplates:
    """Professional ATS-optimized resume templates"""

    def __init__(self):
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()

    def _setup_custom_styles(self):
        """Setup custom paragraph styles for resume sections"""

        # Name style (top of resume)
        self.styles.add(
            ParagraphStyle(
                name="ResumeName",
                parent=self.styles["Heading1"],
                fontSize=24,
                textColor=colors.HexColor("#1a1a1a"),
                spaceAfter=6,
                alignment=TA_CENTER,
                fontName="Helvetica-Bold",
            )
        )

        # Contact info style
        self.styles.add(
            ParagraphStyle(
                name="ContactInfo",
                parent=self.styles["Normal"],
                fontSize=10,
                textColor=colors.HexColor("#333333"),
                alignment=TA_CENTER,
                spaceAfter=12,
            )
        )

        # Section heading style
        self.styles.add(
            ParagraphStyle(
                name="SectionHeading",
                parent=self.styles["Heading2"],
                fontSize=14,
                textColor=colors.HexColor("#2E86AB"),
                spaceAfter=8,
                spaceBefore=12,
                fontName="Helvetica-Bold",
                borderWidth=0,
                borderPadding=0,
                borderColor=colors.HexColor("#2E86AB"),
                borderRadius=0,
            )
        )

        # Job title / position style
        self.styles.add(
            ParagraphStyle(
                name="JobTitle",
                parent=self.styles["Normal"],
                fontSize=11,
                textColor=colors.HexColor("#1a1a1a"),
                fontName="Helvetica-Bold",
                spaceAfter=2,
            )
        )

        # Company / organization style
        self.styles.add(
            ParagraphStyle(
                name="Company",
                parent=self.styles["Normal"],
                fontSize=10,
                textColor=colors.HexColor("#4F5D75"),
                fontName="Helvetica-Oblique",
                spaceAfter=4,
            )
        )

        # Body text style
        self.styles.add(
            ParagraphStyle(
                name="ResumeBody",
                parent=self.styles["Normal"],
                fontSize=10,
                textColor=colors.HexColor("#333333"),
                spaceAfter=6,
                leading=14,
                alignment=TA_JUSTIFY,
            )
        )

        # Bullet point style
        self.styles.add(
            ParagraphStyle(
                name="BulletPoint",
                parent=self.styles["Normal"],
                fontSize=10,
                textColor=colors.HexColor("#333333"),
                leftIndent=20,
                bulletIndent=10,
                spaceAfter=4,
                leading=14,
            )
        )

    def parse_resume_content(self, text, name="", contact_info=None):
        """
        Parse resume text into structured sections
        Returns: dict with sections
        """
        sections = {
            "name": name,
            "contact": contact_info or {},
            "summary": "",
            "experience": [],
            "education": [],
            "skills": [],
            "other_sections": [],
        }

        # Split into lines
        lines = text.split("\n")

        current_section = None
        current_content = []

        # Common section headers
        section_keywords = {
            "summary": [
                "summary",
                "professional summary",
                "profile",
                "objective",
                "about",
            ],
            "experience": [
                "experience",
                "work experience",
                "employment",
                "professional experience",
                "work history",
            ],
            "education": ["education", "academic", "qualifications"],
            "skills": [
                "skills",
                "technical skills",
                "core competencies",
                "expertise",
            ],
        }

        for line in lines:
            line_stripped = line.strip()

            if not line_stripped:
                continue

            # Check if this is a section header
            is_section = False
            line_lower = line_stripped.lower()

            for section_type, keywords in section_keywords.items():
                if any(keyword in line_lower for keyword in keywords):
                    # Save previous section
                    if current_section and current_content:
                        if current_section == "summary":
                            sections["summary"] = "\n".join(current_content)
                        elif current_section in ["experience", "education"]:
                            sections[current_section].append("\n".join(current_content))
                        elif current_section == "skills":
                            sections["skills"].extend(current_content)

                    current_section = section_type
                    current_content = []
                    is_section = True
                    break

            if not is_section and current_section:
                current_content.append(line_stripped)

        # Save final section
        if current_section and current_content:
            if current_section == "summary":
                sections["summary"] = "\n".join(current_content)
            elif current_section in ["experience", "education"]:
                sections[current_section].append("\n".join(current_content))
            elif current_section == "skills":
                sections["skills"].extend(current_content)

        return sections

    def create_modern_template(
        self, text, name="Professional", contact_info=None, filename=None
    ):
        """
        Create a modern ATS-optimized resume PDF
        Clean, professional design with good whitespace
        """
        buffer = BytesIO()
        doc = SimpleDocTemplate(
            buffer,
            pagesize=letter,
            rightMargin=0.75 * inch,
            leftMargin=0.75 * inch,
            topMargin=0.75 * inch,
            bottomMargin=0.75 * inch,
        )

        story = []

        # Parse content
        sections = self.parse_resume_content(text, name, contact_info)

        # Header - Name
        if sections["name"]:
            story.append(Paragraph(sections["name"], self.styles["ResumeName"]))

        # Contact Information
        contact_parts = []
        if sections["contact"].get("email"):
            contact_parts.append(sections["contact"]["email"])
        if sections["contact"].get("phone"):
            contact_parts.append(sections["contact"]["phone"])
        if sections["contact"].get("location"):
            contact_parts.append(sections["contact"]["location"])

        if contact_parts:
            contact_text = " | ".join(contact_parts)
            story.append(Paragraph(contact_text, self.styles["ContactInfo"]))

        story.append(Spacer(1, 0.1 * inch))

        # Professional Summary
        if sections["summary"]:
            story.append(
                Paragraph("PROFESSIONAL SUMMARY", self.styles["SectionHeading"])
            )
            story.append(
                HRFlowable(
                    width="100%",
                    thickness=1,
                    color=colors.HexColor("#2E86AB"),
                    spaceAfter=8,
                )
            )
            story.append(Paragraph(sections["summary"], self.styles["ResumeBody"]))
            story.append(Spacer(1, 0.15 * inch))

        # Experience
        if sections["experience"]:
            story.append(Paragraph("EXPERIENCE", self.styles["SectionHeading"]))
            story.append(
                HRFlowable(
                    width="100%",
                    thickness=1,
                    color=colors.HexColor("#2E86AB"),
                    spaceAfter=8,
                )
            )

            for exp in sections["experience"]:
                # Parse experience entry
                lines = exp.split("\n")
                if lines:
                    # First line is usually job title
                    story.append(Paragraph(lines[0], self.styles["JobTitle"]))

                    # Rest of the content
                    for line in lines[1:]:
                        if line.startswith("•") or line.startswith("-"):
                            story.append(
                                Paragraph(
                                    f"• {line[1:].strip()}", self.styles["BulletPoint"]
                                )
                            )
                        else:
                            story.append(Paragraph(line, self.styles["ResumeBody"]))

                    story.append(Spacer(1, 0.1 * inch))

        # Education
        if sections["education"]:
            story.append(Paragraph("EDUCATION", self.styles["SectionHeading"]))
            story.append(
                HRFlowable(
                    width="100%",
                    thickness=1,
                    color=colors.HexColor("#2E86AB"),
                    spaceAfter=8,
                )
            )

            for edu in sections["education"]:
                lines = edu.split("\n")
                for line in lines:
                    if line.strip():
                        story.append(Paragraph(line, self.styles["ResumeBody"]))
                story.append(Spacer(1, 0.1 * inch))

        # Skills
        if sections["skills"]:
            story.append(Paragraph("SKILLS", self.styles["SectionHeading"]))
            story.append(
                HRFlowable(
                    width="100%",
                    thickness=1,
                    color=colors.HexColor("#2E86AB"),
                    spaceAfter=8,
                )
            )

            # Join skills with bullets
            skills_text = " • ".join(
                [s.strip() for s in sections["skills"] if s.strip()]
            )
            story.append(Paragraph(skills_text, self.styles["ResumeBody"]))

        # Build PDF
        doc.build(story)
        buffer.seek(0)
        return buffer

    def create_classic_template(
        self, text, name="Professional", contact_info=None, filename=None
    ):
        """
        Create a classic ATS-optimized resume PDF
        Traditional, conservative design
        """
        buffer = BytesIO()
        doc = SimpleDocTemplate(
            buffer,
            pagesize=letter,
            rightMargin=1 * inch,
            leftMargin=1 * inch,
            topMargin=1 * inch,
            bottomMargin=1 * inch,
        )

        story = []
        sections = self.parse_resume_content(text, name, contact_info)

        # Header - Name (classic centered style)
        if sections["name"]:
            name_style = ParagraphStyle(
                "ClassicName",
                parent=self.styles["ResumeName"],
                fontSize=18,
                fontName="Times-Bold",
                spaceAfter=4,
            )
            story.append(Paragraph(sections["name"].upper(), name_style))

        # Contact (classic style)
        contact_parts = []
        if sections["contact"].get("email"):
            contact_parts.append(sections["contact"]["email"])
        if sections["contact"].get("phone"):
            contact_parts.append(sections["contact"]["phone"])
        if sections["contact"].get("location"):
            contact_parts.append(sections["contact"]["location"])

        if contact_parts:
            contact_style = ParagraphStyle(
                "ClassicContact",
                parent=self.styles["ContactInfo"],
                fontSize=10,
                fontName="Times-Roman",
            )
            story.append(Paragraph(" | ".join(contact_parts), contact_style))

        story.append(Spacer(1, 0.2 * inch))

        # Classic section style
        classic_section_style = ParagraphStyle(
            "ClassicSection",
            parent=self.styles["SectionHeading"],
            fontSize=12,
            fontName="Times-Bold",
            textColor=colors.black,
            spaceAfter=6,
            spaceBefore=10,
        )

        # Add sections with classic formatting
        if sections["summary"]:
            story.append(Paragraph("OBJECTIVE", classic_section_style))
            story.append(
                HRFlowable(width="100%", thickness=2, color=colors.black, spaceAfter=6)
            )
            story.append(Paragraph(sections["summary"], self.styles["ResumeBody"]))
            story.append(Spacer(1, 0.15 * inch))

        if sections["experience"]:
            story.append(Paragraph("PROFESSIONAL EXPERIENCE", classic_section_style))
            story.append(
                HRFlowable(width="100%", thickness=2, color=colors.black, spaceAfter=6)
            )
            for exp in sections["experience"]:
                lines = exp.split("\n")
                for line in lines:
                    if line.strip():
                        if line.startswith("•") or line.startswith("-"):
                            story.append(
                                Paragraph(
                                    f"• {line[1:].strip()}", self.styles["BulletPoint"]
                                )
                            )
                        else:
                            story.append(Paragraph(line, self.styles["ResumeBody"]))
                story.append(Spacer(1, 0.1 * inch))

        if sections["education"]:
            story.append(Paragraph("EDUCATION", classic_section_style))
            story.append(
                HRFlowable(width="100%", thickness=2, color=colors.black, spaceAfter=6)
            )
            for edu in sections["education"]:
                story.append(Paragraph(edu, self.styles["ResumeBody"]))
                story.append(Spacer(1, 0.1 * inch))

        if sections["skills"]:
            story.append(Paragraph("SKILLS & COMPETENCIES", classic_section_style))
            story.append(
                HRFlowable(width="100%", thickness=2, color=colors.black, spaceAfter=6)
            )
            skills_text = ", ".join(
                [s.strip() for s in sections["skills"] if s.strip()]
            )
            story.append(Paragraph(skills_text, self.styles["ResumeBody"]))

        doc.build(story)
        buffer.seek(0)
        return buffer

    def create_executive_template(
        self, text, name="Professional", contact_info=None, filename=None
    ):
        """
        Create an executive ATS-optimized resume PDF
        Sophisticated design for senior positions
        """
        buffer = BytesIO()
        doc = SimpleDocTemplate(
            buffer,
            pagesize=letter,
            rightMargin=0.75 * inch,
            leftMargin=0.75 * inch,
            topMargin=0.6 * inch,
            bottomMargin=0.75 * inch,
        )

        story = []
        sections = self.parse_resume_content(text, name, contact_info)

        # Executive Name Style
        exec_name_style = ParagraphStyle(
            "ExecName",
            parent=self.styles["ResumeName"],
            fontSize=22,
            fontName="Helvetica-Bold",
            textColor=colors.HexColor("#1a1a1a"),
            alignment=TA_LEFT,
            spaceAfter=4,
        )

        if sections["name"]:
            story.append(Paragraph(sections["name"], exec_name_style))

        # Executive contact style
        exec_contact_style = ParagraphStyle(
            "ExecContact",
            fontSize=9,
            textColor=colors.HexColor("#666666"),
            alignment=TA_LEFT,
            spaceAfter=8,
        )

        contact_parts = []
        if sections["contact"].get("email"):
            contact_parts.append(sections["contact"]["email"])
        if sections["contact"].get("phone"):
            contact_parts.append(sections["contact"]["phone"])
        if sections["contact"].get("location"):
            contact_parts.append(sections["contact"]["location"])

        if contact_parts:
            story.append(Paragraph(" • ".join(contact_parts), exec_contact_style))

        story.append(
            HRFlowable(
                width="100%",
                thickness=2,
                color=colors.HexColor("#2E86AB"),
                spaceAfter=12,
            )
        )

        # Executive section style
        exec_section_style = ParagraphStyle(
            "ExecSection",
            fontSize=13,
            fontName="Helvetica-Bold",
            textColor=colors.HexColor("#2E86AB"),
            spaceAfter=8,
            spaceBefore=14,
            leftIndent=0,
        )

        # Add sections
        if sections["summary"]:
            story.append(Paragraph("EXECUTIVE PROFILE", exec_section_style))
            story.append(Paragraph(sections["summary"], self.styles["ResumeBody"]))
            story.append(Spacer(1, 0.12 * inch))

        if sections["experience"]:
            story.append(Paragraph("PROFESSIONAL EXPERIENCE", exec_section_style))
            for exp in sections["experience"]:
                lines = exp.split("\n")
                for line in lines:
                    if line.strip():
                        if line.startswith("•") or line.startswith("-"):
                            story.append(
                                Paragraph(
                                    f"• {line[1:].strip()}", self.styles["BulletPoint"]
                                )
                            )
                        else:
                            story.append(Paragraph(line, self.styles["ResumeBody"]))
                story.append(Spacer(1, 0.08 * inch))

        if sections["education"]:
            story.append(Paragraph("EDUCATION & CREDENTIALS", exec_section_style))
            for edu in sections["education"]:
                story.append(Paragraph(edu, self.styles["ResumeBody"]))
                story.append(Spacer(1, 0.06 * inch))

        if sections["skills"]:
            story.append(Paragraph("CORE COMPETENCIES", exec_section_style))
            skills_text = " • ".join(
                [s.strip() for s in sections["skills"] if s.strip()]
            )
            story.append(Paragraph(skills_text, self.styles["ResumeBody"]))

        doc.build(story)
        buffer.seek(0)
        return buffer

    def create_tech_template(
        self, text, name="Professional", contact_info=None, filename=None
    ):
        """
        Create a tech-focused ATS-optimized resume PDF
        Clean, modern design for tech professionals
        """
        buffer = BytesIO()
        doc = SimpleDocTemplate(
            buffer,
            pagesize=letter,
            rightMargin=0.7 * inch,
            leftMargin=0.7 * inch,
            topMargin=0.7 * inch,
            bottomMargin=0.7 * inch,
        )

        story = []
        sections = self.parse_resume_content(text, name, contact_info)

        # Tech Name Style (left-aligned, modern)
        tech_name_style = ParagraphStyle(
            "TechName",
            fontSize=26,
            fontName="Helvetica-Bold",
            textColor=colors.HexColor("#2E86AB"),
            alignment=TA_LEFT,
            spaceAfter=6,
        )

        if sections["name"]:
            story.append(Paragraph(sections["name"], tech_name_style))

        # Contact info in modern tech style
        tech_contact_style = ParagraphStyle(
            "TechContact",
            fontSize=9,
            textColor=colors.HexColor("#4F5D75"),
            alignment=TA_LEFT,
            spaceAfter=10,
        )

        contact_parts = []
        if sections["contact"].get("email"):
            contact_parts.append(f"📧 {sections['contact']['email']}")
        if sections["contact"].get("phone"):
            contact_parts.append(f"📱 {sections['contact']['phone']}")
        if sections["contact"].get("location"):
            contact_parts.append(f"📍 {sections['contact']['location']}")

        if contact_parts:
            story.append(Paragraph(" | ".join(contact_parts), tech_contact_style))

        story.append(Spacer(1, 0.15 * inch))

        # Tech section style with color accent
        tech_section_style = ParagraphStyle(
            "TechSection",
            fontSize=14,
            fontName="Helvetica-Bold",
            textColor=colors.HexColor("#2E86AB"),
            spaceAfter=6,
            spaceBefore=12,
        )

        # Add sections with tech styling
        if sections["summary"]:
            story.append(Paragraph("// PROFESSIONAL SUMMARY", tech_section_style))
            story.append(
                HRFlowable(
                    width="100%",
                    thickness=1,
                    color=colors.HexColor("#06A77D"),
                    spaceAfter=8,
                )
            )
            story.append(Paragraph(sections["summary"], self.styles["ResumeBody"]))
            story.append(Spacer(1, 0.12 * inch))

        if sections["skills"]:
            story.append(Paragraph("// TECHNICAL SKILLS", tech_section_style))
            story.append(
                HRFlowable(
                    width="100%",
                    thickness=1,
                    color=colors.HexColor("#06A77D"),
                    spaceAfter=8,
                )
            )
            skills_text = " • ".join(
                [s.strip() for s in sections["skills"] if s.strip()]
            )
            story.append(Paragraph(skills_text, self.styles["ResumeBody"]))
            story.append(Spacer(1, 0.12 * inch))

        if sections["experience"]:
            story.append(Paragraph("// EXPERIENCE", tech_section_style))
            story.append(
                HRFlowable(
                    width="100%",
                    thickness=1,
                    color=colors.HexColor("#06A77D"),
                    spaceAfter=8,
                )
            )
            for exp in sections["experience"]:
                lines = exp.split("\n")
                for line in lines:
                    if line.strip():
                        if line.startswith("•") or line.startswith("-"):
                            story.append(
                                Paragraph(
                                    f"▹ {line[1:].strip()}", self.styles["BulletPoint"]
                                )
                            )
                        else:
                            story.append(Paragraph(line, self.styles["ResumeBody"]))
                story.append(Spacer(1, 0.08 * inch))

        if sections["education"]:
            story.append(Paragraph("// EDUCATION", tech_section_style))
            story.append(
                HRFlowable(
                    width="100%",
                    thickness=1,
                    color=colors.HexColor("#06A77D"),
                    spaceAfter=8,
                )
            )
            for edu in sections["education"]:
                story.append(Paragraph(edu, self.styles["ResumeBody"]))
                story.append(Spacer(1, 0.06 * inch))

        doc.build(story)
        buffer.seek(0)
        return buffer


def export_ats_resume(
    text, name="Professional", contact_info=None, template="modern", filename=None
):
    """
    Export resume to ATS-optimized PDF with specified template

    Args:
        text: Resume text content
        name: Person's name
        contact_info: Dict with email, phone, location
        template: Template name ('modern', 'classic', 'executive', 'tech')
        filename: Optional filename for the PDF

    Returns:
        BytesIO buffer with PDF content
    """
    templates = ATSResumeTemplates()

    template_map = {
        "modern": templates.create_modern_template,
        "classic": templates.create_classic_template,
        "executive": templates.create_executive_template,
        "tech": templates.create_tech_template,
    }

    template_func = template_map.get(template.lower(), templates.create_modern_template)

    return template_func(text, name, contact_info, filename)
