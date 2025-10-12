"""
Social Media Resume Generator
Generate content for LinkedIn, Twitter, and portfolio sites.
"""

from typing import Dict, List


class SocialResumeGenerator:
    """Generate social media profiles and bios from resume."""

    def __init__(self):
        self.char_limits = {
            "twitter_bio": 160,
            "linkedin_headline": 220,
            "github_bio": 160,
            "instagram_bio": 150,
        }

    def generate_linkedin_about(
        self,
        name: str,
        title: str,
        years_experience: int,
        key_skills: List[str],
        achievements: List[str],
        passion: str = None,
    ) -> str:
        """Generate LinkedIn About section."""

        skills_text = ", ".join(key_skills[:5])

        about = f"""I'm {name}, a {title} with {years_experience}+ years of experience specializing in {skills_text}.

Throughout my career, I've focused on delivering measurable results:
"""

        # Add top 3 achievements
        for i, achievement in enumerate(achievements[:3], 1):
            about += f"\n• {achievement}"

        if passion:
            about += f"\n\n{passion}"

        about += f"\n\nI'm passionate about leveraging technology to solve real-world problems and driving innovation in everything I do."

        about += f"\n\n💼 Open to: New opportunities, collaborations, and networking\n📫 Let's connect!"

        return about

    def generate_linkedin_headline(
        self, title: str, specialization: str, unique_value: str
    ) -> str:
        """Generate LinkedIn headline (220 char limit)."""

        headline = f"{title} | {specialization} | {unique_value}"

        # Truncate if too long
        if len(headline) > self.char_limits["linkedin_headline"]:
            headline = f"{title} | {specialization}"
            if len(headline) > self.char_limits["linkedin_headline"]:
                headline = headline[: self.char_limits["linkedin_headline"] - 3] + "..."

        return headline

    def generate_twitter_bio(
        self, title: str, interests: List[str], personality_trait: str = None
    ) -> str:
        """Generate Twitter bio (160 char limit)."""

        interests_text = " • ".join(interests[:3])

        if personality_trait:
            bio = f"{title} | {interests_text} | {personality_trait}"
        else:
            bio = f"{title} | {interests_text}"

        # Truncate if needed
        if len(bio) > self.char_limits["twitter_bio"]:
            interests_text = " • ".join(interests[:2])
            bio = f"{title} | {interests_text}"

        return bio[: self.char_limits["twitter_bio"]]

    def generate_github_bio(
        self, focus_area: str, languages: List[str], current_project: str = None
    ) -> str:
        """Generate GitHub bio (160 char limit)."""

        langs_text = ", ".join(languages[:4])

        if current_project:
            bio = f"{focus_area} | {langs_text} | Currently: {current_project}"
        else:
            bio = f"{focus_area} developer | {langs_text}"

        return bio[: self.char_limits["github_bio"]]

    def generate_github_readme_profile(
        self,
        name: str,
        title: str,
        skills: List[str],
        current_focus: str,
        fun_fact: str = None,
    ) -> str:
        """Generate GitHub profile README."""

        readme = f"""# Hi there, I'm {name}! 👋

## About Me
🚀 {title} passionate about building amazing things with code

## 🔭 Currently Working On
{current_focus}

## 🛠️ Tech Stack
"""

        # Group skills with emojis
        for skill in skills[:8]:
            readme += f"- {skill}\n"

        if fun_fact:
            readme += f"\n## ⚡ Fun Fact\n{fun_fact}\n"

        readme += """
## 📫 How to Reach Me
- LinkedIn: [Your LinkedIn]
- Email: [Your Email]
- Portfolio: [Your Website]

## 📊 GitHub Stats
![Your GitHub stats](https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true)
"""

        return readme

    def generate_portfolio_bio(
        self,
        name: str,
        title: str,
        specialties: List[str],
        years_experience: int,
        personal_touch: str,
    ) -> str:
        """Generate portfolio website bio."""

        specialties_text = ", ".join(specialties)

        bio = f"""Hello! I'm {name}, a {title} with {years_experience}+ years of experience.

I specialize in {specialties_text}, bringing creative solutions to complex problems.

{personal_touch}

When I'm not coding, you'll find me exploring new technologies, contributing to open-source projects, or sharing knowledge with the developer community.

Let's build something amazing together!"""

        return bio

    def generate_elevator_pitches(
        self,
        name: str,
        title: str,
        unique_value: str,
        key_achievement: str,
        call_to_action: str,
    ) -> Dict[str, str]:
        """Generate elevator pitches of different lengths."""

        pitches = {}

        # 30-second pitch (75-90 words)
        pitches["30_second"] = f"""Hi, I'm {name}, a {title}. {unique_value}. 
Recently, {key_achievement}. {call_to_action}."""

        # 60-second pitch (150-175 words)
        pitches["60_second"] = f"""Hello, my name is {name}, and I'm a {title}.

{unique_value}. Throughout my career, I've focused on delivering results that matter. 
For example, {key_achievement}.

I'm passionate about using technology to solve real-world problems and love collaborating with teams that share this vision. 
{call_to_action}."""

        # 2-minute pitch (300-350 words)
        pitches[
            "2_minute"
        ] = f"""Good morning/afternoon, I'm {name}, and I work as a {title}.

What drives me is {unique_value.lower()}. Over the years, I've had the opportunity to work on diverse projects 
that have challenged me to grow both technically and professionally.

One of my proudest achievements was {key_achievement}. This experience taught me the importance of 
persistence, collaboration, and innovative thinking.

My approach to work is simple: understand the problem deeply, collaborate with stakeholders, and deliver 
solutions that create real value. I believe in continuous learning and staying updated with industry trends.

I'm particularly interested in opportunities where I can apply my skills to make a meaningful impact. 
{call_to_action}.

I'd love to hear more about your challenges and explore how we might work together."""

        return pitches

    def generate_email_signature(
        self,
        name: str,
        title: str,
        company: str = None,
        email: str = None,
        phone: str = None,
        linkedin: str = None,
        website: str = None,
    ) -> str:
        """Generate professional email signature."""

        signature = f"""Best regards,

{name}
{title}"""

        if company:
            signature += f"\n{company}"

        signature += "\n"

        if email:
            signature += f"\n📧 {email}"
        if phone:
            signature += f"\n📱 {phone}"
        if linkedin:
            signature += f"\n💼 {linkedin}"
        if website:
            signature += f"\n🌐 {website}"

        return signature

    def generate_conference_bio(
        self,
        name: str,
        title: str,
        company: str,
        expertise: List[str],
        speaking_topics: List[str],
        word_limit: int = 100,
    ) -> str:
        """Generate conference speaker bio."""

        expertise_text = ", ".join(expertise[:3])
        topics_text = ", ".join(speaking_topics[:2])

        bio = f"""{name} is a {title} at {company}, specializing in {expertise_text}. 
With extensive experience in {topics_text}, {name.split()[0]} has helped organizations 
transform their technology landscape. {name.split()[0]} is passionate about sharing 
knowledge and fostering innovation in the tech community."""

        words = bio.split()
        if len(words) > word_limit:
            bio = " ".join(words[:word_limit]) + "..."

        return bio

    def generate_slack_status(
        self, current_focus: str, mood: str = "working"
    ) -> Dict[str, str]:
        """Generate Slack status messages."""

        statuses = {
            "working": {"text": f"🔨 {current_focus}", "emoji": ":hammer:"},
            "meeting": {"text": "📅 In a meeting", "emoji": ":calendar:"},
            "focused": {"text": f"🎯 Deep work: {current_focus}", "emoji": ":dart:"},
            "lunch": {"text": "🍴 Lunch break", "emoji": ":fork_and_knife:"},
            "learning": {"text": f"📚 Learning: {current_focus}", "emoji": ":books:"},
        }

        return statuses.get(mood, statuses["working"])

    def optimize_for_platform(self, text: str, platform: str) -> Dict[str, any]:
        """Optimize text for specific platform."""

        char_limit = self.char_limits.get(platform, 500)

        optimized = text[:char_limit]
        is_truncated = len(text) > char_limit

        # Add platform-specific formatting
        hashtags_recommended = 0
        if platform == "twitter_bio":
            hashtags_recommended = 0  # Don't use hashtags in bio
        elif platform == "linkedin_headline":
            # LinkedIn headlines don't typically use hashtags
            hashtags_recommended = 0

        return {
            "optimized_text": optimized,
            "original_length": len(text),
            "final_length": len(optimized),
            "is_truncated": is_truncated,
            "characters_remaining": char_limit - len(optimized),
            "hashtags_recommended": hashtags_recommended,
            "platform_tips": self._get_platform_tips(platform),
        }

    def _get_platform_tips(self, platform: str) -> List[str]:
        """Get platform-specific tips."""

        tips = {
            "twitter_bio": [
                "Keep it concise and punchy",
                "Use keywords people search for",
                "Add personality",
                "Include what you do + what you care about",
            ],
            "linkedin_headline": [
                "Use keywords for searchability",
                "Highlight your unique value",
                "Include your target role",
                "Make it specific, not generic",
            ],
            "github_bio": [
                "Mention your focus area",
                "List key technologies",
                "Keep it professional but authentic",
                "Update with current projects",
            ],
            "linkedin_about": [
                "Start with a strong hook",
                "Use first person (I, not 'he/she')",
                "Include quantifiable achievements",
                "End with a call-to-action",
            ],
        }

        return tips.get(platform, ["Keep it professional and authentic"])

    def generate_all_profiles(self, resume_data: Dict) -> Dict[str, str]:
        """Generate all social profiles at once."""

        name = resume_data.get("name", "Professional")
        title = resume_data.get("title", "Your Title")
        skills = resume_data.get("skills", [])

        return {
            "linkedin_headline": self.generate_linkedin_headline(
                title, skills[0] if skills else "Technology", "Driving Innovation"
            ),
            "twitter_bio": self.generate_twitter_bio(
                title,
                skills[:3] if skills else ["Tech", "Innovation"],
                "Always Learning",
            ),
            "github_bio": self.generate_github_bio(
                title.split()[0] if title else "Software",
                skills[:4] if skills else ["Python", "JavaScript"],
                "Building cool stuff",
            ),
            "portfolio_bio": self.generate_portfolio_bio(
                name,
                title,
                skills[:3] if skills else ["Development"],
                resume_data.get("years_experience", 3),
                "I love turning ideas into reality through clean, efficient code.",
            ),
        }
