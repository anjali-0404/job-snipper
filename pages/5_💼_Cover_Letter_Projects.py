"""
Cover Letter Generation & Project Suggestions Page
Generate tailored cover letters and get project recommendations.
"""

import streamlit as st
import os
import sys
import json
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.color_scheme import get_unified_css
from agents.coverletter_agent import generate_cover_letter
from agents.project_agent import suggest_projects
from dotenv import load_dotenv

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Cover Letter & Projects - ResumeMasterAI", page_icon="💼", layout="wide"
)

# Apply unified color scheme
st.markdown(get_unified_css(), unsafe_allow_html=True)

# Initialize session state
if "parsed" not in st.session_state:
    st.session_state.parsed = None
if "cover_letter" not in st.session_state:
    st.session_state.cover_letter = None
if "projects" not in st.session_state:
    st.session_state.projects = None
if "jd_for_cl" not in st.session_state:
    st.session_state.jd_for_cl = ""

# Header
st.markdown("# 💼 Cover Letter & Project Suggestions")

# Check if resume is parsed
if not st.session_state.parsed:
    st.warning("⚠️ Please upload and parse a resume first!")
    if st.button("📄 Go to Upload Page"):
        st.switch_page("pages/1_📄_Upload_Resume.py")
    st.stop()

# Tabs for two features
tab1, tab2 = st.tabs(["📝 Cover Letter Generator", "🚀 Project Suggestions"])

