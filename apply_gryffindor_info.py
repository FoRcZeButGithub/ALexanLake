# -*- coding: utf-8 -*-
"""
Apply authentic Gryffindor Scarf and Relics atmosphere to the Information Tab in index.html.
Uses images/gryffindor-relics.jpg (provided by the user).
"""

import re
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ==============================================================================
# 1. NEW CSS FOR GRYFFINDOR INFORMATION TAB ATMOSPHERE
# ==============================================================================
relics_css = """
        /* ==========================================================================
           GRYFFINDOR SCARF & RELICS ATMOSPHERE (INFORMATION TAB)
           Authentic House Artifacts, Knitted Scarf Accents, and Common Room Hearth
           ========================================================================== */

        /* Scarf Accent Drape Header */
        .gryffindor-scarf-drape-header {
            position: relative;
            margin-bottom: 26px;
            padding: 14px 24px;
            background: 
                repeating-linear-gradient(
                    -45deg,
                    #52040a 0px,
                    #52040a 22px,
                    #1e0204 22px,
                    #1e0204 24px,
                    #b8821a 24px,
                    #dca22e 34px,
                    #b8821a 34px,
                    #b8821a 36px,
                    #52040a 36px,
                    #52040a 40px,
                    #b8821a 40px,
                    #dca22e 50px,
                    #b8821a 50px,
                    #b8821a 52px,
                    #52040a 52px,
                    #760b13 74px
                );
            border: 2px solid var(--gold-antique);
            border-radius: 12px;
            box-shadow: 
                0 10px 30px rgba(0, 0, 0, 0.9),
                inset 0 0 25px rgba(0, 0, 0, 0.8),
                0 0 20px rgba(220, 162, 46, 0.25);
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 16px;
            overflow: hidden;
        }

        .gryffindor-scarf-drape-header::before {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(90deg, rgba(20,2,4,0.7) 0%, rgba(20,2,4,0.3) 50%, rgba(20,2,4,0.7) 100%);
            pointer-events: none;
        }

        /* Scarf Fringes at the ends */
        .scarf-tassel-strip {
            display: flex;
            gap: 4px;
            position: relative;
            z-index: 2;
        }
        .scarf-tassel {
            width: 5px;
            height: 24px;
            background: linear-gradient(180deg, #b8821a 0%, #52040a 80%, #200204 100%);
            border-radius: 0 0 3px 3px;
            box-shadow: 1px 2px 4px rgba(0,0,0,0.8);
        }
        .scarf-tassel:nth-child(even) {
            background: linear-gradient(180deg, #dca22e 0%, #760b13 80%, #300306 100%);
            height: 28px;
        }

        .scarf-header-content {
            position: relative;
            z-index: 2;
            display: flex;
            align-items: center;
            gap: 14px;
        }

        .scarf-crest-mini {
            width: 44px;
            height: 44px;
            border-radius: 50%;
            background: radial-gradient(circle, #7a0c16 0%, #2a0307 100%);
            border: 2px solid #dfa22c;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.9), 0 0 10px rgba(223,162,44,0.5);
            flex-shrink: 0;
        }
        .scarf-crest-mini svg {
            width: 24px;
            height: 24px;
            fill: #ffd875;
        }

        .scarf-header-titles {
            display: flex;
            flex-direction: column;
        }

        .scarf-header-title-main {
            font-family: 'Sarun HarryPotter', 'Harry Potter', cursive;
            font-size: 1.85rem;
            color: #ffd875;
            text-shadow: 0 2px 8px rgba(0,0,0,0.9), 0 0 15px rgba(223,162,44,0.6);
            letter-spacing: 1px;
            line-height: 1.15;
        }

        .scarf-header-title-sub {
            font-family: 'SOV Yoona', serif;
            font-size: 1.25rem;
            color: #f7e2b8;
            letter-spacing: 0.3px;
        }

        .scarf-header-badge {
            position: relative;
            z-index: 2;
            background: rgba(30, 4, 8, 0.88);
            border: 1.5px solid #dfa22c;
            border-radius: 9999px;
            padding: 6px 18px;
            font-family: 'SOV Yoona', serif;
            font-size: 1.15rem;
            color: #ffd875;
            display: flex;
            align-items: center;
            gap: 8px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.8);
            cursor: pointer;
            transition: all 0.25s ease;
        }
        .scarf-header-badge:hover {
            background: rgba(80, 10, 20, 0.95);
            border-color: #ffe699;
            color: #ffffff;
            transform: scale(1.04);
            box-shadow: 0 6px 20px rgba(223,162,44,0.5);
        }

        /* Information Dual Column */
        .info-dual-column {
            display: grid;
            grid-template-columns: 400px 1fr !important;
            gap: 32px !important;
            align-items: start;
        }

        /* Left Column: Gryffindor Relics Reliquary Box */
        .gryffindor-relics-box {
            position: relative;
            background: #140204;
            border: 2px solid var(--gold-antique);
            border-radius: 14px;
            padding: 12px;
            box-shadow: 
                0 18px 45px rgba(0, 0, 0, 0.95),
                0 0 25px rgba(212, 163, 55, 0.3),
                inset 0 0 35px rgba(0, 0, 0, 0.8);
            display: flex;
            flex-direction: column;
            gap: 12px;
            transition: box-shadow 0.35s ease, border-color 0.35s ease;
        }
        .gryffindor-relics-box:hover {
            border-color: #ffd875;
            box-shadow: 
                0 22px 55px rgba(0, 0, 0, 0.98),
                0 0 35px rgba(243, 194, 82, 0.5),
                inset 0 0 30px rgba(0, 0, 0, 0.7);
        }

        /* Corner filigree ornaments */
        .relic-filigree {
            position: absolute;
            width: 32px;
            height: 32px;
            pointer-events: none;
            z-index: 10;
        }
        .relic-filigree.top-left { top: 6px; left: 6px; }
        .relic-filigree.top-right { top: 6px; right: 6px; transform: scaleX(-1); }
        .relic-filigree.bottom-left { bottom: 6px; left: 6px; transform: scaleY(-1); }
        .relic-filigree.bottom-right { bottom: 6px; right: 6px; transform: scale(-1); }

        /* The Relics Stage with user photo */
        .relics-stage-wrapper {
            position: relative;
            border-radius: 10px;
            overflow: hidden;
            border: 1px solid rgba(223, 162, 44, 0.4);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.9);
            background: #090102;
            cursor: pointer;
        }

        .relics-photo-img {
            width: 100%;
            height: 480px;
            object-fit: cover;
            object-position: center 30%;
            display: block;
            filter: contrast(1.08) brightness(1.02) saturate(1.06);
            transition: transform 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), filter 0.4s ease;
        }
        .relics-stage-wrapper:hover .relics-photo-img {
            transform: scale(1.035);
            filter: contrast(1.12) brightness(1.06) saturate(1.1);
        }

        /* Ambient Hearth Vignette */
        .relics-stage-vignette {
            position: absolute;
            inset: 0;
            background: 
                radial-gradient(circle at 50% 40%, transparent 45%, rgba(18, 2, 4, 0.5) 80%, rgba(10, 1, 2, 0.88) 100%),
                linear-gradient(180deg, rgba(0,0,0,0.3) 0%, transparent 20%, transparent 75%, rgba(10,1,2,0.92) 100%);
            pointer-events: none;
            z-index: 2;
        }

        /* Interactive Hotspots / Relic Pins */
        .relic-pin {
            position: absolute;
            z-index: 6;
            cursor: pointer;
            transform: translate(-50%, -50%);
            transition: transform 0.25s ease;
        }

        .relic-pin-beacon {
            width: 32px;
            height: 32px;
            border-radius: 50%;
            background: radial-gradient(circle, #dfa22c 0%, #7c0b14 70%, #200204 100%);
            border: 2px solid #ffd875;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 
                0 0 14px rgba(223, 162, 44, 0.85),
                0 4px 10px rgba(0, 0, 0, 0.9);
            font-size: 15px;
            color: #ffffff;
            transition: all 0.25s ease;
            position: relative;
        }

        .relic-pin-ripple {
            position: absolute;
            inset: -6px;
            border-radius: 50%;
            border: 1.5px solid rgba(243, 194, 82, 0.65);
            animation: relicPulse 2.2s infinite ease-out;
            pointer-events: none;
        }

        @keyframes relicPulse {
            0% {
                transform: scale(0.85);
                opacity: 0.9;
            }
            70% {
                transform: scale(1.6);
                opacity: 0;
            }
            100% {
                transform: scale(1.6);
                opacity: 0;
            }
        }

        .relic-pin:hover {
            transform: translate(-50%, -50%) scale(1.18);
            z-index: 20;
        }
        .relic-pin:hover .relic-pin-beacon {
            background: radial-gradient(circle, #ffd875 0%, #aa101c 70%, #300306 100%);
            border-color: #ffffff;
            box-shadow: 0 0 22px rgba(255, 216, 117, 1), 0 6px 14px rgba(0,0,0,0.95);
        }

        /* Tooltip on Relic Pin */
        .relic-tooltip {
            position: absolute;
            bottom: calc(100% + 10px);
            left: 50%;
            transform: translateX(-50%) translateY(6px);
            background: rgba(22, 2, 5, 0.96);
            border: 1.5px solid #dfa22c;
            border-radius: 8px;
            padding: 8px 14px;
            min-width: 170px;
            max-width: 220px;
            text-align: center;
            box-shadow: 0 8px 24px rgba(0,0,0,0.95), 0 0 16px rgba(223,162,44,0.4);
            pointer-events: none;
            opacity: 0;
            visibility: hidden;
            transition: all 0.25s ease;
            z-index: 25;
        }
        .relic-tooltip::after {
            content: '';
            position: absolute;
            top: 100%;
            left: 50%;
            transform: translateX(-50%);
            border: 6px solid transparent;
            border-top-color: #dfa22c;
        }
        .relic-pin:hover .relic-tooltip {
            opacity: 1;
            visibility: visible;
            transform: translateX(-50%) translateY(0);
        }

        .relic-tooltip-title {
            font-family: 'Sarun HarryPotter', 'Harry Potter', cursive;
            font-size: 1.25rem;
            color: #ffd875;
            line-height: 1.2;
            margin-bottom: 3px;
        }
        .relic-tooltip-desc {
            font-family: 'SOV Yoona', serif;
            font-size: 1.05rem;
            color: #f0dbb0;
            line-height: 1.4;
        }
        .relic-tooltip-hint {
            font-family: 'SOV Yoona', serif;
            font-size: 0.95rem;
            color: #dfa22c;
            margin-top: 4px;
        }

        /* Plaque at the bottom of the relics box */
        .relics-brass-plaque {
            background: linear-gradient(135deg, #240306 0%, #170103 100%);
            border: 1.5px solid rgba(223, 162, 44, 0.45);
            border-radius: 8px;
            padding: 12px 14px;
            text-align: center;
            box-shadow: inset 0 0 15px rgba(0,0,0,0.8);
            position: relative;
        }

        .plaque-latin {
            font-family: 'Sarun HarryPotter', 'Harry Potter', cursive;
            font-size: 1.35rem;
            color: #ffd875;
            letter-spacing: 1.5px;
            text-shadow: 0 0 10px rgba(223,162,44,0.4);
        }

        .plaque-thai {
            font-family: 'SOV Yoona', serif;
            font-size: 1.2rem;
            color: #ebd1a2;
            margin-top: 2px;
            letter-spacing: 0.2px;
        }

        .plaque-inspect-btn {
            margin-top: 10px;
            width: 100%;
            background: linear-gradient(180deg, #5c070e 0%, #2f0205 100%);
            color: #fff2cc;
            border: 1.5px solid var(--gold-antique);
            border-radius: 6px;
            padding: 8px 12px;
            font-family: 'SOV Yoona', serif;
            font-weight: bold;
            font-size: 1.2rem;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(0,0,0,0.7);
            transition: all 0.22s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }
        .plaque-inspect-btn:hover {
            background: linear-gradient(180deg, #7c0b14 0%, #440408 100%);
            border-color: #ffd875;
            color: #ffffff;
            transform: translateY(-2px);
            box-shadow: 0 6px 18px rgba(223,162,44,0.45);
        }

        /* Right Column: Relic Quick Chips Strip */
        .relic-chips-container {
            margin-bottom: 18px;
            background: rgba(20, 2, 4, 0.85);
            border: 1.5px solid rgba(223, 162, 44, 0.35);
            border-radius: 10px;
            padding: 10px 14px;
            box-shadow: 0 6px 18px rgba(0,0,0,0.7);
        }

        .relic-chips-title {
            font-family: 'SOV Yoona', serif;
            font-size: 1.2rem;
            color: #dfa22c;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 8px;
            font-weight: bold;
        }

        .relic-chips-row {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }

        .relic-chip {
            background: linear-gradient(180deg, #380509 0%, #1e0204 100%);
            border: 1px solid rgba(223, 162, 44, 0.45);
            border-radius: 9999px;
            padding: 6px 14px;
            font-family: 'SOV Yoona', serif;
            font-size: 1.15rem;
            color: #f7e2b8;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
            box-shadow: 0 3px 8px rgba(0,0,0,0.6);
            transition: all 0.22s ease;
            user-select: none;
        }
        .relic-chip:hover {
            background: linear-gradient(180deg, #610912 0%, #300306 100%);
            border-color: #ffd875;
            color: #ffffff;
            transform: translateY(-2px);
            box-shadow: 0 5px 14px rgba(223,162,44,0.4);
        }
        .relic-chip .chip-icon {
            font-size: 14px;
        }

        @media (max-width: 950px) {
            .info-dual-column {
                grid-template-columns: 1fr !important;
            }
            .relics-photo-img {
                height: 420px;
            }
        }
"""

