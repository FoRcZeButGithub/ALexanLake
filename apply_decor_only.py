# -*- coding: utf-8 -*-
"""
Apply purely decorative Gryffindor Scarf & House Atmosphere to the Information Tab in index.html.
Strictly:
- NO extra buttons or features added (preserves the exact original 5 grimoire buttons and stats card).
- NO emojis or stickers.
- Authentic Gryffindor Scarf weave ribbon accent.
- Authentic Gryffindor still life photo (images/gryffindor-relics.jpg) in an antique Hogwarts picture frame.
- Clean typography for Thai and English headings.
"""

import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read current index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Clean typography for .stats-header-title so Thai text isn't corrupted
html = re.sub(
    r'\.stats-header-title\s*\{[^}]*font-family:[^;]+;',
    """.stats-header-title {
            font-family: 'Cinzel', 'SOV Yoona', serif;""",
    html,
    count=1
)

# 2. Pure decorative Gryffindor Scarf and Relics CSS
decor_css = """
        /* ==========================================================================
           GRYFFINDOR SCARF & RELICS PURE DECORATION (INFORMATION TAB)
           100% Atmospheric Hogwarts aesthetics without extra buttons or emojis
           ========================================================================== */

        /* Decorative Scarf Trim Ribbon under Information Title */
        .gryffindor-scarf-ribbon {
            position: relative;
            height: 12px;
            width: 100%;
            margin-top: -12px;
            margin-bottom: 24px;
            border-radius: 4px;
            background: repeating-linear-gradient(
                -45deg,
                #500308 0px,
                #500308 14px,
                #1e0204 14px,
                #1e0204 16px,
                #b57f18 16px,
                #dca22e 24px,
                #b57f18 24px,
                #b57f18 26px,
                #500308 26px,
                #500308 28px,
                #b57f18 28px,
                #dca22e 36px,
                #b57f18 36px,
                #b57f18 38px,
                #500308 38px,
                #760b13 52px
            );
            border: 1px solid rgba(220, 162, 46, 0.45);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.8), inset 0 0 8px rgba(0, 0, 0, 0.6);
            display: flex;
            align-items: center;
            justify-content: space-between;
            overflow: hidden;
            pointer-events: none;
        }

        .gryffindor-scarf-ribbon::before,
        .gryffindor-scarf-ribbon::after {
            content: '';
            width: 16px;
            height: 100%;
            background: repeating-linear-gradient(
                90deg,
                #dca22e 0px,
                #dca22e 2px,
                transparent 2px,
                transparent 4px
            );
            opacity: 0.85;
        }

        /* Adjust info-dual-column for balanced layout */
        .info-dual-column {
            display: grid;
            grid-template-columns: 360px 1fr !important;
            gap: 28px !important;
            align-items: start;
        }

        /* Gryffindor Relics Portrait Frame */
        .relics-portrait-frame {
            position: relative;
            height: 500px;
            border-radius: 10px;
            border: 8px solid #240306;
            outline: 2px solid var(--gold-antique);
            background: #110103;
            box-shadow: 
                0 18px 45px rgba(0, 0, 0, 0.95),
                0 0 25px rgba(212, 163, 55, 0.25),
                inset 0 0 30px rgba(0, 0, 0, 0.8);
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            transition: transform 0.3s ease, box-shadow 0.3s ease, outline-color 0.3s ease;
        }

        .relics-portrait-frame:hover {
            transform: translateY(-4px);
            box-shadow: 
                0 22px 55px rgba(0, 0, 0, 0.98),
                0 0 35px rgba(243, 194, 82, 0.45);
            outline-color: #ffd875;
        }

        /* The Relics Photo */
        .relics-frame-img {
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center 25%;
            display: block;
            filter: contrast(1.08) brightness(0.98) saturate(1.05);
            transition: transform 0.6s cubic-bezier(0.165, 0.84, 0.44, 1), filter 0.5s ease;
        }

        .relics-portrait-frame:hover .relics-frame-img {
            transform: scale(1.035);
            filter: contrast(1.12) brightness(1.04) saturate(1.1);
        }

        /* Atmospheric Vignette & Hearth Gradient */
        .relics-frame-vignette {
            position: absolute;
            inset: 0;
            background: 
                radial-gradient(circle at 50% 35%, transparent 40%, rgba(20, 2, 4, 0.4) 75%, rgba(10, 1, 2, 0.85) 100%),
                linear-gradient(180deg, rgba(15, 2, 4, 0.2) 0%, transparent 35%, rgba(15, 2, 4, 0.75) 65%, rgba(10, 1, 2, 0.96) 100%);
            pointer-events: none;
            z-index: 2;
        }

        /* Floating Corner Filigrees (Pure SVG, Gold Metallic) */
        .frame-filigree {
            position: absolute;
            width: 26px;
            height: 26px;
            pointer-events: none;
            z-index: 5;
            opacity: 0.85;
        }
        .frame-filigree.top-left { top: 6px; left: 6px; }
        .frame-filigree.top-right { top: 6px; right: 6px; transform: scaleX(-1); }

        /* Top Gryffindor Crest Badge */
        .relics-crest-badge {
            position: absolute;
            top: 12px;
            right: 12px;
            z-index: 6;
            background: rgba(25, 2, 6, 0.92);
            border: 1.5px solid #dfa22c;
            border-radius: 9999px;
            padding: 4px 12px;
            display: flex;
            align-items: center;
            gap: 6px;
            box-shadow: 0 4px 14px rgba(0, 0, 0, 0.85), 0 0 10px rgba(223, 162, 44, 0.3);
            pointer-events: none;
        }
        .relics-crest-badge svg {
            width: 14px;
            height: 14px;
            fill: #dfa22c;
        }
        .relics-crest-badge span {
            font-family: 'Cinzel', serif;
            font-size: 0.75rem;
            font-weight: 700;
            color: #ffd875;
            letter-spacing: 1.5px;
            text-transform: uppercase;
        }

        /* Bottom Lore Plaque */
        .relics-frame-plaque {
            position: relative;
            z-index: 5;
            padding: 16px 18px;
            text-align: center;
            background: linear-gradient(180deg, transparent 0%, rgba(18, 2, 4, 0.85) 30%, rgba(10, 1, 2, 0.98) 100%);
        }

        .relics-plaque-title {
            font-family: 'Cinzel', serif;
            font-size: 1.15rem;
            font-weight: 700;
            color: #ffd875;
            letter-spacing: 2px;
            text-transform: uppercase;
            text-shadow: 0 2px 8px rgba(0, 0, 0, 0.9), 0 0 12px rgba(223, 162, 44, 0.5);
        }

        .relics-plaque-desc {
            font-family: 'SOV Yoona', serif;
            font-size: 1.18rem;
            color: #ebd1a2;
            margin-top: 6px;
            line-height: 1.6;
            letter-spacing: 0.2px;
        }

        .relics-plaque-quote {
            font-family: 'SOV Yoona', serif;
            font-size: 1.05rem;
            color: #c99330;
            margin-top: 4px;
            font-style: italic;
        }

        @media (max-width: 900px) {
            .info-dual-column {
                grid-template-columns: 1fr !important;
            }
            .relics-portrait-frame {
                height: 440px;
                max-width: 400px;
                margin: 0 auto;
            }
        }
"""

