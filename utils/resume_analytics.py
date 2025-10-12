"""
Advanced Resume Analytics
Provides keyword analysis, readability scoring, and improvement suggestions.
"""

import re
from collections import Counter


class ResumeAnalytics:
    """Comprehensive resume analysis tools"""

    # Common action verbs for resumes
    ACTION_VERBS = [
        "achieved",
        "improved",
        "trained",
        "managed",
        "created",
        "resolved",
        "volunteered",
        "influenced",
        "increased",
        "decreased",
        "developed",
        "designed",
        "implemented",
        "launched",
        "established",
        "optimized",
        "streamlined",
        "spearheaded",
        "orchestrated",
        "executed",
        "delivered",
        "generated",
        "led",
        "directed",
        "coordinated",
        "facilitated",
        "mentored",
        "trained",
        "supervised",
        "analyzed",
        "evaluated",
        "researched",
        "investigated",
        "built",
        "engineered",
        "architected",
        "programmed",
        "automated",
    ]

    # Weak words to avoid
    WEAK_WORDS = [
        "responsible for",
        "duties included",
        "worked on",
        "helped with",
        "assisted",
        "tried to",
        "various",
        "several",
        "many",
        "some",
        "few",
    ]

    # Technical skills by category
    TECH_SKILLS = {
        "programming": [
            "python",
            "java",
            "javascript",
            "c++",
            "c#",
            "ruby",
            "php",
            "swift",
            "kotlin",
            "go",
            "rust",
            "typescript",
            "scala",
        ],
        "web": [
            "html",
            "css",
            "react",
            "angular",
            "vue",
            "node.js",
            "express",
            "django",
            "flask",
            "spring",
            "asp.net",
        ],
        "database": [
            "sql",
            "mysql",
            "postgresql",
            "mongodb",
            "redis",
            "oracle",
            "nosql",
            "dynamodb",
        ],
        "cloud": [
            "aws",
            "azure",
            "gcp",
            "docker",
            "kubernetes",
            "terraform",
            "jenkins",
            "ci/cd",
        ],
        "data": [
            "machine learning",
            "data science",
            "pandas",
            "numpy",
            "tensorflow",
            "pytorch",
            "scikit-learn",
            "tableau",
            "power bi",
        ],
    }

    def __init__(self, text):
        """Initialize with resume text"""
        self.text = text
        self.text_lower = text.lower()
        self.words = re.findall(r"\b[a-z]+\b", self.text_lower)
        self.sentences = re.split(r"[.!?]+", text)

    def keyword_density_analysis(self, top_n=20):
        """
        Analyze keyword density and frequency
        Returns top keywords with their counts and percentages
        """
        # Remove common stop words
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
            "were",
            "been",
            "be",
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
            "can",
            "this",
            "that",
            "these",
            "those",
        }

        # Filter words
        filtered_words = [w for w in self.words if w not in stop_words and len(w) > 3]

        # Count frequency
        word_counts = Counter(filtered_words)

        # Calculate percentages
        total_words = len(filtered_words)
        keyword_data = []

        for word, count in word_counts.most_common(top_n):
            percentage = (count / total_words) * 100
            keyword_data.append(
                {"keyword": word, "count": count, "percentage": percentage}
            )

        return keyword_data

    def action_verb_analysis(self):
        """
        Analyze usage of strong action verbs
        Returns statistics and suggestions
        """
        found_verbs = []
        for verb in self.ACTION_VERBS:
            if verb in self.text_lower:
                count = self.text_lower.count(verb)
                found_verbs.append({"verb": verb, "count": count})

        # Sort by count
        found_verbs.sort(key=lambda x: x["count"], reverse=True)

        # Calculate action verb density
        total_sentences = len([s for s in self.sentences if s.strip()])
        action_verb_count = sum(v["count"] for v in found_verbs)
        density = (
            (action_verb_count / total_sentences * 100) if total_sentences > 0 else 0
        )

        return {
            "found_verbs": found_verbs,
            "total_action_verbs": action_verb_count,
            "unique_action_verbs": len(found_verbs),
            "density_percentage": density,
            "suggested_verbs": [
                v
                for v in self.ACTION_VERBS
                if v not in [fv["verb"] for fv in found_verbs]
            ][:10],
        }

    def weak_phrases_detection(self):
        """
        Detect weak phrases that should be replaced
        Returns list of weak phrases found with suggestions
        """
        found_weak = []
        for weak in self.WEAK_WORDS:
            if weak in self.text_lower:
                # Find context (sentence containing the weak phrase)
                for sentence in self.sentences:
                    if weak in sentence.lower():
                        found_weak.append(
                            {
                                "phrase": weak,
                                "context": sentence.strip()[:100] + "...",
                                "suggestion": self._suggest_replacement(weak),
                            }
                        )
                        break

        return found_weak

    def _suggest_replacement(self, weak_phrase):
        """Suggest replacement for weak phrases"""
        replacements = {
            "responsible for": "Managed, Led, Oversaw, Directed",
            "duties included": "Achieved, Executed, Delivered",
            "worked on": "Developed, Built, Created, Implemented",
            "helped with": "Contributed to, Supported, Facilitated",
            "assisted": "Collaborated with, Partnered with, Supported",
        }
        return replacements.get(weak_phrase, "Use a strong action verb")

    def quantifiable_achievements_analysis(self):
        """
        Identify quantifiable achievements (numbers, percentages, metrics)
        Returns statistics and suggestions
        """
        # Find numbers and metrics
        numbers = re.findall(r"\d+[%\+\-]?", self.text)
        percentages = re.findall(r"\d+%", self.text)
        currency = re.findall(r"[\$€£]\d+[KMB]?", self.text)
        time_periods = re.findall(
            r"\d+\s*(?:years?|months?|weeks?|days?)", self.text_lower
        )
        team_sizes = re.findall(
            r"\d+\s*(?:people|team|members|employees|users|customers)", self.text_lower
        )

        total_metrics = (
            len(numbers)
            + len(percentages)
            + len(currency)
            + len(time_periods)
            + len(team_sizes)
        )

        # Calculate density
        total_sentences = len([s for s in self.sentences if s.strip()])
        metrics_per_sentence = (
            total_metrics / total_sentences if total_sentences > 0 else 0
        )

        return {
            "total_metrics": total_metrics,
            "numbers": numbers,
            "percentages": percentages,
            "currency": currency,
            "time_periods": time_periods,
            "team_sizes": team_sizes,
            "metrics_per_sentence": metrics_per_sentence,
            "has_good_quantification": total_metrics >= 5,
        }

    def readability_score(self):
        """
        Calculate Flesch Reading Ease score
        Higher score = easier to read (60-70 is optimal for resumes)
        """

        # Count syllables (approximation)
        def count_syllables(word):
            word = word.lower()
            vowels = "aeiouy"
            syllable_count = 0
            previous_was_vowel = False

            for char in word:
                is_vowel = char in vowels
                if is_vowel and not previous_was_vowel:
                    syllable_count += 1
                previous_was_vowel = is_vowel

            # Adjust for silent e
            if word.endswith("e"):
                syllable_count -= 1

            # Every word has at least one syllable
            if syllable_count == 0:
                syllable_count = 1

            return syllable_count

        # Calculate metrics
        total_sentences = len([s for s in self.sentences if s.strip()])
        total_words = len(self.words)
        total_syllables = sum(count_syllables(word) for word in self.words)

        if total_sentences == 0 or total_words == 0:
            return {
                "score": 0,
                "grade_level": "N/A",
                "interpretation": "Insufficient text",
            }

        # Flesch Reading Ease formula
        avg_sentence_length = total_words / total_sentences
        avg_syllables_per_word = total_syllables / total_words

        flesch_score = (
            206.835 - (1.015 * avg_sentence_length) - (84.6 * avg_syllables_per_word)
        )

        # Flesch-Kincaid Grade Level
        grade_level = 0.39 * avg_sentence_length + 11.8 * avg_syllables_per_word - 15.59

        # Interpretation
        if flesch_score >= 80:
            interpretation = "Very Easy"
        elif flesch_score >= 70:
            interpretation = "Easy"
        elif flesch_score >= 60:
            interpretation = "Standard (Ideal for resumes)"
        elif flesch_score >= 50:
            interpretation = "Fairly Difficult"
        elif flesch_score >= 30:
            interpretation = "Difficult"
        else:
            interpretation = "Very Difficult"

        return {
            "score": round(flesch_score, 1),
            "grade_level": round(grade_level, 1),
            "interpretation": interpretation,
            "avg_sentence_length": round(avg_sentence_length, 1),
            "avg_syllables_per_word": round(avg_syllables_per_word, 2),
            "total_words": total_words,
            "total_sentences": total_sentences,
        }

    def technical_skills_analysis(self):
        """
        Identify technical skills mentioned in resume
        Returns categorized skills found
        """
        found_skills = {}

        for category, skills in self.TECH_SKILLS.items():
            found_in_category = []
            for skill in skills:
                if skill in self.text_lower:
                    found_in_category.append(skill)

            if found_in_category:
                found_skills[category] = found_in_category

        total_skills = sum(len(skills) for skills in found_skills.values())

        return {
            "found_skills": found_skills,
            "total_skills": total_skills,
            "categories_covered": len(found_skills),
        }

    def resume_length_analysis(self):
        """
        Analyze resume length and provide recommendations
        """
        word_count = len(self.text.split())
        char_count = len(self.text)
        line_count = len(self.text.split("\n"))

        # Estimate pages (rough estimate: 500 words per page)
        estimated_pages = word_count / 500

        # Recommendations based on word count
        if word_count < 300:
            recommendation = (
                "Too short - Add more details about achievements and experience"
            )
            status = "short"
        elif 300 <= word_count < 400:
            recommendation = (
                "On the short side - Consider adding more quantifiable achievements"
            )
            status = "slightly_short"
        elif 400 <= word_count <= 800:
            recommendation = "Ideal length - Well balanced for ATS and human readers"
            status = "optimal"
        elif 800 < word_count <= 1000:
            recommendation = "Slightly long - Consider condensing some sections"
            status = "slightly_long"
        else:
            recommendation = "Too long - Trim to most relevant and impactful content"
            status = "long"

        return {
            "word_count": word_count,
            "char_count": char_count,
            "line_count": line_count,
            "estimated_pages": round(estimated_pages, 1),
            "status": status,
            "recommendation": recommendation,
        }

    def comprehensive_analysis(self):
        """
        Run all analyses and return comprehensive report
        """
        return {
            "keywords": self.keyword_density_analysis(),
            "action_verbs": self.action_verb_analysis(),
            "weak_phrases": self.weak_phrases_detection(),
            "quantifiable": self.quantifiable_achievements_analysis(),
            "readability": self.readability_score(),
            "technical_skills": self.technical_skills_analysis(),
            "length": self.resume_length_analysis(),
        }


