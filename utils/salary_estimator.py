"""
Salary Estimator
Estimate market value based on resume data.
"""

from typing import Dict, List, Any


class SalaryEstimator:
    """Estimate salary based on experience, skills, and location."""

    def __init__(self):
        # Base salaries by role (in USD, national average)
        self.base_salaries = {
            "software engineer": 95000,
            "senior software engineer": 130000,
            "data scientist": 110000,
            "product manager": 115000,
            "devops engineer": 105000,
            "frontend developer": 85000,
            "backend developer": 95000,
            "full stack developer": 100000,
            "machine learning engineer": 125000,
            "engineering manager": 155000,
            "technical lead": 140000,
            "qa engineer": 75000,
            "ui/ux designer": 80000,
            "data analyst": 70000,
            "business analyst": 75000,
            "project manager": 95000,
            "system administrator": 70000,
            "database administrator": 85000,
            "security engineer": 110000,
            "cloud architect": 145000,
        }

        # Location multipliers (compared to national average)
        self.location_multipliers = {
            "san francisco": 1.45,
            "new york": 1.35,
            "seattle": 1.30,
            "boston": 1.25,
            "los angeles": 1.20,
            "austin": 1.15,
            "chicago": 1.10,
            "denver": 1.10,
            "atlanta": 1.05,
            "phoenix": 1.00,
            "dallas": 1.05,
            "miami": 1.00,
            "remote": 0.95,
            "other": 0.90,
        }

        # Skills premiums (percentage increase)
        self.skills_premium = {
            "aws": 8,
            "kubernetes": 10,
            "react": 6,
            "python": 7,
            "machine learning": 15,
            "ai": 15,
            "blockchain": 20,
            "go": 12,
            "rust": 15,
            "tensorflow": 12,
            "pytorch": 12,
            "docker": 8,
            "microservices": 10,
            "graphql": 8,
            "typescript": 6,
            "java": 5,
            "c++": 7,
            "scala": 12,
            "spark": 10,
            "hadoop": 8,
        }

    def estimate_salary(
        self,
        job_title: str,
        years_experience: int,
        skills: List[str],
        education_level: str,
        location: str,
        company_size: str = "medium",
    ) -> Dict[str, Any]:
        """Estimate salary range based on profile."""

        # Get base salary
        base_salary = self._get_base_salary(job_title)

        # Apply experience multiplier
        experience_multiplier = self._calculate_experience_multiplier(years_experience)
        salary_with_exp = base_salary * experience_multiplier

        # Apply skills premium
        skills_boost = self._calculate_skills_premium(skills)
        salary_with_skills = salary_with_exp * (1 + skills_boost / 100)

        # Apply education multiplier
        education_multiplier = self._get_education_multiplier(education_level)
        salary_with_edu = salary_with_skills * education_multiplier

        # Apply location multiplier
        location_mult = self._get_location_multiplier(location)
        final_base = salary_with_edu * location_mult

        # Apply company size adjustment
        company_multiplier = self._get_company_size_multiplier(company_size)
        final_salary = final_base * company_multiplier

        # Create range (±10%)
        min_salary = int(final_salary * 0.90)
        max_salary = int(final_salary * 1.10)
        median_salary = int(final_salary)

        return {
            "estimated_range": {
                "min": min_salary,
                "median": median_salary,
                "max": max_salary,
                "currency": "USD",
            },
            "breakdown": {
                "base_salary": int(base_salary),
                "with_experience": int(salary_with_exp),
                "with_skills": int(salary_with_skills),
                "with_education": int(salary_with_edu),
                "with_location": int(final_base),
                "final_estimated": median_salary,
            },
            "factors": {
                "experience_years": years_experience,
                "experience_multiplier": round(experience_multiplier, 2),
                "skills_premium": round(skills_boost, 1),
                "education_multiplier": round(education_multiplier, 2),
                "location_multiplier": round(location_mult, 2),
                "company_size_multiplier": round(company_multiplier, 2),
            },
            "top_skills_contributing": self._get_top_contributing_skills(skills)[:5],
            "formatted_range": f"${min_salary:,} - ${max_salary:,}",
            "confidence": self._calculate_confidence(job_title, location),
        }

    def _get_base_salary(self, job_title: str) -> int:
        """Get base salary for role."""
        job_title_lower = job_title.lower()

        # Try exact match first
        if job_title_lower in self.base_salaries:
            return self.base_salaries[job_title_lower]

        # Try partial match
        for key in self.base_salaries:
            if key in job_title_lower or job_title_lower in key:
                return self.base_salaries[key]

        # Default to mid-range
        return 90000

    def _calculate_experience_multiplier(self, years: int) -> float:
        """Calculate multiplier based on experience."""
        if years <= 1:
            return 0.75
        elif years <= 2:
            return 0.85
        elif years <= 3:
            return 0.95
        elif years <= 5:
            return 1.0
        elif years <= 7:
            return 1.15
        elif years <= 10:
            return 1.30
        elif years <= 15:
            return 1.45
        else:
            return 1.55

    def _calculate_skills_premium(self, skills: List[str]) -> float:
        """Calculate total skills premium."""
        total_premium = 0

        for skill in skills:
            skill_lower = skill.lower()
            if skill_lower in self.skills_premium:
                total_premium += self.skills_premium[skill_lower]

        # Cap at 40% total premium
        return min(total_premium, 40)

    def _get_education_multiplier(self, education: str) -> float:
        """Get multiplier based on education."""
        education_lower = education.lower()

        if "phd" in education_lower or "doctorate" in education_lower:
            return 1.15
        elif "master" in education_lower or "mba" in education_lower:
            return 1.10
        elif "bachelor" in education_lower:
            return 1.0
        elif "associate" in education_lower:
            return 0.95
        else:
            return 0.90

    def _get_location_multiplier(self, location: str) -> float:
        """Get location cost of living multiplier."""
        location_lower = location.lower()

        for key, multiplier in self.location_multipliers.items():
            if key in location_lower:
                return multiplier

        return self.location_multipliers["other"]

    def _get_company_size_multiplier(self, size: str) -> float:
        """Get company size multiplier."""
        size_lower = size.lower()

        if "large" in size_lower or "enterprise" in size_lower:
            return 1.15
        elif "medium" in size_lower:
            return 1.0
        elif "small" in size_lower or "startup" in size_lower:
            return 0.90
        else:
            return 1.0

    def _get_top_contributing_skills(self, skills: List[str]) -> List[Dict[str, Any]]:
        """Get skills that contribute most to salary."""
        contributing = []

        for skill in skills:
            skill_lower = skill.lower()
            if skill_lower in self.skills_premium:
                contributing.append(
                    {
                        "skill": skill,
                        "premium": self.skills_premium[skill_lower],
                        "premium_formatted": f"+{self.skills_premium[skill_lower]}%",
                    }
                )

        # Sort by premium
        contributing.sort(key=lambda x: x["premium"], reverse=True)
        return contributing

    def _calculate_confidence(self, job_title: str, location: str) -> str:
        """Calculate confidence level of estimate."""
        job_title_lower = job_title.lower()
        location_lower = location.lower()

        # High confidence for known roles and locations
        if job_title_lower in self.base_salaries and any(
            loc in location_lower for loc in self.location_multipliers
        ):
            return "High"
        elif job_title_lower in self.base_salaries or any(
            loc in location_lower for loc in self.location_multipliers
        ):
            return "Medium"
        else:
            return "Low"

    def compare_to_market(
        self, current_salary: int, estimated_range: Dict[str, int]
    ) -> Dict[str, Any]:
        """Compare current salary to market estimate."""

        median = estimated_range["median"]
        min_val = estimated_range["min"]
        max_val = estimated_range["max"]

        if current_salary < min_val:
            status = "below_market"
            difference = min_val - current_salary
            percentage = (difference / current_salary) * 100
            message = f"You're earning ${difference:,} ({percentage:.1f}%) below market minimum"
        elif current_salary > max_val:
            status = "above_market"
            difference = current_salary - max_val
            percentage = (difference / max_val) * 100
            message = f"You're earning ${difference:,} ({percentage:.1f}%) above market maximum"
        else:
            status = "at_market"
            difference = abs(current_salary - median)
            percentage = (difference / median) * 100
            message = f"You're within market range (±{percentage:.1f}% of median)"

        return {
            "status": status,
            "current_salary": current_salary,
            "market_median": median,
            "difference": difference,
            "percentage_difference": round(percentage, 1),
            "message": message,
            "recommendation": self._get_salary_recommendation(status, percentage),
        }

    def _get_salary_recommendation(self, status: str, percentage: float) -> str:
        """Get recommendation based on market comparison."""
        if status == "below_market":
            if percentage > 20:
                return "Strong case for significant raise. Prepare to negotiate or explore other opportunities."
            elif percentage > 10:
                return "Consider negotiating a raise at your next review."
            else:
                return "Slightly below market. Monitor for next review cycle."
        elif status == "above_market":
            if percentage > 20:
                return "You're well-compensated. Focus on maintaining value and performance."
            else:
                return "You're at or above market rate. Great position!"
        else:
            return "You're fairly compensated at market rate."

    def generate_negotiation_script(
        self, current_offer: int, target_salary: int, justification_points: List[str]
    ) -> str:
        """Generate salary negotiation script."""

        script = """Thank you so much for the offer. I'm very excited about this opportunity and the chance to contribute to the team.

After careful consideration of the market rates for this role and my qualifications, I was hoping we could discuss the compensation package.

Based on my research and the following factors:
"""

        for point in justification_points[:3]:
            script += f"• {point}\n"

        script += f"""
I was hoping we could explore a salary of ${target_salary:,} instead of the initial ${current_offer:,}.

I believe this better reflects the value I can bring to this role and is aligned with current market rates for similar positions.

I'm confident we can find a solution that works for both of us. What are your thoughts on this?"""

        return script

    def suggest_compensation_package_items(self) -> Dict[str, List[str]]:
        """Suggest non-salary compensation items to negotiate."""

        return {
            "financial": [
                "Signing bonus",
                "Annual bonus structure",
                "Stock options/RSUs",
                "Profit sharing",
                "Relocation assistance",
                "Student loan repayment assistance",
            ],
            "time_off": [
                "Additional vacation days",
                "Flexible work schedule",
                "Remote work options",
                "Sabbatical after X years",
                "Parental leave extension",
            ],
            "professional_development": [
                "Conference attendance budget",
                "Certification/training budget",
                "Tuition reimbursement",
                "Professional membership fees",
                "Mentorship program",
            ],
            "benefits": [
                "Health insurance premium coverage",
                "401(k) matching increase",
                "Gym membership",
                "Commuter benefits",
                "Home office stipend",
                "Phone/internet reimbursement",
            ],
            "career_advancement": [
                "Promotion timeline discussion",
                "Title upgrade",
                "Direct reports",
                "High-visibility projects",
                "Cross-functional opportunities",
            ],
        }

    def estimate_total_compensation(
        self,
        base_salary: int,
        bonus_percentage: float = 0,
        stock_value: int = 0,
        benefits_value: int = 0,
    ) -> Dict[str, Any]:
        """Calculate total compensation package value."""

        annual_bonus = int(base_salary * (bonus_percentage / 100))
        total_comp = base_salary + annual_bonus + stock_value + benefits_value

        return {
            "base_salary": base_salary,
            "annual_bonus": annual_bonus,
            "stock_value": stock_value,
            "benefits_value": benefits_value,
            "total_compensation": total_comp,
            "breakdown_percentage": {
                "base": round((base_salary / total_comp) * 100, 1),
                "bonus": round((annual_bonus / total_comp) * 100, 1),
                "stock": round((stock_value / total_comp) * 100, 1),
                "benefits": round((benefits_value / total_comp) * 100, 1),
            },
            "formatted_total": f"${total_comp:,}",
        }
