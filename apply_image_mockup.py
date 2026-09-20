import os
import re
import shutil

# 1. Backup original index.html
shutil.copyfile('index.html', 'index.html.before_mockup.bak')
print("Backed up index.html to index.html.before_mockup.bak")

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 2. Add Great Vibes & Alex Brush Google Fonts in <head>
gfonts_old = '<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Noto+Serif+Thai:wght@400;600&display=swap" rel="stylesheet">'
gfonts_new = '<link href="https://fonts.googleapis.com/css2?family=Alex+Brush&family=Cinzel:wght@700;900&family=Great+Vibes&family=Noto+Serif+Thai:wght@400;600&display=swap" rel="stylesheet">'

if gfonts_old in html:
    html = html.replace(gfonts_old, gfonts_new)
    print("Updated Google Fonts link")
elif 'Great Vibes' not in html:
    html = html.replace('</head>', f'    {gfonts_new}\n</head>')
    print("Injected Google Fonts link")

# 3. Add CSS for mockup image structure
mockup_css = """
        /* ===== Mockup Image Layout & Aesthetic Styles ===== */
        .top-crest-shield {
            position: absolute;
            top: 24px;
            left: 36px;
            z-index: 25;
            width: 80px;
            height: 96px;
            filter: drop-shadow(0 6px 16px rgba(0, 0, 0, 0.95));
            transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            cursor: pointer;
        }

        .top-crest-shield:hover {
            transform: scale(1.08) translateY(-3px);
        }

        .top-crest-shield img {
            width: 100%;
            height: 100%;
            object-fit: contain;
            display: block;
        }

        .bg-lion-watermark {
            position: fixed;
            top: 48%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 720px;
            max-width: 85vw;
            opacity: 0.18;
            pointer-events: none;
            z-index: 1;
            filter: drop-shadow(0 0 35px rgba(212, 163, 55, 0.35));
        }

        .bg-lion-watermark img {
            width: 100%;
            height: auto;
            display: block;
        }

        /* Seamless showcase container for Home */
        #tab-home .parchment-frame {
            background: transparent;
            border: none;
            outline: none;
            box-shadow: none;
            padding: 10px 0;
        }

        #tab-home .corner-filigree {
            display: none;
        }

        .mockup-home-grid {
            display: grid;
            grid-template-columns: 370px 1fr;
            gap: 48px;
            align-items: center;
            width: 100%;
        }

        /* Circular Character Avatar Frame with Gold Halo Ring */
        .character-circle-wrapper {
            position: relative;
            width: 350px;
            height: 350px;
            max-width: 100%;
            margin: 0 auto;
            cursor: pointer;
            border-radius: 50%;
            transition: transform 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        .character-circle-wrapper:hover {
            transform: scale(1.03);
        }

        /* Outer offset gold ring matching mockup */
        .character-circle-wrapper::before {
            content: '';
            position: absolute;
            inset: -14px;
            border-radius: 50%;
            border: 1.5px solid rgba(223, 162, 44, 0.6);
            pointer-events: none;
            transform: rotate(-14deg);
            box-shadow: 0 0 20px rgba(223, 162, 44, 0.25);
        }

        .character-circle-inner {
            position: relative;
            width: 100%;
            height: 100%;
            border-radius: 50%;
            overflow: hidden;
            border: 3px solid #dfa22c;
            box-shadow: 
                0 0 0 2px rgba(35, 4, 8, 0.8),
                0 0 28px rgba(223, 162, 44, 0.45),
                0 18px 45px rgba(0, 0, 0, 0.95);
            background: #190204;
        }

        .portrait-avatar-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
            transition: transform 0.4s ease;
        }

        .character-circle-wrapper:hover .portrait-avatar-img {
            transform: scale(1.06);
        }

        /* Right Column Narrative */
        .mockup-narrative {
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        /* Large Cursive Script Calligraphy Title */
        .script-title-gold {
            font-family: 'Great Vibes', 'Alex Brush', 'Sarun HarryPotter', cursive;
            font-size: 5rem;
            line-height: 1.08;
            color: #ffd875;
            background: linear-gradient(180deg, #fff3c4 0%, #f5c542 55%, #b88114 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            filter: drop-shadow(0 2px 10px rgba(0, 0, 0, 0.95)) drop-shadow(0 0 20px rgba(243, 194, 82, 0.4));
            margin: 0 0 4px 0;
            text-align: center;
            font-weight: 400;
        }

        .script-subtitle-gold {
            font-family: 'Sarun HarryPotter', 'Harry Potter', 'Cinzel', serif;
            font-size: 2.2rem;
            color: #e5aa37;
            text-align: center;
            letter-spacing: 2px;
            margin-bottom: 20px;
            text-shadow: 0 2px 6px rgba(0, 0, 0, 0.85), 0 0 14px rgba(229, 170, 55, 0.45);
        }

        /* Bio Paragraph in Rich Gold Amber */
        .character-bio-card {
            font-family: 'SOV Yoona', 'Noto Serif Thai', serif;
            font-size: 1.25rem;
            line-height: 1.95;
            letter-spacing: 0.35px;
            color: #ffd269;
            text-shadow: 0 1px 4px rgba(0, 0, 0, 0.95);
            margin-bottom: 24px;
            text-align: justify;
        }

        /* 3 Scene Thumbnails Row */
        .scene-thumbnails-row {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 16px;
        }

        .scene-card-item {
            position: relative;
            aspect-ratio: 16 / 10;
            border: 2.5px solid #140204;
            outline: 1.5px solid rgba(223, 162, 44, 0.35);
            border-radius: 4px;
            overflow: hidden;
            background: #0d0102;
            box-shadow: 0 8px 22px rgba(0, 0, 0, 0.85);
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        .scene-card-item:hover {
            transform: translateY(-5px) scale(1.03);
            outline-color: #ffd875;
            box-shadow: 0 12px 28px rgba(0, 0, 0, 0.95), 0 0 20px rgba(243, 194, 82, 0.55);
        }

        .scene-thumb-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
            transition: transform 0.4s ease;
        }

        .scene-card-item:hover .scene-thumb-img {
            transform: scale(1.08);
        }

        /* Redesigned Dock Navigation with Watermark Sketches */
        .common-room-dock {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: rgba(50, 6, 12, 0.88);
            border-top: 1.5px solid rgba(223, 162, 44, 0.45);
            box-shadow: 0 -8px 28px rgba(0, 0, 0, 0.92);
            z-index: 50;
            padding: 14px 24px;
            backdrop-filter: blur(12px);
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }

        .dock-bg-sketches {
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            opacity: 0.22;
            z-index: 1;
        }

        .dock-bg-sketches img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center;
        }

        .dock-links-row {
            position: relative;
            z-index: 2;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 20px;
        }

        .dock-link {
            background: none;
            border: none;
            color: #e5aa37;
            font-family: 'Sarun HarryPotter', 'Harry Potter', 'Cinzel', serif;
            font-size: 2.2rem;
            font-weight: 700;
            letter-spacing: 1px;
            padding: 4px 16px;
            cursor: pointer;
            transition: all 0.22s ease;
            text-shadow: 0 2px 5px rgba(0, 0, 0, 0.85);
            position: relative;
        }

        .dock-link::after {
            display: none !important;
        }

        .dock-link:hover,
        .dock-link.active {
            color: #fff2be;
            text-shadow: 0 0 16px #ffd875, 0 0 26px #ff7700;
            transform: translateY(-2px);
        }

        .dock-pipe-divider {
            color: #b88628;
            font-size: 2.2rem;
            font-family: serif;
            user-select: none;
            opacity: 0.7;
        }

        .modal-preview-img-box {
            width: 100%;
            max-height: 380px;
            border-radius: 6px;
            overflow: hidden;
            margin-bottom: 16px;
            border: 2px solid var(--gold-antique);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.8);
            background: #110204;
        }

        .modal-preview-img {
            width: 100%;
            height: 100%;
            max-height: 380px;
            object-fit: contain;
            display: block;
        }

        @media (max-width: 960px) {
            .mockup-home-grid {
                grid-template-columns: 1fr;
                gap: 32px;
                text-align: center;
            }
            .character-circle-wrapper {
                width: 280px;
                height: 280px;
            }
            .script-title-gold {
                font-size: 3.8rem;
            }
            .script-subtitle-gold {
                font-size: 1.8rem;
            }
            .dock-link {
                font-size: 1.6rem;
                padding: 4px 8px;
            }
            .dock-pipe-divider {
                font-size: 1.6rem;
            }
            .top-crest-shield {
                width: 60px;
                height: 72px;
                top: 16px;
                left: 18px;
            }
        }
"""