# Inject CSS before the last </style>
last_style = html.rfind('</style>')
if last_style != -1:
    html = html[:last_style] + f'{relics_css}\n    ' + html[last_style:]
    print("[1] Injected Gryffindor Relics CSS before </style>")
else:
    print("ERROR: </style> not found")

# ==============================================================================
# 2. NEW HTML MARKUP FOR #tab-information
# ==============================================================================
new_tab_info_html = """        <!-- ================= TAB 2: INFORMATION (Gryffindor Scarf & House Relics Atmosphere) ================= -->
        <section id="tab-information" class="tab-content">
            
            <!-- 🧣 แถบผ้าพันคอกริฟฟินดอร์ประดับส่วนหัว (Gryffindor Scarf Drape Banner) -->
            <div class="gryffindor-scarf-drape-header">
                <div class="scarf-tassel-strip" aria-hidden="true">
                    <span class="scarf-tassel"></span>
                    <span class="scarf-tassel"></span>
                    <span class="scarf-tassel"></span>
                    <span class="scarf-tassel"></span>
                </div>

                <div class="scarf-header-content">
                    <div class="scarf-crest-mini" aria-hidden="true">
                        <svg viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                    </div>
                    <div class="scarf-header-titles">
                        <span class="scarf-header-title-main">Gryffindor Tower Archives</span>
                        <span class="scarf-header-title-sub">ข้อมูลส่วนตัวและของวิเศษประจำหอพักบ้านกริฟฟินดอร์</span>
                    </div>
                </div>

                <button class="scarf-header-badge" onclick="inspectRelic('scarf')" title="คลิกอ่านประวัติผ้าพันคอกริฟฟินดอร์">
                    <span>🧣 ผ้าพันคอไหมพรมกริฟฟินดอร์</span>
                    <span>✦</span>
                </button>

                <div class="scarf-tassel-strip" aria-hidden="true">
                    <span class="scarf-tassel"></span>
                    <span class="scarf-tassel"></span>
                    <span class="scarf-tassel"></span>
                    <span class="scarf-tassel"></span>
                </div>
            </div>

            <div class="info-dual-column">
                
                <!-- 🦁 ฝั่งซ้าย: ตู้โบราณวัตถุและของสะสมบ้านกริฟฟินดอร์ (Gryffindor Reliquary Showcase) -->
                <div class="gryffindor-relics-box">
                    <!-- Corner Filigree Ornaments -->
                    <svg class="relic-filigree top-left" viewBox="0 0 50 50"><path d="M5,5 L45,5 Q25,15 15,25 Q5,35 5,45 Z" fill="#dfa22c"/></svg>
                    <svg class="relic-filigree top-right" viewBox="0 0 50 50"><path d="M5,5 L45,5 Q25,15 15,25 Q5,35 5,45 Z" fill="#dfa22c"/></svg>
                    <svg class="relic-filigree bottom-left" viewBox="0 0 50 50"><path d="M5,5 L45,5 Q25,15 15,25 Q5,35 5,45 Z" fill="#dfa22c"/></svg>
                    <svg class="relic-filigree bottom-right" viewBox="0 0 50 50"><path d="M5,5 L45,5 Q25,15 15,25 Q5,35 5,45 Z" fill="#dfa22c"/></svg>

                    <!-- แท่นจัดแสดงภาพของสะสมจริง (Interactive Relics Stage) -->
                    <div class="relics-stage-wrapper" id="relicsStage" onclick="inspectRelic('relics_all')" title="คลิกดูรายละเอียดของสะสมทั้งหมด">
                        <img src="images/gryffindor-relics.jpg" alt="Gryffindor House Relics - Scarf, Godric's Sword, Lion Wand, Tie & Hogwarts Trunk" class="relics-photo-img" />
                        
                        <!-- เงาวิกเนตต์บรรยากาศแสงไฟเตาผิง (Hearth Vignette) -->
                        <div class="relics-stage-vignette" aria-hidden="true"></div>

                        <!-- 📍 หมุด Interactive 1: ผ้าพันคอกริฟฟินดอร์ (Gryffindor Scarf) -->
                        <div class="relic-pin" style="top: 38%; left: 16%;" onclick="event.stopPropagation(); inspectRelic('scarf');" role="button" tabindex="0" aria-label="ดูข้อมูลผ้าพันคอกริฟฟินดอร์">
                            <div class="relic-pin-beacon">
                                <span>🧣</span>
                                <div class="relic-pin-ripple"></div>
                            </div>
                            <div class="relic-tooltip">
                                <div class="relic-tooltip-title">Gryffindor Scarf</div>
                                <div class="relic-tooltip-desc">ผ้าพันคอไหมพรมสีแดงเลือดหมูสลับทอง ปักตราอาร์มสิงโตกริฟฟินดอร์</div>
                                <div class="relic-tooltip-hint">✦ คลิกเพื่ออ่านประวัติ</div>
                            </div>
                        </div>

                        <!-- 📍 หมุด Interactive 2: ดาบของก็อดดริก กริฟฟินดอร์ (Godric's Sword) -->
                        <div class="relic-pin" style="bottom: 12%; left: 45%;" onclick="event.stopPropagation(); inspectRelic('sword');" role="button" tabindex="0" aria-label="ดูข้อมูลดาบก็อดดริก กริฟฟินดอร์">
                            <div class="relic-pin-beacon">
                                <span>⚔️</span>
                                <div class="relic-pin-ripple"></div>
                            </div>
                            <div class="relic-tooltip">
                                <div class="relic-tooltip-title">Sword of Gryffindor</div>
                                <div class="relic-tooltip-desc">ดาบเงินสร้างโดยก็อบลิน สลักชื่อ Godric Gryffindor ประดับทับทิมแท้</div>
                                <div class="relic-tooltip-hint">✦ คลิกเพื่ออ่านประวัติ</div>
                            </div>
                        </div>

                        <!-- 📍 หมุด Interactive 3: ไม้กายสิทธิ์หัวสิงโต (Lion Wand) -->
                        <div class="relic-pin" style="top: 26%; left: 43%;" onclick="event.stopPropagation(); inspectRelic('wand');" role="button" tabindex="0" aria-label="ดูข้อมูลไม้กายสิทธิ์หัวสิงโต">
                            <div class="relic-pin-beacon">
                                <span>🪄</span>
                                <div class="relic-pin-ripple"></div>
                            </div>
                            <div class="relic-tooltip">
                                <div class="relic-tooltip-title">Lion-Head Wand</div>
                                <div class="relic-tooltip-desc">ไม้กายสิทธิ์แกะสลักเศียรสิงโตคำราม หัวใจเวทมนตร์แห่งความกล้าหาญ</div>
                                <div class="relic-tooltip-hint">✦ คลิกเพื่ออ่านประวัติ</div>
                            </div>
                        </div>

                        <!-- 📍 หมุด Interactive 4: เนคไทกริฟฟินดอร์และสมุดตราประจำบ้าน (Tie & Crest) -->
                        <div class="relic-pin" style="top: 25%; right: 22%;" onclick="event.stopPropagation(); inspectRelic('tie');" role="button" tabindex="0" aria-label="ดูข้อมูลเนคไทและตราประจำบ้าน">
                            <div class="relic-pin-beacon">
                                <span>👔</span>
                                <div class="relic-pin-ripple"></div>
                            </div>
                            <div class="relic-tooltip">
                                <div class="relic-tooltip-title">House Tie & Crest</div>
                                <div class="relic-tooltip-desc">เนคไทเครื่องแบบลายทางทองคู่ และสมุดตราอาร์มประจำบ้านกริฟฟินดอร์</div>
                                <div class="relic-tooltip-hint">✦ คลิกเพื่ออ่านประวัติ</div>
                            </div>
                        </div>

                        <!-- 📍 หมุด Interactive 5: หีบเวทมนตร์ฮอกวอตส์ (Vintage Hogwarts Trunk) -->
                        <div class="relic-pin" style="top: 14%; left: 50%;" onclick="event.stopPropagation(); inspectRelic('trunk');" role="button" tabindex="0" aria-label="ดูข้อมูลหีบเวทมนตร์">
                            <div class="relic-pin-beacon">
                                <span>🧳</span>
                                <div class="relic-pin-ripple"></div>
                            </div>
                            <div class="relic-tooltip">
                                <div class="relic-tooltip-title">Hogwarts Trunk</div>
                                <div class="relic-tooltip-desc">หีบไม้และหนังโบราณประดับหมุดทองเหลือง สำหรับเก็บสัมภาระเวทมนตร์</div>
                                <div class="relic-tooltip-hint">✦ คลิกเพื่ออ่านประวัติ</div>
                            </div>
                        </div>
                    </div>

                    <!-- แผ่นป้ายทองเหลืองสลักเกียรติยศ (Engraved Brass Plaque) -->
                    <div class="relics-brass-plaque">
                        <div class="plaque-latin">Gryffindor House Heirlooms</div>
                        <div class="plaque-thai">"หอสมบัติและเครื่องใช้ประจำบ้านกริฟฟินดอร์ของอเล็กซ์"</div>
                        <button class="plaque-inspect-btn" onclick="inspectRelic('relics_all')">
                            <span>✦ ตรวจดูบันทึกและของสะสมทั้งหมด</span>
                        </button>
                    </div>
                </div>

                <!-- 📜 ฝั่งขวา: สถิติและหัวข้อข้อมูลเวทมนตร์ -->
                <div>
                    
                    <!-- แถบปุ่มลัดตรวจดูของวิเศษ (Gryffindor Relic Quick Badges) -->
                    <div class="relic-chips-container">
                        <div class="relic-chips-title">
                            <span>🦁 ของวิเศษและเครื่องใช้ประจำตัว (House Relics & Gear)</span>
                        </div>
                        <div class="relic-chips-row">
                            <button class="relic-chip" onclick="inspectRelic('scarf')">
                                <span class="chip-icon">🧣</span>
                                <span>ผ้าพันคอไหมพรม</span>
                            </button>
                            <button class="relic-chip" onclick="inspectRelic('sword')">
                                <span class="chip-icon">⚔️</span>
                                <span>ดาบก็อดดริก</span>
                            </button>
                            <button class="relic-chip" onclick="inspectRelic('wand')">
                                <span class="chip-icon">🪄</span>
                                <span>ไม้กายสิทธิ์สิงโต</span>
                            </button>
                            <button class="relic-chip" onclick="inspectRelic('tie')">
                                <span class="chip-icon">👔</span>
                                <span>เนคไท & ตราบ้าน</span>
                            </button>
                            <button class="relic-chip" onclick="inspectRelic('trunk')">
                                <span class="chip-icon">🧳</span>
                                <span>หีบฮอกวอตส์</span>
                            </button>
                        </div>
                    </div>

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

# Replace existing #tab-information in html
tab_info_pattern = re.compile(r'<section id="tab-information".*?</section>', re.DOTALL)
assert tab_info_pattern.search(html), "ERROR: #tab-information not found"
html = tab_info_pattern.sub(new_tab_info_html, html, count=1)
print("[2] Replaced #tab-information with Gryffindor Scarf & Relics markup")

# ==============================================================================
# 3. EXPAND scrollArchive AND ADD inspectRelic() FUNCTION
# ==============================================================================
relics_archive_entries = """
            scarf: {
                title: "🧣 ผ้าพันคอไหมพรมประจำบ้านกริฟฟินดอร์ / Gryffindor Knitted Scarf",
                html: `<div class="parchment-history-flow">
                    <p class="history-p">
                        <strong>ผ้าพันคอไหมพรมสีแดงเลือดหมูสลับทอง (Scarlet & Gold)</strong> ผืนนี้เป็นหนึ่งในของใช้ที่อเล็กซ์รักและผูกพันมากที่สุด ตัวผ้าถักทอด้วยไหมพรมเนื้อหนานุ่ม ลายทางสองสีกว้างสลับกันตามธรรมเนียมดั้งเดิมของบ้านกริฟฟินดอร์ พร้อมปักตราอาร์มสิงโตคำรามสีทองที่ปลายผ้า
                    </p>
                    <p class="history-p">
                        แม้ชายผ้าพันคอและพู่ถักจะมีรอยขุยจากการใช้งานสมบุกสมบัน ทั้งการซ้อมบินโต้ลมหนาวบนยอดหอคอยกริฟฟินดอร์ และการนั่งเชียร์เพื่อนข้างสนามควิดดิชยามหิมะตกหนัก แต่อเล็กซ์ก็มักจะพันคอไว้เสมอ เพราะมันให้ความรู้สึกอบอุ่นและเป็นเครื่องเตือนใจถึง <em>"ความกล้าหาญที่ไม่เคยสั่นคลอน"</em>
                    </p>
                </div>`
            },
            sword: {
                title: "⚔️ ดาบของก็อดดริก กริฟฟินดอร์ / Sword of Godric Gryffindor",
                html: `<div class="parchment-history-flow">
                    <p class="history-p">
                        <strong>ดาบเงินแท้สร้างโดยก็อบลิน (Goblin-Made Silver Sword)</strong> ผลงานช่างฝีมือของ <em>แรกนุกที่หนึ่ง (Ragnuk the First)</em> กษัตริย์ก็อบลิน สลักอักษรโบราณว่า <strong>"GODRIC GRYFFINDOR"</strong> ตามแนวร่องดาบ ตัวด้ามจับและโกร่งดาบหล่อจากเงินสลักลายสิงโตและประดับอัญมณีทับทิมแท้สีแดงสดสุกปลั่ง
                    </p>
                    <p class="history-p">
                        ตามตำนานฮอกวอตส์ ดาบเล่มนี้มีคุณสมบัติพิเศษในการดูดซับสิ่งใดก็ตามที่ทำให้มันแข็งแกร่งยิ่งขึ้น และจะปรากฏตัวออกมาจาก <em>หมวกคัดสรร</em> ให้แก่ <strong>"นักเรียนบ้านกริฟฟินดอร์ที่มีความกล้าหาญแท้จริงในยามคับขันเท่านั้น"</strong>
                    </p>
                </div>`
            },
            wand: {
                title: "🪄 ไม้กายสิทธิ์หัวสิงโต / The Lion-Head Wand",
                html: `<div class="parchment-history-flow">
                    <p class="history-p">
                        ไม้กายสิทธิ์ประจำตัวของอเล็กซ์ โดดเด่นด้วยการแกะสลัก <strong>เศียรสิงโตคำราม</strong> ประดับอยู่บนยอดด้ามจับ ตัวไม้ทำจากไม้โอ๊กดำเนื้อแกร่ง บิดเกลียวเวียนตามธรรมชาติ สื่อถึงความดุดัน ความมุ่งมั่น และความว่องไวในการร่ายคาถาตอบโต้
                    </p>
                    <p class="history-p">
                        แกนกลางบรรจุ <em>ขนแผงคอสิงโตผสมเอ็นหัวใจมังกร</em> ทำให้มีพลังในการร่ายคาถาป้องกันตัวจากศาสตร์มืดได้อย่างหนักแน่นและเฉียบขาด เหมาะสมอย่างยิ่งสำหรับอดีตเชสเซอร์ควิดดิชผู้มีปฏิกิริยาตอบสนองในเสี้ยววินาที
                    </p>
                </div>`
            },
            tie: {
                title: "👔 เนคไทกริฟฟินดอร์และสมุดตราประจำบ้าน / House Tie & Harlequin Crest",
                html: `<div class="parchment-history-flow">
                    <p class="history-p">
                        <strong>เนคไทเครื่องแบบนักเรียนฮอกวอตส์</strong> สีเลือดหมูเข้มตัดด้วยลายทางคู่สีทอง พร้อมปักตราสัญลักษณ์สิงโตทองตัวเล็กที่ชายเนคไท คู่กับ <strong>สมุดตราประจำบ้านกริฟฟินดอร์ลายข้าวหลามตัด (Harlequin Crest Tome)</strong> ยุคโบราณ
                    </p>
                    <p class="history-p">
                        แม้เสื้อคลุมของอเล็กซ์จะดูเก่าปอนเนื่องจากฐานะทางบ้าน แต่เขาก็สวมเนคไทและติดตราบ้านด้วยความภาคภูมิใจในเกียรติยศแห่งกริฟฟินดอร์อยู่เสมอ
                    </p>
                </div>`
            },
            trunk: {
                title: "🧳 หีบเดินทางฮอกวอตส์โบราณ / Vintage Hogwarts Leather Trunk",
                html: `<div class="parchment-history-flow">
                    <p class="history-p">
                        <strong>หีบเดินทางทำจากไม้และหนังแท้โบราณ</strong> เสริมมุมและหมุดทองเหลืองรมดำ ประทับตราอาร์มประจำบ้านกริฟฟินดอร์ตรงกลาง หีบใบนี้สืบทอดมาจากพ่อแม่ของอเล็กซ์ซึ่งเคยเป็นมือปราบมาร
                    </p>
                    <p class="history-p">
                        ภายในหีบแบ่งเป็นช่องลับหลายชั้น สำหรับเก็บทั้งตำราเวทมนตร์คาถา อุปกรณ์ดูแลไม้กวาดแข่งขัน และส่วนประกอบลับสำหรับประดิษฐ์ประทัดและระเบิดควันแกล้งคน
                    </p>
                </div>`
            },
            relics_all: {
                title: "🦁 มรดกและของสะสมบ้านกริฟฟินดอร์ / Gryffindor House Heirlooms",
                html: `<div class="parchment-history-flow">
                    <div class="history-chapter">
                        <h4 class="history-subtitle">✦ คอลเลกชันของสะสมและของวิเศษประจำหอพักกริฟฟินดอร์</h4>
                        <p class="history-p">
                            ภาพชุดของสะสมนี้ประกอบด้วย <strong>ผ้าพันคอไหมพรมกริฟฟินดอร์</strong>, <strong>ดาบของก็อดดริก กริฟฟินดอร์</strong>, <strong>ไม้กายสิทธิ์สลักหัวสิงโต</strong>, <strong>เนคไทเครื่องแบบ</strong> และ <strong>หีบเดินทางโบราณ</strong> ซึ่งรวบรวมจิตวิญญาณแห่งความกล้าหาญ ความมุ่งมั่น และความอบอุ่นของบ้านสิงห์ไว้อย่างครบถ้วน
                        </p>
                    </div>
                    <div class="history-quote-box">
                        <div class="quote-text">"สิ่งของเหล่านี้อาจมีรอยขีดข่วนและเก่าไปตามกาลเวลา... แต่หัวใจที่กล้าหาญของกริฟฟินดอร์จะคงอยู่ตลอดไป"</div>
                    </div>
                </div>`
            },"""

# Insert new entries into scrollArchive
scroll_archive_target = "const scrollArchive = {"
assert scroll_archive_target in html, "ERROR: scrollArchive not found"
html = html.replace(scroll_archive_target, scroll_archive_target + relics_archive_entries, 1)
print("[3] Added Gryffindor relic entries to scrollArchive")

# Add inspectRelic function
inspect_func = """
        // ================= Inspect Gryffindor Relic =================
        function inspectRelic(relicKey) {
            // Trigger visual magic sparks
            if (typeof createMagicSpark === 'function') {
                for (let i = 0; i < 5; i++) {
                    setTimeout(() => createMagicSpark(), i * 80);
                }
            }

            // Brief pulse on the relics stage
            const stage = document.getElementById('relicsStage');
            if (stage) {
                stage.style.boxShadow = '0 0 35px rgba(243, 194, 82, 0.9), 0 0 60px rgba(180, 20, 30, 0.7)';
                setTimeout(() => stage.style.boxShadow = '', 600);
            }

            // Open the scroll modal with the selected relic lore
            openScroll(relicKey);
        }
"""

last_script = html.rfind('</script>')
assert last_script != -1, "ERROR: </script> not found"
html = html[:last_script] + f'{inspect_func}\n' + html[last_script:]
print("[4] Added inspectRelic() function before </script>")

# Write back updated HTML
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: index.html updated successfully with Gryffindor Scarf & Relics Atmosphere!")
