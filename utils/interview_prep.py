"""
Interview Prep Generator
Generate interview questions and practice scenarios from resume.
"""

import re
from typing import Dict, List, Any
import random


class InterviewPrep:
    """Generate interview questions and preparation materials from resume."""

    def __init__(self):
        self.behavioral_templates = [
            "Tell me about a time when you {action}.",
            "Describe a situation where you had to {action}.",
            "Give me an example of when you {action}.",
            "Can you share an experience where you {action}?",
            "Walk me through a time you {action}.",
        ]

        self.technical_templates = [
            "How would you {action}?",
            "Explain your approach to {action}.",
            "What's your experience with {action}?",
            "Describe how you would {action}.",
            "What methods do you use to {action}?",
        ]

    def generate_questions(self, resume_text: str) -> Dict[str, List[str]]:
        """
        Generate interview questions based on resume content.

        Args:
            resume_text: Resume content

        Returns:
            Dictionary of question categories
        """
        questions = {
            "behavioral": [],
            "technical": [],
            "situational": [],
            "experience_based": [],
            "achievements": [],
        }

        # Generate behavioral questions
        questions["behavioral"] = self._generate_behavioral_questions(resume_text)

        # Generate technical questions
        questions["technical"] = self._generate_technical_questions(resume_text)

        # Generate situational questions
        questions["situational"] = self._generate_situational_questions(resume_text)

        # Generate experience-based questions
        questions["experience_based"] = self._generate_experience_questions(resume_text)

        # Generate achievement questions
        questions["achievements"] = self._generate_achievement_questions(resume_text)

        return questions

    def _generate_behavioral_questions(self, resume_text: str) -> List[str]:
        """Generate behavioral questions using STAR method."""
        text_lower = resume_text.lower()
        questions = []

        # Extract action verbs from resume
        action_verbs = [
            "led",
            "managed",
            "developed",
            "created",
            "implemented",
            "improved",
            "increased",
            "reduced",
            "designed",
            "built",
            "collaborated",
            "coordinated",
            "analyzed",
            "solved",
        ]

        found_actions = [verb for verb in action_verbs if verb in text_lower]

        # Generate questions from found actions
        for action in found_actions[:10]:
            template = random.choice(self.behavioral_templates)
            questions.append(
                template.format(action=action + " a project or initiative")
            )

        # Add common behavioral questions
        common_behavioral = [
            "Tell me about a time when you faced a significant challenge at work. How did you handle it?",
            "Describe a situation where you had to work with a difficult team member. What was the outcome?",
            "Give me an example of when you had to meet a tight deadline. How did you ensure success?",
            "Tell me about a time when you failed. What did you learn from it?",
            "Describe a situation where you had to adapt to significant changes. How did you manage?",
            "Tell me about a time when you had to persuade others to see things your way.",
            "Give me an example of when you went above and beyond your job responsibilities.",
            "Describe a time when you had to make a difficult decision with limited information.",
            "Tell me about a conflict you resolved at work.",
            "Give me an example of when you demonstrated leadership, even if you weren't in a leadership role.",
        ]

        questions.extend(common_behavioral[:5])
        return questions[:15]

    def _generate_technical_questions(self, resume_text: str) -> List[str]:
        """Generate technical questions based on skills mentioned."""
        text_lower = resume_text.lower()
        questions = []

        # Common technical skills
        tech_skills = {
            "python": "Explain the difference between lists and tuples in Python.",
            "java": "What are the main principles of object-oriented programming in Java?",
            "javascript": "Explain the concept of closures in JavaScript.",
            "react": "How does the virtual DOM work in React?",
            "sql": "Explain the difference between INNER JOIN and LEFT JOIN.",
            "docker": "What are the benefits of using Docker containers?",
            "aws": "Explain the difference between EC2 and Lambda.",
            "git": "What's the difference between git merge and git rebase?",
            "api": "What's the difference between REST and GraphQL APIs?",
            "database": "Explain database normalization and its benefits.",
            "algorithm": "What's the time complexity of binary search?",
            "testing": "Explain the difference between unit testing and integration testing.",
            "agile": "Describe the Scrum framework and its key ceremonies.",
            "security": "What is SQL injection and how do you prevent it?",
            "cloud": "Explain the difference between IaaS, PaaS, and SaaS.",
        }

        # Find mentioned skills
        for skill, question in tech_skills.items():
            if skill in text_lower:
                questions.append(question)

        # Add general technical questions
        general_tech = [
            "Walk me through your approach to debugging a complex issue.",
            "How do you stay updated with new technologies and best practices?",
            "Describe your experience with version control and collaboration tools.",
            "Explain how you would optimize the performance of a slow application.",
            "What's your approach to writing clean, maintainable code?",
            "Describe your testing strategy for a new feature.",
            "How do you handle technical debt in a project?",
            "Explain your experience with CI/CD pipelines.",
        ]

        questions.extend(general_tech[: 8 - len(questions)])
        return questions[:15]

    def _generate_situational_questions(self, resume_text: str) -> List[str]:
        """Generate hypothetical situational questions."""
        situational = [
            "How would you handle a situation where you disagree with your manager's technical decision?",
            "What would you do if you discovered a critical bug right before a major release?",
            "How would you prioritize if you had three high-priority tasks but could only complete one?",
            "What would you do if a teammate wasn't pulling their weight on a project?",
            "How would you handle receiving negative feedback from a peer?",
            "What would you do if you realized you made a mistake that affected the team?",
            "How would you approach learning a new technology required for an urgent project?",
            "What would you do if you had to choose between meeting a deadline and ensuring code quality?",
            "How would you handle a situation where a client's requirements keep changing?",
            "What would you do if you identified a security vulnerability in production code?",
        ]

        return situational

    def _generate_experience_questions(self, resume_text: str) -> List[str]:
        """Generate questions about specific experiences."""
        questions = []
        text_lower = resume_text.lower()

        # Look for company names or roles
        if "experience" in text_lower or "worked" in text_lower:
            questions.append(
                "Tell me about your most significant project in your current/recent role."
            )
            questions.append(
                "What was the biggest challenge you faced in your last position?"
            )
            questions.append(
                "Describe your day-to-day responsibilities in your current role."
            )

        # Look for specific technologies
        questions.append(
            "Walk me through a project where you used the technologies mentioned in your resume."
        )
        questions.append(
            "Which project from your experience are you most proud of and why?"
        )

        # Team experience
        if "team" in text_lower or "collaborate" in text_lower:
            questions.append("Describe your experience working in a team environment.")
            questions.append("What role do you typically take in a team setting?")

        # Leadership
        if "led" in text_lower or "managed" in text_lower or "leader" in text_lower:
            questions.append("Tell me about your leadership experience.")
            questions.append("How do you motivate and manage team members?")

        # Add general experience questions
        general_exp = [
            "Why are you interested in leaving your current position?",
            "What attracts you to this role and our company?",
            "Where do you see yourself in 5 years?",
            "What's your ideal work environment?",
            "What are your salary expectations?",
            "What are your greatest strengths and weaknesses?",
            "Why should we hire you over other candidates?",
        ]

        questions.extend(general_exp[: 10 - len(questions)])
        return questions[:15]

    def _generate_achievement_questions(self, resume_text: str) -> List[str]:
        """Generate questions about specific achievements."""
        questions = []

        # Look for metrics and achievements
        metrics = re.findall(
            r"\d+[%\+\-]|\d+\s*(?:years?|months?)|[\$€£]\d+", resume_text.lower()
        )

        if metrics:
            questions.append(
                "Tell me about the achievement you're most proud of from your resume."
            )
            questions.append("How did you measure the success of your projects?")
            questions.append(
                "Walk me through how you achieved the results mentioned in your resume."
            )

        # Achievement-focused questions
        achievement_questions = [
            "Describe a time when you exceeded expectations on a project.",
            "Tell me about an innovation or improvement you implemented.",
            "What's the biggest impact you've made in your career?",
            "Describe a time when you received recognition for your work.",
            "Tell me about a problem you solved that had significant impact.",
            "What's your most significant professional accomplishment?",
            "Describe a time when you saved the company time or money.",
            "Tell me about a complex problem you solved.",
            "What's the most challenging project you've worked on?",
            "Describe your biggest contribution to a team's success.",
        ]

        questions.extend(achievement_questions[: 12 - len(questions)])
        return questions[:12]

    def generate_star_templates(self, questions: List[str]) -> List[Dict[str, str]]:
        """
        Generate STAR method templates for questions.

        Args:
            questions: List of questions

        Returns:
            List of STAR templates
        """
        templates = []

        for question in questions[:10]:  # Limit to top 10
            template = {
                "question": question,
                "situation": "Describe the context or background...",
                "task": "Explain what needed to be done or the challenge...",
                "action": "Detail the specific actions you took...",
                "result": "Share the outcomes and what you learned...",
                "example": self._generate_example_answer(question),
            }
            templates.append(template)

        return templates

    def _generate_example_answer(self, question: str) -> str:
        """Generate an example STAR answer."""
        return """Example STAR Answer:
        
Situation: In my previous role at XYZ Company, we were facing a critical deadline...

Task: I was responsible for leading the team to deliver the feature while maintaining quality...

Action: I implemented daily standups, broke down the work into manageable sprints, and coordinated with stakeholders...

Result: We delivered the project 2 days ahead of schedule, reduced bugs by 40%, and received positive feedback from the client. This experience taught me the importance of clear communication and agile methodologies."""

    def generate_practice_scenarios(self, resume_text: str) -> List[Dict[str, Any]]:
        """
        Generate practice scenarios for mock interviews.

        Args:
            resume_text: Resume content

        Returns:
            List of practice scenarios
        """
        scenarios = []

        # Technical challenge scenario
        scenarios.append(
            {
                "type": "Technical Challenge",
                "scenario": "The interviewer asks you to design a system on a whiteboard",
                "tips": [
                    "Ask clarifying questions about requirements",
                    "Start with a high-level architecture",
                    "Explain your thought process out loud",
                    "Consider scalability and trade-offs",
                    "Be prepared to dive deep into any component",
                ],
                "time_limit": "30-45 minutes",
            }
        )

        # Behavioral scenario
        scenarios.append(
            {
                "type": "Behavioral Round",
                "scenario": "The interviewer asks about past experiences using STAR method",
                "tips": [
                    "Prepare 5-7 STAR stories beforehand",
                    "Use specific examples with metrics",
                    "Show what you learned from each experience",
                    "Keep answers concise (2-3 minutes)",
                    "Practice out loud before the interview",
                ],
                "time_limit": "45-60 minutes",
            }
        )

        # Case study scenario
        scenarios.append(
            {
                "type": "Case Study",
                "scenario": "Solve a business problem or analyze a scenario",
                "tips": [
                    "Structure your approach (framework)",
                    "Ask questions to clarify the problem",
                    "Think out loud and explain your reasoning",
                    "Consider multiple perspectives",
                    "Provide a clear recommendation",
                ],
                "time_limit": "30-45 minutes",
            }
        )

        # Culture fit scenario
        scenarios.append(
            {
                "type": "Culture Fit",
                "scenario": "Discuss your work style, values, and career goals",
                "tips": [
                    "Research company values beforehand",
                    "Be authentic and honest",
                    "Show enthusiasm for the role",
                    "Ask thoughtful questions",
                    "Explain how you align with their mission",
                ],
                "time_limit": "30 minutes",
            }
        )

        return scenarios

    def generate_questions_to_ask(self, job_level: str = "mid") -> List[Dict[str, str]]:
        """
        Generate good questions to ask the interviewer.

        Args:
            job_level: junior, mid, or senior

        Returns:
            List of questions with categories
        """
        questions = []

        # About the role
        questions.append(
            {
                "category": "About the Role",
                "question": "What does a typical day look like for someone in this position?",
                "why_ask": "Shows interest in day-to-day responsibilities",
            }
        )

        questions.append(
            {
                "category": "About the Role",
                "question": "What are the biggest challenges facing the team right now?",
                "why_ask": "Demonstrates problem-solving mindset",
            }
        )

        questions.append(
            {
                "category": "About the Role",
                "question": "How do you measure success for this position?",
                "why_ask": "Shows goal-oriented approach",
            }
        )

        # About the team
        questions.append(
            {
                "category": "About the Team",
                "question": "Can you tell me about the team I'll be working with?",
                "why_ask": "Interest in collaboration",
            }
        )

        questions.append(
            {
                "category": "About the Team",
                "question": "What's the team's approach to professional development?",
                "why_ask": "Shows desire to grow and learn",
            }
        )

        # About the company
        questions.append(
            {
                "category": "About the Company",
                "question": "What's the company's vision for the next 3-5 years?",
                "why_ask": "Long-term thinking and commitment",
            }
        )

        questions.append(
            {
                "category": "About the Company",
                "question": "How would you describe the company culture?",
                "why_ask": "Cultural fit assessment",
            }
        )

        # About growth
        if job_level in ["junior", "mid"]:
            questions.append(
                {
                    "category": "Growth & Development",
                    "question": "What opportunities are there for learning and development?",
                    "why_ask": "Shows ambition and desire to improve",
                }
            )

        if job_level == "senior":
            questions.append(
                {
                    "category": "Leadership",
                    "question": "What's the leadership style of the team and organization?",
                    "why_ask": "Alignment on management approach",
                }
            )

        # Next steps
        questions.append(
            {
                "category": "Next Steps",
                "question": "What are the next steps in the interview process?",
                "why_ask": "Shows continued interest and organization",
            }
        )

        return questions
