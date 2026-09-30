# -*- coding: utf-8 -*-
"""
Apply the Out-of-Frame Pop-Out Character Card for Alexan Lake
in the About tab (#tab-about) with authentic Gryffindor theme.
"""
import shutil
import re

# 1. Backup
shutil.copyfile('index.html', 'index.html.before_popout.bak')
print("[1] Created index.html.before_popout.bak")

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# =========================================================================
# 2. NEW HTML MARKUP FOR THE POPOUT PORTRAIT CARD
# =========================================================================
old_portrait_pattern = r'<div class="character-portrait-box"[^>]*>[\s\S]*?</div>\s*</div>'

new_portrait_html = """                <!-- 🦁 Alexan Lake Character Pop-Out Card (ตัวละครทะลุล้นออกจาก Frame ตามแบบ) -->
                <div class="character-portrait-box popout-portrait-container">
                    <div class="portrait-inner-art popout-art-stage" id="aboutPopoutStage">
                        <!-- Ambient Radiant Glow Behind the Card -->
                        <div class="popout-ambient-glow" aria-hidden="true"></div>

                        <!-- The Rounded Card Frame (Background & Gold Border) -->
                        <div class="popout-card-frame">
                            <!-- Background Inner Atmosphere (Gryffindor Deep Crimson Velvet & Lion Watermark) -->
                            <div class="popout-card-bg">
                                <div class="popout-card-watermark" aria-hidden="true">
                                    <img src="images/bg-lion.jpg" alt="" onerror="this.style.display='none';" />
                                </div>
                                <div class="popout-card-glow-core"></div>
                                <div class="popout-card-corner-ornament topleft"></div>
                                <div class="popout-card-corner-ornament topright"></div>
                            </div>
                        </div>

                        <!-- Character Pop-Out Layer (Head & Hair extends 75px ABOVE the card, bottom is clipped to the card) -->
                        <div class="popout-character-layer">
                            <img src="images/alexan-info-cropped.png" alt="Alexan Nigelus Lake" class="popout-character-img"
                                onerror="this.onerror=null; this.src='images/Alexan-info.png';" />
                            <div class="popout-character-shimmer"></div>
                        </div>

                        <!-- Card Bottom Gilded Overlay & Cursive Calligraphy (matching reference image) -->
                        <div class="popout-card-overlay">
                            <div class="popout-cursive-name">
                                <span class="cursive-main">Alexan</span>
                                <span class="cursive-sub">Nigelus Lake</span>
                            </div>
                            <div class="popout-house-pill">
                                <span class="pill-lion">🦁</span>
                                <span>Gryffindor • Year 6</span>
                            </div>
                        </div>
                    </div>

                    <!-- Warning Quote Plaque below the character card -->
                    <div class="popout-rules-plaque">
                        <div class="rules-quote-text">
                            "อย่าเดินย่องเข้ามาจากข้างหลังด้านซ้าย... ถ้าไม่อยากโดนคาถาหงายหลัง"
                        </div>
                        <div class="rules-author-tag">
                            <span class="spark-star">✦</span> บันทึกเตือนความจำ (Alex's Rules)
                        </div>
                    </div>
                </div>"""

# Find exact location of character-portrait-box inside #tab-about
about_start = html.find('id="tab-about"')
pos_box = html.find('<div class="character-portrait-box"', about_start)
pos_rules_block = html.find('<div class="rules-tome-block">', pos_box)

if pos_box != -1 and pos_rules_block != -1:
    html = html[:pos_box] + new_portrait_html + "\n\n                " + html[pos_rules_block:]
    print("[2] Successfully replaced portrait box HTML with pop-out card markup.")
else:
    print("[ERROR] Could not find portrait box in #tab-about!")

