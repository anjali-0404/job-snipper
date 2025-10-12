"""
Resume Upload & Parsing Page
Upload your resume and parse it into structured data.
"""

import streamlit as st
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.color_scheme import get_unified_css
from utils.ui_components import apply_custom_css, create_hero_section
from utils.file_utils import save_uploaded_file, detect_file_type
from agents.parser_agent import parse_resume
from dotenv import load_dotenv

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Upload Resume - ResumeMasterAI", page_icon="📄", layout="wide"
)

# Apply unified color scheme
st.markdown(get_unified_css(), unsafe_allow_html=True)

# Apply custom styling
apply_custom_css()

# Initialize session state
if "parsed" not in st.session_state:
    st.session_state.parsed = None
if "file_path" not in st.session_state:
    st.session_state.file_path = None
if "file_type" not in st.session_state:
    st.session_state.file_type = None

# Header
st.markdown("# 📄 Upload & Parse Your Resume")
st.markdown(
    """
<div class="custom-card">
    <p style="font-size: 1.1rem; color: #4F5D75;">
        Upload your resume in PDF or DOCX format. Our advanced AI will extract and structure 
        all relevant information including skills, experience, education, and more.
    </p>
</div>
""",
    unsafe_allow_html=True,
)

# Create two columns for layout
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 📤 Upload Your Resume")

    uploaded_file = st.file_uploader(
        "Choose your resume file",
        type=["pdf", "docx"],
        help="Supported formats: PDF, DOCX. Maximum file size: 10MB",
    )

    if uploaded_file:
        # Save and process file
        with st.spinner("Saving file..."):
            saved_path = save_uploaded_file(uploaded_file)
            mime, simple_type = detect_file_type(saved_path)
            st.session_state.file_path = saved_path
            st.session_state.file_type = simple_type

        st.success(f"✅ File uploaded successfully: `{uploaded_file.name}`")
        st.info(f"📋 File type detected: **{simple_type.upper()}**")

        # Parse button
        if st.button("🔍 Parse Resume", use_container_width=True, type="primary"):
            with st.spinner("🤖 AI is parsing your resume... This may take a moment."):
                try:
                    parsed = parse_resume(
                        st.session_state.file_path, st.session_state.file_type
                    )
                    st.session_state.parsed = parsed
                    st.success("✅ Resume parsed successfully!")
                    st.balloons()
                except Exception as e:
                    st.error(f"❌ Error parsing resume: {e}")

    # Tips section
    with st.expander("💡 Tips for Best Results"):
        st.markdown("""
        - **Use a clear, well-formatted resume**: Standard fonts and clear sections work best
        - **Avoid heavy graphics**: Text-based content is easier to parse
        - **Include keywords**: Use industry-standard terms for skills and roles
        - **Check OCR quality**: For scanned PDFs, ensure text is readable
        - **File size**: Keep files under 10MB for optimal performance
        """)

