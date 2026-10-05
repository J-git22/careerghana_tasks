import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'DocTitle',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=18,
    leading=22,
    textColor=colors.HexColor('#1E293B'),
    spaceAfter=4
)

subtitle_style = ParagraphStyle(
    'DocSubTitle',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=10,
    leading=14,
    textColor=colors.HexColor('#475569'),
    spaceAfter=12
)

h1_style = ParagraphStyle(
    'SectionH1',
    parent=styles['Heading2'],
    fontName='Helvetica-Bold',
    fontSize=12,
    leading=16,
    textColor=colors.HexColor('#0F172A'),
    spaceBefore=10,
    spaceAfter=5
)

body_style = ParagraphStyle(
    'Body',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9,
    leading=13,
    textColor=colors.HexColor('#334155'),
    spaceAfter=5
)

bullet_style = ParagraphStyle(
    'Bullet',
    parent=body_style,
    leftIndent=15,
    spaceAfter=2
)

code_style = ParagraphStyle(
    'CodeBlock',
    parent=styles['Code'],
    fontName='Courier',
    fontSize=8,
    leading=11,
    textColor=colors.HexColor('#0F172A'),
    backColor=colors.HexColor('#F1F5F9'),
    borderPadding=6,
    spaceBefore=3,
    spaceAfter=5
)

