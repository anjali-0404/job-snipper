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
Generate {num_projects} practical project ideas that will help someone learn and demonstrate these skills: {skills_str}

For each project, provide:
1. Title: A clear, concise project name
2. Description: 2-3 sentences explaining what to build and why it's valuable
3. Skills: List the specific technologies/skills used (from the input skills and related ones)
4. Difficulty: Beginner, Intermediate, or Advanced
5. Duration: Estimated time to complete (e.g., "1-2 weeks", "3-4 weeks")

Format each project as:
PROJECT {{number}}
Title: {{title}}
Description: {{description}}
Skills: {{skill1}}, {{skill2}}, {{skill3}}
Difficulty: {{level}}
Duration: {{time}}

Make projects practical, portfolio-worthy, and progressively challenging.
"""

        llm = get_llm()
        if llm.is_available():
            # Use multi-model LLM with automatic fallback
            response_text = generate_text(prompt, temperature=0.7, max_tokens=2048)
            # Parse the response into structured projects
            projects = _parse_project_response(response_text, skills_list)
            return projects
        else:
            # Fallback when no LLM is available
            return _generate_fallback_projects(skills_list, num_projects)

    except Exception as e:
        print(f"Project suggestion failed: {e}")
        return _generate_fallback_projects(skills_list, num_projects)


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


def _generate_fallback_projects(skills_list, num_projects):
    """Generate simple project suggestions without AI"""
    # Map project templates with their ACTUAL required skills
    project_templates = [
        {
            "title": "Portfolio Website with {skill}",
            "description": "Build a personal portfolio website showcasing your projects and skills using {skill}. Include responsive design, contact form, and project gallery.",
            "difficulty": "Beginner",
            "duration": "1-2 weeks",
            "required_skills": [
                "HTML",
                "CSS",
                "JavaScript",
                "React",
                "Vue",
                "Angular",
                "Next.js",
            ],
        },
        {
            "title": "Task Management App using {skill}",
            "description": "Create a full-stack task management application with user authentication, CRUD operations, and real-time updates using {skill}.",
            "difficulty": "Intermediate",
            "duration": "2-3 weeks",
            "required_skills": [
                "React",
                "Node.js",
                "Express",
                "MongoDB",
                "PostgreSQL",
                "REST API",
                "Authentication",
            ],
        },
        {
            "title": "Data Dashboard with {skill}",
            "description": "Build an interactive data visualization dashboard that fetches, processes, and displays data using {skill}. Include charts, filters, and export functionality.",
            "difficulty": "Intermediate",
            "duration": "2-4 weeks",
            "required_skills": [
                "Python",
                "Pandas",
                "Matplotlib",
                "Seaborn",
                "Plotly",
                "D3.js",
                "Tableau",
                "Power BI",
            ],
        },
        {
            "title": "E-commerce Platform using {skill}",
            "description": "Develop a complete e-commerce solution with product catalog, shopping cart, payment integration, and order management using {skill}.",
            "difficulty": "Advanced",
            "duration": "4-6 weeks",
            "required_skills": [
                "React",
                "Node.js",
                "Payment Gateway",
                "Stripe",
                "Database",
                "AWS",
                "Docker",
            ],
        },
        {
            "title": "Real-time Chat Application with {skill}",
            "description": "Build a real-time messaging application with WebSocket support, user presence, typing indicators, and message history using {skill}.",
            "difficulty": "Advanced",
            "duration": "3-5 weeks",
            "required_skills": [
                "WebSocket",
                "Socket.io",
                "Node.js",
                "Express",
                "Docker",
                "Redis",
                "MongoDB",
            ],
        },
    ]

def _generate_fallback_projects(skills_list, num_projects):
    """Generate simple project suggestions without AI"""
    # Map project templates with their ACTUAL required skills
    project_templates = [
        {
            "title": "Portfolio Website with {skill}",
            "description": "Build a personal portfolio website showcasing your projects and skills using {skill}. Include responsive design, contact form, and project gallery.",
            "difficulty": "Beginner",
            "duration": "1-2 weeks",
            "required_skills": [
                "HTML",
                "CSS",
                "JavaScript",
                "React",
                "Vue",
                "Angular",
                "Next.js",
            ],
        },
        {
            "title": "Task Management App using {skill}",
            "description": "Create a full-stack task management application with user authentication, CRUD operations, and real-time updates using {skill}.",
            "difficulty": "Intermediate",
            "duration": "2-3 weeks",
            "required_skills": [
                "React",
                "Node.js",
                "Express",
                "MongoDB",
                "PostgreSQL",
                "REST API",
                "Authentication",
            ],
        },
        {
            "title": "Data Dashboard with {skill}",
            "description": "Build an interactive data visualization dashboard that fetches, processes, and displays data using {skill}. Include charts, filters, and export functionality.",
            "difficulty": "Intermediate",
            "duration": "2-4 weeks",
            "required_skills": [
                "Python",
                "Pandas",
                "Matplotlib",
                "Seaborn",
                "Plotly",
                "D3.js",
                "Tableau",
                "Power BI",
            ],
        },
        {
            "title": "E-commerce Platform using {skill}",
            "description": "Develop a complete e-commerce solution with product catalog, shopping cart, payment integration, and order management using {skill}.",
            "difficulty": "Advanced",
            "duration": "4-6 weeks",
            "required_skills": [
                "React",
                "Node.js",
                "Payment Gateway",
                "Stripe",
                "Database",
                "AWS",
                "Docker",
            ],
        },
        {
            "title": "Real-time Chat Application with {skill}",
            "description": "Build a real-time messaging application with WebSocket support, user presence, typing indicators, and message history using {skill}.",
            "difficulty": "Advanced",
            "duration": "3-5 weeks",
            "required_skills": [
                "WebSocket",
                "Socket.io",
                "Node.js",
                "Express",
                "Docker",
                "Redis",
                "MongoDB",
            ],
        },
        {
            "title": "Machine Learning Model with {skill}",
            "description": "Develop a machine learning model for prediction or classification tasks using {skill}. Include data preprocessing, model training, and evaluation metrics.",
            "difficulty": "Advanced",
            "duration": "3-6 weeks",
            "required_skills": [
                "Python",
                "TensorFlow",
                "PyTorch",
                "Scikit-learn",
                "Keras",
                "Machine Learning",
                "Data Science",
            ],
        },
        {
            "title": "Mobile App with {skill}",
            "description": "Create a mobile application with user interface, local data storage, and API integration using {skill}.",
            "difficulty": "Intermediate",
            "duration": "2-4 weeks",
            "required_skills": [
                "React Native",
                "Flutter",
                "Swift",
                "Kotlin",
                "Android",
                "iOS",
            ],
        },
        {
            "title": "API Gateway/Microservices with {skill}",
            "description": "Build a scalable microservices architecture with API gateway, service discovery, and containerization using {skill}.",
            "difficulty": "Advanced",
            "duration": "3-5 weeks",
            "required_skills": [
                "Docker",
                "Kubernetes",
                "Node.js",
                "Go",
                "Java",
                "Spring Boot",
                "Microservices",
            ],
        },
        {
            "title": "Cloud Infrastructure Project with {skill}",
            "description": "Design and deploy a cloud-based infrastructure with load balancing, auto-scaling, and monitoring using {skill}.",
            "difficulty": "Advanced",
            "duration": "2-4 weeks",
            "required_skills": ["AWS", "Azure", "GCP", "Cloud", "Infrastructure", "DevOps"],
        },
        {
            "title": "Content Management System with {skill}",
            "description": "Build a CMS with user roles, content versioning, and publishing workflow using {skill}.",
            "difficulty": "Intermediate",
            "duration": "3-4 weeks",
            "required_skills": [
                "Node.js",
                "Express",
                "React",
                "PostgreSQL",
                "Authentication",
            ],
        },
    ]

    projects = []
    used_skills = set()  # Track used skills to avoid duplicates
    
    for i in range(min(num_projects, len(project_templates))):
        template = project_templates[i]

        # Find the best matching skill from user's list for this project type
        matching_skills = [
            s
            for s in skills_list
            if s.lower() in [req.lower() for req in template["required_skills"]]
        ]

        # Filter out already used skills to ensure variety
        unused_matching_skills = [s for s in matching_skills if s.lower() not in used_skills]
        
        if unused_matching_skills:
            # Use the first unused matching skill
            skill = unused_matching_skills[0]
            used_skills.add(skill.lower())
            # Get all matching skills for the project
            project_skills = (
                unused_matching_skills[:3] if len(unused_matching_skills) >= 3 else unused_matching_skills
            )
        elif matching_skills:
            # If all matching skills are used, use first matching skill anyway
            skill = matching_skills[0]
            # Get all matching skills for the project
            project_skills = (
                matching_skills[:3] if len(matching_skills) >= 3 else matching_skills
            )
        else:
            # If no match, use template's first required skill
            skill = template["required_skills"][0]
            # Use template's required skills
            project_skills = template["required_skills"][:3]

        project = {
            "title": template["title"].format(skill=skill),
            "description": template["description"].format(skill=skill),
            "skills": project_skills,
            "difficulty": template["difficulty"],
            "duration": template["duration"],
        }
        projects.append(project)

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
