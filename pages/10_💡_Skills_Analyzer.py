"""
Skills Analyzer - Identify Skills Gaps & Growth Opportunities
Analyze your skills against industry standards and get personalized recommendations.
"""

import streamlit as st
import sys
from pathlib import Path
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from utils.skills_analyzer import SkillsAnalyzer
from utils.color_scheme import get_unified_css
from dotenv import load_dotenv

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Skills Analyzer - ResumeMasterAI", page_icon="💡", layout="wide"
)

# Apply unified CSS
st.markdown(get_unified_css(), unsafe_allow_html=True)

# Custom CSS
st.markdown(
    """
<style>
    .skill-card {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
    }
    
    .skill-level {
        display: inline-block;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: bold;
        margin: 0.25rem;
    }
    
    .level-expert {
        background: #10b981;
        color: white;
    }
    
    .level-advanced {
        background: #3b82f6;
        color: white;
    }
    
    .level-intermediate {
        background: #f59e0b;
        color: white;
    }
    
    .level-beginner {
        background: #ef4444;
        color: white;
    }
    
    .gap-alert {
        background: #fef3c7;
        border-left: 4px solid #f59e0b;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .recommendation-box {
        background: #f0f9ff;
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 4px solid #3b82f6;
        margin: 1rem 0;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Header
st.markdown("# 💡 Skills Analyzer")
st.markdown("### Identify gaps, get personalized learning paths, and stay competitive")

# Initialize session state
if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None

# Sidebar Configuration
with st.sidebar:
    st.header("⚙️ Analysis Settings")

    # Target Role
    st.subheader("🎯 Target Role")
    target_role = st.text_input(
        "Desired Job Title",
        placeholder="e.g., Senior Full Stack Developer",
        help="What role are you targeting?",
    )

    industry = st.selectbox(
        "Industry",
        [
            "Technology",
            "Finance",
            "Healthcare",
            "Consulting",
            "Marketing",
            "Sales",
            "Engineering",
            "Education",
        ],
    )

    # Current Level
    st.subheader("📊 Current Level")
    experience_level = st.select_slider(
        "Experience Level",
        options=["Entry", "Junior", "Mid-Level", "Senior", "Lead", "Expert"],
        value="Mid-Level",
    )

    years_experience = st.slider(
        "Years of Experience", min_value=0, max_value=30, value=5
    )

    # Analysis Focus
    st.subheader("🔍 Focus Areas")
    analyze_technical = st.checkbox("Technical Skills", value=True)
    analyze_soft = st.checkbox("Soft Skills", value=True)
    analyze_tools = st.checkbox("Tools & Technologies", value=True)
    analyze_certs = st.checkbox("Certifications", value=True)

# Main Content
tab1, tab2, tab3, tab4 = st.tabs(
    ["📝 Input", "📊 Analysis", "📈 Gaps", "🎯 Recommendations"]
)

with tab1:
    st.markdown("## 📝 Your Current Skills")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 💻 Technical Skills")
        current_tech_skills = st.text_area(
            "Current Technical Skills (comma-separated)",
            placeholder="Python, JavaScript, React, SQL, AWS...",
            height=150,
            help="List all your technical skills",
        )

        st.markdown("### 🎨 Soft Skills")
        current_soft_skills = st.text_area(
            "Current Soft Skills (comma-separated)",
            placeholder="Leadership, Communication, Problem-solving...",
            height=100,
        )

    with col2:
        st.markdown("### 🛠️ Tools & Technologies")
        current_tools = st.text_area(
            "Tools & Platforms (comma-separated)",
            placeholder="Git, Docker, Kubernetes, Jenkins, Jira...",
            height=150,
        )

        st.markdown("### 🏆 Certifications")
        current_certs = st.text_area(
            "Certifications (comma-separated)",
            placeholder="AWS Certified, PMP, CISSP...",
            height=100,
        )

    st.markdown("### 📄 Or Upload Your Resume")
    uploaded_file = st.file_uploader(
        "Upload resume (PDF, DOCX, TXT)",
        type=["pdf", "docx", "txt"],
        help="We'll extract skills automatically",
    )

    # Analyze Button
    if st.button("🔍 Analyze My Skills", type="primary", use_container_width=True):
        if not target_role:
            st.error("❌ Please enter a target role")
        elif not current_tech_skills and not uploaded_file:
            st.error("❌ Please enter your skills or upload a resume")
        else:
            with st.spinner("🤖 Analyzing your skills..."):
                try:
                    analyzer = SkillsAnalyzer()

                    # Prepare input
                    input_data = {
                        "target_role": target_role,
                        "industry": industry,
                        "experience_level": experience_level,
                        "years_experience": years_experience,
                        "current_skills": {
                            "technical": [
                                s.strip()
                                for s in current_tech_skills.split(",")
                                if s.strip()
                            ],
                            "soft": [
                                s.strip()
                                for s in current_soft_skills.split(",")
                                if s.strip()
                            ],
                            "tools": [
                                s.strip() for s in current_tools.split(",") if s.strip()
                            ],
                            "certifications": [
                                c.strip() for c in current_certs.split(",") if c.strip()
                            ],
                        },
                        "resume_file": uploaded_file,
                    }

                    # Perform analysis
                    result = analyzer.analyze(input_data)
                    st.session_state.analysis_result = result

                    st.success("✅ Analysis complete!")

                except Exception as e:
                    st.error(f"❌ Error analyzing skills: {str(e)}")

with tab2:
    st.markdown("## 📊 Skills Analysis")

    if st.session_state.analysis_result:
        result = st.session_state.analysis_result

        # Overall Score
        col1, col2, col3 = st.columns(3)

        with col1:
            overall_score = result.get("overall_score", 0)
            st.markdown(
                f"""
            <div class="skill-card">
                <h3>Overall Match</h3>
                <h1 style="font-size: 3rem;">{overall_score}%</h1>
                <p>Match to target role</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

        with col2:
            skills_count = result.get("skills_matched", 0)
            total_skills = result.get("total_required_skills", 0)
            st.markdown(
                f"""
            <div class="skill-card">
                <h3>Skills Matched</h3>
                <h1 style="font-size: 3rem;">{skills_count}/{total_skills}</h1>
                <p>Required skills covered</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

        with col3:
            readiness = result.get("role_readiness", "Moderate")
            color_map = {
                "Ready": "#10b981",
                "Almost Ready": "#3b82f6",
                "Moderate": "#f59e0b",
                "Needs Work": "#ef4444",
            }
            st.markdown(
                f"""
            <div class="skill-card">
                <h3>Role Readiness</h3>
                <h1 style="font-size: 2rem; color: {color_map.get(readiness, "#f59e0b")};">{readiness}</h1>
                <p>Current preparedness</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

        # Skills Breakdown
        st.markdown("### 📈 Skills Breakdown")

        categories = result.get("category_scores", {})
        if categories:
            fig = go.Figure()

            fig.add_trace(
                go.Scatterpolar(
                    r=list(categories.values()),
                    theta=list(categories.keys()),
                    fill="toself",
                    name="Your Skills",
                    line_color="#667eea",
                )
            )

            fig.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
                showlegend=True,
                height=500,
            )

            st.plotly_chart(fig, use_container_width=True)

        # Skills by Proficiency
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🌟 Your Strengths")
            strengths = result.get("strengths", [])
            for skill in strengths[:5]:
                st.markdown(
                    f"""
                <div class="recommendation-box">
                    <strong>{skill["name"]}</strong><br>
                    Level: <span class="skill-level level-expert">Expert</span><br>
                    <small>{skill.get("description", "")}</small>
                </div>
                """,
                    unsafe_allow_html=True,
                )

        with col2:
            st.markdown("### 📚 Skills to Develop")
            to_develop = result.get("skills_to_develop", [])
            for skill in to_develop[:5]:
                priority = skill.get("priority", "Medium")
                color = {"High": "#ef4444", "Medium": "#f59e0b", "Low": "#3b82f6"}.get(
                    priority, "#6b7280"
                )
                st.markdown(
                    f"""
                <div class="gap-alert">
                    <strong>{skill["name"]}</strong><br>
                    Priority: <span style="color: {color}; font-weight: bold;">{priority}</span><br>
                    <small>{skill.get("reason", "")}</small>
                </div>
                """,
                    unsafe_allow_html=True,
                )

    else:
        st.info("👈 Complete the analysis first to see your skills breakdown")

with tab3:
    st.markdown("## 📈 Skills Gap Analysis")

    if st.session_state.analysis_result:
        result = st.session_state.analysis_result

        # Gap Overview
        st.markdown("### 🎯 Gap Summary")

        gaps = result.get("skill_gaps", [])

        if gaps:
            # Create gap visualization
            gap_df = pd.DataFrame(gaps)

            fig = px.bar(
                gap_df,
                x="importance",
                y="skill",
                orientation="h",
                title="Skills Gap by Importance",
                color="priority",
                color_discrete_map={
                    "High": "#ef4444",
                    "Medium": "#f59e0b",
                    "Low": "#3b82f6",
                },
            )
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)

            # Detailed gaps
            st.markdown("### 📋 Detailed Gap Analysis")

            for gap in gaps:
                priority = gap.get("priority", "Medium")
                importance = gap.get("importance", 50)

                with st.expander(f"**{gap['skill']}** - {priority} Priority"):
                    col1, col2 = st.columns([2, 1])

                    with col1:
                        st.markdown(
                            f"**Why it matters:** {gap.get('reason', 'Important for role')}"
                        )
                        st.markdown(
                            f"**Current level:** {gap.get('current_level', 'None')}"
                        )
                        st.markdown(
                            f"**Target level:** {gap.get('target_level', 'Intermediate')}"
                        )

                    with col2:
                        st.metric("Importance", f"{importance}%")
                        st.progress(importance / 100)
        else:
            st.success(
                "🎉 No major skill gaps detected! You're well-prepared for the target role."
            )

        # Industry Comparison
        st.markdown("### 🌍 Industry Comparison")

        col1, col2, col3 = st.columns(3)

        with col1:
            industry_avg = result.get("industry_average_score", 70)
            your_score = result.get("overall_score", 0)
            diff = your_score - industry_avg
            st.metric("vs Industry Average", f"{your_score}%", f"{diff:+.1f}%")

        with col2:
            peer_avg = result.get("peer_average_score", 65)
            diff = your_score - peer_avg
            st.metric("vs Experience Peers", f"{your_score}%", f"{diff:+.1f}%")

        with col3:
            top_performers = result.get("top_performer_score", 90)
            diff = your_score - top_performers
            st.metric("vs Top Performers", f"{your_score}%", f"{diff:+.1f}%")

    else:
        st.info("👈 Complete the analysis first to see your skill gaps")

