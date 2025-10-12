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

### ✍️ AI Resume Rewriting

- Intelligent resume optimization
- ATS score tracking with color-coded badges
- Custom instruction support
- **5 Export Formats**: TXT, Markdown, DOCX, PDF, Copy to Clipboard

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

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Google AI (Gemini) API key (optional but recommended)

### Installation

1. **Clone the repository**

```bash
git clone <repository-url>
cd "job snipper"
```

1.1 **Install dependencies**

```bash
pip install -r requirements.txt
```

1.2 **Configure API keys**

```bash
# Copy the example secrets file
copy .streamlit\secrets.toml.example .streamlit\secrets.toml

# Edit secrets.toml and add your API keys
notepad .streamlit\secrets.toml
```

1.3 **Run the application**

```bash
streamlit run Home.py
```

The application will open in your default browser at `http://localhost:8501`

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

See `requirements.txt` for complete list.

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

1. **Home (🚀)** - Landing page with feature overview
2. **Upload Resume (📄)** - Parse and upload resumes
3. **Analysis & Scoring (📊)** - ATS scoring and analytics
4. **Job Matching (🎯)** - Match resumes to job descriptions
5. **Resume Rewrite (✍️)** - AI-powered optimization
6. **Cover Letter & Projects (💼)** - Generate cover letters and project ideas
7. **Job Search (🔍)** - Search for jobs
8. **Resume Builder (🏗️)** - Build professional resumes from scratch

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
