"""
Email Generator - Professional Email Templates
Generate polished emails for networking, follow-ups, applications, and more.
"""

import streamlit as st
import sys
from pathlib import Path
from datetime import datetime

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from utils.email_generator import EmailGenerator
from utils.color_scheme import get_unified_css
from dotenv import load_dotenv

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Email Generator - ResumeMasterAI", page_icon="📧", layout="wide"
)

# Apply unified CSS
st.markdown(get_unified_css(), unsafe_allow_html=True)

# Custom CSS
st.markdown(
    """
<style>
    .email-preview {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        border: 2px solid #e5e7eb;
        margin: 1rem 0;
        font-family: 'Arial', sans-serif;
    }
    
    .email-header {
        border-bottom: 2px solid #e5e7eb;
        padding-bottom: 1rem;
        margin-bottom: 1.5rem;
    }
    
    .email-field {
        margin: 0.5rem 0;
        font-size: 0.95rem;
    }
    
    .email-body {
        line-height: 1.8;
        color: #1f2937;
    }
    
    .template-card {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        cursor: pointer;
        transition: transform 0.3s;
    }
    
    .template-card:hover {
        transform: translateY(-5px);
    }
    
    .tip-box {
        background: #f0f9ff;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #3b82f6;
        margin: 1rem 0;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Header
st.markdown("# 📧 Email Generator")
st.markdown("### Create professional, polished emails in seconds")

# Initialize session state
if "generated_email" not in st.session_state:
    st.session_state.generated_email = None

# Sidebar Configuration
with st.sidebar:
    st.header("⚙️ Email Settings")

    # Email Type
    st.subheader("📨 Email Type")
    email_type = st.selectbox(
        "Select Template",
        [
            "Application Email",
            "Follow-Up After Interview",
            "Networking Request",
            "Thank You Email",
            "Cold Email to Recruiter",
            "LinkedIn Connection Request",
            "Salary Negotiation",
            "Job Offer Acceptance",
            "Job Offer Decline",
            "Resignation Letter",
            "Reference Request",
            "Informational Interview Request",
        ],
    )

    # Tone
    st.subheader("🎨 Tone")
    tone = st.select_slider(
        "Formality",
        options=["Very Formal", "Formal", "Professional", "Friendly", "Casual"],
        value="Professional",
    )

    # Length
    st.subheader("📏 Length")
    length = st.select_slider(
        "Email Length", options=["Brief", "Medium", "Detailed"], value="Medium"
    )

    # Additional Options
    st.subheader("✨ Options")
    include_greeting = st.checkbox("Include Greeting", value=True)
    include_signature = st.checkbox("Include Signature", value=True)
    add_call_to_action = st.checkbox("Add Call-to-Action", value=True)

# Main Content
tab1, tab2, tab3 = st.tabs(["✍️ Compose", "📚 Templates", "💡 Tips"])

with tab1:
    st.markdown(f"## Generate: {email_type}")

    # Context Section
    st.markdown("### 📋 Context & Details")

    col1, col2 = st.columns(2)

    with col1:
        # Sender Info
        st.markdown("#### Your Information")
        your_name = st.text_input("Your Full Name", placeholder="John Doe")
        your_email = st.text_input("Your Email", placeholder="john.doe@email.com")
        your_phone = st.text_input(
            "Your Phone (Optional)", placeholder="+1 (555) 123-4567"
        )
        your_title = st.text_input(
            "Your Current Title", placeholder="Software Engineer"
        )

    with col2:
        # Recipient Info
        st.markdown("#### Recipient Information")
        recipient_name = st.text_input("Recipient's Name", placeholder="Jane Smith")
        recipient_email = st.text_input("Recipient's Email", placeholder="jane.smith@techcorp.com")
        recipient_title = st.text_input(
            "Recipient's Title", placeholder="Hiring Manager"
        )
        company_name = st.text_input("Company Name", placeholder="Tech Corp")
        position = st.text_input(
            "Position (if applicable)", placeholder="Senior Developer"
        )

    # Email-specific fields
    st.markdown("### 🎯 Specific Details")

    if "Application" in email_type:
        job_description = st.text_area(
            "Job Description (paste key requirements)",
            placeholder="Paste the job description or key requirements...",
            height=100,
        )
        why_interested = st.text_area(
            "Why are you interested in this role?",
            placeholder="Explain your interest in the position and company...",
            height=80,
        )
        key_qualifications = st.text_area(
            "Your Key Qualifications (bullet points)",
            placeholder="• 5 years of Python experience\n• Led team of 10 developers\n• Expertise in cloud architecture",
            height=100,
        )

    elif "Follow-Up" in email_type or "Thank You" in email_type:
        interview_date = st.date_input("Interview Date", datetime.now())
        interviewer_name = st.text_input("Interviewer's Name", recipient_name)
        specific_topics = st.text_area(
            "Topics Discussed (Optional)",
            placeholder="Cloud architecture, team culture, project timeline...",
            height=80,
        )
        additional_info = st.text_area(
            "Additional Information to Include",
            placeholder="Any information you forgot to mention or want to emphasize...",
            height=80,
        )

    elif "Networking" in email_type or "Informational" in email_type:
        connection_context = st.text_area(
            "How do you know them / Why reaching out?",
            placeholder="Saw your talk at DevCon 2024, connected on LinkedIn, mutual connection Sarah...",
            height=80,
        )
        what_you_want = st.text_area(
            "What are you asking for?",
            placeholder="15-minute call to discuss career advice, insights on the industry, etc...",
            height=80,
        )
        your_background = st.text_area(
            "Brief Background (2-3 sentences)",
            placeholder="Software engineer with 5 years experience, transitioning to AI/ML...",
            height=80,
        )

    elif "Negotiation" in email_type:
        current_offer = st.number_input(
            "Current Offer ($)", min_value=0, value=100000, step=5000
        )
        desired_salary = st.number_input(
            "Desired Salary ($)", min_value=0, value=120000, step=5000
        )
        justification = st.text_area(
            "Justification for Higher Salary",
            placeholder="Market research, competing offers, unique qualifications...",
            height=100,
        )

    elif "Resignation" in email_type:
        last_day = st.date_input("Proposed Last Day", datetime.now())
        reason = st.text_area(
            "Reason for Leaving (Optional)",
            placeholder="New opportunity, career change, relocation...",
            height=80,
        )
        transition_offer = st.text_area(
            "Transition Support Offered",
            placeholder="Train replacement, document processes, complete current projects...",
            height=80,
        )

    else:
        # Generic fields for other email types
        main_purpose = st.text_area(
            "Main Purpose of Email",
            placeholder="What do you want to accomplish with this email?",
            height=100,
        )
        key_points = st.text_area(
            "Key Points to Include",
            placeholder="List the main points you want to cover...",
            height=100,
        )

    # Additional Notes
    additional_notes = st.text_area(
        "Additional Notes / Special Instructions",
        placeholder="Any specific points to include or avoid...",
        height=80,
    )

    # Generate Button
    if st.button("✨ Generate Email", type="primary", use_container_width=True):
        if not your_name or not recipient_name:
            st.error("❌ Please provide at least your name and recipient's name")
        else:
            with st.spinner("🤖 Crafting your professional email..."):
                try:
                    generator = EmailGenerator()

                    # Prepare input data
                    input_data = {
                        "email_type": email_type,
                        "tone": tone,
                        "length": length,
                        "sender": {
                            "name": your_name,
                            "email": your_email,
                            "phone": your_phone,
                            "title": your_title,
                        },
                        "recipient": {
                            "name": recipient_name,
                            "title": recipient_title,
                            "company": company_name,
                            "position": position,
                        },
                        "include_greeting": include_greeting,
                        "include_signature": include_signature,
                        "add_call_to_action": add_call_to_action,
                        "additional_notes": additional_notes,
                    }

                    # Add email-specific data
                    if "Application" in email_type:
                        input_data["job_description"] = job_description
                        input_data["why_interested"] = why_interested
                        input_data["qualifications"] = key_qualifications
                    elif "Follow-Up" in email_type or "Thank You" in email_type:
                        input_data["interview_date"] = str(interview_date)
                        input_data["topics"] = specific_topics
                        input_data["additional_info"] = additional_info
                    elif "Networking" in email_type or "Informational" in email_type:
                        input_data["connection_context"] = connection_context
                        input_data["request"] = what_you_want
                        input_data["background"] = your_background
                    elif "Negotiation" in email_type:
                        input_data["current_offer"] = current_offer
                        input_data["desired_salary"] = desired_salary
                        input_data["justification"] = justification
                    elif "Resignation" in email_type:
                        input_data["last_day"] = str(last_day)
                        input_data["reason"] = reason
                        input_data["transition"] = transition_offer
                    else:
                        input_data["purpose"] = main_purpose
                        input_data["key_points"] = key_points

                    # Generate email
                    result = generator.generate(input_data)
                    st.session_state.generated_email = result

                    st.success("✅ Email generated successfully!")

                except Exception as e:
                    st.error(f"❌ Error generating email: {str(e)}")

    # Display Generated Email
    if st.session_state.generated_email:
        st.markdown("---")
        st.markdown("## 📧 Your Generated Email")

        result = st.session_state.generated_email

        # Email Preview
        st.markdown(
            f"""
        <div class="email-preview">
            <div class="email-header">
                <div class="email-field"><strong>From:</strong> {result.get("from", "")}</div>
                <div class="email-field"><strong>To:</strong> {result.get("to", "")}</div>
                <div class="email-field"><strong>Subject:</strong> {result.get("subject", "")}</div>
            </div>
            <div class="email-body">
                {result.get("body", "").replace(chr(10), "<br>")}
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        # Alternative Subjects
        alt_subjects = result.get("alternative_subjects", [])
        if alt_subjects:
            st.markdown("### 📝 Alternative Subject Lines")
            for idx, subject in enumerate(alt_subjects, 1):
                st.markdown(f"{idx}. {subject}")

        # Export Options
        st.markdown("---")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            email_text = (
                f"Subject: {result.get('subject', '')}\n\n{result.get('body', '')}"
            )
            st.download_button(
                label="📄 Download as TXT",
                data=email_text,
                file_name=f"{email_type.replace(' ', '_')}.txt",
                mime="text/plain",
            )

        with col2:
            if st.button("📋 Copy to Clipboard"):
                st.info("✅ Use Ctrl+C to copy the email above")

        with col3:
            if st.button("📧 Open in Email Client"):
                mailto_link = f"mailto:{recipient_email if 'recipient_email' in locals() else ''}?subject={result.get('subject', '')}&body={result.get('body', '')}"
                st.markdown(f"[Open Email Client]({mailto_link})")

        with col4:
            if st.button("🔄 Generate Another"):
                st.session_state.generated_email = None
                st.rerun()

with tab2:
    st.markdown("## 📚 Email Templates")

    st.markdown("### Quick Template Selection")

    templates = {
        "Application Email": "Professional email to accompany your resume when applying for a position",
        "Follow-Up After Interview": "Polite follow-up email after an interview to express continued interest",
        "Networking Request": "Request to connect with someone in your industry for advice or opportunities",
        "Thank You Email": "Express gratitude after an interview or meeting",
        "Cold Email to Recruiter": "Initial outreach to a recruiter about opportunities",
        "LinkedIn Connection Request": "Personalized message when connecting on LinkedIn",
        "Salary Negotiation": "Professional negotiation of salary or benefits",
        "Job Offer Acceptance": "Formal acceptance of a job offer",
        "Job Offer Decline": "Politely declining a job offer",
        "Resignation Letter": "Professional resignation from current position",
        "Reference Request": "Asking someone to serve as a reference",
        "Informational Interview Request": "Requesting an informational interview for career insights",
    }

    for template_name, description in templates.items():
        with st.expander(f"**{template_name}**"):
            st.write(description)

            # Show template example
            st.markdown("**Example Structure:**")
            if "Application" in template_name:
                st.markdown("""
                - Opening: Express interest in position
                - Body: Highlight relevant qualifications
                - Show knowledge of company
                - Call to action: Request interview
                - Closing: Thank them for consideration
                """)
            elif "Follow-Up" in template_name:
                st.markdown("""
                - Thank them for their time
                - Reiterate interest in position
                - Mention specific discussion points
                - Add any forgotten information
                - Express enthusiasm for next steps
                """)
            elif "Networking" in template_name:
                st.markdown("""
                - Explain connection/introduction
                - Brief background about yourself
                - Specific request (call, coffee, advice)
                - Respect their time
                - Clear call to action
                """)

with tab3:
    st.markdown("## 💡 Email Writing Tips")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### ✅ Do's
        
        **Structure:**
        - ✅ Clear, specific subject line
        - ✅ Professional greeting
        - ✅ Concise opening
        - ✅ Organized body paragraphs
        - ✅ Strong closing with CTA
        
        **Content:**
        - ✅ Be specific and concrete
        - ✅ Show enthusiasm
        - ✅ Proofread carefully
        - ✅ Personalize for recipient
        - ✅ Keep it concise
        - ✅ Use proper grammar
        
        **Tone:**
        - ✅ Professional but warm
        - ✅ Confident, not arrogant
        - ✅ Grateful and positive
        - ✅ Match recipient's style
        """)

    with col2:
        st.markdown("""
        ### ❌ Don'ts
        
        **Structure:**
        - ❌ Vague subject lines
        - ❌ Long, rambling paragraphs
        - ❌ No clear purpose
        - ❌ Missing signature
        - ❌ Wall of text
        
        **Content:**
        - ❌ Generic templates
        - ❌ Spelling/grammar errors
        - ❌ TMI (too much info)
        - ❌ Negative language
        - ❌ Demands or ultimatums
        - ❌ Unnecessary details
        
        **Tone:**
        - ❌ Too casual or formal
        - ❌ Desperate or pushy
        - ❌ Overly apologetic
        - ❌ Entitled attitude
        """)

    st.markdown("---")
    st.markdown("### 📧 Email Best Practices")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        **Timing**
        - Send during business hours
        - Tuesday-Thursday optimal
        - Morning or early afternoon
        - Follow up after 3-5 days
        - Be patient with responses
        """)

    with col2:
        st.markdown("""
        **Subject Lines**
        - Keep under 50 characters
        - Be specific and clear
        - Include position/company
        - Action-oriented
        - Avoid spam triggers
        """)

    with col3:
        st.markdown("""
        **Follow-Up**
        - Wait appropriate time
        - Reference previous email
        - Add new value/info
        - Keep it brief
        - Know when to stop
        """)

# Resources
st.markdown("---")
st.markdown("## 📚 Additional Resources")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 📖 Learning
    - Email etiquette guides
    - Professional writing courses
    - Business communication books
    - Grammar resources
    - Industry-specific tips
    """)

with col2:
    st.markdown("""
    ### 🛠️ Tools
    - Grammarly
    - Hemingway Editor
    - Email tracking tools
    - Template libraries
    - Signature generators
    """)

with col3:
    st.markdown("""
    ### 💡 Tips
    - Read successful emails
    - Practice regularly
    - Get feedback
    - Test subject lines
    - Track responses
    """)

# Footer
st.markdown("---")
st.markdown(
    """
<div style='text-align: center; color: #6b7280;'>
    <p>💡 <strong>Pro Tip:</strong> Always proofread before sending, and personalize each email!</p>
</div>
""",
    unsafe_allow_html=True,
)
