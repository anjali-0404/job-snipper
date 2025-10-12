"""
Skills Gap Analyzer
Analyze skill gaps and suggest learning paths.
"""

from typing import Dict, List, Any


class SkillsAnalyzer:
    """Analyze skills and identify gaps."""

    def __init__(self):
        self.skill_categories = {
            "Programming Languages": [
                "python",
                "java",
                "javascript",
                "typescript",
                "c++",
                "c#",
                "go",
                "rust",
                "ruby",
                "php",
                "swift",
                "kotlin",
                "scala",
                "r",
            ],
            "Web Technologies": [
                "html",
                "css",
                "react",
                "angular",
                "vue",
                "node",
                "express",
                "django",
                "flask",
                "fastapi",
                "spring",
                "asp.net",
                "next.js",
            ],
            "Databases": [
                "sql",
                "mysql",
                "postgresql",
                "mongodb",
                "redis",
                "elasticsearch",
                "oracle",
                "sql server",
                "dynamodb",
                "cassandra",
            ],
            "Cloud & DevOps": [
                "aws",
                "azure",
                "gcp",
                "docker",
                "kubernetes",
                "jenkins",
                "ci/cd",
                "terraform",
                "ansible",
                "git",
                "github",
                "gitlab",
            ],
            "Data & Analytics": [
                "machine learning",
                "data analysis",
                "pandas",
                "numpy",
                "tensorflow",
                "pytorch",
                "scikit-learn",
                "tableau",
                "power bi",
                "spark",
                "hadoop",
            ],
            "Soft Skills": [
                "leadership",
                "communication",
                "teamwork",
                "problem solving",
                "critical thinking",
                "agile",
                "scrum",
                "project management",
            ],
        }

        # Certification recommendations
        self.certifications = {
            "aws": {
                "name": "AWS Certified Solutions Architect",
                "provider": "Amazon Web Services",
                "level": "Associate",
                "avg_salary_boost": "15%",
                "url": "https://aws.amazon.com/certification/",
            },
            "azure": {
                "name": "Microsoft Azure Fundamentals",
                "provider": "Microsoft",
                "level": "Fundamental",
                "avg_salary_boost": "12%",
                "url": "https://learn.microsoft.com/certifications/",
            },
            "python": {
                "name": "Python Institute Certification",
                "provider": "Python Institute",
                "level": "Associate",
                "avg_salary_boost": "10%",
                "url": "https://pythoninstitute.org/certification",
            },
            "scrum": {
                "name": "Certified Scrum Master (CSM)",
                "provider": "Scrum Alliance",
                "level": "Professional",
                "avg_salary_boost": "8%",
                "url": "https://www.scrumalliance.org/",
            },
            "pmp": {
                "name": "Project Management Professional",
                "provider": "PMI",
                "level": "Professional",
                "avg_salary_boost": "20%",
                "url": "https://www.pmi.org/certifications/project-management-pmp",
            },
        }

    def extract_skills(self, resume_text: str) -> Dict[str, List[str]]:
        """
        Extract skills from resume by category.

        Args:
            resume_text: Resume content

        Returns:
            Dictionary of skills by category
        """
        text_lower = resume_text.lower()
        found_skills = {}

        for category, skills in self.skill_categories.items():
            found_in_category = []
            for skill in skills:
                if skill in text_lower:
                    found_in_category.append(skill)
            found_skills[category] = found_in_category

        return found_skills

    def analyze_skill_gaps(
        self, resume_text: str, job_description: str
    ) -> Dict[str, Any]:
        """
        Analyze skill gaps between resume and job requirements.

        Args:
            resume_text: Resume content
            job_description: Target job description

        Returns:
            Gap analysis results
        """
        resume_skills = self.extract_skills(resume_text)
        job_skills = self.extract_skills(job_description)

        gaps = {}

        for category in self.skill_categories.keys():
            resume_set = set(resume_skills.get(category, []))
            job_set = set(job_skills.get(category, []))

            missing = job_set - resume_set
            matching = job_set & resume_set

            if missing or matching:
                gaps[category] = {
                    "required": list(job_set),
                    "have": list(resume_set),
                    "missing": list(missing),
                    "matching": list(matching),
                    "match_percentage": round(len(matching) / len(job_set) * 100, 1)
                    if job_set
                    else 100,
                }

        # Calculate overall match
        total_required = sum(len(cat.get("required", [])) for cat in gaps.values())
        total_matching = sum(len(cat.get("matching", [])) for cat in gaps.values())
        overall_match = (
            round(total_matching / total_required * 100, 1)
            if total_required > 0
            else 100
        )

        return {
            "overall_match": overall_match,
            "gaps_by_category": gaps,
            "priority_gaps": self._prioritize_gaps(gaps),
            "recommendations": self._generate_gap_recommendations(gaps),
        }

    def _prioritize_gaps(self, gaps: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Prioritize skill gaps by importance."""
        priority_list = []

        # Priority order
        priority_order = {
            "Programming Languages": 1,
            "Web Technologies": 2,
            "Cloud & DevOps": 3,
            "Databases": 4,
            "Data & Analytics": 5,
            "Soft Skills": 6,
        }

        for category, gap_info in gaps.items():
            if gap_info["missing"]:
                priority_list.append(
                    {
                        "category": category,
                        "missing_skills": gap_info["missing"],
                        "priority": priority_order.get(category, 7),
                        "match_percentage": gap_info["match_percentage"],
                    }
                )

        # Sort by priority and match percentage
        priority_list.sort(key=lambda x: (x["priority"], -x["match_percentage"]))

        return priority_list

    def _generate_gap_recommendations(self, gaps: Dict[str, Any]) -> List[str]:
        """Generate actionable recommendations."""
        recommendations = []

        for category, gap_info in gaps.items():
            if gap_info["missing"]:
                missing_count = len(gap_info["missing"])
                missing_skills = ", ".join(gap_info["missing"][:3])

                if missing_count > 0:
                    recommendations.append(
                        f"📚 {category}: Learn {missing_skills}"
                        f"{' and ' + str(missing_count - 3) + ' more' if missing_count > 3 else ''}"
                    )

        return recommendations[:10]

    def suggest_learning_paths(
        self, missing_skills: List[str], current_level: str = "intermediate"
    ) -> List[Dict[str, Any]]:
        """
        Suggest learning paths for missing skills.

        Args:
            missing_skills: List of skills to learn
            current_level: Current skill level (beginner, intermediate, advanced)

        Returns:
            List of learning resources
        """
        learning_paths = []

        # Resource templates
        resources = {
            "python": {
                "beginner": [
                    {
                        "name": "Python for Everybody (Coursera)",
                        "duration": "8 months",
                        "type": "Course",
                    },
                    {
                        "name": "Automate the Boring Stuff with Python",
                        "duration": "50 hours",
                        "type": "Book",
                    },
                ],
                "intermediate": [
                    {
                        "name": "Python Data Structures",
                        "duration": "7 weeks",
                        "type": "Course",
                    },
                    {
                        "name": "Effective Python",
                        "duration": "60 hours",
                        "type": "Book",
                    },
                ],
            },
            "react": {
                "beginner": [
                    {
                        "name": "React - The Complete Guide (Udemy)",
                        "duration": "48 hours",
                        "type": "Course",
                    },
                    {
                        "name": "Official React Tutorial",
                        "duration": "10 hours",
                        "type": "Tutorial",
                    },
                ],
                "intermediate": [
                    {
                        "name": "Advanced React Patterns",
                        "duration": "20 hours",
                        "type": "Course",
                    },
                    {
                        "name": "React Testing Library",
                        "duration": "15 hours",
                        "type": "Tutorial",
                    },
                ],
            },
            "aws": {
                "beginner": [
                    {
                        "name": "AWS Cloud Practitioner Essentials",
                        "duration": "6 hours",
                        "type": "Course",
                    },
                    {
                        "name": "AWS Certified Solutions Architect",
                        "duration": "3 months",
                        "type": "Certification",
                    },
                ],
                "intermediate": [
                    {
                        "name": "AWS Solutions Architect Associate",
                        "duration": "4 months",
                        "type": "Certification",
                    },
                    {
                        "name": "Advanced AWS Networking",
                        "duration": "30 hours",
                        "type": "Course",
                    },
                ],
            },
            "docker": {
                "beginner": [
                    {
                        "name": "Docker for Beginners",
                        "duration": "12 hours",
                        "type": "Course",
                    },
                    {
                        "name": "Docker Official Documentation",
                        "duration": "20 hours",
                        "type": "Documentation",
                    },
                ],
                "intermediate": [
                    {
                        "name": "Docker Mastery",
                        "duration": "40 hours",
                        "type": "Course",
                    },
                    {
                        "name": "Docker Compose and Swarm",
                        "duration": "25 hours",
                        "type": "Tutorial",
                    },
                ],
            },
        }

        for skill in missing_skills[:10]:
            skill_lower = skill.lower()

            if skill_lower in resources:
                learning_paths.append(
                    {
                        "skill": skill,
                        "resources": resources[skill_lower].get(
                            current_level, resources[skill_lower].get("beginner", [])
                        ),
                        "estimated_time": "2-4 months",
                        "priority": "High"
                        if skill_lower in ["python", "javascript", "aws", "react"]
                        else "Medium",
                    }
                )
            else:
                # Generic recommendations
                learning_paths.append(
                    {
                        "skill": skill,
                        "resources": [
                            {
                                "name": f"{skill} Official Documentation",
                                "duration": "20 hours",
                                "type": "Documentation",
                            },
                            {
                                "name": f"{skill} Tutorial on YouTube",
                                "duration": "10 hours",
                                "type": "Video",
                            },
                            {
                                "name": f"Udemy: {skill} Complete Guide",
                                "duration": "30 hours",
                                "type": "Course",
                            },
                        ],
                        "estimated_time": "1-3 months",
                        "priority": "Medium",
                    }
                )

        return learning_paths

    def recommend_certifications(
        self, resume_text: str, job_description: str = None
    ) -> List[Dict[str, Any]]:
        """
        Recommend relevant certifications.

        Args:
            resume_text: Resume content
            job_description: Optional job description

        Returns:
            List of certification recommendations
        """
        text_to_analyze = resume_text.lower()
        if job_description:
            text_to_analyze += " " + job_description.lower()

        recommendations = []

        for skill_key, cert_info in self.certifications.items():
            if skill_key in text_to_analyze:
                recommendations.append(
                    {
                        **cert_info,
                        "relevance": "High",
                        "reason": f"Relevant to your {skill_key.upper()} experience",
                    }
                )

        # Add general recommendations
        if not recommendations:
            recommendations = [
                {
                    **self.certifications["pmp"],
                    "relevance": "Medium",
                    "reason": "Valuable for career advancement",
                }
            ]

        return recommendations[:5]

    def get_industry_trends(self, industry: str = "technology") -> Dict[str, Any]:
        """
        Get trending skills for an industry.

        Args:
            industry: Industry name

        Returns:
            Trending skills data
        """
        trends = {
            "technology": {
                "hot_skills": [
                    {
                        "skill": "AI/Machine Learning",
                        "growth": "+45%",
                        "demand": "Very High",
                    },
                    {
                        "skill": "Cloud Computing (AWS/Azure)",
                        "growth": "+38%",
                        "demand": "Very High",
                    },
                    {"skill": "DevOps/CI/CD", "growth": "+32%", "demand": "High"},
                    {"skill": "Python", "growth": "+28%", "demand": "Very High"},
                    {"skill": "React/Frontend", "growth": "+25%", "demand": "High"},
                    {"skill": "Kubernetes", "growth": "+40%", "demand": "High"},
                    {"skill": "Cybersecurity", "growth": "+35%", "demand": "Very High"},
                    {"skill": "Data Engineering", "growth": "+42%", "demand": "High"},
                ],
                "declining_skills": [
                    {"skill": "Flash", "growth": "-80%", "demand": "Very Low"},
                    {"skill": "jQuery", "growth": "-15%", "demand": "Low"},
                ],
                "emerging_skills": [
                    "Large Language Models (LLMs)",
                    "Edge Computing",
                    "Web3/Blockchain",
                    "Rust Programming",
                    "GraphQL",
                ],
            }
        }

        return trends.get(industry, trends["technology"])

    def create_skill_development_plan(
        self, gap_analysis: Dict[str, Any], timeframe: str = "6 months"
    ) -> Dict[str, Any]:
        """
        Create a structured skill development plan.

        Args:
            gap_analysis: Results from analyze_skill_gaps
            timeframe: Target timeframe (3 months, 6 months, 1 year)

        Returns:
            Development plan with milestones
        """
        priority_gaps = gap_analysis["priority_gaps"]

        plan = {
            "timeframe": timeframe,
            "total_skills": len(
                [skill for gap in priority_gaps for skill in gap["missing_skills"]]
            ),
            "phases": [],
        }

        # Determine number of phases based on timeframe
        phases_count = {"3 months": 2, "6 months": 3, "1 year": 4}.get(timeframe, 3)

        skills_per_phase = max(1, plan["total_skills"] // phases_count)

        phase_num = 1
        current_skills = []

        for gap in priority_gaps:
            for skill in gap["missing_skills"]:
                current_skills.append({"skill": skill, "category": gap["category"]})

                if len(current_skills) >= skills_per_phase:
                    plan["phases"].append(
                        {
                            "phase": phase_num,
                            "duration": f"{int(timeframe.split()[0]) // phases_count} months",
                            "skills": current_skills.copy(),
                            "goals": [
                                f"Complete {skill['skill']} fundamentals"
                                for skill in current_skills[:2]
                            ],
                            "milestone": f"Build project using {current_skills[0]['skill']}",
                        }
                    )
                    current_skills = []
                    phase_num += 1

        # Add remaining skills
        if current_skills:
            plan["phases"].append(
                {
                    "phase": phase_num,
                    "duration": f"{int(timeframe.split()[0]) // phases_count} months",
                    "skills": current_skills,
                    "goals": [
                        f"Complete {skill['skill']} fundamentals"
                        for skill in current_skills
                    ],
                    "milestone": "Polish resume with new skills",
                }
            )

        return plan
