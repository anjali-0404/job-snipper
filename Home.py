"""
ResumeMasterAI - Landing Page
Professional multi-page resume analysis and optimization tool.
"""

import streamlit as st
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils.color_scheme import get_unified_css
from utils.ui_components import apply_custom_css
from dotenv import load_dotenv

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="ResumeMasterAI - Home",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Apply unified color scheme
st.markdown(get_unified_css(), unsafe_allow_html=True)

# Apply enhanced custom styling for dark/light mode
st.markdown(
    """
<style>
    /* Advanced Animated Background */
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(5deg); }
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.05); opacity: 0.9; }
    }
    
    @keyframes slideInLeft {
        from { opacity: 0; transform: translateX(-50px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    @keyframes slideInRight {
        from { opacity: 0; transform: translateX(50px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes glow {
        0%, 100% { box-shadow: 0 0 20px rgba(102, 126, 234, 0.5), 0 0 40px rgba(118, 75, 162, 0.3); }
        50% { box-shadow: 0 0 30px rgba(102, 126, 234, 0.8), 0 0 60px rgba(118, 75, 162, 0.5); }
    }
    
    /* Hero Section - Futuristic Design */
    .hero-container {
        position: relative;
        padding: 7rem 3rem 4rem;
        text-align: center;
        background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #4facfe);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        border-radius: 50px;
        margin: 1rem 1.5rem 3rem;
        overflow: hidden;
        box-shadow: 0 30px 90px rgba(102, 126, 234, 0.6);
        min-height: 520px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding-top: 8rem;
    }
    
    .hero-container::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 1px, transparent 1px);
        background-size: 50px 50px;
        animation: float 20s linear infinite;
        opacity: 0.4;
    }
    
    .hero-container::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at 20% 80%, rgba(255,255,255,0.2) 0%, transparent 50%),
                    radial-gradient(circle at 80% 20%, rgba(255,255,255,0.15) 0%, transparent 50%);
        pointer-events: none;
    }
    
    .hero-title {
        position: relative;
        z-index: 2;
        font-size: 3.8rem;
        font-weight: 900;
        color: white !important;
        margin: 2.5rem 0 1.2rem 0;
        text-shadow: 0 8px 30px rgba(0, 0, 0, 0.4), 0 4px 15px rgba(0, 0, 0, 0.3);
        letter-spacing: -2px;
        line-height: 1.1;
        animation: fadeInUp 0.8s ease-out;
    }
    
    .hero-subtitle {
        position: relative;
        z-index: 2;
        font-size: 1.3rem;
        color: rgba(255, 255, 255, 0.98) !important;
        margin: 0 auto 2rem;
        max-width: 700px;
        font-weight: 400;
        line-height: 1.6;
        animation: fadeInUp 1s ease-out;
        text-shadow: 0 3px 15px rgba(0, 0, 0, 0.4);
    }
    
    .hero-cta {
        position: relative;
        z-index: 2;
        display: inline-block;
        padding: 1.1rem 3rem;
        font-size: 1.15rem;
        font-weight: 700;
        color: #667eea !important;
        background: white;
        border: none;
        border-radius: 50px;
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        text-decoration: none !important;
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.3), 0 5px 15px rgba(255, 255, 255, 0.2);
        animation: fadeInUp 1.2s ease-out;
        overflow: hidden;
    }
    
    .hero-cta::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
        transition: left 0.5s;
    }
    
    .hero-cta:hover::before {
        left: 100%;
    }
    
    .hero-cta:hover {
        transform: translateY(-8px) scale(1.08);
        box-shadow: 0 25px 70px rgba(0, 0, 0, 0.4), 0 10px 25px rgba(102, 126, 234, 0.4);
        color: #667eea;
    }
    
    /* Animated Badge with Neon Effect */
    .beta-badge {
        position: absolute;
        top: 1.5rem;
        right: 2rem;
        z-index: 3;
        padding: 0.6rem 1.3rem;
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(20px);
        border: 2px solid rgba(255, 255, 255, 0.4);
        border-radius: 60px;
        color: white;
        font-weight: 700;
        font-size: 0.95rem;
        animation: pulse 2s infinite, float 3s ease-in-out infinite;
        box-shadow: 0 0 30px rgba(255, 255, 255, 0.3), inset 0 0 20px rgba(255, 255, 255, 0.1);
    }
    
    /* Feature Cards - Advanced Glassmorphism with 3D Effect */
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
        gap: 2.5rem;
        margin: 4rem 0;
        perspective: 1000px;
        padding: 0 1rem;
    }
    
    .glass-card {
        position: relative;
        padding: 3rem;
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(255, 255, 255, 0.88));
        backdrop-filter: blur(30px) saturate(180%);
        border: 2px solid rgba(102, 126, 234, 0.2);
        border-radius: 28px;
        box-shadow: 0 15px 50px rgba(102, 126, 234, 0.12), inset 0 1px 0 rgba(255, 255, 255, 0.8);
        transition: all 0.5s cubic-bezier(0.23, 1, 0.32, 1);
        overflow: hidden;
        transform-style: preserve-3d;
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    
    @media (prefers-color-scheme: dark) {
        .glass-card {
            background: linear-gradient(135deg, rgba(40, 40, 60, 0.8), rgba(30, 30, 50, 0.6));
            border: 2px solid rgba(255, 255, 255, 0.15);
        }
    }
    
    .glass-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: conic-gradient(from 0deg at 50% 50%, 
            transparent 0deg, 
            rgba(102, 126, 234, 0.3) 90deg, 
            transparent 180deg, 
            rgba(118, 75, 162, 0.3) 270deg, 
            transparent 360deg);
        animation: rotate 10s linear infinite;
        opacity: 0;
        transition: opacity 0.5s;
    }
    
    @keyframes rotate {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .glass-card:hover::before {
        opacity: 1;
    }
    
    .glass-card::after {
        content: '';
        position: absolute;
        top: 2px;
        left: 2px;
        right: 2px;
        bottom: 2px;
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.7));
        border-radius: 28px;
        z-index: -1;
    }
    
    @media (prefers-color-scheme: dark) {
        .glass-card::after {
            background: linear-gradient(135deg, rgba(35, 35, 55, 0.95), rgba(25, 25, 45, 0.85));
        }
    }
    
    .glass-card:hover {
        transform: translateY(-15px) scale(1.03);
        box-shadow: 0 30px 80px rgba(102, 126, 234, 0.35), 
                    0 10px 30px rgba(118, 75, 162, 0.25),
                    inset 0 1px 0 rgba(255, 255, 255, 1);
        border-color: rgba(102, 126, 234, 0.4);
        background: linear-gradient(135deg, rgba(255, 255, 255, 1), rgba(255, 255, 255, 0.98));
    }
    
    .feature-icon {
        font-size: 4rem;
        margin-bottom: 1.5rem;
        display: block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        filter: drop-shadow(0 8px 16px rgba(102, 126, 234, 0.2));
        animation: float 4s ease-in-out infinite;
        transition: all 0.3s ease;
    }
    
    .glass-card:hover .feature-icon {
        transform: scale(1.15) rotate(5deg);
        filter: drop-shadow(0 12px 24px rgba(102, 126, 234, 0.4));
    }
    
    .feature-title {
        font-size: 1.6rem;
        font-weight: 800;
        margin-bottom: 1rem;
        color: #2d3748;
        line-height: 1.3;
        transition: all 0.3s ease;
    }
    
    .glass-card:hover .feature-title {
        color: #667eea;
        transform: translateX(5px);
    }
    
    @media (prefers-color-scheme: dark) {
        .feature-title {
            color: white;
        }
        .glass-card:hover .feature-title {
            color: #4facfe;
        }
    }
    
    .feature-description {
        font-size: 1.05rem;
        line-height: 1.7;
        color: #4a5568;
        opacity: 0.9;
        transition: all 0.3s ease;
        flex-grow: 1;
    }
    
    .glass-card:hover .feature-description {
        opacity: 1;
        color: #2d3748;
    }
    
    /* Stats Section - Futuristic Design */
    .stats-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 2rem;
        margin: 3rem 0;
        padding: 3rem 2.5rem;
        background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #4facfe);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        border-radius: 35px;
        box-shadow: 0 30px 90px rgba(102, 126, 234, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .stats-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at 30% 50%, rgba(255, 255, 255, 0.1) 0%, transparent 50%);
        pointer-events: none;
    }
    
    .stat-item {
        text-align: center;
        color: white;
        position: relative;
        padding: 1.5rem;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 2px solid rgba(255, 255, 255, 0.2);
        transition: all 0.4s ease;
    }
    
    .stat-item:hover {
        transform: translateY(-10px) scale(1.05);
        background: rgba(255, 255, 255, 0.2);
        border-color: rgba(255, 255, 255, 0.4);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
    }
    
    .stat-number {
        font-size: 3.2rem;
        font-weight: 900;
        margin-bottom: 0.6rem;
        text-shadow: 0 6px 20px rgba(0, 0, 0, 0.4), 0 0 40px rgba(255, 255, 255, 0.3);
        animation: fadeInUp 1s ease-out;
        display: block;
    }
    
    .stat-label {
        font-size: 1.05rem;
        opacity: 0.95;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
    }
    
    /* Process Timeline - Modern 3D Style */
    .timeline-container {
        position: relative;
        margin: 5rem 0;
        padding: 4rem 2rem;
    }
    
    .timeline-container::before {
        content: '';
        position: absolute;
        left: 50%;
        top: 0;
        bottom: 0;
        width: 4px;
        background: linear-gradient(180deg, #667eea, #764ba2, #f093fb);
        transform: translateX(-50%);
        box-shadow: 0 0 20px rgba(102, 126, 234, 0.5);
    }
    
    .timeline-item {
        display: flex;
        align-items: center;
        margin: 3rem 0;
        gap: 3rem;
        position: relative;
        animation: slideInLeft 0.6s ease-out;
    }
    
    .timeline-item:nth-child(even) {
        flex-direction: row-reverse;
        animation: slideInRight 0.6s ease-out;
    }
    
    .timeline-number {
        flex-shrink: 0;
        width: 90px;
        height: 90px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 50%;
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.6), inset 0 -5px 20px rgba(0, 0, 0, 0.2);
        border: 4px solid white;
        position: relative;
        z-index: 2;
        transition: all 0.4s ease;
    }
    
    .timeline-item:hover .timeline-number {
        transform: scale(1.15) rotate(360deg);
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.8), inset 0 -5px 20px rgba(0, 0, 0, 0.3);
    }
    
    .timeline-content {
        flex: 1;
        padding: 2.5rem;
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.7));
        backdrop-filter: blur(20px);
        border-radius: 30px;
        border: 2px solid rgba(255, 255, 255, 0.5);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1), inset 0 1px 0 rgba(255, 255, 255, 0.8);
        transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1);
        position: relative;
    }
    
    .timeline-content::before {
        content: '';
        position: absolute;
        width: 0;
        height: 0;
        border-style: solid;
    }
    
    .timeline-item:nth-child(odd) .timeline-content::before {
        left: -15px;
        top: 50%;
        transform: translateY(-50%);
        border-width: 15px 15px 15px 0;
        border-color: transparent rgba(255, 255, 255, 0.9) transparent transparent;
    }
    
    .timeline-item:nth-child(even) .timeline-content::before {
        right: -15px;
        top: 50%;
        transform: translateY(-50%);
        border-width: 15px 0 15px 15px;
        border-color: transparent transparent transparent rgba(255, 255, 255, 0.9);
    }
    
    @media (prefers-color-scheme: dark) {
        .timeline-content {
            background: linear-gradient(135deg, rgba(40, 40, 60, 0.9), rgba(30, 30, 50, 0.7));
            border: 2px solid rgba(255, 255, 255, 0.2);
        }
        .timeline-item:nth-child(odd) .timeline-content::before {
            border-color: transparent rgba(40, 40, 60, 0.9) transparent transparent;
        }
        .timeline-item:nth-child(even) .timeline-content::before {
            border-color: transparent transparent transparent rgba(40, 40, 60, 0.9);
        }
    }
    
    .timeline-content:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 30px 80px rgba(102, 126, 234, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.9);
        border-color: rgba(102, 126, 234, 0.5);
    }
    
    .timeline-title {
        font-size: 1.5rem;
        font-weight: 800;
        margin-bottom: 0.8rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    @media (prefers-color-scheme: dark) {
        .timeline-title {
            -webkit-text-fill-color: #a0aef7;
        }
    }

    
    /* Responsive Design */
    @media (max-width: 768px) {
        .hero-title { 
            font-size: 2.5rem !important; 
            letter-spacing: -1px;
            margin-bottom: 1rem !important;
        }
        .hero-subtitle { 
            font-size: 1.1rem !important; 
            padding: 0 1rem;
            margin-bottom: 1.5rem !important;
        }
        .hero-container { 
            padding: 5rem 1.5rem 3.5rem !important;
            padding-top: 6rem !important;
            margin: 0.5rem 0.5rem 2.5rem !important; 
            border-radius: 35px !important;
            min-height: 420px !important;
        }
        .hero-title {
            margin-top: 2rem !important;
        }
        .hero-cta {
            padding: 1rem 2.2rem !important;
            font-size: 1rem !important;
        }
        .beta-badge {
            top: 0.8rem;
            right: 1rem;
            font-size: 0.75rem;
            padding: 0.5rem 0.9rem;
        }
        .feature-grid { 
            grid-template-columns: 1fr; 
            gap: 2rem;
            margin: 3rem 0;
            padding: 0 0.5rem;
        }
        .glass-card {
            padding: 2.5rem;
        }
        .feature-icon {
            font-size: 3.2rem;
            margin-bottom: 1.2rem;
        }
        .feature-title {
            font-size: 1.4rem;
            margin-bottom: 1rem;
        }
        .feature-description {
            font-size: 1rem;
            line-height: 1.6;
        }
        .stats-container { 
            grid-template-columns: repeat(2, 1fr); 
            padding: 2rem 1.5rem;
            gap: 1.2rem;
            margin: 2rem 0;
        }
        .stat-item {
            padding: 1.2rem;
        }
        .stat-number {
            font-size: 2.2rem;
            margin-bottom: 0.4rem;
        }
        .stat-label {
            font-size: 0.85rem;
            letter-spacing: 0.3px;
        }
        .section-header {
            margin: 3rem 0 2rem;
        }
        .section-title {
            font-size: 2.2rem;
            margin-bottom: 0.8rem;
        }
        .section-subtitle {
            font-size: 1rem;
            padding: 0 1rem;
        }
    }
    
    /* Section Headers - Enhanced Style */
    .section-header {
        text-align: center;
        margin: 4rem 0 3rem;
        position: relative;
        animation: fadeInUp 0.8s ease-out;
    }
    
    .section-header::after {
        content: '';
        position: absolute;
        bottom: -1rem;
        left: 50%;
        transform: translateX(-50%);
        width: 100px;
        height: 4px;
        background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
        border-radius: 2px;
        box-shadow: 0 0 20px rgba(102, 126, 234, 0.5);
    }
    
    .section-title {
        font-size: 2.8rem;
        font-weight: 900;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        background-size: 200% auto;
        animation: gradientShift 5s ease infinite;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
        letter-spacing: -1px;
        text-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
    }
    
    @media (prefers-color-scheme: dark) {
        .section-title {
            background: linear-gradient(135deg, #a0aef7 0%, #c4b0e8 50%, #ffa8d8 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
    }
    
    .section-subtitle {
        font-size: 1.2rem;
        opacity: 0.75;
        max-width: 650px;
        margin: 0 auto;
        font-weight: 400;
        line-height: 1.6;
    }
    
    /* Testimonial Section - Premium Cards */
    .testimonial-card {
        padding: 3rem;
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(255, 255, 255, 0.85));
        backdrop-filter: blur(30px);
        border-radius: 30px;
        border: 2px solid rgba(255, 255, 255, 0.5);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.08), inset 0 1px 0 rgba(255, 255, 255, 0.9);
        margin: 2rem 0;
        transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1);
        position: relative;
        overflow: hidden;
    }
    
    .testimonial-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.1), transparent);
        transition: left 0.6s;
    }
    
    .testimonial-card:hover::before {
        left: 100%;
    }
    
    .testimonial-card:hover {
        transform: translateY(-12px) scale(1.02);
        box-shadow: 0 30px 80px rgba(102, 126, 234, 0.2), inset 0 1px 0 rgba(255, 255, 255, 1);
        border-color: rgba(102, 126, 234, 0.4);
    }
    
    @media (prefers-color-scheme: dark) {
        .testimonial-card {
            background: linear-gradient(135deg, rgba(40, 40, 60, 0.95), rgba(30, 30, 50, 0.85));
            border: 2px solid rgba(255, 255, 255, 0.15);
        }
    }
    
    .quote-icon {
        font-size: 4rem;
        opacity: 0.15;
        line-height: 0;
        background: linear-gradient(135deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .testimonial-avatar {
        width: 60px;
        height: 60px;
        border-radius: 50%;
        border: 3px solid white;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
        transition: transform 0.3s ease;
    }
    
    .testimonial-card:hover .testimonial-avatar {
        transform: scale(1.1) rotate(5deg);
    }
</style>
""",
    unsafe_allow_html=True,
)

