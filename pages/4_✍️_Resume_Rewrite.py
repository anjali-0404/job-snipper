"""
Resume Rewrite & Optimization Page
AI-powered resume rewriting with human-in-the-loop editing.
"""

import streamlit as st
import os
import sys
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.color_scheme import get_unified_css, SUCCESS_GREEN, WARNING_ORANGE, DANGER_RED
from utils.ui_components import apply_custom_css
from agents.rewrite_agent import rewrite_resume
from utils.file_utils import save_uploaded_file
from dotenv import load_dotenv

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Resume Rewrite - ResumeMasterAI", page_icon="✍️", layout="wide"
)

# Apply unified color scheme
st.markdown(get_unified_css(), unsafe_allow_html=True)

# Apply custom styling
apply_custom_css()

# Initialize session state
if "parsed" not in st.session_state:
    st.session_state.parsed = None
if "rewritten" not in st.session_state:
    st.session_state.rewritten = None
if "editing_mode" not in st.session_state:
    st.session_state.editing_mode = False
if "edited_text" not in st.session_state:
    st.session_state.edited_text = ""

# Header
st.markdown("# ✍️ AI-Powered Resume Rewrite")

# Check if resume is parsed
if not st.session_state.parsed:
    st.warning("⚠️ Please upload and parse a resume first!")
    if st.button("📄 Go to Upload Page"):
        st.switch_page("pages/1_📄_Upload_Resume.py")
    st.stop()

st.markdown(
    """
<div class="custom-card">
    <p style="font-size: 1.1rem; color: #4F5D75;">
        Let our AI rewrite your resume to be more impactful, ATS-friendly, and professionally formatted. 
        You can review and edit the AI suggestions before finalizing.
    </p>
</div>
""",
    unsafe_allow_html=True,
)

# Rewrite options
st.markdown("## ⚙️ Optimization Settings")

col1, col2, col3 = st.columns(3)

with col1:
    tone = st.selectbox(
        "Writing Tone",
        ["Professional", "Confident", "Dynamic", "Conservative"],
        help="Choose the tone for your resume",
    )

with col2:
    focus = st.selectbox(
        "Optimization Focus",
        [
            "ATS Optimization",
            "Impact & Achievements",
            "Skills Highlight",
            "Leadership",
            "Technical Depth",
        ],
        help="What aspect should the AI emphasize?",
    )

with col3:
    length = st.selectbox(
        "Target Length",
        ["Concise (1 page)", "Standard (1-2 pages)", "Detailed (2+ pages)"],
        help="Preferred resume length",
    )

# Rewrite button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button(
        "🤖 Generate Optimized Resume", use_container_width=True, type="primary"
    ):
        with st.spinner("✨ AI is rewriting your resume... This may take a minute..."):
            try:
                # Build instruction based on options
                instruction = f"Rewrite this resume with a {tone.lower()} tone, focusing on {focus.lower()}, targeting {length.lower()} length."

                rewritten = rewrite_resume(st.session_state.parsed, instruction)
                st.session_state.rewritten = rewritten
                # Extract the rewritten text from the dict
                st.session_state.edited_text = rewritten.get(
                    "rewritten_text", rewritten.get("raw_text", "")
                )
                st.success("✅ Resume rewrite complete!")
                st.rerun()
            except Exception as e:
                st.error(f"❌ Error during rewriting: {e}")

st.markdown("<br>", unsafe_allow_html=True)

