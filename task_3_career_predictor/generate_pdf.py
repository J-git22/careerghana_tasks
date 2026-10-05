import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.units import inch

pdf_path = r"c:\Users\yevug\OneDrive\Desktop\Python Dev Internship\task_3_career_predictor\Task_3_Career_Predictor_Report.pdf"
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    rightMargin=45, leftMargin=45,
    topMargin=45, bottomMargin=45
)

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

story = []

# Title Banner
story.append(Paragraph('CareerGhana Python Internship — Task 3', title_style))
story.append(Paragraph('<b>Deliverable:</b> Career Path Predictor (First Machine Learning Model) &amp; Writeup<br/><b>Repository:</b> https://github.com/J-git22/careerghana_tasks/tree/main/task_3_career_predictor', subtitle_style))
story.append(HRFlowable(width='100%', thickness=1.5, color=colors.HexColor('#2563EB'), spaceAfter=10))

# 1. Problem Statement
story.append(Paragraph('1. What Problem Does This Model Solve?', h1_style))
story.append(Paragraph('When aspiring tech professionals enter the field, they often wonder which career track best fits their background and personal aptitude. This project develops a supervised machine learning model using Python, Pandas, and Scikit-Learn that evaluates 5 technical skill dimensions and recommends the most aligned tech career track:', body_style))
for track in ['Software Engineering', 'Data Science', 'Cybersecurity', 'UI/UX Design']:
    story.append(Paragraph(f'&bull; <b>{track}</b>', bullet_style))
story.append(Spacer(1, 4))

# 2. Dataset
story.append(Paragraph('2. The Dataset Architecture (dataset.csv)', h1_style))
story.append(Paragraph('The model learns patterns from a curated dataset of 45 student/professional skill profiles rated across 5 core technical dimensions (scale 1 to 5):', body_style))

data = [
    ['Feature Name', 'Skill Domain Evaluated', 'Scale'],
    ['coding', 'Programming syntax, algorithms, data structures & OOP', '1 - 5'],
    ['math_statistics', 'Probability, linear algebra, statistical thinking', '1 - 5'],
    ['networking_security', 'Protocols, system vulnerabilities, defensive security', '1 - 5'],
    ['visual_design', 'UI wireframing, design principles, usability testing', '1 - 5'],
    ['cloud_sysadmin', 'Linux shell, cloud architecture, CI/CD, containers', '1 - 5'],
]
t = Table(data, colWidths=[120, 320, 80])
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

# 3. Model Mechanics
story.append(Paragraph('3. How the Model Works: Decision Tree Algorithm', h1_style))
story.append(Paragraph('We selected a <b>Decision Tree Classifier</b> because of its transparency, explainability, and speed on structured feature sets. It operates like an automated game of <i>20 Questions</i> by recursively identifying optimal thresholds that partition candidates into homogeneous career groups based on Gini impurity minimization.', body_style))

# 4. Evaluation & Results
story.append(Paragraph('4. Training, Evaluation &amp; Accuracy', h1_style))
story.append(Paragraph('The dataset was divided using a <b>stratified 75% train / 25% test split</b> to validate that the model generalizes to unseen candidates rather than simply memorizing training profiles.', body_style))

metrics_data = [
    ['Metric / Feature', 'Result / Contribution'],
    ['Model Test Accuracy', '91.7% on holdout test set'],
    ['Top Feature 1: math_statistics', '35.5% feature importance (primary discriminator for Data Science)'],
    ['Top Feature 2: coding', '34.3% feature importance (differentiates Software Engineering)'],
    ['Top Feature 3: networking_security', '30.3% feature importance (primary driver for Cybersecurity)'],
]
t2 = Table(metrics_data, colWidths=[180, 340])
t2.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0F172A')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 8),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')]),
    ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ('TOPPADDING', (0,0), (-1,-1), 3),
]))
story.append(t2)
story.append(Spacer(1, 6))

# 5. CLI Execution Sample
story.append(Paragraph('5. Verification &amp; Execution Output', h1_style))
sample_output = (
    "&gt; python career_predictor.py --coding 5 --math 2 --security 1 --design 1 --cloud 3<br/>"
    "Input Profile:    {'coding': 5, 'math_statistics': 2, 'networking_security': 1, 'visual_design': 1, 'cloud_sysadmin': 3}<br/>"
    "Predicted Career: &gt;&gt;&gt; SOFTWARE ENGINEERING &lt;&lt;&lt;<br/>"
    "Confidence:       Software Engineering: 100.0% | Cybersecurity: 0.0% | Data Science: 0.0% | UI/UX: 0.0%"
)
story.append(Paragraph(sample_output, code_style))

# 6. Conclusion
story.append(Paragraph('6. Summary &amp; Recommendations', h1_style))
story.append(Paragraph('The model successfully delivers clear, interpretable, data-driven career recommendations. Its high explainability ensures users understand exactly why a pathway is recommended based on their technical aptitudes.', body_style))

doc.build(story)
print("SUCCESS")
