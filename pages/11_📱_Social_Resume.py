"""
Social Resume Generator - Optimize Your Professional Profiles
Generate optimized content for LinkedIn, GitHub, Twitter, and more.
"""

import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from utils.social_resume import SocialResumeGenerator
from utils.color_scheme import get_unified_css
from dotenv import load_dotenv

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Social Resume Generator - ResumeMasterAI", page_icon="📱", layout="wide"
)

# Apply unified CSS
st.markdown(get_unified_css(), unsafe_allow_html=True)

# Custom CSS
st.markdown(
    """
<style>
    .platform-card {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        margin: 1rem 0;
        cursor: pointer;
        transition: transform 0.3s;
    }
    
    .platform-card:hover {
        transform: translateY(-5px);
    }
    
    .generated-content {
        background: #f9fafb;
        padding: 2rem;
        border-radius: 15px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    
    .tip-box {
        background: #f0f9ff;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #3b82f6;
        margin: 1rem 0;
    }
    
    .example-box {
        background: #fef3c7;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    
    .char-count {
        text-align: right;
        color: #6b7280;
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Header
st.markdown("# 📱 Social Resume Generator")
st.markdown("### Optimize your professional presence across all platforms")

# Initialize session state
if "generated_content" not in st.session_state:
    st.session_state.generated_content = {}

# Sidebar Configuration
with st.sidebar:
    st.header("⚙️ Profile Settings")

    # Platform Selection
    st.subheader("🌐 Select Platform")
    platform = st.selectbox(
        "Platform",
        ["LinkedIn", "GitHub", "Twitter/X", "Instagram", "Personal Website"],
        help="Choose the platform to optimize for",
    )

    # Content Type
    st.subheader("📝 Content Type")

    content_types = {
        "LinkedIn": [
            "Headline",
            "About/Summary",
            "Experience Description",
            "Skills Section",
            "Post",
        ],
        "GitHub": [
            "Bio",
            "README Profile",
            "Project Description",
            "Contribution Summary",
        ],
        "Twitter/X": ["Bio", "Pinned Tweet", "Thread", "Profile"],
        "Instagram": ["Bio", "Story Highlights", "Post Caption"],
        "Personal Website": ["Hero Section", "About Me", "Skills", "Portfolio Item"],
    }

    content_type = st.selectbox(
        "What to generate?", content_types.get(platform, ["Profile"])
    )

    # Tone & Style
    st.subheader("🎨 Style")
    tone = st.select_slider(
        "Tone",
        options=["Professional", "Balanced", "Casual", "Creative"],
        value="Balanced",
    )

    include_emojis = st.checkbox("Include Emojis", value=True)
    include_hashtags = st.checkbox(
        "Include Hashtags", value=platform in ["Twitter/X", "Instagram"]
    )

# Main Content
tab1, tab2, tab3 = st.tabs(["📝 Generate", "✨ Examples", "💡 Tips"])

with tab1:
    st.markdown(f"## Generate {content_type} for {platform}")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### 📄 Your Information")

        # Resume Upload
        uploaded_file = st.file_uploader(
            "Upload Your Resume (Optional)",
            type=["pdf", "docx", "txt"],
            help="We'll extract information automatically",
        )

        # Manual Input
        st.markdown("#### Basic Info")

        col_a, col_b = st.columns(2)
        with col_a:
            full_name = st.text_input("Full Name", placeholder="John Doe")
            current_role = st.text_input(
                "Current Role", placeholder="Software Engineer"
            )

        with col_b:
            company = st.text_input("Company", placeholder="Tech Corp")
            location = st.text_input("Location", placeholder="San Francisco, CA")

        # Professional Summary
        professional_summary = st.text_area(
            "Professional Summary",
            placeholder="Brief overview of your experience and expertise...",
            height=100,
        )

        # Key Achievements
        achievements = st.text_area(
            "Key Achievements (one per line)",
            placeholder="Led team of 10 developers\nIncreased revenue by 40%\nBuilt scalable microservices architecture",
            height=100,
        )

        # Skills
        skills = st.text_input(
            "Top Skills (comma-separated)",
            placeholder="Python, AWS, React, Leadership, Machine Learning",
        )

        # Interests/Focus
        focus_areas = st.text_input(
            "Focus Areas/Interests", placeholder="AI, Cloud Computing, DevOps"
        )

    with col2:
        st.markdown("### 🎯 Customization")

        # Platform-specific settings
        if platform == "LinkedIn":
            st.info("""
            **LinkedIn Tips:**
            - Headline: 220 chars
            - Summary: 2,600 chars
            - Use keywords
            - Show personality
            """)

            include_cta = st.checkbox("Include Call-to-Action", value=True)
            target_audience = st.selectbox(
                "Target Audience", ["Recruiters", "Peers", "Clients", "General"]
            )

        elif platform == "GitHub":
            st.info("""
            **GitHub Tips:**
            - Bio: 160 chars
            - Profile README
            - Show projects
            - Use badges
            """)

            show_stats = st.checkbox("Include GitHub Stats", value=True)
            show_languages = st.checkbox("Show Top Languages", value=True)

        elif platform == "Twitter/X":
            st.info("""
            **Twitter/X Tips:**
            - Bio: 160 chars
            - Be concise
            - Use emojis wisely
            - Show personality
            """)

            max_hashtags = st.slider("Max Hashtags", 0, 5, 3)

        elif platform == "Instagram":
            st.info("""
            **Instagram Tips:**
            - Bio: 150 chars
            - Link in bio
            - Visual appeal
            - Emojis welcome
            """)

            include_link = st.checkbox("Include Link", value=True)

        else:  # Personal Website
            st.info("""
            **Website Tips:**
            - Clear messaging
            - SEO-friendly
            - Showcase work
            - Easy to scan
            """)

            seo_optimized = st.checkbox("SEO Optimized", value=True)

    # Generate Button
    if st.button("✨ Generate Content", type="primary", use_container_width=True):
        if not full_name and not uploaded_file:
            st.error("❌ Please provide your name or upload a resume")
        else:
            with st.spinner(f"🤖 Generating {content_type} for {platform}..."):
                try:
                    generator = SocialResumeGenerator()

                    # Prepare input data
                    input_data = {
                        "platform": platform,
                        "content_type": content_type,
                        "tone": tone,
                        "full_name": full_name,
                        "current_role": current_role,
                        "company": company,
                        "location": location,
                        "summary": professional_summary,
                        "achievements": [
                            a.strip() for a in achievements.split("\n") if a.strip()
                        ],
                        "skills": [s.strip() for s in skills.split(",") if s.strip()],
                        "focus_areas": [
                            f.strip() for f in focus_areas.split(",") if f.strip()
                        ],
                        "include_emojis": include_emojis,
                        "include_hashtags": include_hashtags,
                        "resume_file": uploaded_file,
                    }

                    # Add platform-specific settings
                    if platform == "LinkedIn":
                        input_data["include_cta"] = include_cta
                        input_data["target_audience"] = target_audience
                    elif platform == "GitHub":
                        input_data["show_stats"] = show_stats
                        input_data["show_languages"] = show_languages
                    elif platform == "Twitter/X":
                        input_data["max_hashtags"] = max_hashtags
                    elif platform == "Instagram":
                        input_data["include_link"] = include_link
                    elif platform == "Personal Website":
                        input_data["seo_optimized"] = seo_optimized

                    # Generate content
                    result = generator.generate(input_data)
                    st.session_state.generated_content = result

                    st.success(f"✅ {content_type} generated successfully!")

                except Exception as e:
                    st.error(f"❌ Error generating content: {str(e)}")

    # Display Generated Content
    if st.session_state.generated_content:
        st.markdown("---")
        st.markdown("## ✨ Generated Content")

        result = st.session_state.generated_content

        # Primary content
        primary = result.get("primary_content", "")
        char_limit = result.get("character_limit", 0)
        char_count = len(primary)

        st.markdown(
            f"""
        <div class="generated-content">
            <h3>{result.get("content_type", "Content")}</h3>
            <p style="white-space: pre-wrap; font-size: 1.1rem; line-height: 1.6;">{primary}</p>
            <div class="char-count">
                {char_count} characters{f" / {char_limit} limit" if char_limit else ""}
                {" ⚠️ Over limit!" if char_limit and char_count > char_limit else " ✅" if char_limit else ""}
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        # Variations
        variations = result.get("variations", [])
        if variations:
            st.markdown("### 🔄 Alternative Versions")

            for idx, variation in enumerate(variations, 1):
                with st.expander(f"Version {idx}"):
                    st.write(variation)
                    st.markdown(
                        f"<div class='char-count'>{len(variation)} characters</div>",
                        unsafe_allow_html=True,
                    )

        # Additional content (hashtags, keywords, etc.)
        col1, col2 = st.columns(2)

        with col1:
            if result.get("hashtags"):
                st.markdown("### #️⃣ Suggested Hashtags")
                st.write(" ".join(result.get("hashtags", [])))

        with col2:
            if result.get("keywords"):
                st.markdown("### 🔑 SEO Keywords")
                st.write(", ".join(result.get("keywords", [])))

        # Export Options
        st.markdown("---")
        st.markdown("### 📥 Export")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.download_button(
                label="📄 Download as TXT",
                data=primary,
                file_name=f"{platform}_{content_type.replace(' ', '_')}.txt",
                mime="text/plain",
            )

        with col2:
            if st.button("📋 Copy to Clipboard"):
                st.write("✅ Copied! (Use Ctrl+C to copy)")

        with col3:
            if st.button("🔄 Generate Again"):
                st.session_state.generated_content = {}
                st.rerun()

with tab2:
    st.markdown("## ✨ Examples & Inspiration")

    st.markdown(f"### {platform} Examples")

    if platform == "LinkedIn":
        st.markdown(
            """
        #### Example Headline
        <div class="example-box">
        🚀 Senior Software Engineer @ Tech Corp | Cloud Architecture Expert | Building Scalable Solutions | Speaker & Mentor
        </div>
        
        #### Example About Section
        <div class="example-box">
        I'm passionate about building technology that makes a difference. With 8+ years in software engineering, 
        I've led teams to deliver cloud-native solutions that serve millions of users daily.
        
        💡 Specialties: Cloud Architecture, Microservices, DevOps, Team Leadership
        
        🏆 Achievements:
        • Architected platform serving 10M+ users
        • Reduced infrastructure costs by 40%
        • Mentored 20+ junior developers
        
        📫 Let's connect! Always open to discussing technology, innovation, and collaboration opportunities.
        </div>
        """,
            unsafe_allow_html=True,
        )

    elif platform == "GitHub":
        st.markdown(
            """
        #### Example Bio
        <div class="example-box">
        🚀 Full-stack developer | Open source enthusiast | Cloud & DevOps | Always learning
        </div>
        
        #### Example Profile README
        <div class="example-box">
        ## Hi there 👋
        
        I'm John, a software engineer passionate about building scalable web applications and contributing to open source.
        
        ### 🔭 Currently working on
        - Building microservices with Node.js and Kubernetes
        - Contributing to awesome-python-projects
        
        ### 🌱 Learning
        - Rust and WebAssembly
        - Advanced system design patterns
        
        ### 💬 Ask me about
        Cloud architecture, Python, JavaScript, or anything tech!
        
        ### 📫 Reach me
        [LinkedIn](https://linkedin.com/in/johndoe) | [Twitter](https://twitter.com/johndoe)
        </div>
        """,
            unsafe_allow_html=True,
        )

    elif platform == "Twitter/X":
        st.markdown(
            """
        #### Example Bio
        <div class="example-box">
        🚀 Software Engineer @ Tech Corp | Building in public | Thoughts on tech, AI & productivity | DMs open
        </div>
        
        #### Example Thread
        <div class="example-box">
        1/ 🧵 5 lessons I learned after 5 years in software engineering:
        
        2/ Master the fundamentals. Frameworks come and go, but core CS concepts are forever. 
        Algorithms, data structures, and design patterns will serve you throughout your career.
        
        3/ Communication > Code. The best engineers aren't just great coders—they're great communicators.
        Learn to explain complex ideas simply.
        
        [Continue...]
        </div>
        """,
            unsafe_allow_html=True,
        )

    elif platform == "Instagram":
        st.markdown(
            """
        #### Example Bio
        <div class="example-box">
        👨‍💻 Software Engineer | 🚀 Building cool stuff
        💡 Tech tips & career insights
        🔗 Links & resources below ⬇️
        </div>
        """,
            unsafe_allow_html=True,
        )

    else:  # Personal Website
        st.markdown(
            """
        #### Example Hero Section
        <div class="example-box">
        Hi, I'm John Doe 👋
        
        I'm a software engineer who loves building products that make a difference. 
        Currently working on cloud-native solutions at Tech Corp.
        
        I specialize in scalable web applications, cloud architecture, and team leadership.
        </div>
        """,
            unsafe_allow_html=True,
        )

with tab3:
    st.markdown("## 💡 Optimization Tips")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### 📝 Content Best Practices
        
        **Do:**
        - ✅ Be authentic and genuine
        - ✅ Show your personality
        - ✅ Use concrete examples
        - ✅ Include metrics & results
        - ✅ Update regularly
        - ✅ Use keywords naturally
        - ✅ Tell stories
        
        **Don't:**
        - ❌ Use buzzwords excessively
        - ❌ Copy others' content
        - ❌ Be too generic
        - ❌ Lie or exaggerate
        - ❌ Ignore your audience
        - ❌ Forget to proofread
        """)

    with col2:
        st.markdown("""
        ### 🎯 Platform-Specific Tips
        
        **LinkedIn:**
        - Use your headline wisely
        - Write in first person
        - Add rich media
        - Engage with others
        
        **GitHub:**
        - Pin your best projects
        - Write good READMEs
        - Contribute consistently
        - Use descriptive commits
        
        **Twitter/X:**
        - Tweet consistently
        - Engage with community
        - Use threads for depth
        - Be conversational
        
        **Instagram:**
        - Quality over quantity
        - Use stories effectively
        - Engage with comments
        - Post consistently
        """)

    st.markdown("---")
    st.markdown("### 🚀 Profile Optimization Checklist")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        **Profile Basics**
        - [ ] Professional photo
        - [ ] Compelling headline
        - [ ] Complete about/bio
        - [ ] Contact information
        - [ ] Location
        """)

    with col2:
        st.markdown("""
        **Content**
        - [ ] Showcase achievements
        - [ ] Highlight skills
        - [ ] Share projects
        - [ ] Post regularly
        - [ ] Engage with others
        """)

    with col3:
        st.markdown("""
        **Optimization**
        - [ ] Use keywords
        - [ ] Add links
        - [ ] Include media
        - [ ] Update frequently
        - [ ] Track performance
        """)

# Resources
st.markdown("---")
st.markdown("## 📚 Profile Resources")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 🎓 Learning
    - LinkedIn Learning
    - GitHub Skills
    - Social Media Examiner
    - Buffer Blog
    - HubSpot Academy
    """)

with col2:
    st.markdown("""
    ### 🛠️ Tools
    - Canva (graphics)
    - Grammarly (writing)
    - Buffer (scheduling)
    - Analytics tools
    - Link shorteners
    """)

with col3:
    st.markdown("""
    ### 📊 Analytics
    - LinkedIn Analytics
    - GitHub Insights
    - Twitter Analytics
    - Instagram Insights
    - Google Analytics
    """)

# Footer
st.markdown("---")
st.markdown(
    """
<div style='text-align: center; color: #6b7280;'>
    <p>💡 <strong>Pro Tip:</strong> Consistency is key! Update your profiles regularly and stay active in your communities.</p>
</div>
""",
    unsafe_allow_html=True,
)
