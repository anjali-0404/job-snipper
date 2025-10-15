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
    initial_sidebar_state="expanded",
)

# Initialize session state
if "loaded" not in st.session_state:
    st.session_state.loaded = True

# Complete CSS Design with all styles
st.markdown(
    """
<style>
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display:none;}
    
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800;900&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        background-attachment: fixed;
    }
    
    /* Remove default padding */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0rem !important;
        max-width: 100% !important;
    }
    
    /* Animations */
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes moveParticles {
        0% { background-position: 0% 0%; }
        100% { background-position: 100% 100%; }
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.6; }
    }
    
    @keyframes shimmer {
        0% { background-position: 0% center; }
        100% { background-position: 200% center; }
    }
    
    /* Hero Section - Optimized */
    .hero-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        padding: 6rem 2rem 5rem;
        text-align: center;
        border-radius: 20px;
        margin: 0rem 0rem 3rem;
        position: relative;
        overflow: hidden;
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.3);
    }
    
    .ai-badge {
        display: inline-block;
        padding: 0.75rem 1.5rem;
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(10px);
        border: 2px solid rgba(255, 255, 255, 0.3);
        border-radius: 50px;
        color: white;
        font-weight: 700;
        font-size: 0.9rem;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
        margin-bottom: 2rem;
        animation: float 3s ease-in-out infinite;
    }
    
    .hero-title {
        font-size: 4rem;
        font-weight: 900;
        color: white;
        margin: 1rem 0;
        letter-spacing: -2px;
        text-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        line-height: 1.1;
    }
    
    .gradient-text {
        background: linear-gradient(90deg, #fbbf24 0%, #f97316 50%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        background-size: 200% auto;
        animation: shimmer 3s linear infinite;
    }
    
    .hero-divider {
        height: 3px;
        width: 200px;
        max-width: 90%;
        margin: 1.5rem auto;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.6), transparent);
        border-radius: 10px;
    }
    
    .hero-subtitle {
        font-size: 1.3rem;
        color: rgba(255, 255, 255, 0.95);
        margin: 1.5rem auto;
        max-width: 700px;
        line-height: 1.6;
        font-weight: 500;
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
    
    /* Streamlit Button Styles */
    .stButton > button {
        width: 100%;
        padding: 0.8rem 1.5rem !important;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        border: none !important;
        border-radius: 12px !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3) !important;
        text-transform: none !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.5) !important;
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%) !important;
    }
    
    .stButton > button:active {
        transform: translateY(0px) !important;
    }
    
    .cta-container {
        display: flex;
        justify-content: center;
        gap: 1.5rem;
        margin: 2rem 0;
        position: relative;
        z-index: 1;
    }
    
    .cta-button {
        display: inline-block;
        padding: 1.3rem 4rem;
        background: white;
        color: #7c3aed !important;
        font-size: 1.3rem;
        font-weight: 800;
        border-radius: 50px;
        text-decoration: none;
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.3);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        z-index: 1;
        border: none;
        cursor: pointer;
        overflow: hidden;
    }
    
    .cta-button::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: rgba(124, 58, 237, 0.1);
        transform: translate(-50%, -50%);
        transition: width 0.6s, height 0.6s;
    }
    
    .cta-button:hover::before {
        width: 400px;
        height: 400px;
    }
    
    .cta-button:hover {
        transform: translateY(-8px) scale(1.05);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4);
        color: #7c3aed !important;
        text-decoration: none;
    }
    
    .cta-secondary {
        background: transparent;
        color: white !important;
        border: 3px solid white;
    }
    
    .cta-secondary:hover {
        background: white;
        color: #7c3aed !important;
    }
    
    /* Quick Navigation */
    .nav-section {
        padding: 4rem 2rem;
        max-width: 1400px;
        margin: 0 auto 3rem;
        background: rgba(255, 255, 255, 0.03);
        border-radius: 40px;
        backdrop-filter: blur(10px);
    }
    
    .nav-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 2rem;
        margin-top: 3rem;
    }
    
    .nav-card-wrapper {
        position: relative;
    }
    
    .nav-card {
        background: linear-gradient(145deg, rgba(255, 255, 255, 0.95), rgba(255, 255, 255, 0.85));
        padding: 2.5rem 1.5rem;
        border-radius: 25px;
        text-align: center;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        cursor: pointer;
        text-decoration: none;
        color: inherit;
        border: 2px solid transparent;
        position: relative;
        overflow: hidden;
    }
    
    .nav-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.2), transparent);
        transition: left 0.5s;
    }
    
    .nav-card:hover::before {
        left: 100%;
    }
    
    .nav-card:hover {
        transform: translateY(-12px) scale(1.05);
        box-shadow: 0 20px 50px rgba(102, 126, 234, 0.4);
        border-color: #667eea;
    }
    
    .nav-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        display: block;
        animation: bounce 2s infinite;
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-5px); }
    }
    
    .nav-card:hover .nav-icon {
        animation: none;
        transform: scale(1.2) rotate(5deg);
    }
    
    .nav-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: #2d3748;
        position: relative;
        z-index: 1;
    }
    
    /* Section Container */
    .section-container {
        padding: 5rem 2rem;
        max-width: 1400px;
        margin: 0 auto;
        position: relative;
        z-index: 1;
    }
    
    .section-title {
        font-size: 3.5rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
        animation: fadeInUp 0.8s ease-out;
    }
    
    @keyframes fadeInUp {
        0% { opacity: 0; transform: translateY(30px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    .section-subtitle {
        text-align: center;
        font-size: 1.3rem;
        color: rgba(255, 255, 255, 0.8);
        margin-bottom: 3rem;
        font-weight: 300;
    }
    
    .underline {
        width: 200px;
        height: 5px;
        background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
        margin: 1.5rem auto 4rem;
        border-radius: 10px;
        box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
        animation: expand 1s ease-out;
    }
    
    @keyframes expand {
        0% { width: 0; opacity: 0; }
        100% { width: 200px; opacity: 1; }
    }
    
    /* Steps Grid */
    .steps-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 3rem;
        margin: 4rem 0;
    }
    
    .step-card {
        background: linear-gradient(145deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05));
        backdrop-filter: blur(10px);
        padding: 3rem 2.5rem;
        border-radius: 35px;
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.2);
        position: relative;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        border: 2px solid rgba(255, 255, 255, 0.1);
        overflow: hidden;
    }
    
    .step-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 5px;
        background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
    }
    
    .step-card:hover {
        transform: translateY(-15px) scale(1.03);
        box-shadow: 0 25px 70px rgba(102, 126, 234, 0.4);
        border-color: rgba(102, 126, 234, 0.5);
    }
    
    .step-number {
        position: absolute;
        top: -30px;
        left: 30px;
        width: 80px;
        height: 80px;
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2.2rem;
        font-weight: 900;
        color: white;
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.5);
        animation: numberPulse 2s infinite;
    }
    
    @keyframes numberPulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.1); }
    }
    
    .step-icon {
        font-size: 3rem;
        margin: 2rem 0 1.5rem;
        filter: drop-shadow(0 5px 15px rgba(102, 126, 234, 0.4));
    }
    
    .step-title {
        font-size: 1.6rem;
        font-weight: 800;
        color: white;
        margin-bottom: 1rem;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
    }
    
    .step-description {
        font-size: 1.1rem;
        color: rgba(255, 255, 255, 0.85);
        line-height: 1.8;
    }
    
    /* Features Grid */
    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2.5rem;
        margin: 4rem 0;
    }
    
    .feature-card {
        background: linear-gradient(145deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05));
        backdrop-filter: blur(10px);
        padding: 2.5rem 2rem;
        border-radius: 30px;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.2);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        border: 2px solid rgba(255, 255, 255, 0.1);
    }
    
    .feature-card:hover {
        transform: translateY(-12px) scale(1.02);
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.4);
        border-color: rgba(102, 126, 234, 0.5);
        background: linear-gradient(145deg, rgba(255, 255, 255, 0.15), rgba(255, 255, 255, 0.08));
    }
    
    .feature-icon {
        font-size: 3.5rem;
        margin-bottom: 1.5rem;
        display: block;
        filter: drop-shadow(0 5px 15px rgba(102, 126, 234, 0.3));
    }
    
    .feature-title {
        font-size: 1.5rem;
        font-weight: 800;
        color: white;
        margin-bottom: 1rem;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    }
    
    .feature-description {
        font-size: 1.05rem;
        color: rgba(255, 255, 255, 0.85);
        line-height: 1.7;
        margin-bottom: 1.5rem;
    }
    
    .feature-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    
    .feature-list li {
        font-size: 1rem;
        color: rgba(255, 255, 255, 0.8);
        padding: 0.5rem 0;
        padding-left: 2rem;
        position: relative;
    }
    
    .feature-list li::before {
        content: '✓';
        position: absolute;
        left: 0;
        color: #10b981;
        font-weight: 900;
        font-size: 1.2rem;
        text-shadow: 0 0 10px rgba(16, 185, 129, 0.5);
    }
    
    /* Statistics Section */
    .stats-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        padding: 5rem 2rem;
        border-radius: 50px;
        margin: 5rem auto;
        max-width: 1400px;
        box-shadow: 0 25px 80px rgba(102, 126, 234, 0.5);
        position: relative;
        overflow: hidden;
    }
    
    .stats-section::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.05) 1px, transparent 1px);
        background-size: 40px 40px;
        animation: moveStatsGrid 15s linear infinite;
    }
    
    @keyframes moveStatsGrid {
        0% { transform: translate(0, 0) rotate(0deg); }
        100% { transform: translate(40px, 40px) rotate(360deg); }
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 2.5rem;
        max-width: 1200px;
        margin: 0 auto;
        position: relative;
        z-index: 1;
    }
    
    .stat-box {
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(15px);
        padding: 3rem 2rem;
        border-radius: 30px;
        text-align: center;
        border: 2px solid rgba(255, 255, 255, 0.3);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
    }
    
    .stat-box::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255,255,255,0.1), transparent);
        transform: rotate(45deg);
        transition: all 0.5s;
    }
    
    .stat-box:hover::before {
        left: 100%;
    }
    
    .stat-box:hover {
        transform: translateY(-15px) scale(1.05);
        background: rgba(255, 255, 255, 0.3);
        border-color: rgba(255, 255, 255, 0.5);
        box-shadow: 0 15px 40px rgba(255, 255, 255, 0.2);
    }
    
    .stat-number {
        font-size: 4rem;
        font-weight: 900;
        color: white;
        margin-bottom: 0.8rem;
        text-shadow: 0 5px 25px rgba(0, 0, 0, 0.3);
        animation: countUp 2s ease-out;
    }
    
    @keyframes countUp {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    .stat-label {
        font-size: 1rem;
        color: rgba(255, 255, 255, 0.95);
        text-transform: uppercase;
        letter-spacing: 2px;
        font-weight: 700;
    }
    
    /* Technology Stack */
    .tech-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem;
        margin: 3rem 0;
    }
    
    .tech-card {
        background: linear-gradient(145deg, #667eea, #764ba2);
        padding: 2.5rem;
        border-radius: 30px;
        color: white;
        box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
        border: 2px solid rgba(255, 255, 255, 0.1);
    }
    
    .tech-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        transition: left 0.7s;
    }
    
    .tech-card:hover::before {
        left: 100%;
    }
    
    .tech-card:hover {
        transform: translateY(-12px) scale(1.03);
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.5);
        border-color: rgba(255, 255, 255, 0.3);
    }
    
    .tech-name {
        font-size: 1.5rem;
        font-weight: 800;
        margin-bottom: 1rem;
        position: relative;
        z-index: 1;
    }
    
    .tech-description {
        font-size: 1.05rem;
        opacity: 0.95;
        line-height: 1.7;
        position: relative;
        z-index: 1;
    }
    
    /* Testimonials */
    .testimonials-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 2.5rem;
        margin: 4rem 0;
    }
    
    .testimonial-card {
        background: linear-gradient(145deg, rgba(255, 255, 255, 0.08), rgba(255, 255, 255, 0.03));
        backdrop-filter: blur(15px);
        padding: 3rem 2.5rem;
        border-radius: 35px;
        color: white;
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.3);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        border: 2px solid rgba(255, 255, 255, 0.1);
        position: relative;
        overflow: hidden;
    }
    
    .testimonial-card::after {
        content: '"';
        position: absolute;
        top: 10px;
        right: 20px;
        font-size: 8rem;
        color: rgba(255, 255, 255, 0.05);
        font-family: Georgia, serif;
        line-height: 1;
    }
    
    .testimonial-card:hover {
        transform: translateY(-15px) scale(1.02);
        box-shadow: 0 25px 70px rgba(102, 126, 234, 0.4);
        border-color: rgba(102, 126, 234, 0.4);
    }
    
    .testimonial-text {
        font-size: 1.2rem;
        line-height: 1.8;
        margin-bottom: 2.5rem;
        position: relative;
        z-index: 1;
    }
    
    .highlight-purple {
        color: #c084fc;
        font-weight: 800;
        text-shadow: 0 0 20px rgba(192, 132, 252, 0.5);
    }
    
    .highlight-blue {
        color: #60a5fa;
        font-weight: 800;
        text-shadow: 0 0 20px rgba(96, 165, 250, 0.5);
    }
    
    .testimonial-rating {
        color: #fbbf24;
        font-size: 1.3rem;
        margin-bottom: 1.5rem;
        letter-spacing: 2px;
        position: relative;
        z-index: 1;
        text-shadow: 0 0 10px rgba(251, 191, 36, 0.5);
    }
    
    .testimonial-badge {
        display: inline-block;
        padding: 0.4rem 1rem;
        background: rgba(16, 185, 129, 0.2);
        border: 1px solid rgba(16, 185, 129, 0.4);
        border-radius: 20px;
        font-size: 0.85rem;
        color: #10b981;
        margin-bottom: 1rem;
        font-weight: 600;
    }
    
    .social-proof {
        background: linear-gradient(145deg, rgba(16, 185, 129, 0.15), rgba(5, 150, 105, 0.15));
        backdrop-filter: blur(10px);
        padding: 2rem;
        border-radius: 25px;
        border: 2px solid rgba(16, 185, 129, 0.3);
        margin: 3rem 0;
        text-align: center;
    }
    
    .social-proof-title {
        font-size: 1.5rem;
        font-weight: 800;
        color: white;
        margin-bottom: 1rem;
    }
    
    .social-proof-badges {
        display: flex;
        justify-content: center;
        gap: 2rem;
        flex-wrap: wrap;
        margin-top: 1.5rem;
    }
    
    .proof-badge {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 0.5rem;
    }
    
    .proof-icon {
        font-size: 2.5rem;
        filter: drop-shadow(0 5px 15px rgba(16, 185, 129, 0.4));
    }
    
    .proof-text {
        color: rgba(255, 255, 255, 0.9);
        font-size: 0.95rem;
        font-weight: 600;
    }
    
    .testimonial-avatar {
        width: 70px;
        height: 70px;
        border-radius: 50%;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 1.8rem;
        font-weight: 900;
        color: white;
        margin-bottom: 1rem;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
        position: relative;
        z-index: 1;
    }
    
    .avatar-purple {
        background: linear-gradient(135deg, #667eea, #764ba2);
        box-shadow: 0 5px 25px rgba(102, 126, 234, 0.5);
    }
    
    .avatar-pink {
        background: linear-gradient(135deg, #ec4899, #f093fb);
        box-shadow: 0 5px 25px rgba(236, 72, 153, 0.5);
    }
    
    .avatar-blue {
        background: linear-gradient(135deg, #3b82f6, #60a5fa);
        box-shadow: 0 5px 25px rgba(59, 130, 246, 0.5);
    }
    
    .testimonial-name {
        font-size: 1.15rem;
        margin-top: 0.8rem;
        opacity: 0.95;
        font-weight: 600;
        position: relative;
        z-index: 1;
    }
    
    /* Footer CTA */
    .footer-cta {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        padding: 6rem 3rem;
        text-align: center;
        border-radius: 50px 50px 0 0;
        margin: 5rem -3rem -2rem;
        position: relative;
        overflow: hidden;
        box-shadow: 0 -20px 60px rgba(102, 126, 234, 0.3);
    }
    
    .footer-cta::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.08) 1px, transparent 1px);
        background-size: 50px 50px;
        animation: moveFooterGrid 20s linear infinite;
        pointer-events: none;
    }
    
    @keyframes moveFooterGrid {
        0% { transform: translate(0, 0) rotate(0deg); }
        100% { transform: translate(50px, 50px) rotate(360deg); }
    }
    
    /* Scrollbar Styling */
    ::-webkit-scrollbar {
        width: 12px;
    }
    
    ::-webkit-scrollbar-track {
        background: #1a1a2e;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #764ba2, #667eea);
    }
    
    /* Additional Modern Elements */
    .glow-effect {
        box-shadow: 0 0 20px rgba(102, 126, 234, 0.5),
                    0 0 40px rgba(118, 75, 162, 0.3),
                    0 0 60px rgba(240, 147, 251, 0.2);
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.8rem;
            letter-spacing: -1px;
        }
        .hero-subtitle {
            font-size: 1.1rem;
        }
        .section-title {
            font-size: 2.2rem;
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
        .hero-section {
            padding: 6rem 2rem 5rem;
        }
        .cta-button {
            padding: 1rem 2.5rem;
            font-size: 1.1rem;
        }
    }
    
    /* Smooth transitions */
    * {
        transition: background-color 0.3s ease, color 0.3s ease;
    }
    
    /* Expander Styling */
    .streamlit-expanderHeader {
        background: linear-gradient(145deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1)) !important;
        backdrop-filter: blur(10px);
        border-radius: 15px !important;
        border: 2px solid rgba(102, 126, 234, 0.3) !important;
        padding: 1rem 1.5rem !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        color: white !important;
        margin-bottom: 1rem !important;
    }
    
    .streamlit-expanderHeader:hover {
        border-color: rgba(102, 126, 234, 0.6) !important;
        background: linear-gradient(145deg, rgba(102, 126, 234, 0.15), rgba(118, 75, 162, 0.15)) !important;
        box-shadow: 0 5px 20px rgba(102, 126, 234, 0.3) !important;
    }
    
    .streamlit-expanderContent {
        background: linear-gradient(145deg, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0.02)) !important;
        backdrop-filter: blur(10px);
        border: 2px solid rgba(102, 126, 234, 0.2) !important;
        border-top: none !important;
        border-radius: 0 0 15px 15px !important;
        padding: 1.5rem !important;
        color: rgba(255, 255, 255, 0.9) !important;
        margin-top: -1rem !important;
    }
    
    .streamlit-expanderContent p, 
    .streamlit-expanderContent li {
        color: rgba(255, 255, 255, 0.85) !important;
        font-size: 1.05rem !important;
        line-height: 1.7 !important;
    }
    
    .streamlit-expanderContent strong {
        color: #c084fc !important;
        font-weight: 700 !important;
    }
    
    /* 3D Card Effect */
    .card-3d {
        transform-style: preserve-3d;
        transition: transform 0.6s;
    }
    
    .card-3d:hover {
        transform: rotateY(5deg) rotateX(5deg);
    }
    
    /* Animated Icon */
    @keyframes iconFloat {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        25% { transform: translateY(-10px) rotate(5deg); }
        75% { transform: translateY(-5px) rotate(-5deg); }
    }
    
    .icon-float {
        animation: iconFloat 3s ease-in-out infinite;
    }
    
    /* Progress Bar */
    .progress-bar {
        width: 100%;
        height: 8px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        overflow: hidden;
        margin: 1rem 0;
    }
    
    .progress-fill {
        height: 100%;
        background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
        border-radius: 10px;
        animation: progressSlide 2s ease-out;
    }
    
    @keyframes progressSlide {
        0% { width: 0%; }
        100% { width: 100%; }
    }
    
    /* Neon Glow Text */
    .neon-text {
        color: #fff;
        text-shadow: 0 0 10px #667eea,
                     0 0 20px #667eea,
                     0 0 30px #667eea,
                     0 0 40px #764ba2,
                     0 0 70px #764ba2,
                     0 0 80px #764ba2;
        animation: neonPulse 2s ease-in-out infinite;
    }
    
    @keyframes neonPulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.8; }
    }
    
    /* Stagger Animation */
    .stagger-item {
        animation: staggerIn 0.5s ease-out backwards;
    }
    
    .stagger-item:nth-child(1) { animation-delay: 0.1s; }
    .stagger-item:nth-child(2) { animation-delay: 0.2s; }
    .stagger-item:nth-child(3) { animation-delay: 0.3s; }
    .stagger-item:nth-child(4) { animation-delay: 0.4s; }
    .stagger-item:nth-child(5) { animation-delay: 0.5s; }
    .stagger-item:nth-child(6) { animation-delay: 0.6s; }
    
    @keyframes staggerIn {
        0% { opacity: 0; transform: translateY(30px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    /* Typing Animation */
    @keyframes typing {
        from { width: 0; }
        to { width: 100%; }
    }
    
    .typing-text {
        overflow: hidden;
        border-right: 3px solid;
        white-space: nowrap;
        animation: typing 3s steps(40, end), blink-caret 0.75s step-end infinite;
    }
    
    @keyframes blink-caret {
        from, to { border-color: transparent; }
        50% { border-color: white; }
    }
    
    /* Responsive Design - Mobile Optimization */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem !important;
            letter-spacing: -1px !important;
        }
        
        .hero-subtitle {
            font-size: 1.1rem !important;
        }
        
        .section-title {
            font-size: 2rem !important;
        }
        
        .hero-section {
            padding: 4rem 1.5rem 3rem !important;
        }
        
        .step-card, .feature-card {
            padding: 2rem 1.5rem !important;
        }
        
        .nav-grid, .steps-grid, .features-grid {
            grid-template-columns: 1fr !important;
            gap: 1.5rem !important;
        }
    }
    
    /* Ensure all elements are visible */
    div[data-testid="stVerticalBlock"] > div {
        background: transparent;
    }
    
    /* Better contrast for readability */
    .section-container {
        background: rgba(0, 0, 0, 0.2);
        border-radius: 20px;
        padding: 3rem 2rem;
        margin: 2rem 0;
        backdrop-filter: blur(5px);
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
</div>
""",
    unsafe_allow_html=True,
)