last_style = html.rfind('</style>')
assert last_style != -1
html = html[:last_style] + f'{decor_css}\n    ' + html[last_style:]
print("[1] Injected clean decorative CSS")

# 3. New HTML markup for #tab-information (NO extra buttons, NO emojis)
new_tab_info = """        <!-- ================= TAB 2: INFORMATION ================= -->
        <section id="tab-information" class="tab-content">
            <h2 class="section-ribbon-title">Information / ข้อมูลส่วนตัว</h2>
            
            <!-- ผ้าพันคอกริฟฟินดอร์ประดับตกแต่งส่วนหัว (Decorative Gryffindor Scarf Trim) -->
            <div class="gryffindor-scarf-ribbon" aria-hidden="true"></div>

            <div class="info-dual-column">
                
                <!-- 🦁 ฝั่งซ้าย: ภาพของสะสมบ้านกริฟฟินดอร์และผ้าพันคอในกรอบวินเทจ (Pure Decorative Relics Frame) -->
                <div class="relics-portrait-frame">
                    <img src="images/gryffindor-relics.jpg" alt="Gryffindor Scarf, Godric's Sword, Lion Wand, Tie and Hogwarts Trunk" class="relics-frame-img" />
                    <div class="relics-frame-vignette" aria-hidden="true"></div>

                    <!-- มุมกรอบทองเหลือง (Corner Filigree) -->
                    <svg class="frame-filigree top-left" viewBox="0 0 50 50"><path d="M5,5 L45,5 Q25,15 15,25 Q5,35 5,45 Z" fill="#dfa22c"/></svg>
                    <svg class="frame-filigree top-right" viewBox="0 0 50 50"><path d="M5,5 L45,5 Q25,15 15,25 Q5,35 5,45 Z" fill="#dfa22c"/></svg>

                    <!-- ตรากริฟฟินดอร์โลหะทอง (Gryffindor Relics Crest Badge) -->
                    <div class="relics-crest-badge" aria-hidden="true">
                        <svg viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                        <span>Gryffindor Heritage</span>
                    </div>

                    <!-- ป้ายข้อความด้านล่างภาพ (Lore Plaque) -->
                    <div class="relics-frame-plaque">
                        <div class="relics-plaque-title">Gryffindor Relics & Scarf</div>
                        <div class="relics-plaque-desc">
                            "ความเร็วน่ะไม่ใช่แค่เรื่องของการบิน<br />แต่มันคือการตัดสินใจในเสี้ยววินาที"
                        </div>
                        <div class="relics-plaque-quote">— Alex Lake</div>
                    </div>
                </div>

                <!-- 📜 ฝั่งขวา: สถิติและปุ่มหัวข้อเดิม (Keep exact original buttons & stats, NO extra buttons!) -->
                <div>
                    <!-- สถิติและค่าพลังตัวละคร (Character Stats Bar) -->
                    <div class="character-stats-card">
                        <div class="stats-header-title">
                            <img src="images/hogwarts-logo.png" alt="Hogwarts"
                                style="width: 24px; height: 24px; object-fit: contain; margin-right: 8px;" />
                            <span>อัตราความสามารถและสถิติเวทมนตร์ (Character Attributes)</span>
                        </div>
                        <div class="stat-row">
                            <div class="stat-label-bar">
                                <span>◆ ความกล้าหาญและความมุทะลุ (Courage & Audacity)</span>
                                <span>95%</span>
                            </div>
                            <div class="stat-track">
                                <div class="stat-fill" data-percent="95"></div>
                            </div>
                        </div>
                        <div class="stat-row">
                            <div class="stat-label-bar">
                                <span>◆ ทักษะการบินและการไล่หวดบลัดเจอร์ (Quidditch Prowess)</span>
                                <span>97%</span>
                            </div>
                            <div class="stat-track">
                                <div class="stat-fill" data-percent="97"></div>
                            </div>
                        </div>
                        <div class="stat-row">
                            <div class="stat-label-bar">
                                <span>◆ การทดลองแกล้งคนและระเบิดควัน (Pranks & Fireworks)</span>
                                <span>92%</span>
                            </div>
                            <div class="stat-track">
                                <div class="stat-fill" data-percent="92"></div>
                            </div>
                        </div>
                        <div class="stat-row">
                            <div class="stat-label-bar">
                                <span>◆ การป้องกันตัวจากศาสตร์มืด (Dark Arts Defense)</span>
                                <span>86%</span>
                            </div>
                            <div class="stat-track">
                                <div class="stat-fill" data-percent="86"></div>
                            </div>
                        </div>
                        <div class="stat-row">
                            <div class="stat-label-bar">
                                <span>◆ กำแพงหัวใจและการจีบ (Romance Defense)</span>
                                <span>99%</span>
                            </div>
                            <div class="stat-track">
                                <div class="stat-fill" data-percent="99"></div>
                            </div>
                        </div>
                    </div>

                    <div class="spell-topics-grid">
                        <button class="grimoire-btn" onclick="openScroll('history')">I. ประวัติความเป็นมา</button>
                        <button class="grimoire-btn" onclick="openScroll('likes')">II. สิ่งที่โปรดปราน</button>
                        <button class="grimoire-btn" onclick="openScroll('dislikes')">III. สิ่งที่ไม่พึงใจ</button>
                        <button class="grimoire-btn full-span" onclick="openScroll('magic')">IV.
                            อุปกรณ์เวทมนตร์และทักษะพิเศษ</button>
                        <button class="grimoire-btn" onclick="openScroll('others')">V. บันทึกลับฮอกวอตส์</button>
                    </div>

                    <!-- แถบเสียงพากย์ไดอะล็อกเวทมนตร์ -->
                    <div class="magic-voice-banner">
                        <button class="wand-play-trigger" id="audioToggle" onclick="toggleSparksAudio()"
                            title="ร่ายคาถาฟังเสียง">
                            <svg id="playIconSvg" viewBox="0 0 24 24">
                                <polygon points="5 3 19 12 5 21 5 3"></polygon>
                            </svg>
                        </button>
                        <div class="soundwave-sparks" id="sparkWave"></div>
                        <span class="voice-label-tag">Enchanted Spell Synthesizer</span>
                    </div>
                </div>
            </div>
        </section>"""