with col2:
    st.markdown("### 📊 Parsed Data")

    if st.session_state.parsed:
        # Display parsed information in organized sections

        # Basic Info
        with st.expander("👤 Basic Information", expanded=True):
            parsed = st.session_state.parsed

            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown(f"**Name:** {parsed.get('name', 'Not detected')}")
                st.markdown(f"**Email:** {parsed.get('email', 'Not detected')}")
            with col_b:
                st.markdown(f"**Phone:** {parsed.get('phone', 'Not detected')}")
                st.markdown(f"**Location:** {parsed.get('location', 'Not detected')}")

        # Skills
        with st.expander("💼 Skills", expanded=True):
            skills = parsed.get("skills", [])
            if skills:
                # Display as pills
                skills_html = " ".join(
                    [
                        f'<span style="display: inline-block; background: linear-gradient(135deg, #2E86AB 0%, #06A77D 100%); color: white; padding: 0.3rem 0.8rem; margin: 0.2rem; border-radius: 15px; font-size: 0.9rem;">{skill}</span>'
                        for skill in skills[:30]
                    ]
                )
                st.markdown(skills_html, unsafe_allow_html=True)
                if len(skills) > 30:
                    st.info(f"+ {len(skills) - 30} more skills")
            else:
                st.warning("No skills detected")

        # Experience
        with st.expander("💼 Work Experience", expanded=True):
            experience = parsed.get("experience", [])
            if experience:
                for i, exp in enumerate(experience[:5], 1):
                    if isinstance(exp, dict):
                        st.markdown(
                            f"""
                        <div style="background: #f8f9fa; padding: 1rem; border-radius: 8px; margin-bottom: 0.5rem; border-left: 3px solid #2E86AB;">
                            <strong>{exp.get("title", "Position")}</strong> at <em>{exp.get("company", "Company")}</em><br>
                            <small>{exp.get("duration", "Duration not specified")}</small>
                        </div>
                        """,
                            unsafe_allow_html=True,
                        )
                    else:
                        st.markdown(f"- {exp}")
                if len(experience) > 5:
                    st.info(f"+ {len(experience) - 5} more experiences")
            else:
                st.warning("No work experience detected")

        # Education
        with st.expander("🎓 Education", expanded=True):
            education = parsed.get("education", [])
            if education:
                for edu in education[:3]:
                    if isinstance(edu, dict):
                        st.markdown(
                            f"""
                        <div style="background: #f8f9fa; padding: 1rem; border-radius: 8px; margin-bottom: 0.5rem; border-left: 3px solid #A23B72;">
                            <strong>{edu.get("degree", "Degree")}</strong><br>
                            <em>{edu.get("institution", "Institution")}</em><br>
                            <small>{edu.get("year", "Year not specified")}</small>
                        </div>
                        """,
                            unsafe_allow_html=True,
                        )
                    else:
                        st.markdown(f"- {edu}")
            else:
                st.warning("No education details detected")

        # Raw text preview
        with st.expander("📝 Raw Extracted Text (Preview)"):
            raw_text = parsed.get("raw_text", "")
            if raw_text:
                st.text_area(
                    "Extracted text",
                    raw_text[:1000] + ("..." if len(raw_text) > 1000 else ""),
                    height=200,
                    disabled=True,
                )
            else:
                st.warning("No raw text available")

        # Download parsed data as JSON
        st.markdown("---")
        import json

        json_data = json.dumps(st.session_state.parsed, indent=2)
        st.download_button(
            label="📥 Download Parsed Data (JSON)",
            data=json_data,
            file_name="parsed_resume.json",
            mime="application/json",
            use_container_width=True,
        )

        # Navigation to next step
        st.markdown("---")
        st.markdown("### ✨ Ready for the next step?")
        if st.button(
            "➡️ Analyze & Score Resume", use_container_width=True, type="primary"
        ):
            st.switch_page("pages/2_📊_Analysis_Scoring.py")

    else:
        st.info("👆 Upload and parse a resume to see the extracted data here.")

        # Sample data preview
        st.markdown("### 📋 Sample Output")
        st.markdown("""
        Once parsed, you'll see:
        - ✅ Personal information (name, contact details)
        - ✅ Skills (technical, soft skills, languages)
        - ✅ Work experience with dates and descriptions
        - ✅ Education history
        - ✅ Certifications and achievements
        - ✅ Raw text extraction for reference
        """)

# Progress indicator at bottom
st.markdown("---")
st.markdown(
    """
<div style="text-align: center; padding: 1rem;">
    <p style="color: #4F5D75; font-size: 0.9rem;">
        <strong>Step 1 of 6:</strong> Upload & Parse Resume
    </p>
    <div style="background: #E5E5E5; height: 6px; border-radius: 3px; overflow: hidden; max-width: 600px; margin: 0.5rem auto;">
        <div style="background: linear-gradient(90deg, #2E86AB 0%, #06A77D 100%); height: 100%; width: 16.67%;"></div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)