# Insert CSS right before </style>
last_style_idx = html.rfind('</style>')
if last_style_idx != -1:
    html = html[:last_style_idx] + mockup_css + '\n    ' + html[last_style_idx:]
    print("Injected mockup CSS styles")

# 4. Insert Top-Left Crest & Lion Watermark right after <body>
top_elements = """
    <!-- 🦁 ตราประจำบ้านกริฟฟินดอร์ (Gryffindor Shield Crest) ที่มุมซ้ายบนตามแบบ -->
    <div class="top-crest-shield" id="waxSeal" role="button" tabindex="0" title="Gryffindor House Crest (คลิกเพื่อคำราม)" onclick="triggerCrestRoar()">
        <!-- 📷 [1] ตราโรงเรียน/บ้านกริฟฟินดอร์: images/crest.png -->
        <img src="images/crest.png" alt="Gryffindor Crest" onerror="this.onerror=null; this.src='data:image/svg+xml;utf8,<svg xmlns=\\'http://www.w3.org/2000/svg\\' viewBox=\\'0 0 24 24\\' fill=\\'%23ffd700\\'><path d=\\'M12 2C8.5 2 5 3.5 3 6v9c0 5 9 7 9 7s9-2 9-7V6c-2-2.5-5.5-4-9-4z\\'/></svg>';" />
    </div>

    <!-- 🦁 ลายน้ำสิงโตกริฟฟินดอร์ขนาดใหญ่ตรงกลางพื้นหลัง (Lion Watermark) -->
    <div class="bg-lion-watermark" aria-hidden="true">
        <!-- 📷 [6] ลายน้ำสิงโตพื้นหลัง: images/bg-lion.png -->
        <img src="images/bg-lion.png" alt="" onerror="this.style.display='none';" />
    </div>
"""