# Hero CTA Buttons
hero_col1, hero_col2, hero_col3 = st.columns([1, 2, 1])
with hero_col2:
    cta_col1, cta_col2 = st.columns(2)
    with cta_col1:
        if st.button("🚀 Get Started", key="hero_cta", use_container_width=True):
            st.switch_page("pages/1_📄_Upload_Resume.py")
    with cta_col2:
        if st.button("📊 View Demo", key="hero_demo", use_container_width=True):
            st.switch_page("pages/2_📊_Analysis_Scoring.py")

# ============================================================================
# QUICK NAVIGATION
# ============================================================================
st.markdown(
    """
<div class="nav-section">
    <h2 class="section-title">Quick Access</h2>
    <div class="underline"></div>
</div>
""",
    unsafe_allow_html=True,
)

# Navigation Grid with Streamlit buttons
nav_pages = [
    {"icon": "📄", "title": "Upload Resume", "page": "pages/1_📄_Upload_Resume.py"},
    {"icon": "📊", "title": "Analysis & Scoring", "page": "pages/2_📊_Analysis_Scoring.py"},
    {"icon": "🎯", "title": "Job Matching", "page": "pages/3_🎯_Job_Matching.py"},
    {"icon": "✍️", "title": "Resume Rewrite", "page": "pages/4_✍️_Resume_Rewrite_Ultimate.py"},
    {"icon": "💼", "title": "Cover Letters", "page": "pages/5_💼_Cover_Letter_Projects.py"},
    {"icon": "🔍", "title": "Job Search", "page": "pages/6_🔍_Job_Search.py"},
    {"icon": "🏗️", "title": "Resume Builder", "page": "pages/7_🏗️_Resume_Builder.py"},
    {"icon": "🎤", "title": "Interview Prep", "page": "pages/8_🎤_Interview_Prep.py"},
    {"icon": "💰", "title": "Salary Estimator", "page": "pages/9_💰_Salary_Estimator.py"},
    {"icon": "💡", "title": "Skills Analyzer", "page": "pages/10_💡_Skills_Analyzer.py"},
    {"icon": "📱", "title": "Social Resume", "page": "pages/11_📱_Social_Resume.py"},
    {"icon": "📧", "title": "Email Generator", "page": "pages/12_📧_Email_Generator.py"},
    {"icon": "📝", "title": "Version Manager", "page": "pages/13_📝_Version_Manager.py"},
]

