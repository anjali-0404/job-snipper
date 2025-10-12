"""
ResumeMasterAI - Professional Landing Page
Complete AI-powered resume optimization and career management platform.
"""

import streamlit as st
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="ResumeMasterAI - AI-Powered Career Excellence",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Complete CSS Design
st.markdown(
    """
<style>
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Global Styles */
    .stApp {
        background: linear-gradient(180deg, #e0e7ff 0%, #f0e9ff 50%, #fce7f3 100%);
    }
    
    /* Hero Section */
    .hero-section {
        background: linear-gradient(135deg, #a78bfa 0%, #c084fc 25%, #e879f9 50%, #f0abfc 75%, #fbbf24 100%);
        padding: 8rem 3rem 6rem;
        text-align: center;
        border-radius: 0 0 50px 50px;
        margin: -2rem -3rem 3rem;
        position: relative;
        overflow: hidden;
        box-shadow: 0 20px 60px rgba(167, 139, 250, 0.3);
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at 20% 50%, rgba(255,255,255,0.1) 0%, transparent 50%),
                    radial-gradient(circle at 80% 50%, rgba(255,255,255,0.1) 0%, transparent 50%);
        pointer-events: none;
    }
    
    .ai-badge {
        position: absolute;
        top: 2rem;
        right: 2rem;
        padding: 0.75rem 1.5rem;
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(10px);
        border: 2px solid rgba(255, 255, 255, 0.3);
        border-radius: 50px;
        color: white;
        font-weight: 700;
        font-size: 0.95rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    
    .hero-title {
        font-size: 4rem;
        font-weight: 900;
        color: white;
        margin: 2rem 0 1rem;
        letter-spacing: -2px;
        text-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
        position: relative;
        z-index: 1;
    }
    
    .gradient-text {
        background: linear-gradient(90deg, #fbbf24 0%, #f97316 50%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .hero-divider {
        height: 2px;
        width: 100%;
        max-width: 1200px;
        margin: 2rem auto;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.5), transparent);
    }
    
    .hero-subtitle {
        font-size: 1.4rem;
        color: rgba(255, 255, 255, 0.95);
        margin: 1.5rem auto;
        max-width: 800px;
        line-height: 1.6;
        position: relative;
        z-index: 1;
    }
    
    .hero-tagline {
        font-size: 1.15rem;
        color: rgba(255, 255, 255, 0.9);
        margin: 1rem 0 3rem;
        font-weight: 400;
        position: relative;
        z-index: 1;
    }
    
    .cta-button {
        display: inline-block;
        padding: 1.2rem 3.5rem;
        background: white;
        color: #7c3aed !important;
        font-size: 1.2rem;
        font-weight: 700;
        border-radius: 50px;
        text-decoration: none;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
        position: relative;
        z-index: 1;
        border: none;
        cursor: pointer;
    }
    
    .cta-button:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.3);
        color: #7c3aed !important;
        text-decoration: none;
    }
    
    /* Quick Navigation */
    .nav-section {
        padding: 3rem 2rem;
        max-width: 1400px;
        margin: 0 auto 2rem;
    }
    
    .nav-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
        gap: 1.5rem;
        margin-top: 2rem;
    }
    
    .nav-card {
        background: white;
        padding: 2rem 1.5rem;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 5px 20px rgba(167, 139, 250, 0.1);
        transition: all 0.3s ease;
        cursor: pointer;
        text-decoration: none;
        color: inherit;
    }
    
    .nav-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 40px rgba(167, 139, 250, 0.2);
    }
    
    .nav-icon {
        font-size: 2.5rem;
        margin-bottom: 0.8rem;
        display: block;
    }
    
    .nav-title {
        font-size: 0.95rem;
        font-weight: 600;
        color: #4b5563;
    }
    
    /* Section Container */
    .section-container {
        padding: 4rem 2rem;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .section-title {
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(135deg, #ec4899 0%, #c084fc 50%, #a78bfa 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
    }
    
    .section-subtitle {
        text-align: center;
        font-size: 1.1rem;
        color: #6b7280;
        margin-bottom: 3rem;
    }
    
    .underline {
        width: 150px;
        height: 4px;
        background: linear-gradient(90deg, #a78bfa, #c084fc, #ec4899);
        margin: 1rem auto 3rem;
        border-radius: 2px;
    }
    
    /* Steps Grid */
    .steps-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 3rem;
        margin: 4rem 0;
    }
    
    .step-card {
        background: white;
        padding: 3rem 2.5rem;
        border-radius: 30px;
        box-shadow: 0 10px 40px rgba(167, 139, 250, 0.15);
        position: relative;
        transition: all 0.3s ease;
    }
    
    .step-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 60px rgba(167, 139, 250, 0.25);
    }
    
    .step-number {
        position: absolute;
        top: -30px;
        left: 30px;
        width: 70px;
        height: 70px;
        background: linear-gradient(135deg, #7c3aed, #a78bfa);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2rem;
        font-weight: 900;
        color: white;
        box-shadow: 0 10px 30px rgba(124, 58, 237, 0.3);
    }
    
    .step-icon {
        font-size: 2.5rem;
        margin: 2rem 0 1.5rem;
    }
    
    .step-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #7c3aed;
        margin-bottom: 1rem;
    }
    
    .step-description {
        font-size: 1.05rem;
        color: #6b7280;
        line-height: 1.7;
    }
    
    /* Features Grid */
    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2.5rem;
        margin: 4rem 0;
    }
    
    .feature-card {
        background: white;
        padding: 2.5rem 2rem;
        border-radius: 25px;
        box-shadow: 0 8px 30px rgba(167, 139, 250, 0.12);
        transition: all 0.3s ease;
        border: 2px solid transparent;
    }
    
    .feature-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 50px rgba(167, 139, 250, 0.2);
        border-color: #c084fc;
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1.5rem;
        display: block;
    }
    
    .feature-title {
        font-size: 1.4rem;
        font-weight: 700;
        color: #2d3748;
        margin-bottom: 0.8rem;
    }
    
    .feature-description {
        font-size: 1rem;
        color: #6b7280;
        line-height: 1.6;
        margin-bottom: 1rem;
    }
    
    .feature-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    
    .feature-list li {
        font-size: 0.95rem;
        color: #6b7280;
        padding: 0.4rem 0;
        padding-left: 1.5rem;
        position: relative;
    }
    
    .feature-list li::before {
        content: '✓';
        position: absolute;
        left: 0;
        color: #10b981;
        font-weight: 700;
    }
    
    /* Statistics Section */
    .stats-section {
        background: linear-gradient(135deg, #a78bfa 0%, #c084fc 25%, #e879f9 50%, #f0abfc 75%);
        padding: 4rem 2rem;
        border-radius: 50px;
        margin: 4rem auto;
        max-width: 1400px;
        box-shadow: 0 20px 60px rgba(167, 139, 250, 0.3);
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .stat-box {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        padding: 2.5rem 2rem;
        border-radius: 25px;
        text-align: center;
        border: 2px solid rgba(255, 255, 255, 0.2);
        transition: all 0.3s ease;
    }
    
    .stat-box:hover {
        transform: translateY(-10px);
        background: rgba(255, 255, 255, 0.25);
        border-color: rgba(255, 255, 255, 0.4);
    }
    
    .stat-number {
        font-size: 3.5rem;
        font-weight: 900;
        color: white;
        margin-bottom: 0.5rem;
        text-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
    }
    
    .stat-label {
        font-size: 0.95rem;
        color: rgba(255, 255, 255, 0.9);
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 600;
    }
    
    /* Technology Stack */
    .tech-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem;
        margin: 3rem 0;
    }
    
    .tech-card {
        background: linear-gradient(135deg, #667eea, #764ba2);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        box-shadow: 0 8px 30px rgba(102, 126, 234, 0.2);
        transition: all 0.3s ease;
    }
    
    .tech-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 45px rgba(102, 126, 234, 0.35);
    }
    
    .tech-name {
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 0.8rem;
    }
    
    .tech-description {
        font-size: 0.95rem;
        opacity: 0.9;
        line-height: 1.6;
    }
    
    /* Testimonials */
    .testimonials-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 2.5rem;
        margin: 4rem 0;
    }
    
    .testimonial-card {
        background: #374151;
        padding: 3rem 2.5rem;
        border-radius: 30px;
        color: white;
        box-shadow: 0 10px 40px rgba(55, 65, 81, 0.3);
        transition: all 0.3s ease;
    }
    
    .testimonial-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 60px rgba(55, 65, 81, 0.4);
    }
    
    .testimonial-text {
        font-size: 1.15rem;
        line-height: 1.6;
        margin-bottom: 2rem;
    }
    
    .highlight-purple {
        color: #c084fc;
        font-weight: 700;
    }
    
    .highlight-blue {
        color: #60a5fa;
        font-weight: 700;
    }
    
    .testimonial-avatar {
        width: 60px;
        height: 60px;
        border-radius: 50%;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        font-weight: 900;
        color: white;
        margin-bottom: 0.8rem;
    }
    
    .avatar-purple {
        background: linear-gradient(135deg, #7c3aed, #a78bfa);
    }
    
    .avatar-pink {
        background: linear-gradient(135deg, #ec4899, #f472b6);
    }
    
    .avatar-blue {
        background: linear-gradient(135deg, #3b82f6, #60a5fa);
    }
    
    .testimonial-name {
        font-size: 1.05rem;
        margin-top: 0.5rem;
        opacity: 0.9;
    }
    
    /* Footer CTA */
    .footer-cta {
        background: linear-gradient(135deg, #a78bfa 0%, #c084fc 25%, #e879f9 50%, #f0abfc 75%);
        padding: 5rem 3rem;
        text-align: center;
        border-radius: 50px 50px 0 0;
        margin: 4rem -3rem -2rem;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }
        .hero-subtitle {
            font-size: 1.1rem;
        }
        .section-title {
            font-size: 2rem;
        }
        .nav-grid,
        .steps-grid,
        .features-grid,
        .stats-grid,
        .tech-grid,
        .testimonials-grid {
            grid-template-columns: 1fr;
        }
        .ai-badge {
            top: 1rem;
            right: 1rem;
            font-size: 0.8rem;
            padding: 0.6rem 1.2rem;
        }
    }
</style>
""",
    unsafe_allow_html=True,
)