# Check header wax seal and replace or keep
old_header_pattern = re.compile(r'<!-- ตราประทับขี้ผึ้ง & สโลแกนประจำบ้าน -->\s*<header class="gryffindor-header-crest">.*?</header>', re.DOTALL)
if old_header_pattern.search(html):
    html = old_header_pattern.sub(top_elements.strip(), html, count=1)
    print("Replaced old header with top-crest-shield and bg-lion-watermark")
else:
    # Insert right after snitch
    snitch_idx = html.find('<!-- ลูกสนิชสีทอง (The Golden Snitch) -->')
    if snitch_idx != -1:
        html = html[:snitch_idx] + top_elements + '\n\n    ' + html[snitch_idx:]
        print("Inserted top-crest-shield and bg-lion-watermark before snitch")

# 5. Replace TAB 1: HOME content with the mockup structure
tab_home_new = """        <!-- ================= TAB 1: HOME (เลย์เอาต์ตามรูปต้นแบบ) ================= -->
        <section id="tab-home" class="tab-content active">
            <div class="parchment-frame">
                <div class="mockup-home-grid">
                    
                    <!-- 🖼️ ฝั่งซ้าย: กรอบรูปโปรไฟล์ทรงกลมขอบทองคู่ (Circular Portrait Frame) -->
                    <div class="character-circle-wrapper" id="mainPortrait" role="button" tabindex="0" aria-label="กรอบรูป Alexan (คลิกเพื่อร่ายคาถาผู้พิทักษ์)" onmousemove="handlePortraitTilt(event)" onmouseleave="resetPortraitTilt()" onclick="triggerPatronusSpell()">
                        <div class="character-circle-inner">
                            <!-- 📷 [2] รูปโปรไฟล์วงกลมด้านซ้าย: images/alexan-profile.png (แทนที่ไฟล์นี้ด้วยรูปวาดของคุณได้เลย) -->
                            <img src="images/alexan-profile.png" alt="Alexan Nigelus Lake" class="portrait-avatar-img" onerror="this.onerror=null; this.src='images/crest.png';" />
                            <div class="portrait-shimmer" id="portraitShimmer"></div>
                        </div>
                    </div>

                    <!-- 📜 ฝั่งขวา: ชื่อลายมือตวัดสีทอง, ชื่อเล่น, ข้อความบรรยาย และซีน 3 ช่อง -->
                    <div class="mockup-narrative">
                        <!-- ✒️ ชื่อตัวละครลายมือตวัดสีทอง (Cursive Script Calligraphy) -->
                        <h1 class="script-title-gold">Alexan Nigelus Lake</h1>
                        <div class="script-subtitle-gold">Alexan / Alex</div>

                        <!-- 📜 ข้อความบรรยายตัวละคร (Bio Description) -->
                        <div class="character-bio-card">
                            อเล็กซ์เป็นคนเลือดร้อนและมุทะลุเหมือนกับไฟเยอร์โบลด์ที่เขาขึ้นขี่ทุกครั้งในการแข่งขันควิดดิช
                            เขาเป็นคนที่อาจดูเหมือนคนที่มักจะลงมือทำก่อนคิดและมันก็เป็นเช่นนั้น แต่ก็แน่นอนนั้นล่ะ
                            เขาไม่ใช่คนที่คิดในทางแง่บวกหรือแง่ลบแต่จะคิดเป็นเปอร์เซ็นความสำเร็จหรือไม่สำเร็จกี่เปอร์เซ็นเสียมากกว่า
                            แต่เพราะความมุทะลุเลือดพล่านเหมือนลูกบลัดเจอร์ของเขา ทำให้ส่วนใหญ่แล้วจะลงมือทำเสียก่อนจะได้คิดถึงเปอร์เซ็นเหล่านั้น
                            และที่สำคัญ เขาเป็นคนฉลาดอย่างน่าเหลือเชื่อแม้จะดูเหมือนพวกไม่เอาไหนด้านการเรียนแต่ก็อีกนั่นแหล่ะ
                            มักจะเอาความฉลาดไปใช้กับการเล่นตลกเสียงดังตึงตัง
                        </div>

                        <!-- 🎬 แถบภาพซีน 3 ช่องแนวนอน (3 Horizontal Scene Thumbnails) -->
                        <div class="scene-thumbnails-row">
                            <!-- ซีนที่ 1: Hogsmeade -->
                            <div class="scene-card-item" role="button" tabindex="0" aria-label="ดูภาพ Hogsmeade Stroll" onclick="openGalleryItem(0)" title="คลิกตรวจดูภาพ: Hogsmeade Stroll">
                                <!-- 📷 [3] ภาพซีนที่ 1: images/scene-1.jpg -->
                                <img src="images/scene-1.jpg" alt="Hogsmeade Stroll" class="scene-thumb-img" onerror="this.onerror=null; this.src='images/alexan-profile.png';" />
                            </div>

                            <!-- ซีนที่ 2: Winter Scarf -->
                            <div class="scene-card-item" role="button" tabindex="0" aria-label="ดูภาพ Winter Scarf" onclick="openGalleryItem(1)" title="คลิกตรวจดูภาพ: Winter Scarf">
                                <!-- 📷 [4] ภาพซีนที่ 2: images/scene-2.jpg -->
                                <img src="images/scene-2.jpg" alt="Winter Scarf" class="scene-thumb-img" onerror="this.onerror=null; this.src='images/alexan-profile.png';" />
                            </div>

                            <!-- ซีนที่ 3: Quidditch Pitch -->
                            <div class="scene-card-item" role="button" tabindex="0" aria-label="ดูภาพ Quidditch Pitch" onclick="openGalleryItem(2)" title="คลิกตรวจดูภาพ: Quidditch Pitch">
                                <!-- 📷 [5] ภาพซีนที่ 3: images/scene-3.jpg -->
                                <img src="images/scene-3.jpg" alt="Quidditch Pitch" class="scene-thumb-img" onerror="this.onerror=null; this.src='images/alexan-profile.png';" />
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </section>"""

