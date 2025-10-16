from services.project_suggester import suggest_projects as _suggest_projects_service
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.llm_utils import get_llm, generate_text
from dotenv import load_dotenv

load_dotenv()


def suggest_projects(skills_list, num_projects=5):
    """
    Generate project suggestions for given skills using AI

    Args:
        skills_list: List of skills to create projects for
        num_projects: Number of project suggestions to generate

    Returns:
        List of project dictionaries with title, description, skills, difficulty, duration
    """
    try:
        if not skills_list:
            return []

        skills_str = ", ".join(skills_list)

        prompt = f"""
Generate {num_projects} unique and practical project ideas specifically using these technologies: {skills_str}

IMPORTANT RULES:
- Each project MUST use the technologies from this list: {skills_str}
- Projects should be creative, unique, and portfolio-worthy
- Make projects progressively challenging from beginner to advanced
- Focus on real-world applications that demonstrate mastery of these specific skills

For each project, provide:
1. Title: A clear, creative project name (not generic)
2. Description: 2-3 sentences explaining what to build, key features, and why it's valuable for a portfolio
3. Skills: List the specific technologies from the input list that will be used (you can combine multiple from: {skills_str})
4. Difficulty: Beginner, Intermediate, or Advanced
5. Duration: Estimated time to complete (e.g., "1-2 weeks", "3-4 weeks")

Format each project as:
PROJECT {{number}}
Title: {{title}}
Description: {{description}}
Skills: {{skill1}}, {{skill2}}, {{skill3}}
Difficulty: {{level}}
Duration: {{time}}

EXAMPLE FORMAT:
PROJECT 1
Title: Real-time Collaborative Code Editor
Description: Build a web-based code editor where multiple users can edit code simultaneously with syntax highlighting and live cursors. Include user authentication, room management, and code execution features. Perfect for demonstrating real-time communication and full-stack skills.
Skills: React, Node.js, Socket.io, MongoDB
Difficulty: Advanced
Duration: 3-4 weeks

Now generate {num_projects} unique projects using ONLY these technologies: {skills_str}
"""

        llm = get_llm()
        if llm.is_available():
            # Use multi-model LLM with automatic fallback
            response_text = generate_text(prompt, temperature=0.8, max_tokens=3000)
            # Parse the response into structured projects
            projects = _parse_project_response(response_text, skills_list)
            
            # Validate that projects were generated
            if projects and len(projects) > 0:
                return projects
            else:
                raise Exception("No projects generated from AI response")
        else:
            raise Exception("LLM not available. Please configure your API key.")

    except Exception as e:
        print(f"Project suggestion failed: {e}")
        # Return error message instead of fallback
        return [{
            "title": "⚠️ AI Configuration Required",
            "description": f"Unable to generate custom projects. Error: {str(e)}. Please ensure your AI API key is configured in the settings.",
            "skills": skills_list,
            "difficulty": "N/A",
            "duration": "N/A"
        }]


def _parse_project_response(response_text, skills_list):
    """Parse AI response into structured project dictionaries"""
    projects = []
    current_project = {}

    for line in response_text.split("\n"):
        line = line.strip()
        if line.startswith("Title:"):
            if current_project and "title" in current_project:
                projects.append(current_project)
            current_project = {"title": line.replace("Title:", "").strip()}
        elif line.startswith("Description:"):
            current_project["description"] = line.replace("Description:", "").strip()
        elif line.startswith("Skills:"):
            skills = line.replace("Skills:", "").strip().split(",")
            current_project["skills"] = [s.strip() for s in skills]
        elif line.startswith("Difficulty:"):
            current_project["difficulty"] = line.replace("Difficulty:", "").strip()
        elif line.startswith("Duration:"):
            current_project["duration"] = line.replace("Duration:", "").strip()

    # Add last project
    if current_project and "title" in current_project:
        projects.append(current_project)

    # Ensure all projects have required fields
    for p in projects:
        p.setdefault("title", "Untitled Project")
        p.setdefault("description", "No description available")
        p.setdefault("skills", skills_list[:3])
        p.setdefault("difficulty", "Intermediate")
        p.setdefault("duration", "2-4 weeks")

    return projects


def suggest_projects_agent(parsed_resume, missing_skills):
    """
    Legacy function for backward compatibility
    Suggest projects to improve skill gaps
    """
    try:
        return _suggest_projects_service(parsed_resume, missing_skills)
    except Exception as e:
        print(f"Project agent failed: {e}")
        return []
