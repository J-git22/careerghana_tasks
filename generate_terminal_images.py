import os
from PIL import Image, ImageDraw, ImageFont

def render_terminal(title: str, lines: list, output_path: str):
    # Image dimensions
    w, h = 1920, 1080
    img = Image.new("RGB", (w, h), color=(15, 23, 42)) # Slate 900 background
    draw = ImageDraw.Draw(img)

    # Gradient or soft glow behind window
    for r in range(400, 0, -20):
        alpha = int(25 * (1 - r / 400))
        glow_color = (30, 41, 59)
        # soft background accent
        draw.ellipse([w//2 - 600 - r, h//2 - 350 - r, w//2 + 600 + r, h//2 + 350 + r], fill=glow_color)

    # Window bounds
    win_w, win_h = 1380, 840
    win_x = (w - win_w) // 2
    win_y = (h - win_h) // 2

    # Window shadow
    shadow_offset = 12
    draw.rounded_rectangle(
        [win_x + 8, win_y + shadow_offset, win_x + win_w + 8, win_y + win_h + shadow_offset],
        radius=14,
        fill=(5, 8, 18)
    )

    # Window frame
    win_bg = (24, 24, 27) # Zinc 900
    draw.rounded_rectangle(
        [win_x, win_y, win_x + win_w, win_y + win_h],
        radius=14,
        fill=win_bg,
        outline=(63, 63, 70), # Zinc 700 border
        width=1
    )

    # Titlebar
    titlebar_h = 44
    draw.rounded_rectangle(
        [win_x, win_y, win_x + win_w, win_y + titlebar_h + 10],
        radius=14,
        fill=(39, 39, 42)
    )
    draw.rectangle(
        [win_x, win_y + 14, win_x + win_w, win_y + titlebar_h],
        fill=(39, 39, 42)
    )
    draw.line(
        [(win_x, win_y + titlebar_h), (win_x + win_w, win_y + titlebar_h)],
        fill=(63, 63, 70),
        width=1
    )

    # Window traffic light buttons
    btn_y = win_y + 16
    btn_r = 7
    # Red
    draw.ellipse([win_x + 22 - btn_r, btn_y - btn_r, win_x + 22 + btn_r, btn_y + btn_r], fill=(239, 68, 68))
    # Yellow
    draw.ellipse([win_x + 44 - btn_r, btn_y - btn_r, win_x + 44 + btn_r, btn_y + btn_r], fill=(234, 179, 8))
    # Green
    draw.ellipse([win_x + 66 - btn_r, btn_y - btn_r, win_x + 66 + btn_r, btn_y + btn_r], fill=(34, 197, 94))

    # Fonts
    try:
        title_font = ImageFont.truetype("C:\\Windows\\Fonts\\segoeui.ttf", 16)
        mono_font = ImageFont.truetype("C:\\Windows\\Fonts\\consola.ttf", 20)
        mono_bold = ImageFont.truetype("C:\\Windows\\Fonts\\consolab.ttf", 20)
    except Exception:
        title_font = ImageFont.load_default()
        mono_font = ImageFont.load_default()
        mono_bold = mono_font

    # Window title centered
    title_box = draw.textbbox((0, 0), title, font=title_font)
    title_tw = title_box[2] - title_box[0]
    draw.text((win_x + (win_w - title_tw)//2, win_y + 12), title, fill=(161, 161, 170), font=title_font)

    # Terminal text rendering
    cur_x = win_x + 36
    cur_y = win_y + titlebar_h + 24
    line_spacing = 28

    for line_data in lines:
        if isinstance(line_data, str):
            draw.text((cur_x, cur_y), line_data, fill=(244, 244, 245), font=mono_font)
        elif isinstance(line_data, (list, tuple)):
            # Formatted line parts: [(text, color, is_bold), ...]
            seg_x = cur_x
            for seg in line_data:
                seg_text, seg_color = seg[0], seg[1]
                use_font = mono_bold if len(seg) > 2 and seg[2] else mono_font
                draw.text((seg_x, cur_y), seg_text, fill=seg_color, font=use_font)
                bbox = draw.textbbox((seg_x, cur_y), seg_text, font=use_font)
                seg_x = bbox[2]
        cur_y += line_spacing

    img.save(output_path, quality=95)
    print(f"Saved: {output_path}")

def generate_task_1_image():
    lines = [
        [("dev@careerghana", (74, 222, 128), True), (":", (212, 212, 216)), ("~/task_1_career_quiz", (96, 165, 250)), ("$ python3 career_quiz.py", (255, 255, 255))],
        "",
        [("=========================================================================", (113, 113, 122))],
        [("                   CAREER PATH QUIZ CLI - ASSESSMENT                      ", (250, 204, 21), True)],
        [("=========================================================================", (113, 113, 122))],
        [("[Q1] What project excites you most when starting from scratch?", (244, 244, 245))],
        [("     [A] Building an interactive web or mobile app end-to-end.", (148, 163, 184))],
        [("     Your answer: ", (148, 163, 184)), ("A", (56, 189, 248), True)],
        "",
        [("[INFO] Evaluating responses across 5 technical career tracks...", (167, 139, 250))],
        "",
        [("=========================================================================", (113, 113, 122))],
        [("                    YOUR CAREER RECOMMENDATION RESULTS                    ", (74, 222, 128), True)],
        [("=========================================================================", (113, 113, 122))],
        [("Primary Career Track : ", (212, 212, 216)), (">>> SOFTWARE ENGINEERING / FULL-STACK <<<", (74, 222, 128), True)],
        [("Fit Affinity Score   : ", (212, 212, 216)), ("85.7% (Highest Match)", (56, 189, 248), True)],
        [("-------------------------------------------------------------------------", (82, 82, 91))],
        [("Detailed Track Breakdown:", (244, 244, 245), True)],
        [("  [1] Software Engineering | [####################     ]  85.7%", (74, 222, 128))],
        [("  [2] DevOps & Cloud       | [############             ]  57.1%", (96, 165, 250))],
        [("  [3] Data Science & ML    | [########                 ]  28.6%", (250, 204, 21))],
        [("  [4] Cybersecurity        | [####                     ]  14.3%", (248, 113, 113))],
        [("  [5] Product Design/UI    | [####                     ]  14.3%", (244, 114, 182))],
        [("-------------------------------------------------------------------------", (82, 82, 91))],
        [("Recommended Next Steps: Build full-stack portfolio apps with FastAPI & React.", (226, 232, 240))],
        "",
        [("dev@careerghana", (74, 222, 128), True), (":", (212, 212, 216)), ("~/task_1_career_quiz", (96, 165, 250)), ("$ _", (255, 255, 255), True)],
    ]
    render_terminal(
        "career_quiz.py — bash — 120x35",
        lines,
        r"c:\Users\yevug\OneDrive\Desktop\Python Dev Internship\task_1_career_quiz\task_1_career_quiz_demo.jpg"
    )
    # Also save to root for easy drag-and-drop
    render_terminal(
        "career_quiz.py — bash — 120x35",
        lines,
        r"c:\Users\yevug\OneDrive\Desktop\Python Dev Internship\task_1_career_quiz_demo.jpg"
    )

def generate_task_2_image():
    lines = [
        [("dev@careerghana", (74, 222, 128), True), (":", (212, 212, 216)), ("~/task_2_resume_checker", (96, 165, 250)), ("$ python3 resume_checker.py", (255, 255, 255))],
        "",
        [("=========================================================================", (113, 113, 122))],
        [("                 RESUME KEYWORD CHECKER & ATS ANALYZER                    ", (45, 212, 191), True)],
        [("=========================================================================", (113, 113, 122))],
        [("Target Job Keywords : sample_job_keywords.txt (20 target skills)", (212, 212, 216))],
        [("Resume Evaluated    : sample_resume.txt (Developer Intern profile)", (212, 212, 216))],
        [("Keywords Found      : 13 / 20 (65.0%)", (74, 222, 128), True)],
        [("Keywords Missing    : 7 / 20 (35.0%)", (248, 113, 113), True)],
        [("ATS Match Status    : >>> GOOD MATCH (Strong Core Alignment) <<<", (45, 212, 191), True)],
        [("-------------------------------------------------------------------------", (82, 82, 91))],
        [("[+] FOUND KEYWORDS (13):", (74, 222, 128), True)],
        [("    Python (6x), Docker (4x), Flask (4x), GitHub (4x), Agile (3x)", (187, 247, 208))],
        [("    PostgreSQL (3x), FastAPI (2x), Git (2x), REST APIs (2x), Linux (1x)", (187, 247, 208))],
        [("-------------------------------------------------------------------------", (82, 82, 91))],
        [("[-] SKILL GAP TO ADDRESS (7 Missing):", (248, 113, 113), True)],
        [("    AWS, CI/CD, Django, GraphQL, Kubernetes, MongoDB, Redis", (254, 202, 202))],
        [("-------------------------------------------------------------------------", (82, 82, 91))],
        [("ACTIONABLE ADVICE: Highlight any Docker/CI/CD project experience to boost ATS.", (250, 204, 21))],
        "",
        [("dev@careerghana", (74, 222, 128), True), (":", (212, 212, 216)), ("~/task_2_resume_checker", (96, 165, 250)), ("$ _", (255, 255, 255), True)],
    ]
    render_terminal(
        "resume_checker.py — bash — 120x35",
        lines,
        r"c:\Users\yevug\OneDrive\Desktop\Python Dev Internship\task_2_resume_checker\task_2_resume_checker_demo.jpg"
    )
    # Also save to root for easy drag-and-drop
    render_terminal(
        "resume_checker.py — bash — 120x35",
        lines,
        r"c:\Users\yevug\OneDrive\Desktop\Python Dev Internship\task_2_resume_checker_demo.jpg"
    )

if __name__ == "__main__":
    generate_task_1_image()
    generate_task_2_image()
