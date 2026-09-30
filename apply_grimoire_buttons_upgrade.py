# -*- coding: utf-8 -*-
"""
Apply 4 specific grimoire buttons upgrades requested by user:
1. Gilded Filigree Corners & Double Gilded Border
2. Tooled Leather / Burgundy Velvet Texture with Bevel & Candlelight Emboss
3. Brass Roman Numeral Stamp Seal & Golden Flourishes under Thai text
4. Aged Dark Oak Panel Plinth with Gryffindor Lion Watermark (~12% opacity)
"""

import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the CSS for .spell-topics-grid and .grimoire-btn
new_grimoire_css = """
        /* ==========================================================================
           GRIMOIRE ARCHIVE PLINTH & ENHANCED TOILED LEATHER BUTTONS
           1. Gilded Filigree Corners & Double Gilded Border
           2. Tooled Leather / Burgundy Velvet with Candlelight Bevel & Emboss
           3. Brass Roman Numeral Stamp Seal & Golden Flourishes
           4. Aged Dark Oak Panel Plinth with Gryffindor Lion Watermark
           ========================================================================== */

        /* 4. The Backdrop Plinth (แผงแท่นไม้โอ๊คขัดเงา) */
        .grimoire-plinth-panel {
            position: relative;
            background: 
                radial-gradient(ellipse at 50% 30%, #200407 0%, #120103 80%, #0a0102 100%);
            border: 2px solid #5a3814;
            outline: 1.5px solid rgba(223, 162, 44, 0.45);
            outline-offset: -4px;
            border-radius: 12px;
            padding: 16px 18px 20px 18px;
            margin-bottom: 22px;
            box-shadow: 
                inset 0 0 35px rgba(0, 0, 0, 0.95),
                inset 0 1px 2px rgba(223, 162, 44, 0.35),
                0 12px 30px rgba(0, 0, 0, 0.85);
            overflow: hidden;
        }

        /* Subtle Gryffindor Lion Watermark (10-15% Opacity) */
        .plinth-lion-watermark {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -42%);
            width: 260px;
            height: 260px;
            background-image: url('images/crest.png');
            background-repeat: no-repeat;
            background-position: center;
            background-size: contain;
            opacity: 0.13;
            pointer-events: none;
            filter: sepia(0.8) saturate(2.5) hue-rotate(-20deg) drop-shadow(0 0 15px rgba(223, 162, 44, 0.3));
            z-index: 1;
        }

        .plinth-header-bar {
            position: relative;
            z-index: 2;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
            margin-bottom: 14px;
        }

        .plinth-header-line {
            flex: 1;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(223, 162, 44, 0.45), transparent);
        }

        .plinth-header-text {
            font-family: 'Cinzel', 'SOV Yoona', serif;
            font-size: 0.92rem;
            font-weight: 700;
            letter-spacing: 1.5px;
            color: #dfa22c;
            text-transform: uppercase;
            text-shadow: 0 1px 4px rgba(0, 0, 0, 0.9);
            white-space: nowrap;
        }

        .spell-topics-grid {
            position: relative;
            z-index: 2;
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 14px;
            margin-bottom: 0;
        }

        /* 1 & 2. Gilded Buttons: Double Border, Filigree Corners, Tooled Velvet Texture & Emboss */
        .grimoire-btn {
            position: relative;
            background: 
                radial-gradient(ellipse at 50% 20%, #630811 0%, #3a0307 65%, #180103 100%),
                repeating-linear-gradient(
                    45deg,
                    rgba(0, 0, 0, 0.09) 0px,
                    rgba(0, 0, 0, 0.09) 2px,
                    transparent 2px,
                    transparent 4px
                );
            border: 1.5px solid #dfa22c;
            border-radius: 6px;
            padding: 13px 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            cursor: pointer;
            outline: none;
            /* Bevel & Emboss (มิติขอบยุบ-นูน) */
            box-shadow: 
                inset 0 1.5px 2px rgba(255, 230, 150, 0.45),
                inset 0 -2.5px 6px rgba(0, 0, 0, 0.85),
                0 6px 16px rgba(0, 0, 0, 0.8),
                0 2px 4px rgba(0, 0, 0, 0.95);
            transition: all 0.26s cubic-bezier(0.165, 0.84, 0.44, 1);
            user-select: none;
            overflow: hidden;
        }

        /* Double Gilded Border (กรอบทองคู่) */
        .grimoire-btn::before {
            content: '';
            position: absolute;
            inset: 3.5px;
            border: 1px solid rgba(223, 162, 44, 0.55);
            border-radius: 4px;
            pointer-events: none;
            box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.6);
            transition: border-color 0.25s ease, box-shadow 0.25s ease;
            z-index: 2;
        }

        /* 1. Filigree Brackets at 4 Corners (ลายฉลุทองเหลืองโบราณ) */
        .btn-filigree {
            position: absolute;
            width: 14px;
            height: 14px;
            pointer-events: none;
            z-index: 4;
            opacity: 0.85;
            transition: opacity 0.25s ease, filter 0.25s ease;
        }
        .btn-filigree.top-left {
            top: 2px;
            left: 2px;
        }
        .btn-filigree.top-right {
            top: 2px;
            right: 2px;
            transform: scaleX(-1);
        }
        .btn-filigree.bottom-left {
            bottom: 2px;
            left: 2px;
            transform: scaleY(-1);
        }
        .btn-filigree.bottom-right {
            bottom: 2px;
            right: 2px;
            transform: scale(-1);
        }

        /* Button Hover & Active States */
        .grimoire-btn:hover {
            background: 
                radial-gradient(ellipse at 50% 15%, #7a0b16 0%, #480409 65%, #1e0204 100%),
                repeating-linear-gradient(45deg, rgba(0, 0, 0, 0.09) 0px, rgba(0, 0, 0, 0.09) 2px, transparent 2px, transparent 4px);
            border-color: #ffd875;
            transform: translateY(-2.5px);
            box-shadow: 
                inset 0 1.5px 3px rgba(255, 240, 180, 0.75),
                inset 0 -2px 6px rgba(0, 0, 0, 0.8),
                0 10px 22px rgba(0, 0, 0, 0.9),
                0 0 16px rgba(223, 162, 44, 0.35);
        }

        .grimoire-btn:hover::before {
            border-color: rgba(255, 216, 117, 0.85);
            box-shadow: inset 0 0 8px rgba(223, 162, 44, 0.3);
        }

        .grimoire-btn:hover .btn-filigree {
            opacity: 1;
            filter: drop-shadow(0 0 3px rgba(255, 216, 117, 0.8));
        }

        .grimoire-btn:active {
            transform: translateY(1px);
            box-shadow: 
                inset 0 2px 5px rgba(0, 0, 0, 0.9),
                inset 0 -1px 2px rgba(255, 230, 150, 0.3),
                0 3px 8px rgba(0, 0, 0, 0.9);
        }

        .grimoire-btn.full-span {
            grid-column: span 2;
        }

        /* 3. Roman Numeral Brass Seal (ตราสลักเลขโรมัน) */
        .roman-seal {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-width: 25px;
            height: 25px;
            padding: 0 4px;
            border-radius: 4px;
            background: linear-gradient(135deg, #3d050a 0%, #170103 100%);
            border: 1.5px solid #dfa22c;
            box-shadow: 
                inset 0 1px 2px rgba(255, 220, 130, 0.5),
                0 2px 5px rgba(0, 0, 0, 0.8);
            font-family: 'Cinzel', serif;
            font-size: 0.95rem;
            font-weight: 700;
            color: #ffd875;
            text-shadow: 0 1px 3px rgba(0, 0, 0, 0.9), 0 0 8px rgba(223, 162, 44, 0.5);
            flex-shrink: 0;
            letter-spacing: 0.5px;
            position: relative;
            z-index: 3;
            transition: all 0.25s ease;
        }

        .grimoire-btn:hover .roman-seal {
            border-color: #ffe699;
            box-shadow: inset 0 1px 2px rgba(255, 240, 160, 0.8), 0 0 10px rgba(223, 162, 44, 0.6);
            transform: scale(1.05);
        }

        /* 3. Button Content & Golden Flourish (ข้อความภาษาไทยและลวดลายเถาวัลย์เส้นบาง) */
        .btn-content {
            display: flex;
            flex-direction: column;
            align-items: center;
            position: relative;
            z-index: 3;
        }

        .btn-title {
            font-family: 'SOV Yoona', 'Samphan Condensed', serif;
            font-size: 1.35rem;
            font-weight: bold;
            color: #f7e4be;
            letter-spacing: 0.35px;
            text-shadow: 0 1px 3px rgba(0, 0, 0, 0.9);
            line-height: 1.3;
            transition: color 0.25s ease, text-shadow 0.25s ease;
        }

        .grimoire-btn:hover .btn-title {
            color: #ffffff;
            text-shadow: 0 1px 4px rgba(0, 0, 0, 0.9), 0 0 10px rgba(255, 220, 130, 0.5);
        }

        .btn-flourish {
            width: 75%;
            height: 1px;
            margin-top: 2px;
            background: linear-gradient(90deg, transparent 0%, rgba(223, 162, 44, 0.6) 50%, transparent 100%);
            opacity: 0.7;
            transition: width 0.25s ease, opacity 0.25s ease;
        }

        .grimoire-btn:hover .btn-flourish {
            width: 95%;
            opacity: 1;
            background: linear-gradient(90deg, transparent 0%, rgba(255, 216, 117, 0.9) 50%, transparent 100%);
        }
"""