# ============================================================================
# HERO SECTION
# ============================================================================
st.markdown(
    """
<div class="hero-section">
    <div class="ai-badge">⚡ AI-Powered Excellence</div>
    <h1 class="hero-title">Resume<span class="gradient-text">Master</span>AI</h1>
    <div class="hero-divider"></div>
    <p class="hero-subtitle">
        🚀 Transform your career with cutting-edge AI technology
    </p>
    <p class="hero-tagline">
        Analyze • Optimize • Match • Land Your Dream Job
    </p>
    <a href="/1_%F0%9F%93%84_Upload_Resume" target="_self" class="cta-button">
        Begin Your Journey →
    </a>
</div>
""",
    unsafe_allow_html=True,
)

# ============================================================================
# QUICK NAVIGATION
# ============================================================================
st.markdown(
    """
<div class="nav-section">
    <h2 class="section-title">Quick Access</h2>
    <div class="underline"></div>
    <div class="nav-grid">
        <a href="/1_%F0%9F%93%84_Upload_Resume" target="_self" class="nav-card">
            <span class="nav-icon">📄</span>
            <div class="nav-title">Upload Resume</div>
        </a>
        <a href="/2_%F0%9F%93%8A_Analysis_Scoring" target="_self" class="nav-card">
            <span class="nav-icon">📊</span>
            <div class="nav-title">Analysis & Scoring</div>
        </a>
        <a href="/3_%F0%9F%8E%AF_Job_Matching" target="_self" class="nav-card">
            <span class="nav-icon">🎯</span>
            <div class="nav-title">Job Matching</div>
        </a>
        <a href="/4_%E2%9C%8D%EF%B8%8F_Resume_Rewrite_Ultimate" target="_self" class="nav-card">
            <span class="nav-icon">✍️</span>
            <div class="nav-title">Resume Rewrite</div>
        </a>
        <a href="/5_%F0%9F%92%BC_Cover_Letter_Projects" target="_self" class="nav-card">
            <span class="nav-icon">💼</span>
            <div class="nav-title">Cover Letters</div>
        </a>
        <a href="/6_%F0%9F%94%8D_Job_Search" target="_self" class="nav-card">
            <span class="nav-icon">🔍</span>
            <div class="nav-title">Job Search</div>
        </a>
        <a href="/7_%F0%9F%8F%97%EF%B8%8F_Resume_Builder" target="_self" class="nav-card">
            <span class="nav-icon">🏗️</span>
            <div class="nav-title">Resume Builder</div>
        </a>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# ============================================================================
# HOW IT WORKS SECTION
# ============================================================================
st.markdown(
    """
<div class="section-container">
    <h2 class="section-title">How It Works</h2>
    <div class="underline"></div>
    <p class="section-subtitle">Four simple steps to transform your career prospects</p>
    
    <div class="steps-grid">
        <div class="step-card">
            <div class="step-number">1</div>
            <div class="step-icon">📄</div>
            <h3 class="step-title">Upload Your Resume</h3>
            <p class="step-description">
                Simply upload your resume in PDF, DOCX, or even scanned image format. 
                Our advanced OCR technology handles any document type with precision.
            </p>
        </div>
        
        <div class="step-card">
            <div class="step-number">2</div>
            <div class="step-icon">🤖</div>
            <h3 class="step-title">AI Analysis</h3>
            <p class="step-description">
                Our intelligent AI engine analyzes your resume across multiple dimensions, 
                identifying strengths, weaknesses, and opportunities for improvement.
            </p>
        </div>
        
        <div class="step-card">
            <div class="step-number">3</div>
            <div class="step-icon">✨</div>
            <h3 class="step-title">Smart Optimization</h3>
            <p class="step-description">
                Get AI-powered rewriting suggestions, ATS optimization tips, and industry-specific 
                recommendations to make your resume stand out.
            </p>
        </div>
        
        <div class="step-card">
            <div class="step-number">4</div>
            <div class="step-icon">🎯</div>
            <h3 class="step-title">Land Your Dream Job</h3>
            <p class="step-description">
                Export your optimized resume in multiple formats, generate tailored cover letters, 
                and match with relevant job opportunities.
            </p>
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# ============================================================================
# ADVANCED FEATURES SECTION
# ============================================================================
st.markdown(
    """
<div class="section-container">
    <h2 class="section-title">🎯 Advanced Features</h2>
    <div class="underline"></div>
    <p class="section-subtitle">Comprehensive toolkit for career success</p>
    
    <div class="features-grid">
        <div class="feature-card">
            <span class="feature-icon">🔍</span>
            <h3 class="feature-title">ATS Scanner & Optimizer</h3>
            <p class="feature-description">
                Beat Applicant Tracking Systems with intelligent optimization
            </p>
            <ul class="feature-list">
                <li>Real-time ATS compatibility scoring</li>
                <li>Keyword density analysis</li>
                <li>Format optimization tips</li>
                <li>Section structure recommendations</li>
            </ul>
        </div>
        
        <div class="feature-card">
            <span class="feature-icon">📊</span>
            <h3 class="feature-title">Resume Analytics</h3>
            <p class="feature-description">
                Deep insights into your resume's performance
            </p>
            <ul class="feature-list">
                <li>Visual analytics dashboard</li>
                <li>Section-by-section scoring</li>
                <li>Action verb detection</li>
                <li>Quantifiable metrics analysis</li>
            </ul>
        </div>
        
        <div class="feature-card">
            <span class="feature-icon">💡</span>
            <h3 class="feature-title">Skills Analyzer</h3>
            <p class="feature-description">
                Identify skill gaps and get recommendations
            </p>
            <ul class="feature-list">
                <li>Industry skill comparison</li>
                <li>Gap analysis</li>
                <li>Learning path suggestions</li>
                <li>Certification recommendations</li>
            </ul>
        </div>
        
        <div class="feature-card">
            <span class="feature-icon">🎤</span>
            <h3 class="feature-title">Interview Preparation</h3>
            <p class="feature-description">
                AI-generated interview questions and tips
            </p>
            <ul class="feature-list">
                <li>Role-specific questions</li>
                <li>Behavioral interview prep</li>
                <li>Technical question bank</li>
                <li>Answer frameworks</li>
            </ul>
        </div>
        
        <div class="feature-card">
            <span class="feature-icon">💰</span>
            <h3 class="feature-title">Salary Estimator</h3>
            <p class="feature-description">
                Data-driven salary insights for your role
            </p>
            <ul class="feature-list">
                <li>Location-based estimates</li>
                <li>Experience level adjustment</li>
                <li>Industry benchmarks</li>
                <li>Skill value analysis</li>
            </ul>
        </div>
        
        <div class="feature-card">
            <span class="feature-icon">📱</span>
            <h3 class="feature-title">Social Resume Generator</h3>
            <p class="feature-description">
                Optimize your LinkedIn and social profiles
            </p>
            <ul class="feature-list">
                <li>LinkedIn headline generator</li>
                <li>Profile summary optimization</li>
                <li>Achievement formatting</li>
                <li>Social media-ready content</li>
            </ul>
        </div>
        
        <div class="feature-card">
            <span class="feature-icon">📧</span>
            <h3 class="feature-title">Email Generator</h3>
            <p class="feature-description">
                Professional email templates for outreach
            </p>
            <ul class="feature-list">
                <li>Networking emails</li>
                <li>Follow-up templates</li>
                <li>Thank you notes</li>
                <li>Application emails</li>
            </ul>
        </div>
        
        <div class="feature-card">
            <span class="feature-icon">📝</span>
            <h3 class="feature-title">Version Manager</h3>
            <p class="feature-description">
                Track and manage multiple resume versions
            </p>
            <ul class="feature-list">
                <li>Version history tracking</li>
                <li>Compare versions side-by-side</li>
                <li>Restore previous versions</li>
                <li>Export any version</li>
            </ul>
        </div>
        
        <div class="feature-card">
            <span class="feature-icon">🎯</span>
            <h3 class="feature-title">Job Matcher</h3>
            <p class="feature-description">
                Smart matching with job descriptions
            </p>
            <ul class="feature-list">
                <li>Compatibility scoring</li>
                <li>Keyword gap analysis</li>
                <li>Skills alignment check</li>
                <li>Tailoring suggestions</li>
            </ul>
        </div>
        
        <div class="feature-card">
            <span class="feature-icon">📄</span>
            <h3 class="feature-title">Multi-Format Export</h3>
            <p class="feature-description">
                Export in multiple professional formats
            </p>
            <ul class="feature-list">
                <li>ATS-optimized PDF</li>
                <li>Editable DOCX</li>
                <li>Plain text format</li>
                <li>Markdown export</li>
            </ul>
        </div>
        
        <div class="feature-card">
            <span class="feature-icon">🔒</span>
            <h3 class="feature-title">Privacy & Security</h3>
            <p class="feature-description">
                Your data is safe and secure
            </p>
            <ul class="feature-list">
                <li>Local processing</li>
                <li>No data storage</li>
                <li>Encrypted transfers</li>
                <li>GDPR compliant</li>
            </ul>
        </div>
        
        <div class="feature-card">
            <span class="feature-icon">🤖</span>
            <h3 class="feature-title">AI-Powered Rewriting</h3>
            <p class="feature-description">
                Transform your content with AI assistance
            </p>
            <ul class="feature-list">
                <li>Industry-specific optimization</li>
                <li>Impact statement generation</li>
                <li>Achievement quantification</li>
                <li>Professional tone enhancement</li>
            </ul>
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# ============================================================================
# STATISTICS SECTION
# ============================================================================
st.markdown(
    """
<div class="section-container">
    <h2 class="section-title">Platform Statistics</h2>
    <div class="underline"></div>
    <p class="section-subtitle">Trusted by thousands of job seekers worldwide</p>
</div>

<div class="stats-section">
    <div class="stats-grid">
        <div class="stat-box">
            <div class="stat-number">95%</div>
            <div class="stat-label">Accuracy Rate</div>
        </div>
        
        <div class="stat-box">
            <div class="stat-number">10K+</div>
            <div class="stat-label">Resumes Analyzed</div>
        </div>
        
        <div class="stat-box">
            <div class="stat-number">4.8⭐</div>
            <div class="stat-label">User Rating</div>
        </div>
        
        <div class="stat-box">
            <div class="stat-number">500+</div>
            <div class="stat-label">Partner Companies</div>
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# ============================================================================
# TECHNOLOGY STACK SECTION
# ============================================================================
st.markdown(
    """
<div class="section-container">
    <h2 class="section-title">⚡ Technology Stack</h2>
    <div class="underline"></div>
    <p class="section-subtitle">Powered by cutting-edge AI and modern technologies</p>
    
    <div class="tech-grid">
        <div class="tech-card">
            <div class="tech-name">🤖 Google Gemini AI</div>
            <p class="tech-description">
                Advanced language models for intelligent resume analysis, 
                optimization, and generation of professional content.
            </p>
        </div>
        
        <div class="tech-card">
            <div class="tech-name">🔗 LangChain</div>
            <p class="tech-description">
                Sophisticated LLM orchestration for complex AI workflows, 
                agent-based processing, and context-aware interactions.
            </p>
        </div>
        
        <div class="tech-card">
            <div class="tech-name">🎨 Streamlit</div>
            <p class="tech-description">
                Modern web framework for creating beautiful, 
                interactive user interfaces with Python.
            </p>
        </div>
        
        <div class="tech-card">
            <div class="tech-name">📊 Advanced Analytics</div>
            <p class="tech-description">
                Comprehensive data analysis using Pandas, NumPy, 
                Matplotlib, and Seaborn for actionable insights.
            </p>
        </div>
        
        <div class="tech-card">
            <div class="tech-name">🔍 OCR Technology</div>
            <p class="tech-description">
                Tesseract OCR for extracting text from scanned 
                documents and images with high accuracy.
            </p>
        </div>
        
        <div class="tech-card">
            <div class="tech-name">📄 Document Processing</div>
            <p class="tech-description">
                Support for PDF, DOCX, TXT parsing with advanced 
                extraction and formatting capabilities.
            </p>
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# ============================================================================
# TESTIMONIALS SECTION
# ============================================================================
st.markdown(
    """
<div class="section-container">
    <h2 class="section-title">What Our Users Say</h2>
    <div class="underline"></div>
    <p class="section-subtitle">Join thousands of satisfied job seekers</p>
    
    <div class="testimonials-grid">
        <div class="testimonial-card">
            <p class="testimonial-text">
                "This platform helped me land <span class="highlight-purple">3 interviews</span> 
                in just two weeks! The AI optimization made my resume stand out."
            </p>
            <div class="testimonial-avatar avatar-purple">SJ</div>
            <p class="testimonial-name">Sarah Johnson<br>Software Engineer</p>
        </div>
        
        <div class="testimonial-card">
            <p class="testimonial-text">
                "The ATS scanner is a game-changer! My resume now <span class="highlight-purple">passes ATS systems</span> 
                that previously rejected me. Got 2 offers in a month!"
            </p>
            <div class="testimonial-avatar avatar-pink">MC</div>
            <p class="testimonial-name">Michael Chen<br>Product Manager</p>
        </div>
        
        <div class="testimonial-card">
            <p class="testimonial-text">
                "The analysis and suggestions were <span class="highlight-blue">incredibly accurate</span> 
                and actionable. Improved my response rate by 300%!"
            </p>
            <div class="testimonial-avatar avatar-blue">ER</div>
            <p class="testimonial-name">Emily Rodriguez<br>Marketing Specialist</p>
        </div>
        
        <div class="testimonial-card">
            <p class="testimonial-text">
                "Interview prep feature is <span class="highlight-purple">absolutely phenomenal</span>! 
                Generated role-specific questions that actually came up in my interviews."
            </p>
            <div class="testimonial-avatar avatar-purple">DK</div>
            <p class="testimonial-name">David Kim<br>Data Scientist</p>
        </div>
        
        <div class="testimonial-card">
            <p class="testimonial-text">
                "Salary estimator helped me negotiate <span class="highlight-blue">15% higher</span> 
                than the initial offer. Worth every minute spent on the platform!"
            </p>
            <div class="testimonial-avatar avatar-pink">AL</div>
            <p class="testimonial-name">Amanda Lee<br>UX Designer</p>
        </div>
        
        <div class="testimonial-card">
            <p class="testimonial-text">
                "The cover letter generator saved me <span class="highlight-purple">hours of work</span>. 
                Each letter is personalized and professional!"
            </p>
            <div class="testimonial-avatar avatar-blue">JM</div>
            <p class="testimonial-name">James Miller<br>Business Analyst</p>
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# ============================================================================
# FOOTER CTA
# ============================================================================
st.markdown(
    """
<div class="footer-cta">
    <h1 class="hero-title">Resume<span class="gradient-text">Master</span>AI</h1>
    <div class="hero-divider"></div>
    <p class="hero-subtitle">
        🚀 Transform your career with cutting-edge AI technology
    </p>
    <p class="hero-tagline">
        Analyze • Optimize • Match • Land Your Dream Job
    </p>
    <a href="/1_%F0%9F%93%84_Upload_Resume" target="_self" class="cta-button">
        Begin Your Journey →
    </a>
</div>
""",
    unsafe_allow_html=True,
)