tab_info_pattern = re.compile(r'<section id="tab-information".*?</section>', re.DOTALL)
assert tab_info_pattern.search(html), "ERROR: #tab-information not found"
html = tab_info_pattern.sub(new_tab_info, html, count=1)
print("[2] Injected pure decorative #tab-information markup")

# 4. Enhance the existing "magic" entry in scrollArchive with scarf & relics mention (natural enrichment, no extra buttons)
magic_old = """            magic: {
                title: "อุปกรณ์เวทมนตร์และทักษะพิเศษ",
                html: `• <strong>ไม้กวาดไฟเยอร์โบลด์ (Firebolt):</strong> ไม้กวาดความเร็วสูงระดับโลกที่เขารักและทะนุถนอมมากที่สุด<br>
        • <strong>ความชำนาญคาถาป้องกันตัว:</strong> วิชาป้องกันตัวจากศาสตร์มืดและการตอบสนองต่อภัยคุกคามในระยะประชิดที่ฉับไวเหนือกว่ามาตรฐานนักเรียนทั่วไป<br>
        • <strong>สัญชาตญาณสัตว์ป่า:</strong> พัฒนาประสาทการได้ยินและสัญชาตญาณรอบตัวขึ้นมาทดแทนดวงตาข้างซ้ายที่สูญเสียไป`
            },"""

