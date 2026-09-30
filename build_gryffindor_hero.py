# -*- coding: utf-8 -*-
"""
Build authentic Gryffindor Hero Presentation for Alexan Nigelus Lake.
Restores 100% of the Gryffindor & Harry Potter identity, atmosphere, and content,
while upgrading the character presentation to the heroic layered composition.
"""

import shutil
import re

# 1. Restore clean base from backup
shutil.copyfile('index.html.before_poster.bak', 'index.html')
print("[1] Restored clean base from index.html.before_poster.bak")

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 2. Hero Presentation CSS for #tab-home
hero_css = """
        /* ==========================================================================
           AUTHENTIC GRYFFINDOR HERO PRESENTATION (HOME TAB)
           Preserves 100% Harry Potter / Gryffindor theme with modern layered depth
           ========================================================================== */

        .gryffindor-hero-grid {
            display: grid;
            grid-template-columns: 420px 1fr;
            gap: 48px;
            align-items: center;
            width: 100%;
            position: relative;
        }

        /* Hero Stage on the Left */
        .hero-stage-container {
            position: relative;
            width: 100%;
            height: 580px;
            display: flex;
            align-items: flex-end;
            justify-content: center;
            user-select: none;
        }

        /* Layered Depth Cards behind Character */
        .hero-depth-card-1 {
            position: absolute;
            left: 25px;
            top: 30px;
            width: 320px;
            height: 480px;
            border-radius: 28px;
            background: rgba(36, 4, 8, 0.85);
            border: 1.5px solid rgba(223, 162, 44, 0.45);
            box-shadow: 
                0 20px 50px rgba(0, 0, 0, 0.9),
                inset 0 0 30px rgba(0, 0, 0, 0.7);
            pointer-events: none;
            z-index: 1;
            transform: rotate(-4deg);
            transition: transform 0.4s ease;
        }

        .hero-depth-card-2 {
            position: absolute;
            left: 10px;
            top: 70px;
            width: 270px;
            height: 420px;
            border-radius: 24px;
            background: #110103;
            border: 1px solid rgba(223, 162, 44, 0.25);
            box-shadow: 
                0 25px 60px rgba(0, 0, 0, 0.95),
                0 0 25px rgba(223, 162, 44, 0.15);
            pointer-events: none;
            z-index: 2;
            transform: rotate(3deg);
            transition: transform 0.4s ease;
        }

        .hero-stage-container:hover .hero-depth-card-1 {
            transform: rotate(-6deg) translateY(-5px);
        }
        .hero-stage-container:hover .hero-depth-card-2 {
            transform: rotate(5deg) translateY(-3px);
        }

        /* The Hero Artwork Container */
        .hero-artwork-wrapper {
            position: relative;
            z-index: 8;
            width: 100%;
            max-width: 400px;
            height: 560px;
            display: flex;
            align-items: flex-end;
            justify-content: center;
            cursor: pointer;
        }

        .hero-character-img {
            max-width: 100%;
            max-height: 100%;
            object-fit: contain;
            object-position: bottom center;
            display: block;
            filter: drop-shadow(0 15px 35px rgba(0, 0, 0, 0.95)) drop-shadow(0 0 25px rgba(223, 162, 44, 0.35));
            transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        .hero-stage-container:hover .hero-character-img {
            transform: scale(1.04) translateY(-8px);
            filter: drop-shadow(0 20px 45px rgba(0, 0, 0, 0.98)) drop-shadow(0 0 35px rgba(243, 194, 82, 0.55));
        }

        /* Floating Gryffindor Badges */
        .hero-crest-badge {
            position: absolute;
            top: 25px;
            right: 10px;
            z-index: 12;
            background: rgba(25, 2, 6, 0.92);
            border: 1.5px solid #dfa22c;
            border-radius: 9999px;
            padding: 5px 14px;
            display: flex;
            align-items: center;
            gap: 8px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.8), 0 0 14px rgba(223, 162, 44, 0.3);
            font-family: 'Cinzel', serif;
            font-size: 0.78rem;
            font-weight: 700;
            color: #ffd875;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            pointer-events: none;
        }

        .hero-crest-badge svg {
            width: 14px;
            height: 14px;
            fill: #dfa22c;
        }

        .hero-quidditch-pill {
            position: absolute;
            bottom: 25px;
            left: 0;
            z-index: 12;
            background: linear-gradient(135deg, #1c0205 0%, #30050c 100%);
            border: 1.5px solid #dfa22c;
            border-radius: 9999px;
            padding: 7px 18px;
            display: flex;
            align-items: center;
            gap: 10px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.85), 0 0 18px rgba(223, 162, 44, 0.35);
            font-family: 'Cinzel', serif;
            font-size: 0.85rem;
            font-weight: 700;
            color: #ffd875;
            letter-spacing: 1px;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        .hero-quidditch-pill:hover {
            transform: scale(1.08) translateY(-2px);
            border-color: #ffd875;
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.95), 0 0 25px rgba(243, 194, 82, 0.6);
            color: #ffffff;
        }

        .hero-quidditch-pill .pill-star {
            color: #dfa22c;
            font-size: 11px;
        }

        /* Right Column Narrative */
        .gryffindor-hero-narrative {
            display: flex;
            flex-direction: column;
            justify-content: center;
            z-index: 5;
        }

        /* Responsive Layout */
        @media (max-width: 1050px) {
            .gryffindor-hero-grid {
                grid-template-columns: 360px 1fr;
                gap: 32px;
            }
            .hero-stage-container {
                height: 500px;
            }
            .hero-depth-card-1 {
                width: 280px;
                height: 420px;
            }
            .hero-depth-card-2 {
                width: 240px;
                height: 380px;
            }
        }

        @media (max-width: 860px) {
            .gryffindor-hero-grid {
                grid-template-columns: 1fr;
                gap: 40px;
            }
            .hero-stage-container {
                margin: 0 auto;
                height: 480px;
                max-width: 360px;
            }
        }
"""