# =========================================================================
# 3. CSS STYLES FOR THE POPOUT CARD
# =========================================================================
popout_css = """
        /* ==========================================================================
           POPOUT CHARACTER CARD FRAME (ABOUT TAB)
           Character pops out above the top edge while clipped at the bottom
           ========================================================================== */

        .character-portrait-box.popout-portrait-container {
            border: none !important;
            background: transparent !important;
            box-shadow: none !important;
            overflow: visible !important;
            height: auto !important;
            display: flex;
            flex-direction: column;
            align-items: center;
            perspective: 1200px;
            padding: 0;
            cursor: default !important;
        }

        .character-portrait-box.popout-portrait-container::after {
            display: none !important;
        }

        .portrait-inner-art.popout-art-stage {
            position: relative;
            width: 100%;
            max-width: 320px;
            height: 490px;
            overflow: visible;
            background: transparent;
            padding: 0;
            display: flex;
            align-items: flex-end;
            justify-content: center;
            transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
        }

        .character-portrait-box:hover .portrait-inner-art.popout-art-stage {
            transform: translateY(-8px);
        }

        /* Ambient Radiant Aura Glow behind the card */
        .popout-ambient-glow {
            position: absolute;
            top: 60px;
            bottom: -10px;
            left: -10px;
            right: -10px;
            background: radial-gradient(circle at 50% 50%, rgba(223, 162, 44, 0.45) 0%, rgba(138, 14, 25, 0.3) 50%, transparent 75%);
            filter: blur(20px);
            border-radius: 35px;
            pointer-events: none;
            z-index: 0;
            opacity: 0.75;
            transition: opacity 0.4s ease;
        }

        .character-portrait-box:hover .popout-ambient-glow {
            opacity: 1;
            filter: blur(25px);
        }

        /* The Rounded Card Frame (Starts 75px down from the top container edge) */
        .popout-card-frame {
            position: absolute;
            top: 75px;
            bottom: 0;
            left: 0;
            right: 0;
            border-radius: 28px;
            border: 2.5px solid var(--gold-bright);
            background: radial-gradient(circle at 50% 25%, #460911 0%, #200306 70%, #0d0102 100%);
            box-shadow: 
                0 22px 50px rgba(0, 0, 0, 0.95),
                0 0 35px rgba(223, 162, 44, 0.4),
                inset 0 0 30px rgba(0, 0, 0, 0.85);
            z-index: 1;
            overflow: hidden;
            transition: box-shadow 0.4s ease, border-color 0.4s ease;
        }

        .character-portrait-box:hover .popout-card-frame {
            border-color: #ffe6a0;
            box-shadow: 
                0 28px 60px rgba(0, 0, 0, 0.98),
                0 0 50px rgba(243, 199, 102, 0.65),
                inset 0 0 35px rgba(255, 215, 0, 0.2);
        }

        .popout-card-bg {
            position: absolute;
            inset: 0;
            overflow: hidden;
            pointer-events: none;
        }

        .popout-card-watermark {
            position: absolute;
            top: 40%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 220px;
            opacity: 0.18;
            filter: drop-shadow(0 0 15px rgba(223, 162, 44, 0.4));
        }

        .popout-card-watermark img {
            width: 100%;
            height: auto;
            display: block;
        }

        .popout-card-glow-core {
            position: absolute;
            top: 20%;
            left: 50%;
            transform: translateX(-50%);
            width: 200px;
            height: 200px;
            background: radial-gradient(circle, rgba(223, 162, 44, 0.25) 0%, transparent 70%);
            filter: blur(15px);
        }

        /* Gilded Corner Flourishes on Top Card Rim */
        .popout-card-corner-ornament {
            position: absolute;
            top: 10px;
            width: 20px;
            height: 20px;
            border: 2px solid var(--gold-bright);
            box-shadow: 0 0 8px rgba(255, 215, 0, 0.4);
            pointer-events: none;
        }
        .popout-card-corner-ornament.topleft { left: 10px; border-right: none; border-bottom: none; border-top-left-radius: 8px; }
        .popout-card-corner-ornament.topright { right: 10px; border-left: none; border-bottom: none; border-top-right-radius: 8px; }

        /* Character Pop-out Layer (Top unclipped 0 to 75px, Bottom clipped by 28px radius) */
        .popout-character-layer {
            position: absolute;
            top: 0;
            bottom: 0;
            left: 0;
            right: 0;
            border-radius: 0 0 28px 28px;
            overflow: hidden;
            z-index: 3;
            pointer-events: none;
        }

        .popout-character-img {
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 360px;
            max-width: 125%;
            height: 485px;
            object-fit: contain;
            object-position: bottom center;
            filter: drop-shadow(0 12px 25px rgba(0, 0, 0, 0.8));
            transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.2);
        }

        .character-portrait-box:hover .popout-character-img {
            transform: translateX(-50%) translateY(-6px) scale(1.03);
            filter: drop-shadow(0 16px 30px rgba(0, 0, 0, 0.95)) drop-shadow(0 0 15px rgba(223, 162, 44, 0.3));
        }

        .popout-character-shimmer {
            position: absolute;
            inset: 0;
            background: linear-gradient(120deg, transparent 35%, rgba(255, 235, 170, 0.15) 50%, transparent 65%);
            background-size: 200% 200%;
            pointer-events: none;
            animation: magicSheen 7s infinite ease-in-out;
            z-index: 4;
        }

        /* Card Bottom Gilded Overlay & Cursive Calligraphy (matching reference image) */
        .popout-card-overlay {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            padding: 24px 16px 18px;
            background: linear-gradient(to top, rgba(14, 1, 3, 0.95) 0%, rgba(20, 2, 4, 0.72) 65%, transparent 100%);
            border-radius: 0 0 28px 28px;
            z-index: 5;
            pointer-events: none;
            text-align: center;
        }

        .popout-cursive-name {
            display: flex;
            flex-direction: column;
            align-items: center;
            line-height: 1.1;
        }

        .popout-cursive-name .cursive-main {
            font-family: 'Satisfy', 'Lobster Two', cursive;
            font-size: 2.5rem;
            color: #ffffff;
            text-shadow: 
                0 2px 10px rgba(0, 0, 0, 0.95),
                0 0 20px rgba(223, 162, 44, 0.65);
            letter-spacing: 0.5px;
        }

        .popout-cursive-name .cursive-sub {
            font-family: 'Sarun HarryPotter', 'Cinzel', cursive, serif;
            font-size: 1.15rem;
            color: var(--gold-bright);
            letter-spacing: 1.5px;
            text-shadow: 0 2px 6px #000;
            margin-top: -2px;
        }

        .popout-house-pill {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            margin-top: 8px;
            padding: 4px 14px;
            border-radius: 20px;
            background: rgba(45, 8, 12, 0.9);
            border: 1px solid var(--gold-antique);
            color: #ffe6a0;
            font-family: 'SOV Yoona', 'Noto Serif Thai', serif;
            font-size: 0.95rem;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.6);
        }

        .popout-house-pill .pill-lion {
            font-size: 1rem;
        }

        /* Warning Quote Plaque below the character card */
        .popout-rules-plaque {
            margin-top: 16px;
            width: 100%;
            max-width: 320px;
            background: radial-gradient(ellipse at center, rgba(42, 6, 10, 0.92) 0%, rgba(16, 2, 4, 0.96) 100%);
            border: 1.5px solid var(--gold-antique);
            border-radius: 12px;
            padding: 12px 16px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.7);
            text-align: center;
            transition: all 0.3s ease;
        }

        .popout-rules-plaque:hover {
            border-color: var(--gold-bright);
            box-shadow: 0 10px 28px rgba(0, 0, 0, 0.85), 0 0 15px rgba(223, 162, 44, 0.25);
            transform: translateY(-2px);
        }

        .rules-quote-text {
            font-family: 'SOV Yoona', 'Samphan Condensed', 'Noto Serif Thai', serif;
            font-size: 1.25rem;
            color: #ffe6a0;
            line-height: 1.75;
            letter-spacing: 0.3px;
        }

        .rules-author-tag {
            font-family: 'Sarun HarryPotter', 'Cinzel', serif;
            font-size: 1rem;
            color: var(--gold-bright);
            margin-top: 6px;
            letter-spacing: 0.5px;
        }

        .rules-author-tag .spark-star {
            color: #ffe6a0;
            margin-right: 2px;
        }
"""

# Insert popout_css into the stylesheet before </style>
html = html.replace('</style>', popout_css + '\n    </style>')
print("[3] Added Pop-Out Card CSS styles into stylesheet.")

# 4. Save
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("[4] index.html updated successfully with pop-out card!")
