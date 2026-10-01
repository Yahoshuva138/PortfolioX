import os
from PIL import Image, ImageDraw, ImageFont

WIDTH = 1200
HEIGHT = 750

def get_font(size, bold=False):
    font_paths = [
        "C:\\Windows\\Fonts\\segoeuib.ttf" if bold else "C:\\Windows\\Fonts\\segoeui.ttf",
        "C:\\Windows\\Fonts\\arialbd.ttf" if bold else "C:\\Windows\\Fonts\\arial.ttf",
        "C:\\Windows\\Fonts\\consola.ttf"
    ]
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()

def draw_browser_chrome(draw, title, url):
    draw.rectangle([(0, 0), (WIDTH, HEIGHT)], fill=(11, 15, 25))
    draw.rectangle([(0, 0), (WIDTH, 56)], fill=(20, 27, 45))
    draw.line([(0, 56), (WIDTH, 56)], fill=(37, 49, 78), width=1)
    
    draw.ellipse([(24, 20), (38, 34)], fill=(244, 63, 94))
    draw.ellipse([(46, 20), (60, 34)], fill=(251, 191, 36))
    draw.ellipse([(68, 20), (82, 34)], fill=(52, 211, 153))
    
    draw.rounded_rectangle([(110, 12), (760, 44)], radius=6, fill=(11, 15, 25), outline=(45, 59, 90), width=1)
    draw.text((128, 18), f"https://{url}", fill=(148, 163, 184), font=get_font(15))
    draw.text((800, 17), title, fill=(203, 213, 225), font=get_font(16, bold=True))

def create_mockup_1():
    img = Image.new("RGB", (WIDTH, HEIGHT), color=(11, 15, 25))
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "Smart Document Assistant", "smart-doc-assistant.org")
    
    draw.rectangle([(0, 56), (WIDTH, 125)], fill=(16, 22, 38))
    draw.text((60, 78), "SMART DOCUMENT ASSISTANT", fill=(99, 102, 241), font=get_font(22, bold=True))
    
    draw.rounded_rectangle([(870, 75), (1140, 110)], radius=18, fill=(16, 185, 129))
    draw.text((890, 83), "100% Client-Side Privacy", fill=(255, 255, 255), font=get_font(14, bold=True))
    
    draw.rounded_rectangle([(60, 150), (1140, 290)], radius=14, fill=(20, 27, 45), outline=(99, 102, 241), width=2)
    draw.text((90, 175), "Reverse Document Matcher & Service Navigator", fill=(248, 250, 252), font=get_font(26, bold=True))
    draw.text((90, 215), "Instant eligibility verification across Aadhaar, Passport, PAN Card & National Scholarships.", fill=(148, 163, 184), font=get_font(16))
    
    draw.rounded_rectangle([(90, 245), (280, 275)], radius=6, fill=(99, 102, 241))
    draw.text((115, 252), "Scan My Documents", fill=(255, 255, 255), font=get_font(14, bold=True))
    
    draw.rounded_rectangle([(300, 245), (480, 275)], radius=6, fill=(37, 49, 78))
    draw.text((325, 252), "Voice Assistant Mode", fill=(226, 232, 240), font=get_font(14, bold=True))

    cards = [
        {"code": "PASS", "title": "Indian Passport", "subtitle": "Tatkaal & Normal", "color": (16, 185, 129), "badge": "100% READY"},
        {"code": "UIDAI", "title": "Aadhaar Card", "subtitle": "Biometric & Address", "color": (56, 189, 248), "badge": "GUIDE READY"},
        {"code": "PAN", "title": "Instant e-PAN", "subtitle": "Form 49A Paperless", "color": (16, 185, 129), "badge": "VERIFIED"},
        {"code": "NSP", "title": "Scholarship OTR", "subtitle": "Central Sector Portal", "color": (245, 158, 11), "badge": "1 DOC LEFT"}
    ]
    
    card_w = 250
    card_h = 255
    start_x = 60
    start_y = 315
    gap = 46
    
    for i, c in enumerate(cards):
        x = start_x + i * (card_w + gap)
        y = start_y
        draw.rounded_rectangle([(x, y), (x + card_w, y + card_h)], radius=12, fill=(18, 25, 42), outline=(37, 49, 78), width=1)
        
        draw.rounded_rectangle([(x + 20, y + 20), (x + 85, y + 48)], radius=6, fill=(30, 41, 65))
        draw.text((x + 28, y + 26), c["code"], fill=(165, 180, 252), font=get_font(13, bold=True))
        
        draw.rounded_rectangle([(x + card_w - 110, y + 22), (x + card_w - 18, y + 46)], radius=10, fill=(11, 15, 25), outline=c["color"], width=1)
        draw.text((x + card_w - 100, y + 27), c["badge"], fill=c["color"], font=get_font(11, bold=True))
        
        draw.text((x + 20, y + 70), c["title"], fill=(241, 245, 249), font=get_font(18, bold=True))
        draw.text((x + 20, y + 100), c["subtitle"], fill=(148, 163, 184), font=get_font(13))
            
        draw.text((x + 20, y + 150), "[OK] Identity Proof", fill=(52, 211, 153), font=get_font(12, bold=True))
        draw.text((x + 20, y + 172), "[OK] Address Proof", fill=(52, 211, 153), font=get_font(12, bold=True))
        
        draw.rounded_rectangle([(x + 20, y + 205), (x + card_w - 20, y + 238)], radius=6, fill=(30, 41, 65))
        draw.text((x + 40, y + 213), "Step-by-Step Guide ->", fill=(99, 102, 241), font=get_font(13, bold=True))

    draw.rectangle([(0, 680), (WIDTH, HEIGHT)], fill=(11, 15, 25))
    draw.line([(0, 680), (WIDTH, 680)], fill=(37, 49, 78), width=1)
    draw.text((60, 705), "Stack: React 19 • TypeScript • Tailwind CSS • Web Speech Synthesis API • 12-Section Portals", fill=(100, 116, 139), font=get_font(14))

    img.save("images/project-1.png")

