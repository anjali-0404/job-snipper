"""
Email & Message Generator
Generate professional outreach emails and messages.
"""

from typing import Dict, Any


class EmailGenerator:
    """Generate professional emails and messages for job search."""

    def __init__(self):
        self.tone_styles = {
            "professional": {
                "greeting": "Dear",
                "closing": "Best regards",
                "style": "formal and respectful",
            },
            "casual": {
                "greeting": "Hi",
                "closing": "Thanks",
                "style": "friendly and approachable",
            },
            "confident": {
                "greeting": "Hello",
                "closing": "Looking forward to connecting",
                "style": "direct and confident",
            },
        }

    def generate_recruiter_email(
        self,
        recruiter_name: str,
        company_name: str,
        position: str,
        your_name: str,
        your_expertise: str,
        tone: str = "professional",
    ) -> str:
        """Generate cold email to recruiter."""

        style = self.tone_styles.get(tone, self.tone_styles["professional"])

        email = f"""Subject: {position} Opportunity at {company_name}

{style["greeting"]} {recruiter_name},

I hope this email finds you well. My name is {your_name}, and I'm reaching out regarding the {position} position at {company_name}.

With my background in {your_expertise}, I believe I would be a strong fit for this role. I'm particularly excited about {company_name}'s mission and would love to contribute to your team's success.

I've attached my resume for your review. I would welcome the opportunity to discuss how my skills and experience align with your needs.

Would you be available for a brief call next week to explore this further?

{style["closing"]},
{your_name}"""

        return email

    def generate_linkedin_request(
        self,
        person_name: str,
        connection_reason: str,
        mutual_interest: str = None,
        tone: str = "professional",
    ) -> str:
        """Generate LinkedIn connection request message."""

        mutual_part = (
            f" I noticed we share an interest in {mutual_interest}."
            if mutual_interest
            else ""
        )

        message = f"""Hi {person_name},

I came across your profile and was impressed by your work in {connection_reason}.{mutual_part}

I'd love to connect and learn more about your experience. Looking forward to staying in touch!"""

        # LinkedIn limits messages to 300 characters
        if len(message) > 300:
            message = f"Hi {person_name}, impressed by your work in {connection_reason}. Would love to connect!"

        return message

    def generate_followup_email(
        self,
        recipient_name: str,
        previous_interaction: str,
        days_since: int,
        your_name: str,
        tone: str = "professional",
    ) -> str:
        """Generate follow-up email after application or interview."""

        style = self.tone_styles.get(tone, self.tone_styles["professional"])

        time_reference = "last week" if days_since <= 7 else f"{days_since} days ago"

        email = f"""Subject: Following Up on {previous_interaction}

{style["greeting"]} {recipient_name},

I wanted to follow up on our {previous_interaction} {time_reference}. I remain very interested in the opportunity and wanted to check if there are any updates.

I'm excited about the possibility of joining your team and contributing to the company's goals. Please let me know if you need any additional information from me.

{style["closing"]},
{your_name}"""

        return email

    def generate_thank_you_email(
        self,
        interviewer_name: str,
        position: str,
        company_name: str,
        specific_discussion_point: str,
        your_name: str,
        tone: str = "professional",
    ) -> str:
        """Generate thank you email after interview."""

        style = self.tone_styles.get(tone, self.tone_styles["professional"])

        email = f"""Subject: Thank You - {position} Interview

{style["greeting"]} {interviewer_name},

Thank you for taking the time to speak with me today about the {position} role at {company_name}. I truly enjoyed our conversation and learning more about the team and the exciting projects you're working on.

I was particularly interested in our discussion about {specific_discussion_point}. It reinforced my enthusiasm for this opportunity and my desire to contribute to your team's success.

Please don't hesitate to reach out if you need any additional information. I look forward to hearing from you about the next steps.

{style["closing"]},
{your_name}"""

        return email

    def generate_networking_email(
        self,
        person_name: str,
        how_you_found_them: str,
        what_you_admire: str,
        your_name: str,
        your_background: str,
        specific_ask: str = "advice",
        tone: str = "professional",
    ) -> str:
        """Generate networking email to industry professional."""

        style = self.tone_styles.get(tone, self.tone_styles["professional"])

        email = f"""Subject: Request for {specific_ask.title()} - {your_background}

{style["greeting"]} {person_name},

I hope this email finds you well. I discovered your profile through {how_you_found_them} and was impressed by {what_you_admire}.

I'm currently {your_background}, and I would greatly appreciate your {specific_ask} as I navigate my career path. Your insights would be invaluable.

Would you be open to a brief 15-20 minute call or coffee chat? I'm happy to work around your schedule.

{style["closing"]},
{your_name}"""

        return email

    def generate_referral_request(
        self,
        friend_name: str,
        company_name: str,
        position: str,
        your_name: str,
        why_good_fit: str,
        tone: str = "casual",
    ) -> str:
        """Generate referral request to friend or connection."""

        style = self.tone_styles.get(tone, self.tone_styles["casual"])

        email = f"""Subject: Quick Favor - {position} at {company_name}

{style["greeting"]} {friend_name},

I hope you're doing well! I wanted to reach out because I noticed that {company_name} has an opening for a {position}, and I think it could be a great fit for me.

{why_good_fit}

I know you work at {company_name}, and I was wondering if you'd be comfortable referring me for this role? I completely understand if it's not possible, but I thought I'd ask.

I'd be happy to send you my resume and any other information you might need.

{style["closing"]},
{your_name}"""

        return email

    def generate_salary_negotiation_email(
        self,
        hiring_manager_name: str,
        position: str,
        current_offer: str,
        desired_salary: str,
        justification: str,
        your_name: str,
        tone: str = "confident",
    ) -> str:
        """Generate salary negotiation email."""

        style = self.tone_styles.get(tone, self.tone_styles["confident"])

        email = f"""Subject: {position} Offer Discussion

{style["greeting"]} {hiring_manager_name},

Thank you for extending the offer for the {position} role. I'm excited about the opportunity to join the team and contribute to the company's success.

After careful consideration of the current market rates and my qualifications, I was hoping we could discuss the compensation package. {justification}

Based on this, I was wondering if we could explore a salary of {desired_salary} instead of the initial {current_offer}. I believe this better reflects the value I can bring to the role.

I'm confident we can find a solution that works for both of us. Would you be open to discussing this further?

{style["closing"]},
{your_name}"""

        return email

    def generate_rejection_response(
        self,
        hiring_manager_name: str,
        company_name: str,
        position: str,
        your_name: str,
        tone: str = "professional",
    ) -> str:
        """Generate professional response to job rejection."""

        style = self.tone_styles.get(tone, self.tone_styles["professional"])

        email = f"""Subject: Thank You - {position} at {company_name}

{style["greeting"]} {hiring_manager_name},

Thank you for letting me know about your decision regarding the {position} role. While I'm disappointed, I appreciate the time you and your team invested in considering my application.

I remain very interested in {company_name} and would love to be considered for future opportunities that align with my skills and experience. Please keep me in mind if any suitable positions open up.

I wish you and the team all the best, and I hope our paths cross again in the future.

{style["closing"]},
{your_name}"""

        return email

    def generate_email_templates(self) -> Dict[str, Dict[str, str]]:
        """Get all email templates with placeholders."""

        templates = {
            "cold_outreach": {
                "subject": "[Position] Opportunity at [Company]",
                "body": "Template for reaching out to recruiters...",
                "when_to_use": "When applying cold to a company",
                "tips": [
                    "Research the company first",
                    "Personalize each email",
                    "Keep it under 200 words",
                    "Include specific value you can add",
                ],
            },
            "follow_up": {
                "subject": "Following Up on [Previous Interaction]",
                "body": "Template for following up...",
                "when_to_use": "After 7-10 days of no response",
                "tips": [
                    "Be polite and professional",
                    "Reference previous interaction",
                    "Keep it brief",
                    "End with clear call-to-action",
                ],
            },
            "thank_you": {
                "subject": "Thank You - [Position] Interview",
                "body": "Template for post-interview thank you...",
                "when_to_use": "Within 24 hours of interview",
                "tips": [
                    "Send within 24 hours",
                    "Reference specific discussion points",
                    "Reaffirm your interest",
                    "Keep it concise",
                ],
            },
        }

        return templates

    def analyze_email_effectiveness(self, email_text: str) -> Dict[str, Any]:
        """Analyze email for effectiveness."""

        word_count = len(email_text.split())
        char_count = len(email_text)

        # Check for key elements
        has_greeting = any(
            greeting in email_text.lower() for greeting in ["dear", "hi", "hello"]
        )
        has_closing = any(
            closing in email_text.lower()
            for closing in ["regards", "best", "sincerely", "thanks"]
        )
        has_call_to_action = "?" in email_text

        # Calculate score
        score = 0
        feedback = []

        if 50 <= word_count <= 200:
            score += 30
            feedback.append("✅ Good length (50-200 words)")
        elif word_count < 50:
            feedback.append("⚠️ Too short - add more context")
        else:
            feedback.append("⚠️ Too long - keep under 200 words")

        if has_greeting:
            score += 20
            feedback.append("✅ Has greeting")
        else:
            feedback.append("❌ Missing greeting")

        if has_closing:
            score += 20
            feedback.append("✅ Has closing")
        else:
            feedback.append("❌ Missing closing")

        if has_call_to_action:
            score += 30
            feedback.append("✅ Has call-to-action")
        else:
            feedback.append("❌ Missing call-to-action")

        # Check for personalization
        if "[" not in email_text and "]" not in email_text:
            feedback.append("✅ No placeholders left")
        else:
            feedback.append("⚠️ Replace placeholders with real information")

        return {
            "score": score,
            "word_count": word_count,
            "char_count": char_count,
            "feedback": feedback,
            "rating": "Excellent"
            if score >= 80
            else "Good"
            if score >= 60
            else "Needs Improvement",
        }