# TAB 1: Cover Letter Generator
with tab1:
    st.markdown(
        """
    <div class="custom-card">
        <p style="font-size: 1.1rem; color: #4F5D75;">
            Create a personalized cover letter tailored to a specific job. 
            Our AI analyzes your resume and the job description to craft a compelling narrative.
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Job details input
    st.markdown("## 📋 Job Details")

    col1, col2 = st.columns(2)

    with col1:
        company_name = st.text_input(
            "Company Name",
            placeholder="e.g., Google, Microsoft, Amazon",
            help="The company you're applying to",
        )

    with col2:
        job_title = st.text_input(
            "Job Title",
            placeholder="e.g., Senior Software Engineer",
            help="The position you're applying for",
        )

    job_description = st.text_area(
        "Job Description (Optional but recommended)",
        value=st.session_state.jd_for_cl,
        height=200,
        placeholder="Paste the job description here for a more tailored cover letter...",
        help="Including the job description helps generate a more targeted cover letter",
    )

    st.session_state.jd_for_cl = job_description

    # Additional preferences
    with st.expander("⚙️ Advanced Options"):
        col1, col2 = st.columns(2)

        with col1:
            tone = st.selectbox(
                "Tone",
                ["Professional", "Enthusiastic", "Formal", "Creative"],
                help="The tone of your cover letter",
            )

        with col2:
            length = st.selectbox(
                "Length",
                [
                    "Concise (3 paragraphs)",
                    "Standard (4 paragraphs)",
                    "Detailed (5+ paragraphs)",
                ],
                help="Preferred cover letter length",
            )

        highlight_skills = st.text_input(
            "Skills to Highlight (comma-separated)",
            placeholder="e.g., Python, Leadership, Machine Learning",
            help="Specific skills you want to emphasize",
        )

    # Generate button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        can_generate = bool(company_name and job_title)
        if st.button(
            "✨ Generate Cover Letter",
            use_container_width=True,
            type="primary",
            disabled=not can_generate,
        ):
            with st.spinner("🤖 AI is crafting your cover letter..."):
                try:
                    # Build context
                    context = {
                        "company": company_name,
                        "position": job_title,
                        "job_description": job_description,
                        "tone": tone.lower(),
                        "highlight_skills": highlight_skills.split(",")
                        if highlight_skills
                        else [],
                    }

                    cover_letter = generate_cover_letter(
                        st.session_state.parsed, context
                    )
                    st.session_state.cover_letter = cover_letter
                    st.success("✅ Cover letter generated!")
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Error generating cover letter: {e}")

    if not can_generate:
        st.info(
            "👆 Please provide at least the company name and job title to generate a cover letter"
        )

    # Display cover letter if generated
    if st.session_state.cover_letter:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("## 📄 Your Cover Letter")

        # Editable text area
        edited_cl = st.text_area(
            "Cover Letter (Editable)",
            value=st.session_state.cover_letter,
            height=500,
            help="Feel free to edit the cover letter as needed",
            label_visibility="collapsed",
        )

        st.session_state.cover_letter = edited_cl

        # Download options
        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            st.download_button(
                label="📄 Download TXT",
                data=edited_cl,
                file_name=f"cover_letter_{company_name.replace(' ', '_')}_{timestamp}.txt",
                mime="text/plain",
                use_container_width=True,
            )

        with col2:
            st.download_button(
                label="📝 Download MD",
                data=edited_cl,
                file_name=f"cover_letter_{company_name.replace(' ', '_')}_{timestamp}.md",
                mime="text/markdown",
                use_container_width=True,
            )

        with col3:
            if st.button("📋 Copy Text", use_container_width=True):
                st.code(edited_cl, language=None)
                st.info("👆 Select and copy the text above")

        with col4:
            if st.button("🔄 Regenerate", use_container_width=True):
                st.session_state.cover_letter = None
                st.rerun()

        # Tips
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            """
        <div class="custom-card" style="background: #E8F5E9; border-left-color: #06A77D;">
            <h4>💡 Cover Letter Tips</h4>
            <ul style="line-height: 2; color: #4F5D75;">
                <li>Personalize the opening paragraph with why you're interested in this specific company</li>
                <li>Use specific examples from your experience that match job requirements</li>
                <li>Show enthusiasm and cultural fit</li>
                <li>Keep it concise - hiring managers spend ~30 seconds per cover letter</li>
                <li>Proofread carefully for typos and grammar errors</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

# TAB 2: Project Suggestions
with tab2:
    st.markdown(
        """
    <div class="custom-card">
        <p style="font-size: 1.1rem; color: #4F5D75;">
            Get personalized project suggestions to enhance your skills and fill gaps in your resume. 
            Perfect for building a strong portfolio!
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Get missing skills from matching if available
    missing_skills = []
    if st.session_state.get("match_info"):
        missing_skills = st.session_state.match_info.get("missing_skills", [])

    if missing_skills:
        st.markdown("## 🎯 Based on Your Skill Gaps")
        st.markdown(
            f"""
        <div class="custom-card" style="background: #E3F2FD;">
            <p style="color: #4F5D75;">
                We identified <strong>{len(missing_skills)}</strong> skills you could develop. 
                Click below to get project recommendations that will help you learn these skills.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    # Custom skill input
    st.markdown("## 🛠️ Skills to Develop")

    col1, col2 = st.columns([3, 1])

    with col1:
        custom_skills = st.text_input(
            "Skills you want to develop (comma-separated)",
            value=", ".join(missing_skills[:5]) if missing_skills else "",
            placeholder="e.g., React, Docker, Machine Learning, AWS",
            help="Enter skills you want to learn through projects",
        )

    with col2:
        num_projects = st.selectbox(
            "Number of Projects",
            [3, 5, 7, 10],
            index=1,
            help="How many project suggestions do you want?",
        )

    # Generate button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button(
            "🚀 Get Project Suggestions",
            use_container_width=True,
            type="primary",
            disabled=not custom_skills.strip(),
        ):
            with st.spinner("🤖 AI is generating project ideas..."):
                try:
                    skills_list = [
                        s.strip() for s in custom_skills.split(",") if s.strip()
                    ]
                    projects = suggest_projects(skills_list, num_projects)
                    st.session_state.projects = projects
                    st.success("✅ Projects generated!")
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Error generating projects: {e}")

    if not custom_skills.strip():
        st.info("👆 Enter skills you want to develop to get project suggestions")

    # Display projects if generated
    if st.session_state.projects:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("## 🎨 Recommended Projects")

        projects = (
            st.session_state.projects
            if isinstance(st.session_state.projects, list)
            else []
        )

        if not projects:
            st.warning("No projects generated. Try again with different skills.")
        else:
            for idx, project in enumerate(projects, 1):
                # Handle both dict and string formats
                if isinstance(project, dict):
                    title = project.get("title", f"Project {idx}")
                    description = project.get("description", "")
                    skills = project.get("skills", [])
                    difficulty = project.get("difficulty", "Intermediate")
                    duration = project.get("duration", "2-4 weeks")
                else:
                    # Fallback for string format
                    title = f"Project {idx}"
                    description = str(project)
                    skills = []
                    difficulty = "Intermediate"
                    duration = "2-4 weeks"

                # Difficulty badge color
                if difficulty.lower() == "beginner":
                    diff_color = "#06A77D"
                elif difficulty.lower() == "advanced":
                    diff_color = "#C73E1D"
                else:
                    diff_color = "#F18F01"

                st.markdown(
                    f"""
                <div class="custom-card" style="background: white; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-left: 4px solid #2E86AB;">
                    <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 1rem;">
                        <h3 style="color: #2D3142; margin: 0;">{idx}. {title}</h3>
                        <div style="display: flex; gap: 0.5rem;">
                            <span style="background: {diff_color}; color: white; padding: 0.25rem 0.75rem; border-radius: 12px; font-size: 0.85rem; font-weight: 600;">
                                {difficulty}
                            </span>
                            <span style="background: #E5E5E5; color: #4F5D75; padding: 0.25rem 0.75rem; border-radius: 12px; font-size: 0.85rem; font-weight: 600;">
                                ⏱️ {duration}
                            </span>
                        </div>
                    </div>
                    <p style="color: #4F5D75; line-height: 1.8; margin-bottom: 1rem;">
                        {description}
                    </p>
                    <div style="margin-top: 1rem;">
                        <strong style="color: #2E86AB;">Skills You'll Learn:</strong><br>
                        <div style="margin-top: 0.5rem;">
                            {"".join([f'<span style="display: inline-block; background: linear-gradient(135deg, #2E86AB 0%, #06A77D 100%); color: white; padding: 0.3rem 0.7rem; margin: 0.25rem; border-radius: 12px; font-size: 0.85rem;">{skill}</span>' for skill in skills]) if skills else '<span style="color: #999;">Skills not specified</span>'}
                        </div>
                    </div>
                </div>
                <br>
                """,
                    unsafe_allow_html=True,
                )

            # Download projects as JSON
            st.markdown("<br>", unsafe_allow_html=True)

            col1, col2, col3 = st.columns([1, 1, 1])

            with col1:
                projects_json = json.dumps(projects, indent=2)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                st.download_button(
                    label="📥 Download Projects (JSON)",
                    data=projects_json,
                    file_name=f"project_suggestions_{timestamp}.json",
                    mime="application/json",
                    use_container_width=True,
                )

            with col2:
                if st.button("🔄 Generate New Projects", use_container_width=True):
                    st.session_state.projects = None
                    st.rerun()

            with col3:
                if st.button(
                    "Next: Job Search →", use_container_width=True, type="primary"
                ):
                    st.switch_page("pages/6_🔍_Job_Search.py")

            # Implementation tips
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(
                """
            <div class="custom-card" style="background: #FFF3E0; border-left-color: #F18F01;">
                <h4>📌 Project Implementation Tips</h4>
                <ul style="line-height: 2; color: #4F5D75;">
                    <li><strong>Start small:</strong> Begin with the beginner projects to build confidence</li>
                    <li><strong>Document well:</strong> Create a detailed README.md for each project</li>
                    <li><strong>Use version control:</strong> Push your code to GitHub with meaningful commits</li>
                    <li><strong>Deploy it:</strong> Host your projects online (Heroku, Netlify, Vercel, etc.)</li>
                    <li><strong>Write about it:</strong> Create a blog post explaining your implementation</li>
                    <li><strong>Add to resume:</strong> Include completed projects in your resume and portfolio</li>
                </ul>
            </div>
            """,
                unsafe_allow_html=True,
            )
    else:
        # Project ideas inspiration
        st.markdown("### 💡 Why Work on Projects?")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                """
            <div class="custom-card">
                <h4>🎯 Benefits</h4>
                <ul style="line-height: 2;">
                    <li>Demonstrate practical skills to employers</li>
                    <li>Fill skill gaps identified in job matching</li>
                    <li>Build a strong portfolio</li>
                    <li>Gain hands-on experience</li>
                    <li>Stand out from other candidates</li>
                </ul>
            </div>
            """,
                unsafe_allow_html=True,
            )

        with col2:
            st.markdown(
                """
            <div class="custom-card">
                <h4>🚀 Project Types We Suggest</h4>
                <ul style="line-height: 2;">
                    <li>Web applications and APIs</li>
                    <li>Data analysis and visualization</li>
                    <li>Machine learning models</li>
                    <li>Mobile apps</li>
                    <li>DevOps and infrastructure</li>
                    <li>Open source contributions</li>
                </ul>
            </div>
            """,
                unsafe_allow_html=True,
            )

# Progress indicator
st.markdown("---")
st.markdown(
    """
<div style="text-align: center; padding: 1rem;">
    <p style="color: #4F5D75; font-size: 0.9rem;">
        <strong>Step 5 of 6:</strong> Cover Letter & Project Suggestions
    </p>
    <div style="background: #E5E5E5; height: 6px; border-radius: 3px; overflow: hidden; max-width: 600px; margin: 0.5rem auto;">
        <div style="background: linear-gradient(90deg, #2E86AB 0%, #06A77D 100%); height: 100%; width: 83.33%;"></div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)