def create_mockup_2():
    img = Image.new("RGB", (WIDTH, HEIGHT), color=(11, 15, 25))
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "Anime Directory & Vault", "anime-directory.yahoshuva.dev")
    
    draw.rectangle([(0, 56), (WIDTH, 125)], fill=(16, 22, 38))
    draw.text((60, 78), "ANIME EXPLORER VAULT", fill=(244, 63, 94), font=get_font(22, bold=True))
    
    draw.rounded_rectangle([(440, 72), (800, 108)], radius=8, fill=(24, 33, 53), outline=(45, 59, 90), width=1)
    draw.text((460, 81), "Search 60+ curated anime titles...", fill=(156, 163, 175), font=get_font(14))
    
    draw.rounded_rectangle([(840, 72), (1140, 108)], radius=8, fill=(30, 41, 65), outline=(244, 63, 94), width=1)
    draw.text((860, 81), "IMDb Curated List ls500222778", fill=(251, 113, 133), font=get_font(13, bold=True))

    draw.rectangle([(0, 125), (WIDTH, 180)], fill=(20, 27, 45))
    categories = ["All (60)", "Action", "Drama", "Sci-Fi", "Fantasy", "Psychological", "Adventure"]
    btn_x = 60
    for i, cat in enumerate(categories):
        is_active = (i == 0)
        bg = (244, 63, 94) if is_active else (30, 41, 65)
        fg = (255, 255, 255) if is_active else (156, 163, 175)
        text_w = len(cat) * 9 + 24
        draw.rounded_rectangle([(btn_x, 138), (btn_x + text_w, 168)], radius=15, fill=bg)
        draw.text((btn_x + 12, 146), cat, fill=fg, font=get_font(13, bold=is_active))
        btn_x += text_w + 12

    anime_list = [
        {"title": "Fullmetal Alchemist", "sub": "Brotherhood", "rank": "RANK #1", "rating": "IMDb 9.1", "ep": "64 Episodes", "tags": "Action, Military, Fantasy", "color": (225, 29, 72)},
        {"title": "Steins;Gate", "sub": "Sci-Fi Masterpiece", "rank": "RANK #2", "rating": "IMDb 9.0", "ep": "24 Episodes", "tags": "Sci-Fi, Thriller, Mystery", "color": (79, 70, 229)},
        {"title": "Attack on Titan", "sub": "Shingeki no Kyojin", "rank": "RANK #3", "rating": "IMDb 9.0", "ep": "88 Episodes", "tags": "Action, Dark Fantasy", "color": (13, 148, 136)},
        {"title": "Hunter x Hunter", "sub": "Chimera Ant Arc", "rank": "RANK #4", "rating": "IMDb 8.9", "ep": "148 Episodes", "tags": "Adventure, Super Power", "color": (217, 119, 6)}
    ]
    
    card_w = 250
    card_h = 390
    start_x = 60
    start_y = 210
    gap = 46
    
    for i, anime in enumerate(anime_list):
        x = start_x + i * (card_w + gap)
        y = start_y
        draw.rounded_rectangle([(x, y), (x + card_w, y + card_h)], radius=12, fill=(18, 25, 42), outline=(37, 49, 78), width=1)
        
        draw.rounded_rectangle([(x + 10, y + 10), (x + card_w - 10, y + 230)], radius=8, fill=anime["color"])
        draw.rounded_rectangle([(x + 20, y + 20), (x + 95, y + 44)], radius=4, fill=(11, 15, 25))
        draw.text((x + 26, y + 26), anime["rank"], fill=(255, 255, 255), font=get_font(11, bold=True))
        
        draw.rounded_rectangle([(x + card_w - 85, y + 20), (x + card_w - 20, y + 44)], radius=4, fill=(11, 15, 25))
        draw.text((x + card_w - 78, y + 26), anime["rating"], fill=(251, 191, 36), font=get_font(11, bold=True))
        
        draw.text((x + 20, y + 120), anime["title"], fill=(255, 255, 255), font=get_font(18, bold=True))
        draw.text((x + 20, y + 148), anime["sub"], fill=(254, 240, 138), font=get_font(14))

        draw.text((x + 14, y + 250), anime["title"], fill=(243, 244, 246), font=get_font(16, bold=True))
        draw.text((x + 14, y + 280), anime["tags"], fill=(156, 163, 175), font=get_font(12))
        draw.text((x + 14, y + 305), anime["ep"], fill=(100, 116, 139), font=get_font(12))

        draw.rounded_rectangle([(x + 14, y + 340), (x + card_w - 14, y + 372)], radius=6, fill=(30, 41, 65))
        draw.text((x + 65, y + 347), "View Synopsis ->", fill=(244, 63, 94), font=get_font(13, bold=True))

    draw.rectangle([(0, 680), (WIDTH, HEIGHT)], fill=(11, 15, 25))
    draw.line([(0, 680), (WIDTH, 680)], fill=(37, 49, 78), width=1)
    draw.text((60, 705), "Stack: Semantic HTML5 • CSS Grid & Flexbox • Vanilla JavaScript • Live Instant Filtering", fill=(100, 116, 139), font=get_font(14))

    img.save("images/project-2.png")