def generate_improvement_score(analytics):
    """
    Generate an overall improvement score based on analytics
    Returns score out of 100 and breakdown
    """
    score = 0
    breakdown = []

    # Action verbs (20 points)
    action_verb_score = min(analytics["action_verbs"]["density_percentage"] / 2, 20)
    score += action_verb_score
    breakdown.append(f"Action Verbs: {action_verb_score:.0f}/20")

    # Quantifiable achievements (25 points)
    metrics_count = analytics["quantifiable"]["total_metrics"]
    quant_score = min((metrics_count / 10) * 25, 25)
    score += quant_score
    breakdown.append(f"Quantifiable Metrics: {quant_score:.0f}/25")

    # Readability (15 points)
    readability = analytics["readability"]["score"]
    if 60 <= readability <= 70:
        read_score = 15
    elif 50 <= readability < 60 or 70 < readability <= 80:
        read_score = 12
    elif 40 <= readability < 50 or 80 < readability <= 90:
        read_score = 8
    else:
        read_score = 5
    score += read_score
    breakdown.append(f"Readability: {read_score}/15")

    # Resume length (15 points)
    length_status = analytics["length"]["status"]
    if length_status == "optimal":
        length_score = 15
    elif length_status in ["slightly_short", "slightly_long"]:
        length_score = 12
    else:
        length_score = 8
    score += length_score
    breakdown.append(f"Length: {length_score}/15")

    # No weak phrases (15 points)
    weak_count = len(analytics["weak_phrases"])
    weak_score = max(15 - (weak_count * 3), 0)
    score += weak_score
    breakdown.append(f"Strong Language: {weak_score}/15")

    # Technical skills (10 points)
    tech_score = min(analytics["technical_skills"]["total_skills"], 10)
    score += tech_score
    breakdown.append(f"Technical Skills: {tech_score}/10")

    return {"score": round(score), "breakdown": breakdown}