# Display results if available
if st.session_state.rewritten:
    st.markdown("## 📝 Rewritten Resume")

    # Toggle editing mode
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        if st.button(
            "🖊️ Enable Editing"
            if not st.session_state.editing_mode
            else "👁️ Preview Mode",
            use_container_width=True,
        ):
            st.session_state.editing_mode = not st.session_state.editing_mode
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # Side-by-side comparison
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
        <div class="custom-card" style="background: #f8f9fa;">
            <h3>📄 Original Resume</h3>
        </div>
        """,
            unsafe_allow_html=True,
        )

        original_text = st.session_state.parsed.get("raw_text", "")
        st.text_area(
            "Original",
            value=original_text,
            height=600,
            disabled=True,
            label_visibility="collapsed",
        )

    with col2:
        st.markdown(
            """
        <div class="custom-card" style="background: linear-gradient(135deg, #E3F2FD 0%, #E8F5E9 100%);">
            <h3>✨ AI-Optimized Resume</h3>
        </div>
        """,
            unsafe_allow_html=True,
        )

        if st.session_state.editing_mode:
            st.session_state.edited_text = st.text_area(
                "Rewritten (Editable)",
                value=st.session_state.edited_text,
                height=600,
                label_visibility="collapsed",
                help="Edit the AI-generated resume as needed",
            )
        else:
            st.text_area(
                "Rewritten",
                value=st.session_state.edited_text,
                height=600,
                disabled=True,
                label_visibility="collapsed",
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # Key improvements
    st.markdown("## 🎯 Key Improvements")

    improvements = [
        {
            "icon": "🎨",
            "title": "Enhanced Formatting",
            "description": "Professional structure with clear sections and hierarchy",
        },
        {
            "icon": "💪",
            "title": "Action-Oriented Language",
            "description": "Strong action verbs and quantifiable achievements",
        },
        {
            "icon": "🤖",
            "title": "ATS Optimization",
            "description": "Keywords and formatting optimized for applicant tracking systems",
        },
        {
            "icon": "📊",
            "title": "Impact Focus",
            "description": "Emphasis on measurable results and contributions",
        },
    ]

    cols = st.columns(4)
    for i, improvement in enumerate(improvements):
        with cols[i]:
            st.markdown(
                f"""
            <div class="custom-card" style="text-align: center; height: 200px;">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">{improvement["icon"]}</div>
                <h4 style="color: #2E86AB; margin-bottom: 0.5rem;">{improvement["title"]}</h4>
                <p style="font-size: 0.85rem; color: #4F5D75;">{improvement["description"]}</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Get the final text for ATS scoring and downloads (ensure it's defined)
    final_text = str(st.session_state.get("edited_text", "") or "")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # ATS Score Tracking
    st.markdown("## 📈 ATS Score Tracking")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Calculate ATS score (basic scoring based on keywords, format, sections)
        ats_score = 0
        score_details = []
        
        # Check for key sections
        sections = ["experience", "education", "skills", "summary", "objective"]
        found_sections = sum(1 for sec in sections if sec.lower() in final_text.lower())
        section_score = (found_sections / len(sections)) * 30
        ats_score += section_score
        score_details.append(f"Key Sections: {found_sections}/{len(sections)} ({section_score:.0f} pts)")
        
        # Check for action verbs
        action_verbs = ["achieved", "managed", "led", "developed", "created", "implemented", "improved", "increased", "reduced"]
        found_verbs = sum(1 for verb in action_verbs if verb.lower() in final_text.lower())
        verb_score = min((found_verbs / 5) * 25, 25)
        ats_score += verb_score
        score_details.append(f"Action Verbs: {found_verbs} found ({verb_score:.0f} pts)")
        
        # Check for quantifiable achievements (numbers)
        import re
        numbers = re.findall(r'\d+[%\+\-]|\d+\s*(?:years?|months?)|[\$€£]\d+|\d+\s*(?:people|team|users|customers)', final_text.lower())
        metrics_score = min((len(numbers) / 3) * 25, 25)
        ats_score += metrics_score
        score_details.append(f"Quantifiable Metrics: {len(numbers)} found ({metrics_score:.0f} pts)")
        
        # Check length (optimal is 400-800 words)
        word_count = len(final_text.split())
        if 400 <= word_count <= 800:
            length_score = 20
        elif 300 <= word_count < 400 or 800 < word_count <= 1000:
            length_score = 15
        else:
            length_score = 10
        ats_score += length_score
        score_details.append(f"Resume Length: {word_count} words ({length_score:.0f} pts)")
        
        # Display score with color (using unified color scheme)
        if ats_score >= 80:
            score_color = SUCCESS_GREEN
            score_emoji = "🎯"
            score_label = "Excellent"
        elif ats_score >= 60:
            score_color = WARNING_ORANGE
            score_emoji = "👍"
            score_label = "Good"
        else:
            score_color = DANGER_RED
            score_emoji = "⚠️"
            score_label = "Needs Work"
        
        st.markdown(f"""
        <div class="custom-card" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; text-align: center;">
            <h1 style="font-size: 4rem; margin: 0; color: white;">{score_emoji}</h1>
            <h2 style="font-size: 3rem; margin: 0.5rem 0; color: white;">{ats_score:.0f}/100</h2>
            <p style="font-size: 1.2rem; margin: 0; color: rgba(255,255,255,0.9);">{score_label}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="custom-card">
            <h4>🎯 ATS Score Breakdown</h4>
        </div>
        """, unsafe_allow_html=True)
        
        for detail in score_details:
            st.markdown(f"- {detail}")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if ats_score < 80:
            st.markdown("""
            <div class="custom-card" style="background: #FFF3E0; border-left-color: #F18F01;">
                <strong>� Tips to Improve ATS Score:</strong>
                <ul style="margin-top: 0.5rem; line-height: 1.8;">
                    <li>Add more action verbs (achieved, managed, led, developed)</li>
                    <li>Include quantifiable metrics (%, $, numbers)</li>
                    <li>Ensure all key sections are present</li>
                    <li>Keep length between 400-800 words</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Download options
    st.markdown("## �💾 Save Your Resume")

    # Import document export utilities
    from utils.document_export import export_to_docx, export_to_pdf
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        # Text file download
        final_text = st.session_state.edited_text
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        st.download_button(
            label="📄 TXT",
            data=final_text,
            file_name=f"resume_optimized_{timestamp}.txt",
            mime="text/plain",
            use_container_width=True,
        )

    with col2:
        # Markdown download
        st.download_button(
            label="📝 MD",
            data=final_text,
            file_name=f"resume_optimized_{timestamp}.md",
            mime="text/markdown",
            use_container_width=True,
        )
    
    with col3:
        # DOCX download
        try:
            # Get contact info if available
            contact_info = {
                "email": st.session_state.parsed.get("email", ""),
                "phone": st.session_state.parsed.get("phone", ""),
                "location": st.session_state.parsed.get("location", "")
            }
            name = st.session_state.parsed.get("name", "Resume")
            
            docx_buffer = export_to_docx(final_text, name, contact_info)
            st.download_button(
                label="📘 DOCX",
                data=docx_buffer,
                file_name=f"resume_optimized_{timestamp}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                use_container_width=True,
            )
        except Exception as e:
            st.button("📘 DOCX", disabled=True, use_container_width=True, help=f"Error: {str(e)}")
    
    with col4:
        # PDF download
        try:
            contact_info = {
                "email": st.session_state.parsed.get("email", ""),
                "phone": st.session_state.parsed.get("phone", ""),
                "location": st.session_state.parsed.get("location", "")
            }
            name = st.session_state.parsed.get("name", "Resume")
            
            pdf_buffer = export_to_pdf(final_text, name, contact_info)
            st.download_button(
                label="📕 PDF",
                data=pdf_buffer,
                file_name=f"resume_optimized_{timestamp}.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
        except Exception as e:
            st.button("� PDF", disabled=True, use_container_width=True, help="Install reportlab: pip install reportlab")
    
    with col5:
        # Copy to clipboard button
        if st.button("📋 Copy", use_container_width=True):
            st.code(final_text, language=None)
            st.info("👆 Select and copy the text above")

    # Next steps
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
    <div class="custom-card" style="background: linear-gradient(135deg, #FFF3E0 0%, #E1F5FE 100%); border-left-color: #F18F01;">
        <h3>📌 Next Steps</h3>
        <ol style="line-height: 2; color: #4F5D75;">
            <li><strong>Review carefully:</strong> Ensure all information is accurate and reflects your experience</li>
            <li><strong>Customize further:</strong> Tailor for specific job applications</li>
            <li><strong>Format professionally:</strong> Use a resume template or Google Docs/Word for final formatting</li>
            <li><strong>Proofread:</strong> Check for typos and consistency</li>
            <li><strong>Get feedback:</strong> Have peers or mentors review your resume</li>
        </ol>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # Navigation buttons
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("← Back to Matching", use_container_width=True):
            st.switch_page("pages/3_🎯_Job_Matching.py")

    with col2:
        if st.button(
            "🔄 Generate New Version", use_container_width=True, type="secondary"
        ):
            st.session_state.rewritten = None
            st.session_state.edited_text = ""
            st.session_state.editing_mode = False
            st.rerun()

    with col3:
        if st.button("Next: Cover Letter →", use_container_width=True, type="primary"):
            st.switch_page("pages/5_💼_Cover_Letter_Projects.py")

else:
    # Tips section when no rewrite yet
    st.markdown("### 💡 What to Expect")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
        <div class="custom-card">
            <h3>✨ AI Enhancements</h3>
            <ul style="line-height: 2;">
                <li><strong>Strong Action Verbs:</strong> Replace weak verbs with impactful ones</li>
                <li><strong>Quantified Achievements:</strong> Add numbers and metrics where possible</li>
                <li><strong>Keyword Optimization:</strong> Include industry-relevant keywords</li>
                <li><strong>Clear Structure:</strong> Improve readability and organization</li>
                <li><strong>Professional Tone:</strong> Ensure consistent, professional language</li>
                <li><strong>Conciseness:</strong> Remove redundancy and filler words</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div class="custom-card">
            <h3>🎯 You're In Control</h3>
            <ul style="line-height: 2;">
                <li><strong>Review Everything:</strong> AI suggestions are starting points</li>
                <li><strong>Edit Freely:</strong> Enable editing mode to make changes</li>
                <li><strong>Regenerate:</strong> Try different tones and focus areas</li>
                <li><strong>Side-by-Side:</strong> Compare original and optimized versions</li>
                <li><strong>Multiple Formats:</strong> Download in TXT or Markdown</li>
                <li><strong>Your Data:</strong> All processing happens securely</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

    # Example improvements
    st.markdown("### 📊 Example Improvements")

    st.markdown(
        """
    <div class="custom-card">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
            <div>
                <h4 style="color: #C73E1D;">❌ Before</h4>
                <div style="background: #fee; padding: 1rem; border-radius: 8px; margin-top: 0.5rem;">
                    <p style="margin: 0; color: #4F5D75; line-height: 1.8;">
                        "Worked on various projects and helped the team with different tasks. 
                        Responsible for managing things and making improvements."
                    </p>
                </div>
            </div>
            <div>
                <h4 style="color: #06A77D;">✅ After</h4>
                <div style="background: #e6ffe6; padding: 1rem; border-radius: 8px; margin-top: 0.5rem;">
                    <p style="margin: 0; color: #4F5D75; line-height: 1.8;">
                        "Led cross-functional team of 5 developers to deliver 3 high-priority projects, 
                        reducing deployment time by 40% and improving system reliability to 99.9% uptime."
                    </p>
                </div>
            </div>
        </div>
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
        <strong>Step 4 of 6:</strong> Resume Rewriting & Optimization
    </p>
    <div style="background: #E5E5E5; height: 6px; border-radius: 3px; overflow: hidden; max-width: 600px; margin: 0.5rem auto;">
        <div style="background: linear-gradient(90deg, #2E86AB 0%, #06A77D 100%); height: 100%; width: 66.67%;"></div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)