old_home_pattern = re.compile(r'<!-- ================= TAB 1: HOME ================= -->\s*<section id="tab-home".*?</section>', re.DOTALL)
if old_home_pattern.search(html):
    html = old_home_pattern.sub(tab_home_new, html, count=1)
    print("Replaced TAB 1: HOME with mockup layout")
else:
    print("WARNING: old_home_pattern not found")

# 6. Replace Dock navigation bar with mockup layout (with sketches and gold pipes)
dock_new = """    <!-- ================= DOCK NAVIGATION (แถบเมนูด้านล่างตามแบบ) ================= -->
    <nav class="common-room-dock" aria-label="Gryffindor Navigation Dock">
        <!-- 📷 [7] ลายน้ำภาพสเก็ตช์แนวยาวด้านหลังแถบเมนู: images/bg-sketches.png -->
        <div class="dock-bg-sketches" aria-hidden="true">
            <img src="images/bg-sketches.png" alt="" onerror="this.style.display='none';" />
        </div>
        
        <div class="dock-links-row">
            <button class="dock-link active" data-tab="home" onclick="switchTab('home')">Home</button>
            <span class="dock-pipe-divider">|</span>
            <button class="dock-link" data-tab="information" onclick="switchTab('information')">Information</button>
            <span class="dock-pipe-divider">|</span>
            <button class="dock-link" data-tab="gallery" onclick="switchTab('gallery')">Gallery</button>
            <span class="dock-pipe-divider">|</span>
            <button class="dock-link" data-tab="about" onclick="switchTab('about')">About</button>
        </div>
    </nav>"""

old_dock_pattern = re.compile(r'<!-- ================= DOCK NAVIGATION ================= -->\s*<nav class="common-room-dock".*?</nav>', re.DOTALL)
if old_dock_pattern.search(html):
    html = old_dock_pattern.sub(dock_new, html, count=1)
    print("Replaced DOCK NAVIGATION with mockup layout")
