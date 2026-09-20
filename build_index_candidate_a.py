import os
import base64
import re

# 1. Read clean source HTML
with open('extracted_user_source.html', 'r', encoding='utf-8', newline='') as f:
    html = f.read().replace('\r', '')

# 2. Update Google Fonts in <head>
old_gfonts = """    <!-- Google Fonts: Noto Serif Thai fallback -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Serif+Thai:wght@300;400;600;700&display=swap" rel="stylesheet">"""

new_gfonts = """    <!-- Google Fonts: Candidate A (Cinzel for Headings, Taviraj for Tabs & Buttons, Noto Serif Thai for Body Text) -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;900&family=Noto+Serif+Thai:wght@300;400;500;600;700&family=Taviraj:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">"""

assert old_gfonts in html, "old_gfonts not found"
html = html.replace(old_gfonts, new_gfonts, 1)

# 3. Custom wizarding fonts @font-face with dual source (Base64 + local fallback)
fonts_map = {
    'Gobitta': ('fonts/GobittaRegular-0vBZ4.otf', 'font/otf', 'opentype'),
    'Harry Potter': ('fonts/HarryPotter-ov4z.ttf', 'font/ttf', 'truetype'),
    'Dragon Hunter': ('fonts/DragonHunter-9Ynxj.otf', 'font/otf', 'opentype'),
    'Sarun Gothic': ('fonts/SarunsGothic1.ttf', 'font/ttf', 'truetype'),
    'Sarun HarryPotter': ('fonts/SarunsHarryPotter.ttf', 'font/ttf', 'truetype'),
    'Samphan Condensed': ('fonts/SamphanCondensed.ttf', 'font/ttf', 'truetype')
}

fonts_css = [
    '    <style>',
    '        /* ===== Custom Wizarding Fonts (Dual Source: Base64 Data URI + Local Path Fallback) ===== */',
    '        /* ทำให้ไฟล์ HTML เป็นแบบ Standalone Single-File โดยสมบูรณ์ ไม่หลุดฟอนต์แม้ส่งไฟล์เดี่ยว */'
]