# Apply custom styling
apply_custom_css()

# Hero Section
st.markdown(
    """
<div class="hero-container">
    <div class="beta-badge">⚡ AI-Powered Excellence</div>
    <h1 class="hero-title">
        Resume<span style="background: linear-gradient(135deg, #f5576c, #f093fb, #ffd89b); -webkit-background-clip: text; -webkit-text-fill-color: transparent; filter: drop-shadow(0 0 30px rgba(240, 147, 251, 0.5));">Master</span>AI
    </h1>
    <p class="hero-subtitle">
        🚀 Transform your career with cutting-edge AI technology<br>
        Analyze • Optimize • Match • Land Your Dream Job
    </p>
    <a href="#get-started" class="hero-cta">
        Begin Your Journey 
        <span style="margin-left: 8px; display: inline-block; transition: transform 0.3s;">→</span>
    </a>
</div>
""",
    unsafe_allow_html=True,
)

# How It Works - Redesigned like the image
st.markdown(
    """
<div class="section-header">
    <h2 class="section-title">How It Works</h2>
    <p class="section-subtitle">Four simple steps to transform your career prospects</p>
</div>
""",
    unsafe_allow_html=True,
)

# Timeline items in 2x2 grid layout - matching the image style
col1, col2 = st.columns(2, gap="large")