else:
    print("WARNING: old_dock_pattern not found")

# 7. Update galleryStories with image paths so Lightbox modal shows images
old_gallery_stories_pattern = re.compile(r'const galleryStories = \[\s*\{.*?\}\s*\];', re.DOTALL)
new_gallery_stories = """const galleryStories = [
            {
                title: "Hogsmeade Stroll / เดินเล่นฮอกส์มี้ด",
                desc: "ช็อตช่วงวันหยุดสุดสัปดาห์ในฤดูหนาวที่หมู่บ้านฮอกส์มี้ด อเล็กซ์แอบพาเพื่อนย่องไปซื้อขนมร้านฮันนี่ดุกส์ และนั่งคุยกันข้างเตาผิงร้านไม้กวาดสามอันพร้อมบัตเตอร์เบียร์ฟองนุ่ม",
                image: "images/scene-1.jpg"
            },
            {
                title: "Winter Scarf / ผ้าพันคอรับลมหนาว",
                desc: "ผ้าพันคอไหมพรมลายทางสีแดงเลือดหมูสลับทองที่ถักเองอย่างเบี้ยวๆ แต่นุ่มอุ่นสบาย ช่วยบังลมหนาวจากยอดหอคอยกริฟฟินดอร์",
                image: "images/scene-2.jpg"
            },
            {
                title: "Quidditch Pitch / สนามควิดดิช",
                desc: "ภาพช่วงก่อนแมตช์การแข่งขันใหญ่กับสลิธีริน อเล็กซ์ถือไม้กวาดและไม้ตีบลัดเจอร์ด้วยสีหน้ามั่นใจเต็มร้อย พร้อมจะพาทีมคว้าชัยชนะ",
                image: "images/scene-3.jpg"
            },
            {
                title: "Prank Fireworks / จังหวะหน้าแดง",
                desc: "เหตุการณ์ตอนที่ตั้งใจจะจุดประทัดควันดักแกล้งเพื่อนในห้องนั่งเล่นรวม แต่โดนจับได้จนแก้ตัวไม่ถูกจนหน้าแดงแจ๋",
                image: "images/alexan-profile.png"
            },
            {
                title: "Duel Training / หลังการดวลฝึกซ้อม",
                desc: "เสื้อคลุมเปื้อนเขม่าควันคาถาหลังฝึกดวลวิชาป้องกันตัวจากศาสตร์มืดจนเหงื่อท่วม แต่ยังมีรอยยิ้มภาคภูมิใจไม่เคยยอมแพ้",
                image: "images/alexan-profile.png"
            },
            {
                title: "Fierce Resolve / จิตวิญญาณกริฟฟินดอร์",
                desc: "แววตาแน่วแน่แม้จะสูญเสียดวงตาข้างซ้ายและขาขวา แต่อเล็กซ์ก็พิสูจน์ให้ทุกคนเห็นว่าหัวใจแห่งความกล้าหาญไม่ได้สูญเสียไปตามร่างกายเลย",
                image: "images/alexan-profile.png"
            }
        ];"""

if old_gallery_stories_pattern.search(html):
    html = old_gallery_stories_pattern.sub(new_gallery_stories, html, count=1)
    print("Updated galleryStories with image paths")

# Update openGalleryItem function to render image if present
old_open_gallery = """        function openGalleryItem(index) {
            const item = galleryStories[index];
            if (!item) return;
            document.getElementById('scrollHeader').innerHTML = item.title;
            document.getElementById('scrollContent').innerHTML = item.desc;
            document.getElementById('scrollModal').classList.add('active');
            isModalOpen = true;"""

new_open_gallery = """        function openGalleryItem(index) {
            const item = galleryStories[index];
            if (!item) return;
            document.getElementById('scrollHeader').innerHTML = item.title;
            let previewImg = item.image ? `<div class="modal-preview-img-box"><img src="${item.image}" alt="${item.title}" class="modal-preview-img" onerror="this.style.display='none'" /></div>` : '';
            document.getElementById('scrollContent').innerHTML = previewImg + `<div class="modal-text-desc" style="line-height: 2;">${item.desc}</div>`;
            document.getElementById('scrollModal').classList.add('active');
            isModalOpen = true;"""

if old_open_gallery in html:
    html = html.replace(old_open_gallery, new_open_gallery)
    print("Updated openGalleryItem function to render preview images in modal")

# 8. Write updated index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully updated index.html with mockup image architecture!")
