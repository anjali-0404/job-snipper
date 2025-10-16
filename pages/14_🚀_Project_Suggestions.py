"""
Project Suggestions Page
Generate projects to fill skill gaps and build your portfolio.
"""

import streamlit as st
import os
import sys
import json
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.color_scheme import get_unified_css
from agents.project_agent import suggest_projects
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Project Suggestions - ResumeMasterAI", page_icon="🚀", layout="wide")

st.markdown(get_unified_css(), unsafe_allow_html=True)

# Ensure parsed resume exists
if "parsed" not in st.session_state or not st.session_state.parsed:
    st.warning("⚠️ Please upload and parse a resume first!")
    if st.button("📄 Go to Upload Page"):
        st.switch_page("pages/1_📄_Upload_Resume.py")
    st.stop()

# Header
st.markdown("# 🚀 Project Suggestions")
st.markdown(
    "<div class=\"custom-card\"><p style=\"font-size:1.05rem;color:#4F5D75;\">Get personalized project ideas to fill skill gaps and strengthen your portfolio.</p></div>",
    unsafe_allow_html=True,
)

# Get missing skills if available
missing_skills = []
if st.session_state.get("match_info"):
    missing_skills = st.session_state.match_info.get("missing_skills", [])

st.markdown("## 🛠️ Skills to Build Projects Around")
col1, col2 = st.columns([3, 1])
with col1:
    skills_input = st.text_input(
        "Skills (comma-separated)",
        value=", ".join(missing_skills[:8]) if missing_skills else ", ".join(st.session_state.parsed.get("skills", [])[:8]),
        placeholder="e.g., React, Docker, Machine Learning",
    )
with col2:
    num_projects = st.selectbox("Number of Projects", [3, 5, 7, 10], index=1)

if st.button("🚀 Get Project Suggestions", use_container_width=True):
    skills_list = [s.strip() for s in skills_input.split(",") if s.strip()]
    if not skills_list:
        st.warning("Please enter at least one skill to generate project suggestions.")
    else:
        with st.spinner("Generating project suggestions..."):
            try:
                projects = suggest_projects(skills_list, num_projects)
                st.session_state.projects = projects
                st.success("✅ Projects generated!")
            except Exception as e:
                st.error(f"Error generating projects: {e}")

# Display suggested projects
if st.session_state.get("projects"):
    st.markdown("<br>", unsafe_allow_html=True)
    for idx, project in enumerate(st.session_state.projects, 1):
        title = project.get("title", f"Project {idx}") if isinstance(project, dict) else f"Project {idx}"
        description = project.get("description", "") if isinstance(project, dict) else str(project)
        skills = project.get("skills", []) if isinstance(project, dict) else []
        difficulty = project.get("difficulty", "Intermediate") if isinstance(project, dict) else "Intermediate"
        duration = project.get("duration", "2-4 weeks") if isinstance(project, dict) else "2-4 weeks"

        diff_color = "#F18F01"
        if difficulty.lower() == "beginner":
            diff_color = "#06A77D"
        elif difficulty.lower() == "advanced":
            diff_color = "#C73E1D"

        st.markdown(
            f"""
        <div class="custom-card" style="background: white; box-shadow: 0 4px 12px rgba(0,0,0,0.05); border-left: 4px solid #2E86AB; padding: 1rem;">
            <div style="display:flex; justify-content: space-between; align-items: start;">
                <h4 style="margin:0; color:#2D3142;">{idx}. {title}</h4>
                <div style="display:flex; gap:0.5rem;">
                    <span style="background: {diff_color}; color: white; padding: 0.25rem 0.6rem; border-radius: 10px; font-size:0.85rem; font-weight:600;">{difficulty}</span>
                    <span style="background: #E5E5E5; color: #4F5D75; padding: 0.25rem 0.6rem; border-radius: 10px; font-size:0.85rem; font-weight:600;">⏱️ {duration}</span>
                </div>
            </div>
            <p style="color:#4F5D75; margin-top:0.5rem;">{description}</p>
            <div style="margin-top:0.5rem;">
                <strong style="color:#2E86AB;">Skills:</strong>
                <div style="margin-top:0.5rem;">{' '.join([f'<span style="display:inline-block; background: linear-gradient(135deg, #2E86AB 0%, #06A77D 100%); color: white; padding: 0.25rem 0.5rem; margin:0.2rem; border-radius:8px; font-size:0.85rem;">{s}</span>' for s in skills]) if skills else '<span style="color:#999;">Skills not specified</span>'}</div>
            </div>
        </div>
        <br>
        """,
            unsafe_allow_html=True,
        )

    # actions
    col1d, col2d, col3d = st.columns([1, 1, 1])
    with col1d:
        pj_json = json.dumps(st.session_state.projects, indent=2)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        st.download_button(
            label="📥 Download Projects (JSON)",
            data=pj_json,
            file_name=f"project_suggestions_{timestamp}.json",
            mime="application/json",
            use_container_width=True,
        )

    with col2d:
        if st.button("🔄 Regenerate Projects", use_container_width=True):
            st.session_state.projects = None
            st.rerun()

    with col3d:
        if st.button("➡️ Continue to Job Search", use_container_width=True, type="primary"):
            st.switch_page("pages/6_🔍_Job_Search.py")

# Progress indicator
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1rem;">
    <p style="color: #4F5D75; font-size: 0.9rem;">
        <strong>Step 5 of 6:</strong> Project Suggestions
    </p>
    <div style="background: #E5E5E5; height: 6px; border-radius: 3px; overflow: hidden; max-width: 600px; margin: 0.5rem auto;">
        <div style="background: linear-gradient(90deg, #2E86AB 0%, #06A77D 100%); height: 100%; width: 83.33%;"></div>
    </div>
</div>
""", unsafe_allow_html=True)
