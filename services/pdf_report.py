from fpdf import FPDF

def generate_resume_report(resume_json, match_info, cover_letter, file_path="data/reports/resume_report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Resume Analysis Report", ln=True)
    
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 8, f"Resume Score: {match_info.get('match_score', 0)}")
    pdf.multi_cell(0, 8, f"Matched Skills: {', '.join(match_info.get('matched_skills', []))}")
    pdf.multi_cell(0, 8, f"Missing Skills: {', '.join(match_info.get('missing_skills', []))}")
    pdf.multi_cell(0, 8, f"Suggested Cover Letter:\n{cover_letter}")

    pdf.output(file_path)
    return file_path