with tab4:
    st.markdown("## 🎯 Personalized Recommendations")

    if st.session_state.analysis_result:
        result = st.session_state.analysis_result

        # Learning Path
        st.markdown("### 📚 Your Learning Path")

        learning_path = result.get("learning_path", [])

        for idx, step in enumerate(learning_path, 1):
            with st.expander(
                f"**Step {idx}: {step['title']}** ({step.get('duration', '4-6 weeks')})"
            ):
                st.markdown(f"**Objective:** {step.get('objective', '')}")

                st.markdown("**Skills to develop:**")
                for skill in step.get("skills", []):
                    st.markdown(f"- {skill}")

                st.markdown("**Recommended resources:**")
                for resource in step.get("resources", []):
                    st.markdown(
                        f"- [{resource['name']}]({resource['url']}) - {resource['type']}"
                    )

                st.markdown(f"**Estimated time:** {step.get('duration', 'Varies')}")

        # Certifications
        st.markdown("### 🏆 Recommended Certifications")

        certifications = result.get("recommended_certifications", [])

        cols = st.columns(2)
        for idx, cert in enumerate(certifications):
            with cols[idx % 2]:
                st.markdown(
                    f"""
                <div class="recommendation-box">
                    <h4>{cert["name"]}</h4>
                    <p><strong>Provider:</strong> {cert.get("provider", "N/A")}</p>
                    <p><strong>Value:</strong> {cert.get("value", "Industry-recognized")}</p>
                    <p><strong>Cost:</strong> {cert.get("cost", "Varies")}</p>
                    <p><strong>Duration:</strong> {cert.get("duration", "3-6 months")}</p>
                </div>
                """,
                    unsafe_allow_html=True,
                )

        # Action Items
        st.markdown("### ✅ Action Items (Next 30 Days)")

        action_items = result.get("action_items", [])

        for item in action_items:
            priority = item.get("priority", "Medium")
            checkbox_key = f"action_{action_items.index(item)}"

            col1, col2 = st.columns([3, 1])
            with col1:
                st.checkbox(
                    f"**{item['title']}** - {item.get('description', '')}",
                    key=checkbox_key,
                )
            with col2:
                st.markdown(
                    f"<span style='color: {'#ef4444' if priority == 'High' else '#f59e0b'};'>{priority} Priority</span>",
                    unsafe_allow_html=True,
                )

        # Download Learning Plan
        st.markdown("---")
        if st.button("📥 Download Learning Plan", type="secondary"):
            # Generate downloadable plan
            plan_text = f"""
# Skills Development Plan
## Target Role: {result.get("target_role", "N/A")}

## Overall Assessment
- Match Score: {result.get("overall_score", 0)}%
- Role Readiness: {result.get("role_readiness", "N/A")}

## Skills Gaps
{chr(10).join(f"- {gap['skill']} ({gap['priority']} priority)" for gap in result.get("skill_gaps", []))}

## Learning Path
{chr(10).join(f"{idx}. {step['title']} - {step.get('duration', 'N/A')}" for idx, step in enumerate(learning_path, 1))}

## Recommended Certifications
{chr(10).join(f"- {cert['name']} ({cert.get('provider', 'N/A')})" for cert in certifications)}
            """

            st.download_button(
                label="Download as TXT",
                data=plan_text,
                file_name="learning_plan.txt",
                mime="text/plain",
            )

    else:
        st.info("👈 Complete the analysis first to get personalized recommendations")

# Resources
st.markdown("---")
st.markdown("## 📚 Learning Resources")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 🎓 Online Learning
    - Coursera
    - Udemy
    - LinkedIn Learning
    - Pluralsight
    - edX
    """)

with col2:
    st.markdown("""
    ### 💻 Practice Platforms
    - LeetCode
    - HackerRank
    - CodeWars
    - GitHub
    - Stack Overflow
    """)

with col3:
    st.markdown("""
    ### 📖 Communities
    - Dev.to
    - Reddit (r/learnprogramming)
    - Discord servers
    - Local meetups
    - Tech conferences
    """)

# Footer
st.markdown("---")
st.markdown(
    """
<div style='text-align: center; color: #6b7280;'>
    <p>💡 <strong>Tip:</strong> Focus on high-priority gaps first and practice consistently!</p>
</div>
""",
    unsafe_allow_html=True,
)