def build_task_1_pdf():
    pdf_path = r"c:\Users\yevug\OneDrive\Desktop\Python Dev Internship\task_1_career_quiz\Task_1_Career_Quiz_Report.pdf"
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        rightMargin=45, leftMargin=45,
        topMargin=45, bottomMargin=45
    )

    story = []
    story.append(Paragraph('CareerGhana Python Internship — Task 1', title_style))
    story.append(Paragraph('<b>Deliverable:</b> Interactive Career Path Quiz CLI Tool &amp; Documentation<br/><b>Repository:</b> https://github.com/J-git22/careerghana_tasks/tree/main/task_1_career_quiz', subtitle_style))
    story.append(HRFlowable(width='100%', thickness=1.5, color=colors.HexColor('#2563EB'), spaceAfter=10))

    story.append(Paragraph('1. Project Overview &amp; Objective', h1_style))
    story.append(Paragraph('The Career Quiz CLI tool is an interactive terminal application designed to guide aspiring technology professionals toward their optimal career specialization. By answering 7 targeted questions exploring developer problem-solving style, preferred work environments, and core interests, users receive an evidence-backed recommendation across 5 key industry tracks:', body_style))
    
    tracks = [
        '<b>Software Engineering / Full-Stack:</b> Building resilient end-to-end applications and backend architectures.',
        '<b>Data Science &amp; Machine Learning:</b> Extracting insights from data, statistics, and predictive modeling.',
        '<b>Cybersecurity Analyst:</b> Auditing vulnerability vectors, threat analysis, and infrastructure defense.',
        '<b>DevOps &amp; Cloud Engineering:</b> Server automation, cloud provisioning, CI/CD, and site reliability.',
        '<b>Product Design &amp; UI/UX:</b> Crafting human-centered user experiences, design systems, and visual interfaces.'
    ]
    for trk in tracks:
        story.append(Paragraph(f'&bull; {trk}', bullet_style))
    story.append(Spacer(1, 4))

    story.append(Paragraph('2. Career Track Evaluation Framework', h1_style))
    data = [
        ['Track ID', 'Career Pathway', 'Core Evaluation Focus'],
        ['SE', 'Software Engineering', 'Algorithms, OOP, system architecture, debugging code'],
        ['DS', 'Data Science / AI', 'Statistics, data modeling, exploratory analysis, metrics'],
        ['CS', 'Cybersecurity', 'Network defenses, penetration testing, cryptography, audit logs'],
        ['DO', 'DevOps & Cloud', 'Containers, Linux shell, infrastructure-as-code, reliability'],
        ['UI', 'Product / UI/UX Design', 'Design empathy, user flow, prototyping, accessibility'],
    ]
    t = Table(data, colWidths=[60, 160, 300])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2563EB')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')]),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('TOPPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t)
    story.append(Spacer(1, 6))

    story.append(Paragraph('3. Algorithm &amp; Scoring Logic', h1_style))
    story.append(Paragraph('Each of the 7 multiple-choice questions maps candidate responses to categorical weight vectors. At completion, scores are normalized into percentage affinity scores, highlighting primary and secondary affinities. The tool outputs visual progress bars, detailed descriptions, curated learning roadmaps, and immediate actionable steps.', body_style))

    story.append(Paragraph('4. Sample Terminal Execution Output', h1_style))
    sample_text = (
        "====================================================================<br/>"
        "                     🏆 YOUR CAREER RECOMMENDATION 🏆<br/>"
        "====================================================================<br/>"
        "Top Match: SOFTWARE ENGINEERING / FULL-STACK DEVELOPMENT (85.7%)<br/>"
        "Affinity Breakdown:<br/>"
        "  [1] Software Engineering  | [####################]  85.7%<br/>"
        "  [2] DevOps &amp; Cloud        | [############        ]  57.1%<br/>"
        "  [3] Data Science / ML     | [########            ]  28.6%<br/>"
        "===================================================================="
    )
    story.append(Paragraph(sample_text, code_style))

    story.append(Paragraph('5. Technical Highlights &amp; Standards', h1_style))
    story.append(Paragraph('&bull; <b>Zero External Dependencies:</b> Built strictly using Python 3 standard library modules for universal compatibility.<br/>&bull; <b>Defensive Input Validation:</b> Robustly handles invalid inputs, case variations, whitespace, EOF, and keyboard interrupts.<br/>&bull; <b>Cross-Platform:</b> Clean execution across Windows, macOS, and Linux terminals.', body_style))

    doc.build(story)
    print("Task 1 PDF generated.")

def build_task_2_pdf():
    pdf_path = r"c:\Users\yevug\OneDrive\Desktop\Python Dev Internship\task_2_resume_checker\Task_2_Resume_Checker_Report.pdf"
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        rightMargin=45, leftMargin=45,
        topMargin=45, bottomMargin=45
    )

    story = []
    story.append(Paragraph('CareerGhana Python Internship — Task 2', title_style))
    story.append(Paragraph('<b>Deliverable:</b> ATS Resume Keyword Checker &amp; Gap Analyzer Report<br/><b>Repository:</b> https://github.com/J-git22/careerghana_tasks/tree/main/task_2_resume_checker', subtitle_style))
    story.append(HRFlowable(width='100%', thickness=1.5, color=colors.HexColor('#0D9488'), spaceAfter=10))

    story.append(Paragraph('1. Project Overview &amp; Objective', h1_style))
    story.append(Paragraph('Modern recruitment workflows rely heavily on Applicant Tracking Systems (ATS) to filter and rank candidates before human review. This tool implements an automated ATS keyword scanner that evaluates candidate resumes against targeted job descriptions to identify exact keyword matches, calculate match percentages, and spotlight critical skill gaps.', body_style))

    story.append(Paragraph('2. Analysis Results &amp; Compatibility Summary', h1_style))
    metrics_data = [
        ['Metric / Indicator', 'Result Value', 'Assessment'],
        ['Resume Evaluated', 'sample_resume.txt', 'Developer intern candidate profile'],
        ['Target Keywords File', 'sample_job_keywords.txt', '20 benchmark skills & technologies'],
        ['Keywords Found', '13 of 20 (65.0%)', 'Strong alignment on core competencies'],
        ['Keywords Missing', '7 of 20 (35.0%)', 'Targeted areas for resume enhancement'],
        ['Compatibility Rating', 'GOOD MATCH', 'Meets majority of core technical requirements'],
    ]
    t = Table(metrics_data, colWidths=[130, 160, 230])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0D9488')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')]),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('TOPPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t)
    story.append(Spacer(1, 6))

    story.append(Paragraph('3. Keyword Distribution &amp; Gap Analysis', h1_style))
    story.append(Paragraph('<b>Found Keywords (with occurrence counts):</b> Python (6x), Docker (4x), Flask (4x), GitHub (4x), Agile (3x), PostgreSQL (3x), FastAPI (2x), Git (2x), REST APIs (2x), SQLite (2x), Linux (1x), TDD (1x), Unit Testing (1x).<br/><br/><b>Identified Skill Gaps:</b> AWS, CI/CD, Django, GraphQL, Kubernetes, MongoDB, Redis.', body_style))

    story.append(Paragraph('4. ATS Report Output Sample', h1_style))
    sample_text = (
        "======================================================================<br/>"
        "                    RESUME KEYWORD CHECKER REPORT<br/>"
        "======================================================================<br/>"
        "Total Keywords Analyzed: 20 | Found: 13 (65.0%) | Missing: 7 (35.0%)<br/>"
        "Compatibility Rating:    GOOD MATCH (Meets most core qualifications)<br/>"
        "----------------------------------------------------------------------<br/>"
        "[+] FOUND (13): Python (6), Docker (4), Flask (4), GitHub (4), ...<br/>"
        "[-] MISSING (7): AWS, CI/CD, Django, GraphQL, Kubernetes, MongoDB, Redis<br/>"
        "======================================================================"
    )
    story.append(Paragraph(sample_text, code_style))

    story.append(Paragraph('5. Actionable Advice &amp; Optimization', h1_style))
    story.append(Paragraph('Candidates are advised to explicitly showcase experience with missing technologies (e.g. AWS deployment, CI/CD pipelines, or container orchestration) in project bullet points to maximize their automated ATS score and interview callback rates.', body_style))

    doc.build(story)
    print("Task 2 PDF generated.")

if __name__ == "__main__":
    build_task_1_pdf()
    build_task_2_pdf()