def create_mockup_3():
    img = Image.new("RGB", (WIDTH, HEIGHT), color=(11, 15, 25))
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "Interactive English Quiz Maker", "quizmaker.yahoshuva.dev")
    
    draw.rectangle([(0, 56), (WIDTH, 125)], fill=(16, 22, 38))
    draw.text((60, 78), "INTERACTIVE QUIZ ENGINE", fill=(168, 85, 247), font=get_font(22, bold=True))
    
    draw.rounded_rectangle([(840, 72), (970, 108)], radius=8, fill=(30, 41, 65))
    draw.text((855, 81), "TIME: 00:45", fill=(234, 179, 8), font=get_font(14, bold=True))
    
    draw.rounded_rectangle([(990, 72), (1140, 108)], radius=8, fill=(30, 41, 65), outline=(168, 85, 247), width=1)
    draw.text((1010, 81), "Score: 8 / 10", fill=(192, 132, 252), font=get_font(14, bold=True))

    draw.rectangle([(0, 125), (WIDTH, 133)], fill=(30, 41, 65))
    draw.rectangle([(0, 125), (int(WIDTH * 0.8), 133)], fill=(168, 85, 247))

    draw.rounded_rectangle([(100, 165), (1100, 290)], radius=14, fill=(20, 27, 45), outline=(99, 102, 241), width=1)
    draw.text((130, 185), "QUESTION 8 OF 10  •  TECHNICAL VOCABULARY & USAGE", fill=(129, 140, 248), font=get_font(14, bold=True))
    draw.text((130, 220), "The senior architect demonstrated that using CSS Grid for 2-dimensional layouts would have", fill=(248, 250, 252), font=get_font(18, bold=True))
    draw.text((130, 250), "a significant [ ______ ] on design responsiveness and maintainability.", fill=(248, 250, 252), font=get_font(18, bold=True))

    options = [
        {"key": "A", "text": "affect (transitive verb form)", "correct": False},
        {"key": "B", "text": "effect (noun form signifying direct outcome or result)", "correct": True},
        {"key": "C", "text": "affectionate (adjective denoting tenderness)", "correct": False},
        {"key": "D", "text": "efficacious (producing intended consequence)", "correct": False}
    ]
    
    opt_y = 315
    for opt in options:
        if opt["correct"]:
            bg = (20, 83, 45)
            outline = (34, 197, 94)
            badge_bg = (34, 197, 94)
            badge_fg = (0, 0, 0)
        else:
            bg = (18, 25, 42)
            outline = (37, 49, 78)
            badge_bg = (30, 41, 65)
            badge_fg = (255, 255, 255)
            
        draw.rounded_rectangle([(100, opt_y), (1100, opt_y + 55)], radius=10, fill=bg, outline=outline, width=2 if opt["correct"] else 1)
        draw.ellipse([(120, opt_y + 12), (150, opt_y + 42)], fill=badge_bg)
        draw.text((130, opt_y + 17), opt["key"], fill=badge_fg, font=get_font(15, bold=True))
        
        draw.text((170, opt_y + 17), opt["text"], fill=(248, 250, 252), font=get_font(16))
        if opt["correct"]:
            draw.text((960, opt_y + 17), "[CORRECT]", fill=(74, 222, 128), font=get_font(14, bold=True))
            
        opt_y += 70

    draw.rounded_rectangle([(100, 610), (260, 650)], radius=8, fill=(30, 41, 65))
    draw.text((130, 622), "< Previous", fill=(203, 213, 225), font=get_font(15, bold=True))

    draw.rounded_rectangle([(940, 610), (1100, 650)], radius=8, fill=(168, 85, 247))
    draw.text((975, 622), "Next Question >", fill=(255, 255, 255), font=get_font(15, bold=True))

    draw.rectangle([(0, 680), (WIDTH, HEIGHT)], fill=(11, 15, 25))
    draw.line([(0, 680), (WIDTH, 680)], fill=(37, 49, 78), width=1)
    draw.text((60, 705), "Stack: HTML5 • CSS Flexbox & Variables • Custom Test Engine • Score Analytics", fill=(100, 116, 139), font=get_font(14))

    img.save("images/project-3.png")

if __name__ == "__main__":
    create_mockup_1()
    create_mockup_2()
    create_mockup_3()
    print("Clean project mockups generated!")
