# ResumeMasterAI 🚀

## AI-Powered Resume Optimization & Career Management Platform

ResumeMasterAI is a comprehensive, multi-page Streamlit application that leverages AI to help job seekers optimize their resumes, match job descriptions, generate cover letters, and build professional resumes from scratch.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Features

### 📄 Resume Upload & Parsing

- Support for PDF, DOCX, and TXT formats
- Advanced OCR for scanned documents
- Intelligent resume parsing with AI

### 📊 Analysis & Scoring

- Comprehensive ATS (Applicant Tracking System) compatibility scoring (100-point scale)
- Section analysis (30 points)
- Action verb detection (25 points)
- Quantifiable metrics analysis (25 points)
- Resume length optimization (20 points)
- Visual analytics and recommendations

### 🎯 Job Matching

- Smart job description matching
- Skills gap analysis
- Keyword optimization suggestions

### ✍️ Ultimate AI Resume Rewriting

- **Comprehensive Resume Optimization** with AI-powered rewriting
- **Multi-Feature Toolkit**:
  - ATS Scanner with real-time scoring and optimization tips
  - Version Management for tracking multiple resume iterations
  - Skills Analyzer with gap analysis and recommendations
  - Interview Preparation with AI-generated questions
  - Salary Estimator based on skills and location
  - Social Resume Generator for LinkedIn optimization
  - Email Generator for professional outreach
- **Advanced Analytics**:
  - Resume grading with detailed feedback
  - Job matching and compatibility scoring
  - Industry-specific optimization
- **Export Options**: Multiple format support (TXT, Markdown, DOCX, PDF)
- **Custom Instructions**: Tailor rewrites to specific job requirements

### 💼 Cover Letter & Project Generation
- AI-powered cover letter generation
- Customizable tone and skill highlighting
- Project suggestion based on skills
- Fallback templates with skill-specific recommendations

### 🔍 Job Search Integration

- Real-time job search capabilities
- Direct integration with job boards

### 🏗️ Resume Builder

- Build professional resumes from scratch
- **Sections**: Personal Info, Work Experience, Education, Skills, Certifications, Projects
- **New Features**:
  - Professional title field
  - Social media links (LinkedIn, GitHub, Twitter, Medium, Stack Overflow, Other)
  - Certificate verification links
  - Certificate issuer organization
- Edit ✏️ and Preview 👁️ modes
- Export to multiple formats

## 📝 Recent Updates

### Version Consolidation

- **Unified Resume Rewrite Page**: Consolidated three separate resume rewrite modules into a single, comprehensive **Ultimate Resume Rewrite** page
- All previous features from basic, enhanced, and ultimate versions are now integrated into one powerful interface
- Streamlined user experience with all career optimization tools in one place

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Google AI (Gemini) API key (optional but recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "job-sniper"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API keys**
   ```bash
   # Copy the example secrets file
   cp .streamlit/secrets.toml.example .streamlit/secrets.toml

   # Edit secrets.toml and add your API keys
   # Use your preferred editor, e.g., nano, vim, or code
   nano .streamlit/secrets.toml
   ```

5. **Run the application**
   ```bash
   streamlit run Home.py
   ```
   The application will open in your default browser at `http://localhost:8501`.

## 📦 Dependencies

Key dependencies include:

- `streamlit>=1.28.0` - Web framework
- `langchain>=0.3.27` - LLM orchestration
- `google-ai-generativelanguage>=0.7` - Google Gemini AI
- `python-docx>=2.8` - DOCX file handling
- `reportlab>=3.6.0` - PDF generation
- `pdfplumber` - PDF parsing
- `pytesseract` - OCR capabilities
- `matplotlib>=3.7.0` - Visualizations
- `seaborn>=0.12.0` - Statistical visualizations
- `pandas>=2.0.0` - Data manipulation

See `requirements.txt` for the complete list.

## 🎨 Design System

ResumeMasterAI features a modern, unified design system:

### Color Palette

- **Primary Gradient**: Purple (#667eea → #764ba2)
- **Secondary Gradient**: Blue-Green (#2E86AB → #06A77D)
- **Accent**: Orange (#F18F01)
- **Status Colors**: Success (#06A77D), Warning (#F18F01), Danger (#C73E1D)

### Design Features

- Glassmorphism effects
- Dark/Light mode compatibility
- Responsive layouts
- Smooth animations
- Consistent styling across all 7 pages

## 📱 Page Structure

1. **Home (🚀)** - Landing page with feature overview and quick navigation
2. **Upload Resume (📄)** - Parse and upload resumes with OCR support
3. **Analysis & Scoring (📊)** - Comprehensive ATS scoring and analytics
4. **Job Matching (🎯)** - Smart matching of resumes to job descriptions
5. **Ultimate Resume Rewrite (✍️)** - AI-powered optimization with advanced career tools
   - ATS Scanner & Optimizer
   - Version Management System
   - Skills Analysis & Gap Identification
   - Interview Prep Generator
   - Salary Estimator
   - Social Resume Generator
   - Professional Email Templates
   - Resume Grading & Feedback
6. **Cover Letter & Projects (💼)** - AI-generated cover letters and project suggestions
7. **Job Search (🔍)** - Real-time job board integration
8. **Resume Builder (🏗️)** - Build professional resumes from scratch with templates

## 🔧 Configuration

### Streamlit Configuration (`.streamlit/config.toml`)

- Theme colors
- Server settings
- Browser preferences

### Secrets Management (`.streamlit/secrets.toml`)

- API keys (Google AI, Groq, OpenAI)
- Service credentials
- **Never commit this file to version control!**

## 🌐 Deployment

### Streamlit Cloud

1. Push code to GitHub
2. Connect repository to Streamlit Cloud
3. Add secrets in Streamlit Cloud dashboard

### Docker

```bash
# Build image
docker build -t resumemasterai .

# Run container
docker run -p 8501:8501 resumemasterai
```

### Heroku

1. Create a new Heroku app
2. Set up environment variables
3. Deploy using Heroku CLI or GitHub integration

## 🙏 Acknowledgments

- **Streamlit** - Web framework
- **LangChain** - LLM orchestration
- **Google Gemini AI** - AI capabilities
- **ReportLab** - PDF generation
- **python-docx** - DOCX handling

---

## Built with ❤️ by the ResumeMasterAI Team

## Empowering job seekers with AI-driven career tools*