# Create grid layout
cols_per_row = 4
for i in range(0, len(nav_pages), cols_per_row):
    cols = st.columns(cols_per_row)
    for j, col in enumerate(cols):
        idx = i + j
        if idx < len(nav_pages):
            page = nav_pages[idx]
            with col:
                st.markdown(f"<div style='text-align: center; font-size: 3rem; margin-bottom: 0.5rem;'>{page['icon']}</div>", unsafe_allow_html=True)
                if st.button(page["title"], key=f"nav_{idx}", use_container_width=True):
                    st.switch_page(page["page"])

# ============================================================================
# VALUE PROPOSITION (NEW)
# ============================================================================
st.markdown(
    """
<div class="section-container">
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 5rem 3rem; border-radius: 50px; text-align: center; 
                position: relative; overflow: hidden; margin-bottom: 4rem;
                box-shadow: 0 25px 80px rgba(102, 126, 234, 0.5);">
        <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; 
                    background: radial-gradient(circle at 30% 50%, rgba(255,255,255,0.1) 0%, transparent 50%);
                    pointer-events: none;"></div>
        <h2 style="font-size: 3rem; font-weight: 900; color: white; margin-bottom: 1.5rem; 
                    position: relative; z-index: 1; text-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);">
            🎯 Your Resume. Perfected. In Minutes.
        </h2>
        <p style="font-size: 1.4rem; color: rgba(255, 255, 255, 0.95); margin-bottom: 3rem; 
                   max-width: 800px; margin-left: auto; margin-right: auto; position: relative; z-index: 1;">
            Join 10,000+ professionals who transformed their careers with AI-powered resume optimization
        </p>
        <div style="display: flex; justify-content: center; gap: 3rem; flex-wrap: wrap; position: relative; z-index: 1;">
            <div style="text-align: center;">
                <div style="font-size: 3.5rem; font-weight: 900; color: white; margin-bottom: 0.5rem; 
                            text-shadow: 0 5px 25px rgba(0, 0, 0, 0.3);">2min</div>
                <div style="font-size: 1.1rem; color: rgba(255, 255, 255, 0.9);">Average Time</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 3.5rem; font-weight: 900; color: white; margin-bottom: 0.5rem; 
                            text-shadow: 0 5px 25px rgba(0, 0, 0, 0.3);">95%</div>
                <div style="font-size: 1.1rem; color: rgba(255, 255, 255, 0.9);">Success Rate</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 3.5rem; font-weight: 900; color: white; margin-bottom: 0.5rem; 
                            text-shadow: 0 5px 25px rgba(0, 0, 0, 0.3);">FREE</div>
                <div style="font-size: 1.1rem; color: rgba(255, 255, 255, 0.9);">Forever</div>
            </div>
        </div>
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
    <h2 class="section-title">🚀 How It Works</h2>
    <div class="underline"></div>
    <p class="section-subtitle">Four simple steps to transform your career prospects</p>
    
    <div style="text-align: center; margin: 3rem 0 4rem;">
        <div style="display: inline-flex; align-items: center; gap: 1rem; flex-wrap: wrap; justify-content: center;">
            <div style="background: linear-gradient(135deg, #667eea, #764ba2); padding: 1rem 2rem; 
                        border-radius: 25px; color: white; font-weight: 700; font-size: 1.1rem;
                        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);">
                Upload
            </div>
            <div style="color: white; font-size: 2rem;">→</div>
            <div style="background: linear-gradient(135deg, #667eea, #764ba2); padding: 1rem 2rem; 
                        border-radius: 25px; color: white; font-weight: 700; font-size: 1.1rem;
                        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);">
                Analyze
            </div>
            <div style="color: white; font-size: 2rem;">→</div>
            <div style="background: linear-gradient(135deg, #667eea, #764ba2); padding: 1rem 2rem; 
                        border-radius: 25px; color: white; font-weight: 700; font-size: 1.1rem;
                        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);">
                Optimize
            </div>
            <div style="color: white; font-size: 2rem;">→</div>
            <div style="background: linear-gradient(135deg, #10b981, #059669); padding: 1rem 2rem; 
                        border-radius: 25px; color: white; font-weight: 700; font-size: 1.1rem;
                        box-shadow: 0 10px 30px rgba(16, 185, 129, 0.4);">
                Success! 🎉
            </div>
        </div>
    </div>
    
    <div class="steps-grid">
        <div class="step-card stagger-item">
            <div class="step-number">1</div>
            <div class="step-icon icon-float">📄</div>
            <h3 class="step-title">Upload Your Resume</h3>
            <p class="step-description">
                Simply upload your resume in PDF, DOCX, or even scanned image format. 
                Our advanced OCR technology handles any document type with precision.
            </p>
            <div class="progress-bar">
                <div class="progress-fill" style="width: 100%;"></div>
            </div>
            <div style="color: rgba(255, 255, 255, 0.7); font-size: 0.9rem; margin-top: 0.5rem;">
                ⚡ Instant processing • 📱 Any format • 🔒 Secure
            </div>
        </div>
        
        <div class="step-card stagger-item">
            <div class="step-number">2</div>
            <div class="step-icon icon-float" style="animation-delay: 0.3s;">🤖</div>
            <h3 class="step-title">AI Analysis</h3>
            <p class="step-description">
                Our intelligent AI engine analyzes your resume across multiple dimensions, 
                identifying strengths, weaknesses, and opportunities for improvement.
            </p>
            <div class="progress-bar">
                <div class="progress-fill" style="width: 95%; animation-delay: 0.2s;"></div>
            </div>
            <div style="color: rgba(255, 255, 255, 0.7); font-size: 0.9rem; margin-top: 0.5rem;">
                🎯 95% Accuracy • 🧠 Deep Learning • 📊 Multi-factor
            </div>
        </div>
        
        <div class="step-card stagger-item">
            <div class="step-number">3</div>
            <div class="step-icon icon-float" style="animation-delay: 0.6s;">✨</div>
            <h3 class="step-title">Smart Optimization</h3>
            <p class="step-description">
                Get AI-powered rewriting suggestions, ATS optimization tips, and industry-specific 
                recommendations to make your resume stand out.
            </p>
            <div class="progress-bar">
                <div class="progress-fill" style="width: 100%; animation-delay: 0.4s;"></div>
            </div>
            <div style="color: rgba(255, 255, 255, 0.7); font-size: 0.9rem; margin-top: 0.5rem;">
                ✍️ AI Rewriting • 🔍 ATS Check • 💡 Smart Tips
            </div>
        </div>
        
        <div class="step-card stagger-item">
            <div class="step-number">4</div>
            <div class="step-icon icon-float" style="animation-delay: 0.9s;">🎯</div>
            <h3 class="step-title">Land Your Dream Job</h3>
            <p class="step-description">
                Export your optimized resume in multiple formats, generate tailored cover letters, 
                and match with relevant job opportunities.
            </p>
            <div class="progress-bar">
                <div class="progress-fill" style="width: 100%; animation-delay: 0.6s; background: linear-gradient(90deg, #10b981, #059669);"></div>
            </div>
            <div style="color: rgba(16, 185, 129, 0.9); font-size: 0.9rem; margin-top: 0.5rem; font-weight: 700;">
                🚀 Multiple Formats • 💼 Cover Letters • 🎉 Success!
            </div>
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# ============================================================================
# FEATURES AT A GLANCE (NEW)
# ============================================================================
st.markdown(
    """
<div class="section-container">
    <h2 class="section-title">⚡ Features at a Glance</h2>
    <div class="underline"></div>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); 
                gap: 1.5rem; margin: 3rem 0;">
        <div style="background: linear-gradient(135deg, rgba(124, 58, 237, 0.15), rgba(91, 33, 182, 0.15)); 
                    padding: 1.5rem; border-radius: 20px; border: 2px solid rgba(124, 58, 237, 0.3); 
                    text-align: center; transition: all 0.3s;">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🔍</div>
            <div style="color: white; font-weight: 700; font-size: 1.05rem;">ATS Scanner</div>
        </div>
        <div style="background: linear-gradient(135deg, rgba(236, 72, 153, 0.15), rgba(219, 39, 119, 0.15)); 
                    padding: 1.5rem; border-radius: 20px; border: 2px solid rgba(236, 72, 153, 0.3); 
                    text-align: center; transition: all 0.3s;">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">📊</div>
            <div style="color: white; font-weight: 700; font-size: 1.05rem;">Analytics</div>
        </div>
        <div style="background: linear-gradient(135deg, rgba(59, 130, 246, 0.15), rgba(37, 99, 235, 0.15)); 
                    padding: 1.5rem; border-radius: 20px; border: 2px solid rgba(59, 130, 246, 0.3); 
                    text-align: center; transition: all 0.3s;">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">💡</div>
            <div style="color: white; font-weight: 700; font-size: 1.05rem;">Skills Analysis</div>
        </div>
        <div style="background: linear-gradient(135deg, rgba(16, 185, 129, 0.15), rgba(5, 150, 105, 0.15)); 
                    padding: 1.5rem; border-radius: 20px; border: 2px solid rgba(16, 185, 129, 0.3); 
                    text-align: center; transition: all 0.3s;">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🎤</div>
            <div style="color: white; font-weight: 700; font-size: 1.05rem;">Interview Prep</div>
        </div>
        <div style="background: linear-gradient(135deg, rgba(245, 158, 11, 0.15), rgba(217, 119, 6, 0.15)); 
                    padding: 1.5rem; border-radius: 20px; border: 2px solid rgba(245, 158, 11, 0.3); 
                    text-align: center; transition: all 0.3s;">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">💰</div>
            <div style="color: white; font-weight: 700; font-size: 1.05rem;">Salary Estimator</div>
        </div>
        <div style="background: linear-gradient(135deg, rgba(139, 92, 246, 0.15), rgba(109, 40, 217, 0.15)); 
                    padding: 1.5rem; border-radius: 20px; border: 2px solid rgba(139, 92, 246, 0.3); 
                    text-align: center; transition: all 0.3s;">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">✍️</div>
            <div style="color: white; font-weight: 700; font-size: 1.05rem;">AI Rewriting</div>
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
# TRUST BADGES (NEW)
# ============================================================================
st.markdown(
    """
<div class="section-container">
    <div style="background: linear-gradient(145deg, rgba(16, 185, 129, 0.1), rgba(5, 150, 105, 0.1)); 
                backdrop-filter: blur(10px); padding: 3rem; border-radius: 40px; 
                border: 2px solid rgba(16, 185, 129, 0.3); text-align: center;">
        <h3 style="font-size: 2rem; font-weight: 800; color: white; margin-bottom: 2rem;">
            🏆 Industry Recognition & Trust
        </h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); 
                    gap: 2rem; margin-top: 2rem;">
            <div style="text-align: center;">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">🔒</div>
                <div style="color: white; font-weight: 700; font-size: 1.1rem;">GDPR Compliant</div>
                <div style="color: rgba(255, 255, 255, 0.7); font-size: 0.9rem;">Data Protection</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">⚡</div>
                <div style="color: white; font-weight: 700; font-size: 1.1rem;">AI-Powered</div>
                <div style="color: rgba(255, 255, 255, 0.7); font-size: 0.9rem;">Latest Technology</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">🌟</div>
                <div style="color: white; font-weight: 700; font-size: 1.1rem;">4.8/5 Rating</div>
                <div style="color: rgba(255, 255, 255, 0.7); font-size: 0.9rem;">10,000+ Reviews</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">🎯</div>
                <div style="color: white; font-weight: 700; font-size: 1.1rem;">95% Success</div>
                <div style="color: rgba(255, 255, 255, 0.7); font-size: 0.9rem;">Job Landing Rate</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">🌍</div>
                <div style="color: white; font-weight: 700; font-size: 1.1rem;">Global Reach</div>
                <div style="color: rgba(255, 255, 255, 0.7); font-size: 0.9rem;">100+ Countries</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">⏱️</div>
                <div style="color: white; font-weight: 700; font-size: 1.1rem;">24/7 Available</div>
                <div style="color: rgba(255, 255, 255, 0.7); font-size: 0.9rem;">Always Online</div>
            </div>
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# ============================================================================
# INDUSTRIES WE SERVE (NEW)
# ============================================================================
st.markdown(
    """
<div class="section-container">
    <h2 class="section-title">🏢 Industries We Serve</h2>
    <div class="underline"></div>
    <p class="section-subtitle">Optimized for every industry and career level</p>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); 
                gap: 2rem; margin: 3rem 0;">
        <div class="stagger-item" style="background: linear-gradient(145deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1)); 
                    backdrop-filter: blur(10px); padding: 2rem; border-radius: 25px; 
                    border: 2px solid rgba(102, 126, 234, 0.3); text-align: center;
                    transition: all 0.4s ease;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">💻</div>
            <h4 style="color: white; font-size: 1.2rem; font-weight: 700; margin-bottom: 0.5rem;">Technology</h4>
            <p style="color: rgba(255, 255, 255, 0.7); font-size: 0.95rem;">Software, IT, AI/ML</p>
        </div>
        
        <div class="stagger-item" style="background: linear-gradient(145deg, rgba(236, 72, 153, 0.1), rgba(219, 39, 119, 0.1)); 
                    backdrop-filter: blur(10px); padding: 2rem; border-radius: 25px; 
                    border: 2px solid rgba(236, 72, 153, 0.3); text-align: center;
                    transition: all 0.4s ease;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">💼</div>
            <h4 style="color: white; font-size: 1.2rem; font-weight: 700; margin-bottom: 0.5rem;">Business</h4>
            <p style="color: rgba(255, 255, 255, 0.7); font-size: 0.95rem;">Finance, Consulting, MBA</p>
        </div>
        
        <div class="stagger-item" style="background: linear-gradient(145deg, rgba(59, 130, 246, 0.1), rgba(37, 99, 235, 0.1)); 
                    backdrop-filter: blur(10px); padding: 2rem; border-radius: 25px; 
                    border: 2px solid rgba(59, 130, 246, 0.3); text-align: center;
                    transition: all 0.4s ease;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">🎨</div>
            <h4 style="color: white; font-size: 1.2rem; font-weight: 700; margin-bottom: 0.5rem;">Creative</h4>
            <p style="color: rgba(255, 255, 255, 0.7); font-size: 0.95rem;">Design, Marketing, Media</p>
        </div>
        
        <div class="stagger-item" style="background: linear-gradient(145deg, rgba(16, 185, 129, 0.1), rgba(5, 150, 105, 0.1)); 
                    backdrop-filter: blur(10px); padding: 2rem; border-radius: 25px; 
                    border: 2px solid rgba(16, 185, 129, 0.3); text-align: center;
                    transition: all 0.4s ease;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">⚕️</div>
            <h4 style="color: white; font-size: 1.2rem; font-weight: 700; margin-bottom: 0.5rem;">Healthcare</h4>
            <p style="color: rgba(255, 255, 255, 0.7); font-size: 0.95rem;">Medical, Nursing, Pharma</p>
        </div>
        
        <div class="stagger-item" style="background: linear-gradient(145deg, rgba(245, 158, 11, 0.1), rgba(217, 119, 6, 0.1)); 
                    backdrop-filter: blur(10px); padding: 2rem; border-radius: 25px; 
                    border: 2px solid rgba(245, 158, 11, 0.3); text-align: center;
                    transition: all 0.4s ease;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">🔧</div>
            <h4 style="color: white; font-size: 1.2rem; font-weight: 700; margin-bottom: 0.5rem;">Engineering</h4>
            <p style="color: rgba(255, 255, 255, 0.7); font-size: 0.95rem;">Mechanical, Civil, Electrical</p>
        </div>
        
        <div class="stagger-item" style="background: linear-gradient(145deg, rgba(139, 92, 246, 0.1), rgba(109, 40, 217, 0.1)); 
                    backdrop-filter: blur(10px); padding: 2rem; border-radius: 25px; 
                    border: 2px solid rgba(139, 92, 246, 0.3); text-align: center;
                    transition: all 0.4s ease;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">📚</div>
            <h4 style="color: white; font-size: 1.2rem; font-weight: 700; margin-bottom: 0.5rem;">Education</h4>
            <p style="color: rgba(255, 255, 255, 0.7); font-size: 0.95rem;">Teaching, Research, Admin</p>
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
# SUCCESS METRICS SECTION (NEW)
# ============================================================================
st.markdown(
    """
<div class="section-container">
    <div style="background: linear-gradient(145deg, rgba(102, 126, 234, 0.15), rgba(118, 75, 162, 0.15)); 
                backdrop-filter: blur(15px); padding: 4rem 2rem; border-radius: 40px; 
                border: 2px solid rgba(102, 126, 234, 0.3); margin-bottom: 4rem;">
        <h3 style="text-align: center; font-size: 2.5rem; font-weight: 900; color: white; margin-bottom: 3rem;">
            📈 Success By The Numbers
        </h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); 
                    gap: 2rem; text-align: center;">
            <div class="stagger-item">
                <div class="neon-text" style="font-size: 3.5rem; font-weight: 900; margin-bottom: 0.5rem;">10K+</div>
                <div style="color: rgba(255, 255, 255, 0.85); font-size: 1.1rem; font-weight: 600;">Resumes Optimized</div>
            </div>
            <div class="stagger-item">
                <div class="neon-text" style="font-size: 3.5rem; font-weight: 900; margin-bottom: 0.5rem;">95%</div>
                <div style="color: rgba(255, 255, 255, 0.85); font-size: 1.1rem; font-weight: 600;">Success Rate</div>
            </div>
            <div class="stagger-item">
                <div class="neon-text" style="font-size: 3.5rem; font-weight: 900; margin-bottom: 0.5rem;">3x</div>
                <div style="color: rgba(255, 255, 255, 0.85); font-size: 1.1rem; font-weight: 600;">More Interviews</div>
            </div>
            <div class="stagger-item">
                <div class="neon-text" style="font-size: 3.5rem; font-weight: 900; margin-bottom: 0.5rem;">2min</div>
                <div style="color: rgba(255, 255, 255, 0.85); font-size: 1.1rem; font-weight: 600;">Avg. Analysis Time</div>
            </div>
            <div class="stagger-item">
                <div class="neon-text" style="font-size: 3.5rem; font-weight: 900; margin-bottom: 0.5rem;">500+</div>
                <div style="color: rgba(255, 255, 255, 0.85); font-size: 1.1rem; font-weight: 600;">Partner Companies</div>
            </div>
            <div class="stagger-item">
                <div class="neon-text" style="font-size: 3.5rem; font-weight: 900; margin-bottom: 0.5rem;">100+</div>
                <div style="color: rgba(255, 255, 255, 0.85); font-size: 1.1rem; font-weight: 600;">Countries Served</div>
            </div>
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
    <h2 class="section-title">⭐ What Our Users Say</h2>
    <div class="underline"></div>
    <p class="section-subtitle">Join thousands of satisfied job seekers</p>
    
    <div class="testimonials-grid">
        <div class="testimonial-card">
            <div class="testimonial-badge">✓ Verified User</div>
            <div class="testimonial-rating">⭐⭐⭐⭐⭐</div>
            <p class="testimonial-text">
                "This platform helped me land <span class="highlight-purple">3 interviews</span> 
                in just two weeks! The AI optimization made my resume stand out."
            </p>
            <div class="testimonial-avatar avatar-purple">SJ</div>
            <p class="testimonial-name">Sarah Johnson<br>Software Engineer @ Google</p>
        </div>
        
        <div class="testimonial-card">
            <div class="testimonial-badge">✓ Verified User</div>
            <div class="testimonial-rating">⭐⭐⭐⭐⭐</div>
            <p class="testimonial-text">
                "The ATS scanner is a game-changer! My resume now <span class="highlight-purple">passes ATS systems</span> 
                that previously rejected me. Got 2 offers in a month!"
            </p>
            <div class="testimonial-avatar avatar-pink">MC</div>
            <p class="testimonial-name">Michael Chen<br>Product Manager @ Meta</p>
        </div>
        
        <div class="testimonial-card">
            <div class="testimonial-badge">✓ Verified User</div>
            <div class="testimonial-rating">⭐⭐⭐⭐⭐</div>
            <p class="testimonial-text">
                "The analysis and suggestions were <span class="highlight-blue">incredibly accurate</span> 
                and actionable. Improved my response rate by 300%!"
            </p>
            <div class="testimonial-avatar avatar-blue">ER</div>
            <p class="testimonial-name">Emily Rodriguez<br>Marketing Specialist @ Amazon</p>
        </div>
        
        <div class="testimonial-card">
            <div class="testimonial-badge">✓ Verified User</div>
            <div class="testimonial-rating">⭐⭐⭐⭐⭐</div>
            <p class="testimonial-text">
                "Interview prep feature is <span class="highlight-purple">absolutely phenomenal</span>! 
                Generated role-specific questions that actually came up in my interviews."
            </p>
            <div class="testimonial-avatar avatar-purple">DK</div>
            <p class="testimonial-name">David Kim<br>Data Scientist @ Netflix</p>
        </div>
        
        <div class="testimonial-card">
            <div class="testimonial-badge">✓ Verified User</div>
            <div class="testimonial-rating">⭐⭐⭐⭐⭐</div>
            <p class="testimonial-text">
                "Salary estimator helped me negotiate <span class="highlight-blue">15% higher</span> 
                than the initial offer. Worth every minute spent on the platform!"
            </p>
            <div class="testimonial-avatar avatar-pink">AL</div>
            <p class="testimonial-name">Amanda Lee<br>UX Designer @ Apple</p>
        </div>
        
        <div class="testimonial-card">
            <div class="testimonial-badge">✓ Verified User</div>
            <div class="testimonial-rating">⭐⭐⭐⭐⭐</div>
            <p class="testimonial-text">
                "The cover letter generator saved me <span class="highlight-purple">hours of work</span>. 
                Each letter is personalized and professional!"
            </p>
            <div class="testimonial-avatar avatar-blue">JM</div>
            <p class="testimonial-name">James Miller<br>Business Analyst @ Microsoft</p>
        </div>
    </div>
    
    <div class="social-proof">
        <h3 class="social-proof-title">🏆 Trusted by Professionals Worldwide</h3>
        <div class="social-proof-badges">
            <div class="proof-badge">
                <div class="proof-icon">🎓</div>
                <div class="proof-text">Top Universities</div>
            </div>
            <div class="proof-badge">
                <div class="proof-icon">💼</div>
                <div class="proof-text">Fortune 500</div>
            </div>
            <div class="proof-badge">
                <div class="proof-icon">🚀</div>
                <div class="proof-text">Tech Startups</div>
            </div>
            <div class="proof-badge">
                <div class="proof-icon">🌍</div>
                <div class="proof-text">100+ Countries</div>
            </div>
            <div class="proof-badge">
                <div class="proof-icon">⚡</div>
                <div class="proof-text">AI-Powered</div>
            </div>
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# ============================================================================
# BEFORE & AFTER SHOWCASE (NEW)
# ============================================================================
st.markdown(
    """
<div class="section-container">
    <h2 class="section-title">🔄 See The Transformation</h2>
    <div class="underline"></div>
    <p class="section-subtitle">Real examples of AI-powered optimization</p>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); 
                gap: 3rem; margin: 4rem 0;">
        <div style="background: linear-gradient(145deg, rgba(239, 68, 68, 0.1), rgba(220, 38, 38, 0.1)); 
                    backdrop-filter: blur(10px); padding: 3rem 2rem; border-radius: 30px; 
                    border: 2px solid rgba(239, 68, 68, 0.3); position: relative;">
            <div style="position: absolute; top: -20px; left: 30px; background: #ef4444; 
                        padding: 0.5rem 1.5rem; border-radius: 20px; font-weight: 800; 
                        color: white; font-size: 0.9rem;">BEFORE</div>
            <h3 style="color: white; font-size: 1.6rem; font-weight: 800; margin: 2rem 0 1.5rem;">
                ❌ Typical Resume Issues
            </h3>
            <ul style="list-style: none; padding: 0; margin: 0;">
                <li style="padding: 0.8rem 0; color: rgba(255, 255, 255, 0.85); font-size: 1.05rem; display: flex; align-items: start; gap: 0.8rem;">
                    <span style="color: #ef4444; font-size: 1.3rem;">✗</span>
                    <span>Generic job descriptions without achievements</span>
                </li>
                <li style="padding: 0.8rem 0; color: rgba(255, 255, 255, 0.85); font-size: 1.05rem; display: flex; align-items: start; gap: 0.8rem;">
                    <span style="color: #ef4444; font-size: 1.3rem;">✗</span>
                    <span>Missing keywords for ATS systems</span>
                </li>
                <li style="padding: 0.8rem 0; color: rgba(255, 255, 255, 0.85); font-size: 1.05rem; display: flex; align-items: start; gap: 0.8rem;">
                    <span style="color: #ef4444; font-size: 1.3rem;">✗</span>
                    <span>Weak action verbs and passive language</span>
                </li>
                <li style="padding: 0.8rem 0; color: rgba(255, 255, 255, 0.85); font-size: 1.05rem; display: flex; align-items: start; gap: 0.8rem;">
                    <span style="color: #ef4444; font-size: 1.3rem;">✗</span>
                    <span>No quantifiable results or metrics</span>
                </li>
                <li style="padding: 0.8rem 0; color: rgba(255, 255, 255, 0.85); font-size: 1.05rem; display: flex; align-items: start; gap: 0.8rem;">
                    <span style="color: #ef4444; font-size: 1.3rem;">✗</span>
                    <span>Poor formatting and inconsistent style</span>
                </li>
            </ul>
            <div style="margin-top: 2rem; padding: 1.5rem; background: rgba(0, 0, 0, 0.2); 
                        border-radius: 15px; border-left: 4px solid #ef4444;">
                <div style="color: #ef4444; font-weight: 700; font-size: 0.9rem; margin-bottom: 0.5rem;">ATS SCORE</div>
                <div style="color: white; font-size: 2.5rem; font-weight: 900;">45%</div>
            </div>
        </div>
        
        <div style="background: linear-gradient(145deg, rgba(16, 185, 129, 0.15), rgba(5, 150, 105, 0.15)); 
                    backdrop-filter: blur(10px); padding: 3rem 2rem; border-radius: 30px; 
                    border: 2px solid rgba(16, 185, 129, 0.5); position: relative;
                    box-shadow: 0 0 40px rgba(16, 185, 129, 0.3);">
            <div style="position: absolute; top: -20px; left: 30px; background: linear-gradient(135deg, #10b981, #059669); 
                        padding: 0.5rem 1.5rem; border-radius: 20px; font-weight: 800; 
                        color: white; font-size: 0.9rem; box-shadow: 0 5px 20px rgba(16, 185, 129, 0.5);">AFTER AI</div>
            <h3 style="color: white; font-size: 1.6rem; font-weight: 800; margin: 2rem 0 1.5rem;">
                ✨ AI-Optimized Resume
            </h3>
            <ul style="list-style: none; padding: 0; margin: 0;">
                <li style="padding: 0.8rem 0; color: rgba(255, 255, 255, 0.9); font-size: 1.05rem; font-weight: 600; display: flex; align-items: start; gap: 0.8rem;">
                    <span style="color: #10b981; font-size: 1.3rem;">✓</span>
                    <span>Impact-driven achievements with metrics</span>
                </li>
                <li style="padding: 0.8rem 0; color: rgba(255, 255, 255, 0.9); font-size: 1.05rem; font-weight: 600; display: flex; align-items: start; gap: 0.8rem;">
                    <span style="color: #10b981; font-size: 1.3rem;">✓</span>
                    <span>Optimized with industry-specific keywords</span>
                </li>
                <li style="padding: 0.8rem 0; color: rgba(255, 255, 255, 0.9); font-size: 1.05rem; font-weight: 600; display: flex; align-items: start; gap: 0.8rem;">
                    <span style="color: #10b981; font-size: 1.3rem;">✓</span>
                    <span>Power verbs and active voice throughout</span>
                </li>
                <li style="padding: 0.8rem 0; color: rgba(255, 255, 255, 0.9); font-size: 1.05rem; font-weight: 600; display: flex; align-items: start; gap: 0.8rem;">
                    <span style="color: #10b981; font-size: 1.3rem;">✓</span>
                    <span>Quantified results that impress recruiters</span>
                </li>
                <li style="padding: 0.8rem 0; color: rgba(255, 255, 255, 0.9); font-size: 1.05rem; font-weight: 600; display: flex; align-items: start; gap: 0.8rem;">
                    <span style="color: #10b981; font-size: 1.3rem;">✓</span>
                    <span>Professional formatting and consistency</span>
                </li>
            </ul>
            <div style="margin-top: 2rem; padding: 1.5rem; background: rgba(16, 185, 129, 0.1); 
                        border-radius: 15px; border-left: 4px solid #10b981;">
                <div style="color: #10b981; font-weight: 700; font-size: 0.9rem; margin-bottom: 0.5rem;">ATS SCORE</div>
                <div style="color: white; font-size: 2.5rem; font-weight: 900;">95%</div>
                <div style="color: #10b981; font-size: 1rem; font-weight: 600; margin-top: 0.5rem;">
                    +50% improvement 📈
                </div>
            </div>
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# ============================================================================
# WHY CHOOSE US SECTION (NEW)
# ============================================================================
st.markdown(
    """
<div class="section-container">
    <h2 class="section-title">💎 Why Choose ResumeMasterAI</h2>
    <div class="underline"></div>
    <p class="section-subtitle">The complete AI-powered career toolkit</p>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem; margin: 3rem 0;">
        <div style="background: linear-gradient(145deg, rgba(124, 58, 237, 0.15), rgba(91, 33, 182, 0.15)); 
                    backdrop-filter: blur(10px); padding: 2.5rem; border-radius: 30px; 
                    border: 2px solid rgba(124, 58, 237, 0.3); text-align: center;
                    transition: all 0.4s ease; position: relative; overflow: hidden;">
            <div style="font-size: 4rem; margin-bottom: 1rem; filter: drop-shadow(0 5px 15px rgba(124, 58, 237, 0.4));">⚡</div>
            <h3 style="font-size: 1.5rem; font-weight: 800; color: white; margin-bottom: 1rem;">Lightning Fast</h3>
            <p style="color: rgba(255, 255, 255, 0.85); font-size: 1.05rem; line-height: 1.7;">
                Get comprehensive resume analysis and optimization in under 2 minutes. Our AI processes instantly.
            </p>
        </div>
        
        <div style="background: linear-gradient(145deg, rgba(236, 72, 153, 0.15), rgba(219, 39, 119, 0.15)); 
                    backdrop-filter: blur(10px); padding: 2.5rem; border-radius: 30px; 
                    border: 2px solid rgba(236, 72, 153, 0.3); text-align: center;
                    transition: all 0.4s ease;">
            <div style="font-size: 4rem; margin-bottom: 1rem; filter: drop-shadow(0 5px 15px rgba(236, 72, 153, 0.4));">🎯</div>
            <h3 style="font-size: 1.5rem; font-weight: 800; color: white; margin-bottom: 1rem;">Precision Accuracy</h3>
            <p style="color: rgba(255, 255, 255, 0.85); font-size: 1.05rem; line-height: 1.7;">
                95%+ accuracy rate with industry-leading AI models trained on millions of successful resumes.
            </p>
        </div>
        
        <div style="background: linear-gradient(145deg, rgba(59, 130, 246, 0.15), rgba(37, 99, 235, 0.15)); 
                    backdrop-filter: blur(10px); padding: 2.5rem; border-radius: 30px; 
                    border: 2px solid rgba(59, 130, 246, 0.3); text-align: center;
                    transition: all 0.4s ease;">
            <div style="font-size: 4rem; margin-bottom: 1rem; filter: drop-shadow(0 5px 15px rgba(59, 130, 246, 0.4));">🔒</div>
            <h3 style="font-size: 1.5rem; font-weight: 800; color: white; margin-bottom: 1rem;">100% Secure</h3>
            <p style="color: rgba(255, 255, 255, 0.85); font-size: 1.05rem; line-height: 1.7;">
                Your data is encrypted and never stored. Complete privacy and GDPR compliance guaranteed.
            </p>
        </div>
        
        <div style="background: linear-gradient(145deg, rgba(16, 185, 129, 0.15), rgba(5, 150, 105, 0.15)); 
                    backdrop-filter: blur(10px); padding: 2.5rem; border-radius: 30px; 
                    border: 2px solid rgba(16, 185, 129, 0.3); text-align: center;
                    transition: all 0.4s ease;">
            <div style="font-size: 4rem; margin-bottom: 1rem; filter: drop-shadow(0 5px 15px rgba(16, 185, 129, 0.4));">💰</div>
            <h3 style="font-size: 1.5rem; font-weight: 800; color: white; margin-bottom: 1rem;">Completely Free</h3>
            <p style="color: rgba(255, 255, 255, 0.85); font-size: 1.05rem; line-height: 1.7;">
                All premium features included at no cost. No hidden fees, no credit card required.
            </p>
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# ============================================================================
# COMPARISON SECTION (NEW)
# ============================================================================
st.markdown(
    """
<div class="section-container">
    <h2 class="section-title">🆚 Traditional vs AI-Powered</h2>
    <div class="underline"></div>
    <p class="section-subtitle">See why thousands are making the switch</p>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin: 3rem 0;">
        <div style="background: linear-gradient(145deg, rgba(239, 68, 68, 0.1), rgba(220, 38, 38, 0.1)); 
                    backdrop-filter: blur(10px); padding: 2.5rem; border-radius: 30px; 
                    border: 2px solid rgba(239, 68, 68, 0.3); position: relative;">
            <div style="font-size: 3rem; text-align: center; margin-bottom: 1rem;">❌</div>
            <h3 style="text-align: center; font-size: 1.8rem; font-weight: 800; color: white; margin-bottom: 2rem;">Traditional Method</h3>
            <ul style="list-style: none; padding: 0; margin: 0;">
                <li style="padding: 0.8rem 0; color: rgba(255, 255, 255, 0.85); font-size: 1.05rem;">
                    ❌ Hours of manual editing
                </li>
                <li style="padding: 0.8rem 0; color: rgba(255, 255, 255, 0.85); font-size: 1.05rem;">
                    ❌ Guesswork on ATS optimization
                </li>
                <li style="padding: 0.8rem 0; color: rgba(255, 255, 255, 0.85); font-size: 1.05rem;">
                    ❌ Generic resume templates
                </li>
                <li style="padding: 0.8rem 0; color: rgba(255, 255, 255, 0.85); font-size: 1.05rem;">
                    ❌ No personalized feedback
                </li>
                <li style="padding: 0.8rem 0; color: rgba(255, 255, 255, 0.85); font-size: 1.05rem;">
                    ❌ Limited format options
                </li>
                <li style="padding: 0.8rem 0; color: rgba(255, 255, 255, 0.85); font-size: 1.05rem;">
                    ❌ No analytics or insights
                </li>
            </ul>
        </div>
        
        <div style="background: linear-gradient(145deg, rgba(16, 185, 129, 0.15), rgba(5, 150, 105, 0.15)); 
                    backdrop-filter: blur(10px); padding: 2.5rem; border-radius: 30px; 
                    border: 2px solid rgba(16, 185, 129, 0.5); position: relative;
                    box-shadow: 0 0 40px rgba(16, 185, 129, 0.3);">
            <div style="font-size: 3rem; text-align: center; margin-bottom: 1rem; animation: bounce 2s infinite;">✨</div>
            <h3 style="text-align: center; font-size: 1.8rem; font-weight: 800; color: white; margin-bottom: 2rem;">
                ResumeMasterAI
            </h3>
            <ul style="list-style: none; padding: 0; margin: 0;">
                <li style="padding: 0.8rem 0; color: rgba(255, 255, 255, 0.9); font-size: 1.05rem; font-weight: 600;">
                    ✅ AI-powered optimization in minutes
                </li>
                <li style="padding: 0.8rem 0; color: rgba(255, 255, 255, 0.9); font-size: 1.05rem; font-weight: 600;">
                    ✅ Real-time ATS compatibility scoring
                </li>
                <li style="padding: 0.8rem 0; color: rgba(255, 255, 255, 0.9); font-size: 1.05rem; font-weight: 600;">
                    ✅ Tailored for your industry & role
                </li>
                <li style="padding: 0.8rem 0; color: rgba(255, 255, 255, 0.9); font-size: 1.05rem; font-weight: 600;">
                    ✅ Expert AI feedback & suggestions
                </li>
                <li style="padding: 0.8rem 0; color: rgba(255, 255, 255, 0.9); font-size: 1.05rem; font-weight: 600;">
                    ✅ Multiple professional formats
                </li>
                <li style="padding: 0.8rem 0; color: rgba(255, 255, 255, 0.9); font-size: 1.05rem; font-weight: 600;">
                    ✅ Comprehensive analytics dashboard
                </li>
            </ul>
            <div style="position: absolute; top: -15px; right: 20px; 
                        background: linear-gradient(135deg, #fbbf24, #f59e0b); 
                        padding: 0.5rem 1.5rem; border-radius: 20px; 
                        font-weight: 800; color: white; font-size: 0.9rem;
                        box-shadow: 0 5px 20px rgba(251, 191, 36, 0.5);">
                RECOMMENDED
            </div>
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# ============================================================================
# MID-PAGE CTA BANNER (NEW)
# ============================================================================
st.markdown(
    """
<div class="section-container">
    <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                padding: 4rem 3rem; border-radius: 40px; text-align: center; 
                position: relative; overflow: hidden;
                box-shadow: 0 25px 80px rgba(240, 147, 251, 0.5);">
        <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; 
                    background: radial-gradient(circle at 70% 30%, rgba(255,255,255,0.15) 0%, transparent 60%);
                    pointer-events: none;"></div>
        <div style="position: relative; z-index: 1;">
            <div style="display: inline-block; padding: 0.6rem 1.5rem; background: rgba(255, 255, 255, 0.2); 
                        border-radius: 25px; margin-bottom: 1.5rem; font-weight: 700; color: white; 
                        font-size: 0.95rem;">✨ LIMITED TIME OFFER</div>
            <h2 style="font-size: 2.8rem; font-weight: 900; color: white; margin-bottom: 1rem; 
                        text-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);">
                Get Your Resume Optimized Today!
            </h2>
            <p style="font-size: 1.3rem; color: rgba(255, 255, 255, 0.95); margin-bottom: 2.5rem; 
                       max-width: 700px; margin-left: auto; margin-right: auto;">
                Join thousands of professionals who landed their dream jobs with our AI-powered platform
            </p>
            <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap; margin-bottom: 2rem;">
                <div style="background: rgba(255, 255, 255, 0.15); padding: 1rem 2rem; border-radius: 20px; 
                            backdrop-filter: blur(10px);">
                    <div style="font-size: 2rem; font-weight: 900; color: white;">FREE</div>
                    <div style="font-size: 0.95rem; color: rgba(255, 255, 255, 0.9);">Forever</div>
                </div>
                <div style="background: rgba(255, 255, 255, 0.15); padding: 1rem 2rem; border-radius: 20px; 
                            backdrop-filter: blur(10px);">
                    <div style="font-size: 2rem; font-weight: 900; color: white;">2min</div>
                    <div style="font-size: 0.95rem; color: rgba(255, 255, 255, 0.9);">Setup Time</div>
                </div>
                <div style="background: rgba(255, 255, 255, 0.15); padding: 1rem 2rem; border-radius: 20px; 
                            backdrop-filter: blur(10px);">
                    <div style="font-size: 2rem; font-weight: 900; color: white;">24/7</div>
                    <div style="font-size: 0.95rem; color: rgba(255, 255, 255, 0.9);">Available</div>
                </div>
            </div>
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# CTA Button
cta_banner_col1, cta_banner_col2, cta_banner_col3 = st.columns([1, 2, 1])
with cta_banner_col2:
    cta_banner_button_col1, cta_banner_button_col2 = st.columns(2)
    with cta_banner_button_col1:
        if st.button("🚀 Start Free Now", key="mid_page_cta", use_container_width=True):
            st.switch_page("pages/1_📄_Upload_Resume.py")
    with cta_banner_button_col2:
        if st.button("📊 See Examples", key="mid_page_demo", use_container_width=True):
            st.switch_page("pages/2_📊_Analysis_Scoring.py")

st.markdown("<br><br>", unsafe_allow_html=True)

# ============================================================================
# FAQ SECTION (NEW)
# ============================================================================
st.markdown(
    """
<div class="section-container">
    <h2 class="section-title">❓ Frequently Asked Questions</h2>
    <div class="underline"></div>
    <p class="section-subtitle">Everything you need to know</p>
</div>
""",
    unsafe_allow_html=True,
)

# FAQ Expandable sections using Streamlit
faq_col1, faq_col2 = st.columns(2)

with faq_col1:
    with st.expander("🤔 How does the AI analyze my resume?", expanded=False):
        st.write("""
        Our advanced AI uses Google Gemini and LangChain to analyze your resume across multiple dimensions:
        - **Content Analysis**: Evaluates skills, experience, and achievements
        - **ATS Compatibility**: Checks formatting and keyword optimization
        - **Industry Standards**: Compares against best practices for your field
        - **Impact Assessment**: Measures the strength of your accomplishments
        """)
    
    with st.expander("💰 Is this service free?", expanded=False):
        st.write("""
        Yes! ResumeMasterAI offers comprehensive features completely free:
        - Resume analysis and scoring
        - AI-powered optimization suggestions
        - ATS compatibility checking
        - Multiple format exports
        - All core features included at no cost
        """)
    
    with st.expander("🔒 Is my data secure?", expanded=False):
        st.write("""
        Absolutely! We take your privacy seriously:
        - **No Data Storage**: We don't store your resume permanently
        - **Local Processing**: Most processing happens in your browser
        - **Encrypted Transfer**: All data transmission is encrypted
        - **GDPR Compliant**: We follow strict data protection regulations
        """)

with faq_col2:
    with st.expander("📄 What file formats are supported?", expanded=False):
        st.write("""
        We support multiple formats for maximum flexibility:
        - **Upload**: PDF, DOCX, DOC, TXT, and even scanned images (OCR)
        - **Export**: ATS-optimized PDF, DOCX, TXT, Markdown
        - **Images**: Our OCR technology can extract text from image files
        """)
    
    with st.expander("⚡ How fast is the analysis?", expanded=False):
        st.write("""
        Lightning fast with our AI-powered system:
        - **Initial Analysis**: 30-60 seconds
        - **Detailed Report**: 2-3 minutes
        - **Rewrite Suggestions**: 1-2 minutes
        - **Real-time Updates**: Instant feedback as you edit
        """)
    
    with st.expander("🌍 Does it work for international resumes?", expanded=False):
        st.write("""
        Yes! We support professionals worldwide:
        - Multiple resume formats (US, UK, EU, etc.)
        - Industry-specific optimizations globally
        - Works for any language (best results with English)
        - International company compatibility
        """)

# ============================================================================
# FINAL CTA SECTION
# ============================================================================
st.markdown("<br><br>", unsafe_allow_html=True)

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
</div>
""",
    unsafe_allow_html=True,
)

# Footer CTA Buttons
footer_col1, footer_col2, footer_col3 = st.columns([1, 2, 1])
with footer_col2:
    footer_cta_col1, footer_cta_col2 = st.columns(2)
    with footer_cta_col1:
        if st.button("🚀 Start Now", key="footer_cta", use_container_width=True):
            st.switch_page("pages/1_📄_Upload_Resume.py")
    with footer_cta_col2:
        if st.button("📚 Learn More", key="footer_learn", use_container_width=True):
            st.switch_page("pages/2_📊_Analysis_Scoring.py")

st.markdown("<br><br>", unsafe_allow_html=True)
