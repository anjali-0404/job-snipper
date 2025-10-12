"""
Professional custom styling and UI components for the Resume AI Assistant.
"""

import streamlit as st


def apply_custom_css():
    """Apply professional custom CSS styling to the Streamlit app."""

    st.markdown(
        """
    <style>
    /* Import modern font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global styling */
    * {
        font-family: 'Inter', 'Segoe UI', sans-serif;
    }
    
    /* Main container */
    .main {
        padding: 0rem 1rem;
    }
    
    /* Streamlit default elements */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Headers */
    h1 {
        color: #2D3142;
        font-weight: 700;
        letter-spacing: -0.5px;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #2E86AB;
    }
    
    h2 {
        color: #2D3142;
        font-weight: 600;
        margin-top: 2rem;
    }
    
    h3 {
        color: #4F5D75;
        font-weight: 500;
    }
    
    /* Custom card styling */
    .custom-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07);
        margin: 1rem 0;
        border-left: 4px solid #2E86AB;
    }
    
    .feature-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        height: 100%;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    /* Hero section */
    .hero-section {
        background: linear-gradient(135deg, #2E86AB 0%, #A23B72 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        text-align: center;
        color: white;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    }
    
    .hero-title {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    }
    
    .hero-subtitle {
        font-size: 1.3rem;
        font-weight: 300;
        opacity: 0.95;
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #2E86AB 0%, #06A77D 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }
    
    /* File uploader */
    .stFileUploader {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        border: 2px dashed #2E86AB;
    }
    
    /* Text input and text area */
    .stTextInput>div>div>input,
    .stTextArea>div>div>textarea {
        border-radius: 8px;
        border: 2px solid #E5E5E5;
        padding: 0.75rem;
        transition: border-color 0.3s ease;
    }
    
    .stTextInput>div>div>input:focus,
    .stTextArea>div>div>textarea:focus {
        border-color: #2E86AB;
        box-shadow: 0 0 0 3px rgba(46, 134, 171, 0.1);
    }
    
    /* Metrics */
    .stMetric {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }
    
    /* Sidebar */
    .css-1d391kg {
        background: linear-gradient(180deg, #2D3142 0%, #4F5D75 100%);
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #2D3142 0%, #4F5D75 100%);
    }
    
    /* Progress bar */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #2E86AB 0%, #06A77D 100%);
    }
    
    /* Info, Success, Warning, Error boxes */
    .stAlert {
        border-radius: 10px;
        border-left-width: 5px;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px 8px 0 0;
        padding: 10px 20px;
        background-color: #f0f2f6;
        font-weight: 500;
    }
    
    .stTabs [aria-selected="true"] {
        background: white;
        color: #2E86AB;
        font-weight: 600;
    }
    
    /* Dataframe */
    .stDataFrame {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: white;
        border-radius: 8px;
        font-weight: 600;
    }
    
    /* Navigation pills */
    .nav-pill {
        display: inline-block;
        padding: 0.5rem 1.5rem;
        margin: 0.25rem;
        background: white;
        border-radius: 20px;
        color: #2E86AB;
        text-decoration: none;
        font-weight: 500;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .nav-pill:hover {
        background: #2E86AB;
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }
    
    /* Score badge */
    .score-badge {
        display: inline-block;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 1.2rem;
    }
    
    .score-excellent {
        background: linear-gradient(135deg, #06A77D 0%, #04D98B 100%);
        color: white;
    }
    
    .score-good {
        background: linear-gradient(135deg, #F18F01 0%, #FFB627 100%);
        color: white;
    }
    
    .score-needs-improvement {
        background: linear-gradient(135deg, #C73E1D 0%, #E85D4A 100%);
        color: white;
    }
    
    /* Stat box */
    .stat-box {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        color: #2E86AB;
        margin: 0;
    }
    
    .stat-label {
        font-size: 0.9rem;
        color: #4F5D75;
        font-weight: 500;
        margin-top: 0.5rem;
    }
    
    /* Timeline */
    .timeline-item {
        position: relative;
        padding-left: 2rem;
        padding-bottom: 1.5rem;
        border-left: 2px solid #2E86AB;
    }
    
    .timeline-item:before {
        content: '';
        position: absolute;
        left: -6px;
        top: 0;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background: #2E86AB;
    }
    
    .timeline-item-completed:before {
        background: #06A77D;
    }
    
    /* Tooltip */
    .tooltip {
        position: relative;
        display: inline-block;
        border-bottom: 1px dotted #2E86AB;
        cursor: help;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #2E86AB 0%, #06A77D 100%);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #2D3142;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )


def create_hero_section(title, subtitle):
    """Create a professional hero section."""
    st.markdown(
        f"""
    <div class="hero-section">
        <div class="hero-title">{title}</div>
        <div class="hero-subtitle">{subtitle}</div>
    </div>
    """,
        unsafe_allow_html=True,
    )


def create_feature_card(icon, title, description):
    """Create a feature card component."""
    return f"""
    <div class="feature-card">
        <div class="feature-icon">{icon}</div>
        <h3>{title}</h3>
        <p>{description}</p>
    </div>
    """


def create_stat_box(number, label):
    """Create a stat box component."""
    return f"""
    <div class="stat-box">
        <div class="stat-number">{number}</div>
        <div class="stat-label">{label}</div>
    </div>
    """


def create_score_badge(score):
    """Create a score badge with appropriate color."""
    if score >= 80:
        badge_class = "score-excellent"
        label = "Excellent"
    elif score >= 60:
        badge_class = "score-good"
        label = "Good"
    else:
        badge_class = "score-needs-improvement"
        label = "Needs Improvement"

    return f"""
    <div class="score-badge {badge_class}">
        {score:.0f}/100 - {label}
    </div>
    """
