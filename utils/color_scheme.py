"""
Unified Color Scheme Configuration for ResumeMasterAI
All pages should use these consistent colors for a professional look
"""

# Primary Brand Colors
PRIMARY_GRADIENT_START = "#667eea"
PRIMARY_GRADIENT_END = "#764ba2"
PRIMARY_GRADIENT = f"linear-gradient(135deg, {PRIMARY_GRADIENT_START} 0%, {PRIMARY_GRADIENT_END} 100%)"

# Secondary Colors
SECONDARY_GRADIENT_START = "#2E86AB"
SECONDARY_GRADIENT_END = "#06A77D"
SECONDARY_GRADIENT = f"linear-gradient(135deg, {SECONDARY_GRADIENT_START} 0%, {SECONDARY_GRADIENT_END} 100%)"

# Accent Colors
ACCENT_ORANGE = "#F18F01"
ACCENT_PINK_START = "#f093fb"
ACCENT_PINK_END = "#f5576c"
ACCENT_PINK_GRADIENT = f"linear-gradient(135deg, {ACCENT_PINK_START} 0%, {ACCENT_PINK_END} 100%)"

# Status Colors
SUCCESS_GREEN = "#06A77D"
WARNING_ORANGE = "#F18F01"
DANGER_RED = "#C73E1D"
INFO_BLUE = "#2E86AB"

# Neutral Colors
BACKGROUND_LIGHT = "#F8F9FA"
CARD_BACKGROUND = "#FFFFFF"
TEXT_PRIMARY = "#2D3142"
TEXT_SECONDARY = "#4F5D75"
BORDER_COLOR = "#E5E5E5"

# Dark Mode Colors (for prefers-color-scheme: dark)
DARK_BACKGROUND = "#1a1a2e"
DARK_CARD = "#16213e"
DARK_TEXT_PRIMARY = "#eaeaea"
DARK_TEXT_SECONDARY = "#bfbfbf"

# Shadow and Effects
SHADOW_SM = "0 2px 8px rgba(0,0,0,0.08)"
SHADOW_MD = "0 4px 12px rgba(0,0,0,0.1)"
SHADOW_LG = "0 8px 24px rgba(0,0,0,0.12)"
GLASS_EFFECT = "backdrop-filter: blur(10px); background: rgba(255, 255, 255, 0.9);"

def get_unified_css():
    """
    Returns unified CSS that should be applied to all pages
    """
    return f"""
    <style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
    
    /* Global Styles */
    * {{
        font-family: 'Inter', sans-serif;
    }}
    
    /* Streamlit Overrides */
    .main {{
        background: {BACKGROUND_LIGHT};
    }}
    
    /* Unified Card Style */
    .unified-card {{
        background: {CARD_BACKGROUND};
        border-radius: 16px;
        padding: 2rem;
        box-shadow: {SHADOW_MD};
        border-left: 4px solid {PRIMARY_GRADIENT_START};
        margin: 1rem 0;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }}
    
    .unified-card:hover {{
        transform: translateY(-4px);
        box-shadow: {SHADOW_LG};
    }}
    
    /* Glass Card Style */
    .glass-card {{
        {GLASS_EFFECT}
        border-radius: 20px;
        padding: 2rem;
        box-shadow: {SHADOW_MD};
        border: 1px solid rgba(255, 255, 255, 0.3);
        margin: 1rem 0;
    }}
    
    /* Gradient Headers */
    .gradient-header {{
        background: {PRIMARY_GRADIENT};
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 800;
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }}
    
    /* Button Styles */
    .stButton > button {{
        background: {PRIMARY_GRADIENT};
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: {SHADOW_SM};
    }}
    
    .stButton > button:hover {{
        transform: translateY(-2px);
        box-shadow: {SHADOW_MD};
    }}
    
    /* Badge Styles */
    .badge-success {{
        background: {SUCCESS_GREEN};
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: 600;
        display: inline-block;
    }}
    
    .badge-warning {{
        background: {WARNING_ORANGE};
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: 600;
        display: inline-block;
    }}
    
    .badge-danger {{
        background: {DANGER_RED};
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: 600;
        display: inline-block;
    }}
    
    /* Progress Bar */
    .progress-bar {{
        background: {BORDER_COLOR};
        height: 8px;
        border-radius: 4px;
        overflow: hidden;
        margin: 1rem 0;
    }}
    
    .progress-fill {{
        background: {SECONDARY_GRADIENT};
        height: 100%;
        transition: width 0.5s ease;
    }}
    
    /* Social Media Icons */
    .social-icon {{
        display: inline-block;
        width: 40px;
        height: 40px;
        background: {PRIMARY_GRADIENT};
        border-radius: 50%;
        text-align: center;
        line-height: 40px;
        color: white;
        margin: 0 0.5rem;
        transition: transform 0.3s ease;
    }}
    
    .social-icon:hover {{
        transform: scale(1.1) rotate(5deg);
    }}
    
    /* Dark Mode Support */
    @media (prefers-color-scheme: dark) {{
        .main {{
            background: {DARK_BACKGROUND};
        }}
        
        .unified-card, .glass-card {{
            background: {DARK_CARD};
            color: {DARK_TEXT_PRIMARY};
            border-color: rgba(255, 255, 255, 0.1);
        }}
        
        .unified-card:hover {{
            box-shadow: 0 8px 24px rgba(0,0,0,0.3);
        }}
    }}
    
    /* Animations */
    @keyframes fadeInUp {{
        from {{
            opacity: 0;
            transform: translateY(30px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
    
    .animate-fade-in {{
        animation: fadeInUp 0.6s ease-out;
    }}
    
    @keyframes pulse {{
        0%, 100% {{
            opacity: 1;
        }}
        50% {{
            opacity: 0.7;
        }}
    }}
    
    .animate-pulse {{
        animation: pulse 2s infinite;
    }}
    </style>
    """