for family, (path, mime, fmt) in fonts_map.items():
    if os.path.exists(path):
        with open(path, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode('utf-8')
        block = f"""        @font-face {{
            font-family: '{family}';
            src: url('data:{mime};charset=utf-8;base64,{b64}') format('{fmt}'),
                 url('{path}') format('{fmt}');
            font-weight: normal;
            font-style: normal;
            font-display: swap;
        }}"""
    else:
        block = f"""        @font-face {{
            font-family: '{family}';
            src: url('{path}') format('{fmt}');
            font-weight: normal;
            font-style: normal;
            font-display: swap;
        }}"""
    fonts_css.append(block)

fonts_css.append('    </style>')
new_fonts_style_block = '\n'.join(fonts_css)

old_fonts_style_pattern = re.compile(r'<style>\s*/\* ===== Custom Wizarding Fonts ===== \*/.*?</style>', re.DOTALL)
assert old_fonts_style_pattern.search(html), "old_fonts_style_pattern not found"
html = old_fonts_style_pattern.sub(new_fonts_style_block, html, count=1)

# 4. Specific CSS replacements for Candidate A typography:
rules_replacements = [
    # 1. Body font
    (
        "            color: var(--ink-dark);\n            font-family: 'Samphan Condensed', 'Noto Serif Thai', serif;\n            min-height: 100vh;",
        "            color: var(--ink-dark);\n            font-family: 'Noto Serif Thai', 'Taviraj', serif;\n            min-height: 100vh;"
    ),
    # 2. Intro latin
    (
        "        .intro-latin {\n            font-family: 'Dragon Hunter', 'Cinzel Decorative', serif;\n            color: var(--gold-bright);",
        "        .intro-latin {\n            font-family: 'Cinzel', serif;\n            font-weight: 700;\n            color: var(--gold-bright);"
    ),
    # 3. Intro title
    (
        "        .intro-title {\n            font-family: 'Sarun HarryPotter', 'Harry Potter', cursive;\n            font-size: 3.5rem;",
        "        .intro-title {\n            font-family: 'Cinzel', 'Sarun HarryPotter', serif;\n            font-size: 3.2rem;\n            font-weight: 900;"
    ),
    # 4. Intro sub
    (
        "        .intro-sub {\n            font-family: 'Gobitta', 'Sarun Gothic', cursive;\n            font-size: 1.6rem;",
        "        .intro-sub {\n            font-family: 'Taviraj', 'Noto Serif Thai', serif;\n            font-size: 1.45rem;\n            font-weight: 500;"
    ),
    # 5. Intro enter button
    (
        "            color: #fff4d0;\n            padding: 12px 36px;\n            font-family: 'Samphan Condensed', 'Noto Serif Thai', serif;\n            font-size: 1.2rem;",
        "            color: #fff4d0;\n            padding: 12px 36px;\n            font-family: 'Taviraj', 'Noto Serif Thai', serif;\n            font-size: 1.15rem;\n            letter-spacing: 0.5px;"
    ),
    # 6. House motto tag
    (
        "        .house-motto-tag {\n            font-family: 'Sarun HarryPotter', 'Harry Potter', serif;\n            font-size: 1.15rem;",
        "        .house-motto-tag {\n            font-family: 'Cinzel', serif;\n            font-size: 1.1rem;\n            letter-spacing: 1.5px;\n            font-weight: 700;"
    ),
    # 7. House sub badge
    (
        "        .house-sub-badge {\n            font-family: 'Samphan Condensed', serif;\n            font-size: 0.95rem;\n            color: #dfcb9f;\n            letter-spacing: 1px;",
        "        .house-sub-badge {\n            font-family: 'Taviraj', 'Noto Serif Thai', serif;\n            font-size: 0.95rem;\n            color: #dfcb9f;\n            letter-spacing: 0.8px;"
    ),
    # 8. Portrait name tag
    (
        "        .portrait-name-tag {\n            font-family: 'Sarun HarryPotter', 'Harry Potter', cursive;\n            font-size: 2.1rem;",
        "        .portrait-name-tag {\n            font-family: 'Cinzel', serif;\n            font-size: 1.85rem;\n            font-weight: 700;\n            letter-spacing: 0.5px;"
    ),
    # 9. Portrait quidditch badge
    (
        "        .portrait-quidditch-badge {\n            margin-top: 10px;\n            font-family: 'Samphan Condensed', serif;\n            font-size: 1rem;\n            letter-spacing: 1px;\n            color: #ffd27d;",
        "        .portrait-quidditch-badge {\n            margin-top: 10px;\n            font-family: 'Taviraj', 'Noto Serif Thai', serif;\n            font-size: 1rem;\n            letter-spacing: 0.8px;\n            font-weight: 600;\n            color: #ffd27d;"
    ),
    # 10. Portrait tap hint
    (
        "        .portrait-tap-hint {\n            margin-top: 12px;\n            font-family: 'Samphan Condensed', serif;\n            font-size: 0.95rem;\n            color: #d1b88a;",
        "        .portrait-tap-hint {\n            margin-top: 12px;\n            font-family: 'Taviraj', 'Noto Serif Thai', serif;\n            font-size: 0.95rem;\n            color: #d1b88a;"
    ),
    # 11. Gilded title
    (
        "        .gilded-title {\n            font-family: 'Sarun HarryPotter', 'Harry Potter', cursive;\n            font-size: 3.4rem;\n            font-weight: 900;",
        "        .gilded-title {\n            font-family: 'Cinzel', 'Sarun HarryPotter', serif;\n            font-size: 3.2rem;\n            font-weight: 900;\n            letter-spacing: 1px;"
    ),
    # 12. Gilded subtitle
    (
        "        .gilded-subtitle {\n            font-family: 'Sarun HarryPotter', 'Gobitta', cursive;\n            font-size: 2.1rem;\n            color: #8c1a20;\n            font-weight: 700;",
        "        .gilded-subtitle {\n            font-family: 'Taviraj', 'Noto Serif Thai', serif;\n            font-size: 1.7rem;\n            color: #8c1a20;\n            font-weight: 600;"
    ),
    # 13. Tome excerpt
    (
        "        .tome-excerpt {\n            font-family: 'Samphan Condensed', 'Noto Serif Thai', serif;\n            font-size: 1.18rem;\n            line-height: 1.85;\n            color: #241407;",
        "        .tome-excerpt {\n            font-family: 'Noto Serif Thai', serif;\n            font-size: 1.12rem;\n            line-height: 1.9;\n            color: #241407;"
    ),
    # 14. Filmstrip thumb
    (
        "            color: var(--gold-bright);\n            font-family: 'Samphan Condensed', serif;\n            font-size: 1.1rem;\n            font-weight: bold;",
        "            color: var(--gold-bright);\n            font-family: 'Taviraj', 'Noto Serif Thai', serif;\n            font-size: 1.1rem;\n            font-weight: 600;"
    ),
    # 15. Section ribbon title
    (
        "        .section-ribbon-title {\n            font-family: 'Sarun HarryPotter', 'Harry Potter', serif;\n            font-size: 2.4rem;",
        "        .section-ribbon-title {\n            font-family: 'Cinzel', 'Taviraj', serif;\n            font-size: 2.2rem;\n            font-weight: 700;\n            letter-spacing: 0.5px;"
    ),
    # 16. Grimoire buttons
    (
        "            padding: 13px 12px;\n            border-radius: 6px;\n            font-family: 'Samphan Condensed', 'Noto Serif Thai', serif;\n            font-weight: 600;\n            font-size: 1.15rem;",
        "            padding: 13px 12px;\n            border-radius: 6px;\n            font-family: 'Taviraj', 'Noto Serif Thai', serif;\n            font-weight: 600;\n            font-size: 1.12rem;\n            letter-spacing: 0.3px;"
    ),
    # 17. Stats header title
    (
        "        .stats-header-title {\n            font-family: 'Sarun HarryPotter', 'Harry Potter', serif;\n            font-size: 1.45rem;",
        "        .stats-header-title {\n            font-family: 'Cinzel', 'Taviraj', serif;\n            font-size: 1.35rem;\n            font-weight: 700;"
    ),
    # 18. Stat label bar
    (
        "        .stat-label-bar {\n            display: flex;\n            justify-content: space-between;\n            font-family: 'Samphan Condensed', serif;\n            font-size: 1.1rem;\n            color: #f1dfbe;\n            font-weight: 600;",
        "        .stat-label-bar {\n            display: flex;\n            justify-content: space-between;\n            font-family: 'Taviraj', 'Noto Serif Thai', serif;\n            font-size: 1.05rem;\n            color: #f1dfbe;\n            font-weight: 600;"
    ),
    # 19. Voice label tag
    (
        "        .voice-label-tag {\n            font-family: 'Sarun HarryPotter', 'Harry Potter', cursive;\n            font-size: 1.3rem;\n            color: var(--gold-bright);\n            letter-spacing: 0.5px;",
        "        .voice-label-tag {\n            font-family: 'Cinzel', serif;\n            font-size: 1.15rem;\n            color: var(--gold-bright);\n            letter-spacing: 1px;\n            font-weight: 600;"
    ),
    # 20. Gallery art title
    (
        "        .gallery-art-title {\n            font-family: 'Sarun HarryPotter', 'Harry Potter', cursive;\n            font-size: 1.8rem;\n            color: #ffe6a0;",
        "        .gallery-art-title {\n            font-family: 'Cinzel', 'Taviraj', serif;\n            font-size: 1.6rem;\n            color: #ffe6a0;\n            font-weight: 700;"
    ),
    # 21. Gallery art desc
    (
        "        .gallery-art-desc {\n            font-family: 'Samphan Condensed', serif;\n            font-size: 1.05rem;\n            color: #e5cb9d;\n            line-height: 1.45;",
        "        .gallery-art-desc {\n            font-family: 'Noto Serif Thai', serif;\n            font-size: 0.98rem;\n            color: #e5cb9d;\n            line-height: 1.6;"
    ),
    # 22. Gallery inspect pill
    (
        "        .gallery-inspect-pill {\n            margin-top: 12px;\n            font-family: 'Samphan Condensed', serif;\n            font-size: 0.95rem;\n            letter-spacing: 1px;\n            color: var(--gold-bright);\n            background: rgba(60, 5, 10, 0.8);",
        "        .gallery-inspect-pill {\n            margin-top: 12px;\n            font-family: 'Taviraj', 'Noto Serif Thai', serif;\n            font-size: 0.95rem;\n            letter-spacing: 1px;\n            font-weight: 600;\n            color: var(--gold-bright);\n            background: rgba(60, 5, 10, 0.8);"
    ),
    # 23. Scroll heading
    (
        "        .scroll-heading {\n            font-family: 'Sarun HarryPotter', 'Harry Potter', serif;\n            font-size: 1.65rem;\n            font-weight: 700;\n            color: #65070e;",
        "        .scroll-heading {\n            font-family: 'Cinzel', 'Taviraj', serif;\n            font-size: 1.55rem;\n            font-weight: 700;\n            color: #65070e;"
    ),
    # 24. Scroll entry
    (
        "        .scroll-entry {\n            font-family: 'Samphan Condensed', 'Noto Serif Thai', serif;\n            font-size: 1.15rem;\n            line-height: 1.8;",
        "        .scroll-entry {\n            font-family: 'Noto Serif Thai', serif;\n            font-size: 1.12rem;\n            line-height: 1.9;"
    ),
    # 25. Dock link
    (
        "            color: var(--gold-antique);\n            font-family: 'Sarun HarryPotter', 'Gobitta', cursive;\n            font-size: 1.8rem;\n            font-weight: 700;",
        "            color: var(--gold-antique);\n            font-family: 'Cinzel', 'Taviraj', serif;\n            font-size: 1.45rem;\n            font-weight: 700;\n            letter-spacing: 1px;"
    ),
    # 26. Inline quote style in info tab
    (
        '<p style="font-family: \'Samphan Condensed\', serif; color: #ecd3a5; font-size: 1.15rem; margin-top: 14px; line-height: 1.65;">',
        '<p style="font-family: \'Noto Serif Thai\', \'Taviraj\', serif; color: #ecd3a5; font-size: 1.08rem; margin-top: 14px; line-height: 1.8;">'
    ),
    # 27. Inline quote style in about tab
    (
        '<p style="font-family: \'Samphan Condensed\', serif; color: #ebd09e; font-size: 1.1rem; margin-top: 14px; line-height: 1.65;">',
        '<p style="font-family: \'Noto Serif Thai\', \'Taviraj\', serif; color: #ebd09e; font-size: 1.08rem; margin-top: 14px; line-height: 1.8;">'
    ),
    # 28. Scroll modal content style
    (
        '<div id="scrollContent" style="font-family: \'Samphan Condensed\', \'Noto Serif Thai\', serif; line-height: 1.85; color: #221408; font-size: 1.15rem;"></div>',
        '<div id="scrollContent" style="font-family: \'Noto Serif Thai\', serif; line-height: 1.9; color: #221408; font-size: 1.15rem;"></div>'
    )
]

for idx, (target, repl) in enumerate(rules_replacements):
    assert target in html, f"Rule replacement #{idx+1} failed: {target[:40]}"
    html = html.replace(target, repl, 1)
print(f"All {len(rules_replacements)} Candidate A typography rules applied perfectly!")

# 5. Insert History Reader CSS & Focus Rings before /* ===== RESPONSIVE ===== */
new_reader_css = """        /* ===== History Lore & Parchment Reader Typography ===== */
        .parchment-history-flow {
            padding: 4px 2px;
        }

        .history-chapter {
            margin-bottom: 22px;
            padding-bottom: 18px;
            border-bottom: 1px dashed rgba(117, 85, 39, 0.4);
        }

        .history-chapter:last-of-type {
            border-bottom: none;
            margin-bottom: 12px;
        }

        .history-subtitle {
            font-family: 'Taviraj', 'Cinzel', serif;
            font-size: 1.35rem;
            color: var(--crimson-crest);
            margin-bottom: 10px;
            letter-spacing: 0.5px;
            display: flex;
            align-items: center;
            gap: 6px;
            font-weight: 700;
        }

        .history-p {
            font-family: 'Noto Serif Thai', serif;
            font-size: 1.15rem;
            line-height: 1.9;
            color: #241306;
            margin-bottom: 10px;
            text-align: justify;
        }

        .history-p strong {
            color: #7b0005;
            font-weight: 700;
        }

        .history-p em {
            color: #553406;
            font-style: normal;
            text-decoration: underline dotted #9c6c2e;
        }

        .history-quote-box {
            background: rgba(201, 147, 48, 0.12);
            border-left: 4px solid var(--gold-antique);
            border-right: 1px solid rgba(201, 147, 48, 0.25);
            padding: 14px 20px;
            margin-top: 18px;
            border-radius: 4px;
            font-style: italic;
            color: #381f06;
            font-size: 1.12rem;
            line-height: 1.75;
            text-align: center;
            box-shadow: inset 0 0 12px rgba(117, 85, 39, 0.1);
            font-family: 'Noto Serif Thai', serif;
        }

        /* ===== Accessibility Focus Rings (Gryffindor Radiant Glow) ===== */
        .wax-seal:focus-visible,
        .character-portrait-box:focus-visible,
        .golden-snitch:focus-visible,
        .filmstrip-thumb:focus-visible,
        .gallery-frame-item:focus-visible,
        .dock-link:focus-visible,
        .grimoire-btn:focus-visible,
        .intro-enter-btn:focus-visible,
        .close-scroll-seal:focus-visible,
        .wand-play-trigger:focus-visible {
            outline: 3px solid var(--gold-bright) !important;
            outline-offset: 4px !important;
            box-shadow: 0 0 16px rgba(255, 232, 158, 0.9) !important;
            border-radius: 6px;
        }

        .wax-seal:focus-visible,
        .close-scroll-seal:focus-visible,
        .wand-play-trigger:focus-visible {
            border-radius: 50%;
        }

        /* ===== RESPONSIVE ===== */"""

responsive_marker = "        /* ===== RESPONSIVE ===== */"
assert responsive_marker in html, "Responsive marker not found"
html = html.replace(responsive_marker, new_reader_css, 1)

# 6. Accessibility attributes (role="button", tabindex="0", aria-label)
a11y_replacements = [
    (
        '<div class="wax-seal" onclick="triggerCrestRoar()">',
        '<div class="wax-seal" id="waxSeal" role="button" tabindex="0" aria-label="Gryffindor House Crest ตราขี้ผึ้งประจำบ้าน (คลิกหรือกด Space/Enter เพื่อคำราม)" onclick="triggerCrestRoar()">'
    ),
    (
        '<div class="character-portrait-box" id="mainPortrait" onmousemove="handlePortraitTilt(event)" onmouseleave="resetPortraitTilt()" onclick="triggerPatronusSpell()">',
        '<div class="character-portrait-box" id="mainPortrait" role="button" tabindex="0" aria-label="กรอบรูปภาพเคลื่อนไหวเวทมนตร์ Alexan (คลิกหรือกด Space/Enter เพื่อร่ายคาถาผู้พิทักษ์ Patronus)" onmousemove="handlePortraitTilt(event)" onmouseleave="resetPortraitTilt()" onclick="triggerPatronusSpell()">'
    ),
    (
        '<div class="golden-snitch" id="goldenSnitch" title="The Golden Snitch (คลิกเพื่อไล่จับลูกสนิช!)" onclick="fleeSnitch()">',
        '<div class="golden-snitch" id="goldenSnitch" role="button" tabindex="0" aria-label="The Golden Snitch ลูกสนิชสีทอง (คลิกหรือกด Space/Enter เพื่อไล่จับลูกสนิช)" title="The Golden Snitch (คลิกหรือกด Space เพื่อไล่จับลูกสนิช!)" onclick="fleeSnitch()">'
    ),
    (
        '<div class="filmstrip-thumb" onclick="openGalleryItem(0)">',
        '<div class="filmstrip-thumb" role="button" tabindex="0" aria-label="ดูภาพย่อ Hogsmeade Stroll" onclick="openGalleryItem(0)">'
    ),
    (
        '<div class="filmstrip-thumb" onclick="openGalleryItem(1)">',
        '<div class="filmstrip-thumb" role="button" tabindex="0" aria-label="ดูภาพย่อ Winter Scarf" onclick="openGalleryItem(1)">'
    ),
    (
        '<div class="filmstrip-thumb" onclick="openGalleryItem(2)">',
        '<div class="filmstrip-thumb" role="button" tabindex="0" aria-label="ดูภาพย่อ Quidditch Pitch" onclick="openGalleryItem(2)">'
    )
]

for target, repl in a11y_replacements:
    assert target in html, f"a11y replacement failed: {target}"
    html = html.replace(target, repl, 1)

gallery_titles = [
    "Hogsmeade Stroll",
    "Winter Scarf",
    "Quidditch Pitch",
    "Prank Fireworks",
    "Duel Training",
    "Fierce Resolve"
]
for idx, title in enumerate(gallery_titles):
    old_tag = f'<div class="gallery-frame-item" onclick="openGalleryItem({idx})">'
    new_tag = f'<div class="gallery-frame-item" role="button" tabindex="0" aria-label="ตรวจดูภาพ {title}" onclick="openGalleryItem({idx})">'
    assert old_tag in html, f"gallery item {idx} not found"
    html = html.replace(old_tag, new_tag, 1)

# 7. Update dock navigation with data-tab
old_dock = """    <nav class="common-room-dock">
        <button class="dock-link active" onclick="switchTab('home')">Home</button>
        <button class="dock-link" onclick="switchTab('information')">Information</button>
        <button class="dock-link" onclick="switchTab('gallery')">Gallery</button>
        <button class="dock-link" onclick="switchTab('about')">About</button>
    </nav>"""

new_dock = """    <nav class="common-room-dock" aria-label="Gryffindor Navigation Dock">
        <button class="dock-link active" data-tab="home" onclick="switchTab('home')">Home</button>
        <button class="dock-link" data-tab="information" onclick="switchTab('information')">Information</button>
        <button class="dock-link" data-tab="gallery" onclick="switchTab('gallery')">Gallery</button>
        <button class="dock-link" data-tab="about" onclick="switchTab('about')">About</button>
    </nav>"""

assert old_dock in html, "old_dock not found"
html = html.replace(old_dock, new_dock, 1)
print("Updated dock navigation with data-tab attributes!")

# 8. Replace script with performance, accessibility, and modal enhancements
old_script_pattern = re.compile(r'<script>\s*// ================= Tab Switching =================.*?</script>', re.DOTALL)

new_script = """<script>
        // ================= Tab Switching (Resilient data-tab Selector) =================
        function switchTab(tabId) {
            document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.dock-link').forEach(el => el.classList.remove('active'));

            const target = document.getElementById(`tab-${tabId}`);
            if (target) {
                target.classList.add('active');
                if (tabId === 'information') {
                    animateStatBars();
                }
            }

            // Query active dock button by data-tab attribute (resilient to language or label changes)
            const activeBtn = document.querySelector(`.dock-link[data-tab="${tabId}"]`);
            if (activeBtn) activeBtn.classList.add('active');

            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        function animateStatBars() {
            setTimeout(() => {
                document.querySelectorAll('.stat-fill').forEach(bar => {
                    const pct = bar.getAttribute('data-percent');
                    bar.style.width = pct + '%';
                });
            }, 100);
        }

        // ================= Scroll Modal Archive & History Flow =================
        const scrollArchive = {
            history: {
                title: "ประวัติความเป็นมา / Biography",
                html: `<div class="parchment-history-flow">
                    <div class="history-chapter">
                        <h4 class="history-subtitle">✦ ๑. ชาติตระกูลและวัยเยาว์ (Early Life & Heritage)</h4>
                        <p class="history-p">
                            พ่อแม่ของอเล็กซ์เคยเป็น <strong>มือปราบมาร (Auror)</strong> ผู้มีชื่อเสียงโด่งดัง ทว่าโศกนาฏกรรมจากการกรำศึกศาสตร์มืดทำให้ทั้งคู่สูญเสียสติสัมปชัญญะ จนต้องเข้ารับการดูแลรักษาถาวรอยู่ที่ <em>โรงพยาบาลเซนต์มังโก้</em>
                        </p>
                        <p class="history-p">
                            นับแต่นั้น อเล็กซ์จึงต้องมาอาศัยอยู่กับ <strong>พ่อทูนหัวซึ่งเป็นมนุษย์หมาป่า</strong> สภาพความเป็นอยู่จึงค่อนข้างยากจนขัดสน ทำให้เสื้อคลุมและของใช้ของเขามักดูเก่าปอนอยู่เสมอ
                        </p>
                    </div>

                    <div class="history-chapter">
                        <h4 class="history-subtitle">✦ ๒. พรสวรรค์บนผืนเวหา (Quidditch Prodigy)</h4>
                        <p class="history-p">
                            ทว่าความยากจนไม่อาจหยุดยั้งความหลงใหลใน <strong>กีฬาควิดดิช</strong> ได้เลยแม้แต่น้อย เขาฝึกบินด้วย <em>ไม้กวาดรุ่นชูตติ้งสตาร์</em> เก่าคร่ำครึของพ่อทูนหัว ไล่หวดลูกบลัดเจอร์อย่างดุเดือดจนฝีมือเข้าตาทีมควิดดิชระดับชาติ
                        </p>
                        <p class="history-p">
                            อเล็กซ์ถูกทาบทามเข้าร่วม <strong>ทีมชาติอังกฤษ — วินบอร์นวอสป์ (Wimbourne Wasps)</strong> ในฐานะตัวสำรองตั้งแต่อายุเพียง 15 ปี และด้วยอานิสงส์นี้ สโมสรจึงได้มอบ <em>ไม้กวาดแข่งรุ่นไฟเยอร์โบลด์ (Firebolt)</em> ให้แก่เขาเพื่อการฝึกซ้อมที่เต็มศักยภาพ
                        </p>
                    </div>

                    <div class="history-chapter">
                        <h4 class="history-subtitle">✦ ๓. โศกนาฏกรรมวิลโลว์จอมหวด (The Whomping Willow Incident)</h4>
                        <p class="history-p">
                            น่าเสียดายที่ในแมตช์การแข่งขันระหว่าง <strong>กริฟฟินดอร์ ปะทะ เรเวนคลอ (ช่วงปี 6)</strong> ไม้กวาดไฟเยอร์โบลด์ของเขาถูกขโมยไปอย่างลึกลับ บีบให้อเล็กซ์ต้องควบไม้กวาดชูตติ้งสตาร์ตัวเก่าลงแข่งขันในสภาพอากาศที่แปรปรวนจัด
                        </p>
                        <p class="history-p">
                            ลมพายุหมุนรุนแรงพัดไม้กวาดหลุดการควบคุมจนพุ่งชนเข้ากับ <strong>ต้นวิลโลว์จอมหวด</strong> อย่างรุนแรง ส่งผลให้อเล็กซ์ต้อง <em>สูญเสียดวงตาข้างซ้ายและขาขวาไปอย่างถาวร</em>
                        </p>
                        <p class="history-p">
                            จากอุบัติเหตุครั้งนั้น เขาถูกถอนชื่อออกจากทีมวินบอร์นวอสป์ ถูกปลดจากตำแหน่งกัปตันทีมกริฟฟินดอร์ และถูกสั่งห้ามแข่งขันควิดดิชอย่างเป็นทางการตลอดกาล
                        </p>
                    </div>

                    <div class="history-quote-box">
                        <div class="quote-text">"แม้จะสูญเสียดวงตาข้างซ้ายและขาขวาไป แต่อเล็กซ์ก็พิสูจน์ให้ทุกคนเห็นว่า... หัวใจแห่งความกล้าหาญของกริฟฟินดอร์ไม่เคยสูญเสียไปตามร่างกายเลย"</div>
                    </div>
                </div>`
            },
            likes: {
                title: "สิ่งที่ชอบ / Likes",
                html: `• <strong>การบินแข่งขันด้วยความเร็วสูง:</strong> และความตื่นเต้นของการไล่หวดบลัดเจอร์ในสนามควิดดิช<br>
        • <strong>การทดลองของเล่นแกล้งคน:</strong> การทดลองประกอบระเบิดควันและประทัดเสียงดังตึงตังเอาไว้แกล้งคน<br>
        • <strong>ของหวานยามดึก:</strong> ขนมพายฟักทองอุ่นๆ รสหวาน และการย่องไปหาของกินในครัวฮอกวอตส์ยามดึก`
            },
            dislikes: {
                title: "สิ่งที่ไม่ชอบ / Dislikes",
                html: `• <strong>ชื่อเต็ม:</strong> การถูกเรียกด้วยชื่อเต็ม "อเล็กซาน"<br>
        • <strong>จุดบอดข้างซ้าย:</strong> การถูกลอบประชิดตัวจากทางด้านซ้าย ซึ่งเป็นจุดบอดสายตาของเขา<br>
        • <strong>การเล่นกับความรู้สึก:</strong> การถูกปฏิบัติเหมือนเป็นตัวสำรองหรือช้อยส์รองของใคร`
            },
            magic: {
                title: "อุปกรณ์เวทมนตร์และทักษะพิเศษ",
                html: `• <strong>ไม้กวาดไฟเยอร์โบลด์ (Firebolt):</strong> ไม้กวาดความเร็วสูงระดับโลกที่เขารักและทะนุถนอมมากที่สุด<br>
        • <strong>ความชำนาญคาถาป้องกันตัว:</strong> วิชาป้องกันตัวจากศาสตร์มืดและการตอบสนองต่อภัยคุกคามในระยะประชิดที่ฉับไวเหนือกว่ามาตรฐานนักเรียนทั่วไป<br>
        • <strong>สัญชาตญาณสัตว์ป่า:</strong> พัฒนาประสาทการได้ยินและสัญชาตญาณรอบตัวขึ้นมาทดแทนดวงตาข้างซ้ายที่สูญเสียไป`
            },
            others: {
                title: "บันทึกลับฮอกวอตส์",
                html: `แม้เสื้อคลุมจะปอนและมีประวัติบาดแผลฉกรรจ์ แต่อเล็กซ์ไม่เคยยอมให้ใครมาแสดงความสงสารเวทนา และพร้อมจะเอาคืนด้วยระเบิดควันแกล้งคนทันทีหากถูกล้อเลียน หรือดูถูกสายเลือดและฐานะ`
            }
        };

        const galleryStories = [
            {
                title: "Hogsmeade Stroll / เดินเล่นฮอกส์มี้ด",
                desc: "ช็อตช่วงวันหยุดสุดสัปดาห์ในฤดูหนาวที่หมู่บ้านฮอกส์มี้ด อเล็กซ์แอบพาเพื่อนย่องไปซื้อขนมร้านฮันนี่ดุกส์ และนั่งคุยกันข้างเตาผิงร้านไม้กวาดสามอันพร้อมบัตเตอร์เบียร์ฟองนุ่ม"
            },
            {
                title: "Winter Scarf / ผ้าพันคอรับลมหนาว",
                desc: "ผ้าพันคอไหมพรมลายทางสีแดงเลือดหมูสลับทองที่ถักเองอย่างเบี้ยวๆ แต่นุ่มอุ่นสบาย ช่วยบังลมหนาวจากยอดหอคอยกริฟฟินดอร์"
            },
            {
                title: "Quidditch Pitch / สนามควิดดิช",
                desc: "ภาพช่วงก่อนแมตช์การแข่งขันใหญ่กับสลิธีริน อเล็กซ์ถือไม้กวาดและไม้ตีบลัดเจอร์ด้วยสีหน้ามั่นใจเต็มร้อย พร้อมจะพาทีมคว้าชัยชนะ"
            },
            {
                title: "Prank Fireworks / จังหวะหน้าแดง",
                desc: "เหตุการณ์ตอนที่ตั้งใจจะจุดประทัดควันดักแกล้งเพื่อนในห้องนั่งเล่นรวม แต่โดนจับได้จนแก้ตัวไม่ถูกจนหน้าแดงแจ๋"
            },
            {
                title: "Duel Training / หลังการดวลฝึกซ้อม",
                desc: "เสื้อคลุมเปื้อนเขม่าควันคาถาหลังฝึกดวลวิชาป้องกันตัวจากศาสตร์มืดจนเหงื่อท่วม แต่ยังมีรอยยิ้มภาคภูมิใจไม่เคยยอมแพ้"
            },
            {
                title: "Fierce Resolve / จิตวิญญาณกริฟฟินดอร์",
                desc: "แววตาแน่วแน่แม้จะสูญเสียดวงตาข้างซ้ายและขาขวา แต่อเล็กซ์ก็พิสูจน์ให้ทุกคนเห็นว่าหัวใจแห่งความกล้าหาญไม่ได้สูญเสียไปตามร่างกายเลย"
            }
        ];

        // ================= Modal Management & Mobile History Back Navigation =================
        let isModalOpen = false;

        function openScroll(key) {
            const item = scrollArchive[key];
            if (!item) return;
            document.getElementById('scrollHeader').innerHTML = item.title;
            document.getElementById('scrollContent').innerHTML = item.html;
            document.getElementById('scrollModal').classList.add('active');
            isModalOpen = true;

            // Push state so mobile back button closes modal smoothly
            try {
                if (!window.history.state || !window.history.state.scrollModalOpen) {
                    window.history.pushState({ scrollModalOpen: true }, '');
                }
            } catch (e) {}
        }

        function openGalleryItem(index) {
            const item = galleryStories[index];
            if (!item) return;
            document.getElementById('scrollHeader').innerHTML = item.title;
            document.getElementById('scrollContent').innerHTML = item.desc;
            document.getElementById('scrollModal').classList.add('active');
            isModalOpen = true;

            try {
                if (!window.history.state || !window.history.state.scrollModalOpen) {
                    window.history.pushState({ scrollModalOpen: true }, '');
                }
            } catch (e) {}
        }

        function closeScroll(fromHistory = false) {
            const modal = document.getElementById('scrollModal');
            if (modal) modal.classList.remove('active');

            if (isModalOpen && !fromHistory) {
                if (window.history.state && window.history.state.scrollModalOpen) {
                    window.history.back();
                }
            }
            isModalOpen = false;
        }

        function closeOnBackdrop(e) {
            if (e.target.id === 'scrollModal') closeScroll();
        }

        // Listen for mobile / browser back button popstate
        window.addEventListener('popstate', (e) => {
            if (isModalOpen) {
                closeScroll(true);
            }
        });

        // ================= Cinematic Intro Dismiss =================
        function dismissIntro() {
            const curtain = document.getElementById('introCurtain');
            if (curtain) {
                curtain.classList.add('dissolve');
                setTimeout(() => curtain.remove(), 1000);
            }
        }

        // ================= Keyboard Accessibility (Escape, Enter, Space) =================
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                dismissIntro();
                closeScroll();
            } else if (e.key === 'Enter' || e.key === ' ') {
                // Support keyboard activation for div[role="button"]
                const target = e.target;
                if (target && target.getAttribute('role') === 'button' && target.tagName !== 'BUTTON') {
                    e.preventDefault();
                    target.click();
                }
            }
        });

        setTimeout(dismissIntro, 2600);

        // ================= Snitch Darting Interaction =================
        function fleeSnitch() {
            const snitch = document.getElementById('goldenSnitch');
            if (!snitch) return;
            const newX = Math.floor(Math.random() * (window.innerWidth - 120)) + 30;
            const newY = Math.floor(Math.random() * (window.innerHeight - 200)) + 40;
            snitch.style.transition = 'all 0.5s cubic-bezier(0.1, 0.9, 0.2, 1)';
            snitch.style.left = newX + 'px';
            snitch.style.top = newY + 'px';
            snitch.style.right = 'auto';

            for (let i = 0; i < 10; i++) {
                createSparkParticle(newX + 12, newY + 12);
            }
        }

        function triggerCrestRoar() {
            const seal = document.querySelector('.wax-seal');
            if (!seal) return;
            seal.style.transform = 'scale(1.25) rotate(15deg)';
            setTimeout(() => seal.style.transform = '', 300);
        }

        function triggerPatronusSpell() {
            const box = document.getElementById('mainPortrait');
            if (!box) return;
            box.style.boxShadow = '0 0 50px rgba(180, 220, 255, 0.9), 0 0 80px rgba(255, 215, 0, 0.8)';
            setTimeout(() => box.style.boxShadow = '', 600);
        }

        // ================= 3D Portrait Tilt Parallax =================
        function handlePortraitTilt(e) {
            const box = document.getElementById('mainPortrait');
            const shimmer = document.getElementById('portraitShimmer');
            if (!box) return;

            const rect = box.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            const centerX = rect.width / 2;
            const centerY = rect.height / 2;

            const rotateX = ((y - centerY) / centerY) * -10;
            const rotateY = ((x - centerX) / centerX) * 10;

            box.style.transform = `perspective(800px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
            if (shimmer) {
                shimmer.style.transform = `translateX(${(x - centerX) * 0.4}px) translateY(${(y - centerY) * 0.4}px)`;
            }
        }

        function resetPortraitTilt() {
            const box = document.getElementById('mainPortrait');
            const shimmer = document.getElementById('portraitShimmer');
            if (box) box.style.transform = 'perspective(800px) rotateX(0deg) rotateY(0deg)';
            if (shimmer) shimmer.style.transform = 'none';
        }

        // ================= Canvas 1: Fireplace Embers (Adaptive & Visibility-Aware) =================
        const canvas = document.getElementById('magicCanvas');
        const ctx = canvas.getContext('2d');
        let width, height;

        function resizeCanvas() {
            width = canvas.width = window.innerWidth;
            height = canvas.height = window.innerHeight;
            const wandCanvas = document.getElementById('wandTrailCanvas');
            if (wandCanvas) {
                wandCanvas.width = width;
                wandCanvas.height = height;
            }
        }
        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();

        class EmberParticle {
            constructor() {
                this.reset();
            }
            reset() {
                this.x = Math.random() * width;
                this.y = height + Math.random() * 50;
                this.size = Math.random() * 2.8 + 0.8;
                this.speedY = Math.random() * 0.9 + 0.35;
                this.speedX = (Math.random() - 0.5) * 0.6;
                this.opacity = Math.random() * 0.7 + 0.3;
                this.decay = Math.random() * 0.003 + 0.0015;
                this.colorType = Math.random();
            }
            update() {
                this.y -= this.speedY;
                this.x += this.speedX + Math.sin(this.y * 0.015) * 0.35;
                this.opacity -= this.decay;
                if (this.opacity <= 0 || this.y < -20) {
                    this.reset();
                }
            }
            draw() {
                ctx.save();
                ctx.globalAlpha = Math.max(0, this.opacity);
                if (this.colorType > 0.65) {
                    ctx.fillStyle = '#ffea78';
                    ctx.shadowColor = '#ffd000';
                    ctx.shadowBlur = 8;
                } else if (this.colorType > 0.3) {
                    ctx.fillStyle = '#ff8822';
                    ctx.shadowColor = '#ff4400';
                    ctx.shadowBlur = 6;
                } else {
                    ctx.fillStyle = '#ff3344';
                    ctx.shadowColor = '#990000';
                    ctx.shadowBlur = 5;
                }

                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fill();
                ctx.restore();
            }
        }

        // Adaptive particle count for mobile vs desktop performance
        const isMobileScreen = window.innerWidth < 768;
        const emberCount = isMobileScreen ? 28 : 55;
        const embers = Array.from({ length: emberCount }, () => new EmberParticle());

        let emberAnimId = null;
        let isEmbersRunning = false;

        function loopEmbers() {
            if (document.hidden) {
                isEmbersRunning = false;
                emberAnimId = null;
                return;
            }
            ctx.clearRect(0, 0, width, height);
            embers.forEach(e => {
                e.update();
                e.draw();
            });
            emberAnimId = requestAnimationFrame(loopEmbers);
        }

        function startEmbers() {
            if (!isEmbersRunning && !document.hidden) {
                isEmbersRunning = true;
                emberAnimId = requestAnimationFrame(loopEmbers);
            }
        }

        function stopEmbers() {
            if (emberAnimId) {
                cancelAnimationFrame(emberAnimId);
                emberAnimId = null;
            }
            isEmbersRunning = false;
        }

        startEmbers();

        // ================= Canvas 2: Wand Sparks Mouse/Touch Trail (On-Demand & Throttled) =================
        const wandCanvas = document.getElementById('wandTrailCanvas');
        const wandCtx = wandCanvas.getContext('2d');
        const sparks = [];
        const MAX_SPARKS = 70; // Cap sparks count to prevent frame drops
        let wandAnimId = null;
        let isWandRunning = false;

        function createSparkParticle(x, y) {
            if (sparks.length >= MAX_SPARKS) {
                sparks.splice(0, sparks.length - MAX_SPARKS + 1);
            }
            sparks.push({
                x: x,
                y: y,
                vx: (Math.random() - 0.5) * 1.8,
                vy: (Math.random() - 0.5) * 1.8 - 0.4,
                size: Math.random() * 3 + 1.2,
                opacity: 1,
                decay: Math.random() * 0.025 + 0.015,
                color: Math.random() > 0.4 ? '#ffea75' : '#ff9a2e'
            });

            // Start spark loop on-demand only when particles exist
            if (!isWandRunning && !document.hidden) {
                startWandSparks();
            }
        }

        let lastMouseSparkTime = 0;
        window.addEventListener('mousemove', (e) => {
            if (document.hidden) return;
            const now = performance.now();
            if (now - lastMouseSparkTime > 22) { // 22ms throttle
                createSparkParticle(e.clientX, e.clientY);
                lastMouseSparkTime = now;
            }
        }, { passive: true });

        // Mobile touch spark effect
        window.addEventListener('touchmove', (e) => {
            if (document.hidden || !e.touches || !e.touches[0]) return;
            const now = performance.now();
            if (now - lastMouseSparkTime > 25) {
                createSparkParticle(e.touches[0].clientX, e.touches[0].clientY);
                lastMouseSparkTime = now;
            }
        }, { passive: true });

        function loopWandSparks() {
            if (document.hidden) {
                isWandRunning = false;
                wandAnimId = null;
                return;
            }

            if (sparks.length === 0) {
                // When sparks finish fading, clear once and IDLE at 0 FPS to save 100% CPU/GPU!
                wandCtx.clearRect(0, 0, width, height);
                isWandRunning = false;
                wandAnimId = null;
                return;
            }

            wandCtx.clearRect(0, 0, width, height);
            for (let i = sparks.length - 1; i >= 0; i--) {
                const s = sparks[i];
                s.x += s.vx;
                s.y += s.vy;
                s.opacity -= s.decay;
                s.size *= 0.97;

                if (s.opacity <= 0 || s.size <= 0.2) {
                    sparks.splice(i, 1);
                    continue;
                }

                wandCtx.save();
                wandCtx.globalAlpha = s.opacity;
                wandCtx.fillStyle = s.color;
                wandCtx.shadowColor = '#ffd000';
                wandCtx.shadowBlur = 8;
                wandCtx.beginPath();
                wandCtx.arc(s.x, s.y, s.size, 0, Math.PI * 2);
                wandCtx.fill();
                wandCtx.restore();
            }

            wandAnimId = requestAnimationFrame(loopWandSparks);
        }

        function startWandSparks() {
            if (!isWandRunning && !document.hidden && sparks.length > 0) {
                isWandRunning = true;
                wandAnimId = requestAnimationFrame(loopWandSparks);
            }
        }

        function stopWandSparks() {
            if (wandAnimId) {
                cancelAnimationFrame(wandAnimId);
                wandAnimId = null;
            }
            isWandRunning = false;
        }

        // ================= Tab Visibility Change (Zero Battery Drain when Inactive) =================
        document.addEventListener('visibilitychange', () => {
            if (document.hidden) {
                stopEmbers();
                stopWandSparks();
                if (isAudioActive && window.audioInterval) {
                    clearInterval(window.audioInterval);
                }
            } else {
                startEmbers();
                if (sparks.length > 0) {
                    startWandSparks();
                }
                if (isAudioActive) {
                    window.audioInterval = setInterval(playMagicalChimeLoop, 2200);
                }
            }
        });

        // ================= Web Audio API Magic Sound Synthesizer =================
        const sparkContainer = document.getElementById('sparkWave');
        for (let i = 0; i < 26; i++) {
            const bar = document.createElement('div');
            bar.className = 'sound-pulse';
            bar.style.height = `${Math.floor(Math.random() * 16) + 6}px`;
            sparkContainer.appendChild(bar);
        }

        let isAudioActive = false;
        let audioCtx = null;

        function playSpellHarpTone(freq, delay, dur) {
            if (!audioCtx) return;
            const osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();

            osc.type = 'triangle';
            osc.frequency.setValueAtTime(freq, audioCtx.currentTime + delay);

            gain.gain.setValueAtTime(0, audioCtx.currentTime + delay);
            gain.gain.linearRampToValueAtTime(0.12, audioCtx.currentTime + delay + 0.05);
            gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + delay + dur);

            osc.connect(gain);
            gain.connect(audioCtx.destination);

            osc.start(audioCtx.currentTime + delay);
            osc.stop(audioCtx.currentTime + delay + dur);
        }

        function playMagicalChimeLoop() {
            if (!isAudioActive || document.hidden) return;
            const chords = [523.25, 659.25, 783.99, 1046.50, 880.00, 659.25];
            chords.forEach((freq, idx) => {
                playSpellHarpTone(freq, idx * 0.18, 0.9);
            });
        }

        function toggleSparksAudio() {
            const btn = document.getElementById('audioToggle');
            isAudioActive = !isAudioActive;
            
            const iconSvg = document.getElementById('playIconSvg');
            if (iconSvg) {
                iconSvg.innerHTML = isAudioActive 
                    ? '<rect x="6" y="4" width="4" height="16"></rect><rect x="14" y="4" width="4" height="16"></rect>'
                    : '<polygon points="5 3 19 12 5 21 5 3"></polygon>';
            }

            if (!audioCtx) {
                const AudioContext = window.AudioContext || window.webkitAudioContext;
                if (AudioContext) audioCtx = new AudioContext();
            }

            const bars = document.querySelectorAll('.sound-pulse');
            if (isAudioActive) {
                playMagicalChimeLoop();
                window.audioInterval = setInterval(playMagicalChimeLoop, 2200);

                window.sparkLoop = setInterval(() => {
                    bars.forEach(b => b.style.height = `${Math.floor(Math.random() * 24) + 6}px`);
                }, 100);
            } else {
                clearInterval(window.audioInterval);
                clearInterval(window.sparkLoop);
                bars.forEach(b => b.style.height = '8px');
            }
        }
    </script>"""

assert old_script_pattern.search(html), "old_script_pattern not found"
html = old_script_pattern.sub(new_script, html, count=1)
print("Replaced script successfully!")

# 9. Write final index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: index.html generated with 100% assertions passing!")
print("Final size:", len(html), "bytes")