with col1:
    # Step 1
    st.markdown(
        """
    <div style="display: flex; align-items: flex-start; gap: 1.5rem; margin: 2.5rem 0;">
        <div style="flex-shrink: 0; width: 80px; height: 80px; display: flex; align-items: center; justify-content: center; font-size: 2.5rem; font-weight: 900; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 50%; box-shadow: 0 15px 40px rgba(102, 126, 234, 0.5), 0 0 0 8px rgba(102, 126, 234, 0.1);">
            1
        </div>
        <div style="flex: 1; padding: 2.5rem; background: white; border-radius: 25px; box-shadow: 0 15px 50px rgba(0, 0, 0, 0.08); transition: all 0.3s ease;">
            <h3 style="font-size: 1.5rem; font-weight: 800; margin-bottom: 1rem; color: #667eea; display: flex; align-items: center; gap: 0.5rem;">
                📄 Upload Your Resume
            </h3>
            <p style="font-size: 1.05rem; line-height: 1.7; color: #4a5568; margin: 0;">
                Simply upload your resume in PDF, DOCX, or even scanned image format. Our advanced OCR technology handles any document type with precision.
            </p>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Step 3
    st.markdown(
        """
    <div style="display: flex; align-items: flex-start; gap: 1.5rem; margin: 2.5rem 0;">
        <div style="flex-shrink: 0; width: 80px; height: 80px; display: flex; align-items: center; justify-content: center; font-size: 2.5rem; font-weight: 900; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white; border-radius: 50%; box-shadow: 0 15px 40px rgba(240, 147, 251, 0.5), 0 0 0 8px rgba(240, 147, 251, 0.1);">
            3
        </div>
        <div style="flex: 1; padding: 2.5rem; background: white; border-radius: 25px; box-shadow: 0 15px 50px rgba(0, 0, 0, 0.08); transition: all 0.3s ease;">
            <h3 style="font-size: 1.5rem; font-weight: 800; margin-bottom: 1rem; color: #f093fb; display: flex; align-items: center; gap: 0.5rem;">
                💡 Get Insights
            </h3>
            <p style="font-size: 1.05rem; line-height: 1.7; color: #4a5568; margin: 0;">
                Receive comprehensive scoring, skill gap analysis, job matching results, and actionable recommendations to enhance your profile.
            </p>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col2:
    # Step 2
    st.markdown(
        """
    <div style="display: flex; align-items: flex-start; gap: 1.5rem; margin: 2.5rem 0;">
        <div style="flex-shrink: 0; width: 80px; height: 80px; display: flex; align-items: center; justify-content: center; font-size: 2.5rem; font-weight: 900; background: linear-gradient(135deg, #764ba2 0%, #a78bce 100%); color: white; border-radius: 50%; box-shadow: 0 15px 40px rgba(118, 75, 162, 0.5), 0 0 0 8px rgba(118, 75, 162, 0.1);">
            2
        </div>
        <div style="flex: 1; padding: 2.5rem; background: white; border-radius: 25px; box-shadow: 0 15px 50px rgba(0, 0, 0, 0.08); transition: all 0.3s ease;">
            <h3 style="font-size: 1.5rem; font-weight: 800; margin-bottom: 1rem; color: #764ba2; display: flex; align-items: center; gap: 0.5rem;">
                🤖 AI Analysis
            </h3>
            <p style="font-size: 1.05rem; line-height: 1.7; color: #4a5568; margin: 0;">
                Our intelligent AI engine analyzes your resume across multiple dimensions, identifying strengths, weaknesses, and opportunities for improvement.
            </p>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Step 4
    st.markdown(
        """
    <div style="display: flex; align-items: flex-start; gap: 1.5rem; margin: 2.5rem 0;">
        <div style="flex-shrink: 0; width: 80px; height: 80px; display: flex; align-items: center; justify-content: center; font-size: 2.5rem; font-weight: 900; background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); color: white; border-radius: 50%; box-shadow: 0 15px 40px rgba(79, 172, 254, 0.5), 0 0 0 8px rgba(79, 172, 254, 0.1);">
            4
        </div>
        <div style="flex: 1; padding: 2.5rem; background: white; border-radius: 25px; box-shadow: 0 15px 50px rgba(0, 0, 0, 0.08); transition: all 0.3s ease;">
            <h3 style="font-size: 1.5rem; font-weight: 800; margin-bottom: 1rem; color: #4facfe; display: flex; align-items: center; gap: 0.5rem;">
                🚀 Optimize & Apply
            </h3>
            <p style="font-size: 1.05rem; line-height: 1.7; color: #4a5568; margin: 0;">
                Use AI-powered rewriting, generate tailored cover letters, explore project suggestions, and discover perfectly matched job opportunities.
            </p>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

# Statistics Section with Gradient Background
st.markdown(
    """
<div class="section-header">
    <h2 class="section-title">Platform Statistics</h2>
    <p class="section-subtitle">Trusted by thousands of job seekers worldwide</p>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="stats-container">
    <div class="stat-item">
        <div class="stat-number">95%</div>
        <div class="stat-label">Accuracy Rate</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">10K+</div>
        <div class="stat-label">Resumes Analyzed</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">4.8⭐</div>
        <div class="stat-label">User Rating</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">500+</div>
        <div class="stat-label">Partner Companies</div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# Testimonials Section
st.markdown(
    """
<div class="section-header">
    <h2 class="section-title">What Our Users Say</h2>
    <p class="section-subtitle">Join thousands of satisfied job seekers</p>
</div>
""",
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
    <div class="testimonial-card">
        <div class="quote-icon">"</div>
        <p style="font-size: 1.1rem; line-height: 1.8; margin: 1.5rem 0; font-weight: 400;">
            "ResumeMasterAI helped me identify gaps I didn't even know existed. 
            Landed <strong style="color: #667eea;">3 interviews</strong> within a week!"
        </p>
        <div style="display: flex; align-items: center; gap: 1.2rem; margin-top: 2rem;">
            <div class="testimonial-avatar" style="width: 60px; height: 60px; border-radius: 50%; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); display: flex; align-items: center; justify-content: center; color: white; font-size: 1.5rem; font-weight: 700;">SJ</div>
            <div>
                <strong style="font-size: 1.1rem; display: block; margin-bottom: 0.3rem;">Sarah Johnson</strong>
                <span style="opacity: 0.7; font-size: 0.95rem;">Software Engineer @ Google</span>
            </div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
    <div class="testimonial-card">
        <div class="quote-icon">"</div>
        <p style="font-size: 1.1rem; line-height: 1.8; margin: 1.5rem 0; font-weight: 400;">
            "The AI rewriting feature transformed my resume. It now <strong style="color: #f093fb;">passes ATS systems</strong> 
            and gets noticed by recruiters!"
        </p>
        <div style="display: flex; align-items: center; gap: 1.2rem; margin-top: 2rem;">
            <div class="testimonial-avatar" style="width: 60px; height: 60px; border-radius: 50%; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); display: flex; align-items: center; justify-content: center; color: white; font-size: 1.5rem; font-weight: 700;">MC</div>
            <div>
                <strong style="font-size: 1.1rem; display: block; margin-bottom: 0.3rem;">Michael Chen</strong>
                <span style="opacity: 0.7; font-size: 0.95rem;">Data Scientist @ Meta</span>
            </div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
    <div class="testimonial-card">
        <div class="quote-icon">"</div>
        <p style="font-size: 1.1rem; line-height: 1.8; margin: 1.5rem 0; font-weight: 400;">
            "Best resume tool I've used. The job matching feature is <strong style="color: #4facfe;">incredibly 
            accurate</strong> and saved me hours of searching!"
        </p>
        <div style="display: flex; align-items: center; gap: 1.2rem; margin-top: 2rem;">
            <div class="testimonial-avatar" style="width: 60px; height: 60px; border-radius: 50%; background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); display: flex; align-items: center; justify-content: center; color: white; font-size: 1.5rem; font-weight: 700;">ER</div>
            <div>
                <strong style="font-size: 1.1rem; display: block; margin-bottom: 0.3rem;">Emily Rodriguez</strong>
                <span style="opacity: 0.7; font-size: 0.95rem;">Product Manager @ Amazon</span>
            </div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

# Call to Action with ID for anchor
st.markdown("<div id='get-started'></div>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    """
<div style="text-align: center; padding: 5rem 3rem; background: linear-gradient(-45deg, rgba(102, 126, 234, 0.15), rgba(118, 75, 162, 0.15), rgba(240, 147, 251, 0.15), rgba(79, 172, 254, 0.15)); background-size: 400% 400%; animation: gradientShift 10s ease infinite; border-radius: 40px; margin: 4rem 0; box-shadow: 0 20px 60px rgba(102, 126, 234, 0.2); border: 2px solid rgba(102, 126, 234, 0.2); position: relative; overflow: hidden;">
    <div style="position: absolute; top: -50%; left: -50%; width: 200%; height: 200%; background: radial-gradient(circle, rgba(255,255,255,0.1) 1px, transparent 1px); background-size: 40px 40px; opacity: 0.5; animation: float 15s linear infinite;"></div>
    <div style="position: relative; z-index: 1;">
        <h2 style="font-size: 3rem; font-weight: 900; margin-bottom: 1.5rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; letter-spacing: -1px;">
            🎯 Ready to Transform Your Career?
        </h2>
        <p style="font-size: 1.4rem; opacity: 0.85; margin-bottom: 2.5rem; max-width: 650px; margin-left: auto; margin-right: auto; line-height: 1.7;">
            Join <strong style="color: #667eea;">10,000+</strong> successful job seekers who landed their dream jobs.<br>
            Start optimizing your resume with AI today! 
        </p>
        <div style="display: flex; gap: 1rem; justify-content: center; align-items: center; flex-wrap: wrap;">
            <span style="font-size: 1.1rem; opacity: 0.7;">✓ Free to Start</span>
            <span style="font-size: 1.1rem; opacity: 0.7;">✓ No Credit Card</span>
            <span style="font-size: 1.1rem; opacity: 0.7;">✓ Instant Results</span>
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<style>
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        font-size: 1.3rem !important;
        font-weight: 700 !important;
        padding: 1.2rem 3rem !important;
        border-radius: 60px !important;
        border: none !important;
        box-shadow: 0 15px 50px rgba(102, 126, 234, 0.4), 0 5px 15px rgba(118, 75, 162, 0.3) !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        cursor: pointer !important;
        position: relative !important;
        overflow: hidden !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-8px) scale(1.05) !important;
        box-shadow: 0 25px 70px rgba(102, 126, 234, 0.6), 0 10px 25px rgba(118, 75, 162, 0.5) !important;
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%) !important;
    }
    
    .stButton > button:active {
        transform: translateY(-4px) scale(1.02) !important;
    }