# Replace old .grimoire-btn CSS block
old_grimoire_pattern = re.compile(
    r'\.spell-topics-grid\s*\{[^}]+\}\s*\.grimoire-btn\s*\{[^}]+\}\s*\.grimoire-btn:hover\s*\{[^}]+\}\s*\.grimoire-btn\.full-span\s*\{[^}]+\}',
    re.DOTALL
)

if old_grimoire_pattern.search(html):
    html = old_grimoire_pattern.sub(new_grimoire_css.strip(), html, count=1)
    print("[1] Replaced old .grimoire-btn CSS with enhanced plinth and button styling")
else:
    # Fallback: inject before </style>
    last_style = html.rfind('</style>')
    html = html[:last_style] + f'{new_grimoire_css}\n    ' + html[last_style:]
    print("[1b] Injected new_grimoire_css before </style>")

# 2. Update HTML markup for the grimoire buttons
new_plinth_html = """                    <!-- 4. แท่นรองแผงไม้โอ๊คโบราณพร้อมลายน้ำสิงโตกริฟฟินดอร์ (Aged Dark Oak Plinth & Lion Watermark) -->
                    <div class="grimoire-plinth-panel">
                        <!-- ลายน้ำสิงโตกริฟฟินดอร์จางๆ (~13% Opacity) -->
                        <div class="plinth-lion-watermark" aria-hidden="true"></div>

                        <!-- แถบคิ้วทองเหลืองสลักหัวข้อแท่น -->
                        <div class="plinth-header-bar">
                            <span class="plinth-header-line"></span>
                            <span class="plinth-header-text">✦ Gryffindor Grimoire Archive • บันทึกคัมภีร์เวทมนตร์ ✦</span>
                            <span class="plinth-header-line"></span>
                        </div>

                        <div class="spell-topics-grid">
                            <!-- บทที่ 1: ประวัติความเป็นมา -->
                            <button class="grimoire-btn" onclick="openScroll('history')" title="เปิดอ่านบทที่ 1: ประวัติความเป็นมา">
                                <svg class="btn-filigree top-left" viewBox="0 0 20 20"><path d="M2,2 L14,2 Q8,4 4,8 Q2,14 2,20 Z" fill="#dfa22c"/><circle cx="5" cy="5" r="1.5" fill="#ffe294"/></svg>
                                <svg class="btn-filigree top-right" viewBox="0 0 20 20"><path d="M2,2 L14,2 Q8,4 4,8 Q2,14 2,20 Z" fill="#dfa22c"/><circle cx="5" cy="5" r="1.5" fill="#ffe294"/></svg>
                                <svg class="btn-filigree bottom-left" viewBox="0 0 20 20"><path d="M2,2 L14,2 Q8,4 4,8 Q2,14 2,20 Z" fill="#dfa22c"/><circle cx="5" cy="5" r="1.5" fill="#ffe294"/></svg>
                                <svg class="btn-filigree bottom-right" viewBox="0 0 20 20"><path d="M2,2 L14,2 Q8,4 4,8 Q2,14 2,20 Z" fill="#dfa22c"/><circle cx="5" cy="5" r="1.5" fill="#ffe294"/></svg>
                                <span class="roman-seal">I</span>
                                <span class="btn-content">
                                    <span class="btn-title">ประวัติความเป็นมา</span>
                                    <span class="btn-flourish"></span>
                                </span>
                            </button>

                            <!-- บทที่ 2: สิ่งที่โปรดปราน -->
                            <button class="grimoire-btn" onclick="openScroll('likes')" title="เปิดอ่านบทที่ 2: สิ่งที่โปรดปราน">
                                <svg class="btn-filigree top-left" viewBox="0 0 20 20"><path d="M2,2 L14,2 Q8,4 4,8 Q2,14 2,20 Z" fill="#dfa22c"/><circle cx="5" cy="5" r="1.5" fill="#ffe294"/></svg>
                                <svg class="btn-filigree top-right" viewBox="0 0 20 20"><path d="M2,2 L14,2 Q8,4 4,8 Q2,14 2,20 Z" fill="#dfa22c"/><circle cx="5" cy="5" r="1.5" fill="#ffe294"/></svg>
                                <svg class="btn-filigree bottom-left" viewBox="0 0 20 20"><path d="M2,2 L14,2 Q8,4 4,8 Q2,14 2,20 Z" fill="#dfa22c"/><circle cx="5" cy="5" r="1.5" fill="#ffe294"/></svg>
                                <svg class="btn-filigree bottom-right" viewBox="0 0 20 20"><path d="M2,2 L14,2 Q8,4 4,8 Q2,14 2,20 Z" fill="#dfa22c"/><circle cx="5" cy="5" r="1.5" fill="#ffe294"/></svg>
                                <span class="roman-seal">II</span>
                                <span class="btn-content">
                                    <span class="btn-title">สิ่งที่โปรดปราน</span>
                                    <span class="btn-flourish"></span>
                                </span>
                            </button>

                            <!-- บทที่ 3: สิ่งที่ไม่พึงใจ -->
                            <button class="grimoire-btn" onclick="openScroll('dislikes')" title="เปิดอ่านบทที่ 3: สิ่งที่ไม่พึงใจ">
                                <svg class="btn-filigree top-left" viewBox="0 0 20 20"><path d="M2,2 L14,2 Q8,4 4,8 Q2,14 2,20 Z" fill="#dfa22c"/><circle cx="5" cy="5" r="1.5" fill="#ffe294"/></svg>
                                <svg class="btn-filigree top-right" viewBox="0 0 20 20"><path d="M2,2 L14,2 Q8,4 4,8 Q2,14 2,20 Z" fill="#dfa22c"/><circle cx="5" cy="5" r="1.5" fill="#ffe294"/></svg>
                                <svg class="btn-filigree bottom-left" viewBox="0 0 20 20"><path d="M2,2 L14,2 Q8,4 4,8 Q2,14 2,20 Z" fill="#dfa22c"/><circle cx="5" cy="5" r="1.5" fill="#ffe294"/></svg>
                                <svg class="btn-filigree bottom-right" viewBox="0 0 20 20"><path d="M2,2 L14,2 Q8,4 4,8 Q2,14 2,20 Z" fill="#dfa22c"/><circle cx="5" cy="5" r="1.5" fill="#ffe294"/></svg>
                                <span class="roman-seal">III</span>
                                <span class="btn-content">
                                    <span class="btn-title">สิ่งที่ไม่พึงใจ</span>
                                    <span class="btn-flourish"></span>
                                </span>
                            </button>

                            <!-- บทที่ 4: อุปกรณ์เวทมนตร์และทักษะพิเศษ (เต็ม 2 คอลัมน์) -->
                            <button class="grimoire-btn full-span" onclick="openScroll('magic')" title="เปิดอ่านบทที่ 4: อุปกรณ์เวทมนตร์และทักษะพิเศษ">
                                <svg class="btn-filigree top-left" viewBox="0 0 20 20"><path d="M2,2 L14,2 Q8,4 4,8 Q2,14 2,20 Z" fill="#dfa22c"/><circle cx="5" cy="5" r="1.5" fill="#ffe294"/></svg>
                                <svg class="btn-filigree top-right" viewBox="0 0 20 20"><path d="M2,2 L14,2 Q8,4 4,8 Q2,14 2,20 Z" fill="#dfa22c"/><circle cx="5" cy="5" r="1.5" fill="#ffe294"/></svg>
                                <svg class="btn-filigree bottom-left" viewBox="0 0 20 20"><path d="M2,2 L14,2 Q8,4 4,8 Q2,14 2,20 Z" fill="#dfa22c"/><circle cx="5" cy="5" r="1.5" fill="#ffe294"/></svg>
                                <svg class="btn-filigree bottom-right" viewBox="0 0 20 20"><path d="M2,2 L14,2 Q8,4 4,8 Q2,14 2,20 Z" fill="#dfa22c"/><circle cx="5" cy="5" r="1.5" fill="#ffe294"/></svg>
                                <span class="roman-seal">IV</span>
                                <span class="btn-content">
                                    <span class="btn-title">อุปกรณ์เวทมนตร์และทักษะพิเศษ</span>
                                    <span class="btn-flourish"></span>
                                </span>
                            </button>

                            <!-- บทที่ 5: บันทึกลับฮอกวอตส์ -->
                            <button class="grimoire-btn" onclick="openScroll('others')" title="เปิดอ่านบทที่ 5: บันทึกลับฮอกวอตส์">
                                <svg class="btn-filigree top-left" viewBox="0 0 20 20"><path d="M2,2 L14,2 Q8,4 4,8 Q2,14 2,20 Z" fill="#dfa22c"/><circle cx="5" cy="5" r="1.5" fill="#ffe294"/></svg>
                                <svg class="btn-filigree top-right" viewBox="0 0 20 20"><path d="M2,2 L14,2 Q8,4 4,8 Q2,14 2,20 Z" fill="#dfa22c"/><circle cx="5" cy="5" r="1.5" fill="#ffe294"/></svg>
                                <svg class="btn-filigree bottom-left" viewBox="0 0 20 20"><path d="M2,2 L14,2 Q8,4 4,8 Q2,14 2,20 Z" fill="#dfa22c"/><circle cx="5" cy="5" r="1.5" fill="#ffe294"/></svg>
                                <svg class="btn-filigree bottom-right" viewBox="0 0 20 20"><path d="M2,2 L14,2 Q8,4 4,8 Q2,14 2,20 Z" fill="#dfa22c"/><circle cx="5" cy="5" r="1.5" fill="#ffe294"/></svg>
                                <span class="roman-seal">V</span>
                                <span class="btn-content">
                                    <span class="btn-title">บันทึกลับฮอกวอตส์</span>
                                    <span class="btn-flourish"></span>
                                </span>
                            </button>
                        </div>
                    </div>"""

old_grid_pattern = re.compile(
    r'<div class="spell-topics-grid">.*?</div>',
    re.DOTALL
)

assert old_grid_pattern.search(html), "ERROR: <div class=\"spell-topics-grid\"> not found"
html = old_grid_pattern.sub(new_plinth_html, html, count=1)
print("[2] Replaced .spell-topics-grid markup with grimoire-plinth-panel and enhanced buttons")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: index.html updated successfully with all 4 grimoire button enhancements!")