magic_new = """            magic: {
                title: "อุปกรณ์เวทมนตร์และทักษะพิเศษ",
                html: `• <strong>ผ้าพันคอไหมพรมและเนคไทกริฟฟินดอร์:</strong> ผ้าพันคอสีเลือดหมูสลับทองที่ถักทอหนานุ่ม ให้ความอบอุ่นยามฝึกบินโต้ลมหนาวบนหอคอยสูง พร้อมตราประจำบ้านที่สวมใส่อย่างภาคภูมิใจ<br>
        • <strong>ไม้กวาดไฟเยอร์โบลด์ (Firebolt):</strong> ไม้กวาดความเร็วสูงระดับโลกที่เขารักและทะนุถนอมมากที่สุด<br>
        • <strong>ไม้กายสิทธิ์สลักเศียรสิงโต:</strong> แกนกลางผสมขนแผงคอสิงโตและเอ็นหัวใจมังกร ตอบสนองต่อคาถาป้องกันตัวจากศาสตร์มืดได้อย่างหนักแน่นเฉียบพลัน<br>
        • <strong>ความชำนาญคาถาป้องกันตัว:</strong> พ่อทูนหัวฝึกฝนการตอบสนองต่อภัยคุกคามในระยะประชิดที่ฉับไวเหนือกว่ามาตรฐานนักเรียนทั่วไป<br>
        • <strong>สัญชาตญาณสัตว์ป่า:</strong> พัฒนาประสาทการได้ยินและสัญชาตญาณรอบตัวขึ้นมาทดแทนดวงตาข้างซ้ายที่สูญเสียไป`
            },"""

if magic_old in html:
    html = html.replace(magic_old, magic_new, 1)
    print("[3] Updated existing magic scroll entry")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: index.html updated with pure decorative Gryffindor Scarf & Relics!")