</style>
""",
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button(
        "🚀 Start Your Journey Now",
        key="cta_button",
        use_container_width=True,
        type="primary",
    ):
        st.switch_page("pages/1_📄_Upload_Resume.py")

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    """
<div style="text-align: center; padding: 3rem 2rem; background: linear-gradient(135deg, rgba(102, 126, 234, 0.05), rgba(118, 75, 162, 0.05)); border-top: 2px solid rgba(102, 126, 234, 0.15); border-radius: 40px 40px 0 0; margin-top: 4rem;">
    <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap; margin-bottom: 2rem;">
        <span style="font-size: 1.05rem; opacity: 0.8;">🔒 Secure & Confidential</span>
        <span style="font-size: 1.05rem; opacity: 0.8;">🤖 Advanced AI Technology</span>
        <span style="font-size: 1.05rem; opacity: 0.8;">✅ GDPR Compliant</span>
        <span style="font-size: 1.05rem; opacity: 0.8;">⚡ Lightning Fast</span>
    </div>
    <div style="width: 80px; height: 3px; background: linear-gradient(90deg, #667eea, #764ba2, #f093fb); margin: 2rem auto; border-radius: 2px;"></div>
    <p style="font-size: 1rem; margin-top: 1.5rem; opacity: 0.7; font-weight: 500;">
        © 2025 ResumeMasterAI. Crafted with <span style="color: #f093fb; font-size: 1.2rem;">❤</span> for ambitious job seekers worldwide.
    </p>
    <p style="font-size: 0.9rem; margin-top: 0.8rem; opacity: 0.5;">
        Empowering careers • One resume at a time
    </p>
</div>
""",
    unsafe_allow_html=True,
)