# Inject Hero CSS before the last </style>
last_style = content.rfind('</style>')
if last_style != -1:
    content = content[:last_style] + f'{hero_css}\n    ' + content[last_style:]
    print("[2] Injected Gryffindor Hero CSS before </style>")

# 3. New HTML markup for tab-home: Authentic Gryffindor with Hero presentation
home_html = """        <!-- ================= TAB 1: HOME (Authentic Gryffindor Hero Presentation) ================= -->
        <section id="tab-home" class="tab-content active">
            <div class="parchment-frame">
                <div class="gryffindor-hero-grid">

                    <!-- 🖼️ ฝั่งซ้าย: การจัดวางตัวละครแบบ Hero Presentation พร้อมมิติความลึก (Layered Depth) -->
                    <div class="hero-stage-container" id="mainPortrait" role="button" tabindex="0"
                         aria-label="รูปภาพ Alexan Nigelus Lake (คลิกเพื่อร่ายประกายคาถาผู้พิทักษ์)"
                         onmousemove="handlePortraitTilt(event)" onmouseleave="resetPortraitTilt()"
                         onclick="triggerPatronusSpell()">

                        <!-- เลเยอร์การ์ดมิติความลึกด้านหลังตัวละคร (Gryffindor Layered Depth Cards) -->
                        <div class="hero-depth-card-1" aria-hidden="true"></div>
                        <div class="hero-depth-card-2" aria-hidden="true"></div>

                        <!-- 🦁 ตรากริฟฟินดอร์ด้านบน (Gryffindor Pride Badge) -->
                        <div class="hero-crest-badge" aria-hidden="true">
                            <svg viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                            <span>Gryffindor Pride</span>
                        </div>

                        <!-- 🧹 ป้ายตำแหน่งควิดดิช (Firebolt • Chaser Pill Badge) -->
                        <div class="hero-quidditch-pill" onclick="event.stopPropagation(); openScroll('magic');" title="คลิกดูข้อมูลอุปกรณ์เวทมนตร์และไม้กวาด">
                            <span class="pill-star">✦</span>
                            <span>Firebolt • Chaser #07</span>
                        </div>

                        <!-- 🖼️ โครงสร้างกรอบรูปตัวละคร (Hero Artwork Frame) -->
                        <div class="hero-artwork-wrapper">
                            <!-- 📷 [จุดใส่รูปตัวละครของคุณ] 
                                 คุณสามารถนำรูปวาดตัวละครของคุณมาแทนที่ images/alexan-profile.jpg?v=5 ได้เลยครับ
                                 แนะนำใช้รูปภาพไดคัทไม่มีพื้นหลัง (.png) เพื่อให้ตัวละครยืนซ้อนทับเลเยอร์ด้านหลังอย่างสมบูรณ์แบบ -->
                            <img id="heroCharacterImg" src="images/alexan-profile.jpg?v=5" alt="Alexan Nigelus Lake"
                                 class="hero-character-img"
                                 onerror="this.onerror=null; this.src='images/hogwarts-logo.png';" />
                            <div class="portrait-shimmer" id="portraitShimmer"></div>
                        </div>

                    </div>

                    <!-- 📜 ฝั่งขวา: ชื่อลายมือตวัดสีทอง, ข้อความบรรยายตัวละคร และแถบซีน 3 ช่อง -->
                    <div class="gryffindor-hero-narrative">
                        <!-- ✒️ ชื่อตัวละครลายมือตวัดสีทอง (Cursive Script Calligraphy) -->
                        <h1 class="script-title-gold">Alexan Nigelus Lake</h1>
                        <div class="script-subtitle-gold">Alexan / Alex • Year 6, Gryffindor</div>

                        <!-- 📜 ข้อความบรรยายตัวละคร (Bio Description) ในฟอนต์ SOV Yoona สีทองอบอุ่น -->
                        <div class="character-bio-card">
                            อเล็กซ์เป็นคนเลือดร้อนและมุทะลุเหมือนกับไฟเยอร์โบลด์ที่เขาขึ้นขี่ทุกครั้งในการแข่งขันควิดดิช
                            เขาเป็นคนที่อาจดูเหมือนคนที่มักจะลงมือทำก่อนคิดและมันก็เป็นเช่นนั้น แต่ก็แน่นอนนั้นล่ะ
                            เขาไม่ใช่คนที่คิดในทางแง่บวกหรือแง่ลบแต่จะคิดเป็นเปอร์เซ็นความสำเร็จหรือไม่สำเร็จกี่เปอร์เซ็นเสียมากกว่า
                            แต่เพราะความมุทะลุเลือดพล่านเหมือนลูกบลัดเจอร์ของเขา
                            ทำให้ส่วนใหญ่แล้วจะลงมือทำเสียก่อนจะได้คิดถึงเปอร์เซ็นเหล่านั้น
                            และที่สำคัญ
                            เขาเป็นคนฉลาดอย่างน่าเหลือเชื่อแม้จะดูเหมือนพวกไม่เอาไหนด้านการเรียนแต่ก็อีกนั่นแหล่ะ
                            มักจะเอาความฉลาดไปใช้กับการเล่นตลกเสียงดังตึงตัง
                        </div>

                        <!-- 🎬 แถบภาพซีน 3 ช่องแนวนอน (3 Horizontal Scene Thumbnails) -->
                        <div class="scene-thumbnails-row">
                            <!-- ซีนที่ 1: Hogsmeade -->
                            <div class="scene-card-item" role="button" tabindex="0" aria-label="ดูภาพ Hogsmeade Stroll"
                                 onclick="openGalleryItem(0)" title="คลิกตรวจดูภาพ: Hogsmeade Stroll">
                                <img src="images/scene-1.jpg?v=2" alt="Hogsmeade Stroll" class="scene-thumb-img"
                                     onerror="this.onerror=null; this.src='images/alexan-profile.jpg?v=2';" />
                            </div>

                            <!-- ซีนที่ 2: Winter Scarf -->
                            <div class="scene-card-item" role="button" tabindex="0" aria-label="ดูภาพ Winter Scarf"
                                 onclick="openGalleryItem(1)" title="คลิกตรวจดูภาพ: Winter Scarf">
                                <img src="images/scene-2.jpg?v=2" alt="Winter Scarf" class="scene-thumb-img"
                                     onerror="this.onerror=null; this.src='images/alexan-profile.jpg?v=2';" />
                            </div>

                            <!-- ซีนที่ 3: Quidditch Pitch -->
                            <div class="scene-card-item" role="button" tabindex="0" aria-label="ดูภาพ Quidditch Pitch"
                                 onclick="openGalleryItem(2)" title="คลิกตรวจดูภาพ: Quidditch Pitch">
                                <img src="images/scene-3.jpg?v=2" alt="Quidditch Pitch" class="scene-thumb-img"
                                     onerror="this.onerror=null; this.src='images/alexan-profile.jpg?v=2';" />
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </section>"""

# Replace existing tab-home section
pattern = r'<section id="tab-home".*?</section>'
match = re.search(pattern, content, re.DOTALL)
if match:
    content = content[:match.start()] + home_html + content[match.end():]
    print("[3] Successfully updated tab-home with Gryffindor Hero layout")
else:
    print("[3] ERROR: Could not find <section id=\"tab-home\">")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("[DONE] Successfully generated index.html!")
