# -*- coding: utf-8 -*-
"""
Upgrade Gallery tab to an immersive Marauder's Map sanctum
and implement the Enchanted 3D Open Grimoire Book Modal for viewing memories.
"""
import shutil
import re
import sys

# 1. Create a safe backup
shutil.copyfile('index.html', 'index.html.before_book.bak')
print("[1] Created index.html.before_book.bak")

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# =========================================================================
# 2. NEW CLEAN GALLERY SECTION HTML (Pure Marauder's Map, no clunky grid/pills)
# =========================================================================
new_gallery_html = """        <!-- ================= TAB 3: GALLERY (IMMERSIVE MARAUDER'S MAP) ================= -->
        <section id="tab-gallery" class="tab-content">
            <h2 class="section-ribbon-title">The Marauder's Map • แผนที่ตัวกวนแห่งฮอกวอตส์</h2>

            <!-- Elegant Marauder's Incantation Spell Ribbon Bar -->
            <div class="marauder-spell-ribbon-bar">
                <button id="toggleMapBtn" class="marauder-ribbon-btn" onclick="toggleMarauderMap()" title="แตะเพื่อร่ายคาถาเปิด/ปิดแผนที่ 3 มิติ">
                    <span class="ribbon-wand-icon">⚡</span>
                    <span id="mapSpellText">แผนลวงสำเร็จแล้ว</span>
                    <span class="ribbon-sub" id="mapSpellSub">"Mischief Managed" • แตะเพื่อพับเก็บแผนที่</span>
                </button>
            </div>

            <!-- 3D Marauder's Map Viewport -->
            <div class="map-viewport-wrapper">
                <div class="map-scale-container">
                    <div class="map-base active" id="maraudersMapBase" onclick="handleMapBaseClick(event)">
                        <!-- Animated Marauder Footsteps & Names -->
                        <div class="footsteps footsteps-1">
                            <div class="footstep left"></div>
                            <div class="footstep right"></div>
                            <div class="scroll-name"><p>Alexan Lake</p></div>
                        </div>
                        <div class="footsteps footsteps-2">
                            <div class="footstep left"></div>
                            <div class="footstep right"></div>
                            <div class="scroll-name"><p>James & Sirius</p></div>
                        </div>

                        <!-- Top Flaps (Cover) -->
                        <div class="map-flap flap--1">
                            <div class="map-flap__front"></div>
                            <div class="map-flap__back"></div>
                        </div>
                        <div class="map-flap flap--2">
                            <div class="map-flap__front"></div>
                            <div class="map-flap__back"></div>
                        </div>

                        <!-- 6 Folding Sides / Castle Wings with Memory Pins -->
                        <!-- Side 1: Left Center (Courtyard & Lake) -->
                        <div class="map-side side-1" style="--image: url('https://meowlivia.s3.us-east-2.amazonaws.com/codepen/map/11.png')">
                            <div class="front">
                                <div class="map-memory-token token-3" id="mapToken-3" onclick="openEnchantedBook(3); event.stopPropagation();" title="เปิดสมุดบันทึก: Prank Fireworks">
                                    <div class="token-compass-pulse"></div>
                                    <div class="token-seal-frame">
                                        <img src="images/alexan-profile.jpg" alt="Prank Fireworks" />
                                    </div>
                                    <div class="token-banner-label">
                                        <span class="label-en">Prank Fireworks</span>
                                    </div>
                                    <div class="token-inspect-hint">📖 เปิดสมุดบันทึก</div>
                                </div>
                            </div>
                            <div class="back"></div>
                        </div>

                        <!-- Side 2: Right Center (Castle Corridors & Staircases) -->
                        <div class="map-side side-2" style="--image: url('https://meowlivia.s3.us-east-2.amazonaws.com/codepen/map/12.png')">
                            <div class="front">
                                <div class="map-memory-token token-4" id="mapToken-4" onclick="openEnchantedBook(4); event.stopPropagation();" title="เปิดสมุดบันทึก: Duel Training">
                                    <div class="token-compass-pulse"></div>
                                    <div class="token-seal-frame">
                                        <img src="images/alexan-profile.jpg" alt="Duel Training" />
                                    </div>
                                    <div class="token-banner-label">
                                        <span class="label-en">Duel Training</span>
                                    </div>
                                    <div class="token-inspect-hint">📖 เปิดสมุดบันทึก</div>
                                </div>
                            </div>
                            <div class="back"></div>
                        </div>

                        <!-- Side 3: Mid-Left Wing (Gryffindor Tower & Battlements) -->
                        <div class="map-side side-3" style="--image: url('https://meowlivia.s3.us-east-2.amazonaws.com/codepen/map/13.png')">
                            <div class="front">
                                <div class="map-memory-token token-1" id="mapToken-1" onclick="openEnchantedBook(1); event.stopPropagation();" title="เปิดสมุดบันทึก: Winter Scarf">
                                    <div class="token-compass-pulse"></div>
                                    <div class="token-seal-frame">
                                        <img src="images/scene-2.jpg" alt="Winter Scarf" />
                                    </div>
                                    <div class="token-banner-label">
                                        <span class="label-en">Winter Scarf</span>
                                    </div>
                                    <div class="token-inspect-hint">📖 เปิดสมุดบันทึก</div>
                                </div>
                            </div>
                            <div class="back"></div>
                        </div>

                        <!-- Side 4: Mid-Right Wing (Quidditch Pitch & Stadium) -->
                        <div class="map-side side-4" style="--image: url('https://meowlivia.s3.us-east-2.amazonaws.com/codepen/map/14.png')">
                            <div class="front">
                                <div class="map-memory-token token-2" id="mapToken-2" onclick="openEnchantedBook(2); event.stopPropagation();" title="เปิดสมุดบันทึก: Quidditch Pitch">
                                    <div class="token-compass-pulse"></div>
                                    <div class="token-seal-frame">
                                        <img src="images/scene-3.jpg" alt="Quidditch Pitch" />
                                    </div>
                                    <div class="token-banner-label">
                                        <span class="label-en">Quidditch Pitch</span>
                                    </div>
                                    <div class="token-inspect-hint">📖 เปิดสมุดบันทึก</div>
                                </div>
                            </div>
                            <div class="back"></div>
                        </div>

                        <!-- Side 5: Outer Left Wing (Hogsmeade Village & Three Broomsticks) -->
                        <div class="map-side side-5" style="--image: url('https://meowlivia.s3.us-east-2.amazonaws.com/codepen/map/15.png')">
                            <div class="front">
                                <div class="map-memory-token token-0" id="mapToken-0" onclick="openEnchantedBook(0); event.stopPropagation();" title="เปิดสมุดบันทึก: Hogsmeade Stroll">
                                    <div class="token-compass-pulse"></div>
                                    <div class="token-seal-frame">
                                        <img src="images/scene-1.jpg" alt="Hogsmeade Stroll" />
                                    </div>
                                    <div class="token-banner-label">
                                        <span class="label-en">Hogsmeade Stroll</span>
                                    </div>
                                    <div class="token-inspect-hint">📖 เปิดสมุดบันทึก</div>
                                </div>
                            </div>
                            <div class="back"></div>
                        </div>

                        <!-- Side 6: Outer Right Wing (The Great Hall & High Sanctum) -->
                        <div class="map-side side-6" style="--image: url('https://meowlivia.s3.us-east-2.amazonaws.com/codepen/map/16.png')">
                            <div class="front">
                                <div class="map-memory-token token-5" id="mapToken-5" onclick="openEnchantedBook(5); event.stopPropagation();" title="เปิดสมุดบันทึก: Fierce Resolve">
                                    <div class="token-compass-pulse"></div>
                                    <div class="token-seal-frame">
                                        <img src="images/alexan-profile.jpg" alt="Fierce Resolve" />
                                    </div>
                                    <div class="token-banner-label">
                                        <span class="label-en">Fierce Resolve</span>
                                    </div>
                                    <div class="token-inspect-hint">📖 เปิดสมุดบันทึก</div>
                                </div>
                            </div>
                            <div class="back"></div>
                        </div>
                    </div>
                </div>
            </div>
        </section>"""

# Replace the old tab-gallery section
start_gallery = html.find('<section id="tab-gallery"')
end_gallery = html.find('</section>', start_gallery) + len('</section>')
html = html[:start_gallery] + new_gallery_html + html[end_gallery:]
print("[2] Successfully replaced Gallery HTML with pure Marauder's Map")

# =========================================================================
# 3. NEW ENCHANTED OPEN BOOK MODAL HTML (Two-page Open Tome)
# =========================================================================
open_book_modal_html = """
    <!-- ================= ENCHANTED GRIMOIRE / OPEN BOOK MODAL (เปิดสมุดบันทึกความทรงจำ) ================= -->
    <div class="enchanted-book-scrim" id="enchantedBookModal" onclick="closeBookOnBackdrop(event)" role="dialog" aria-modal="true" aria-label="สมุดบันทึกความทรงจำเวทมนตร์แห่งฮอกวอตส์">
        <div class="book-modal-wrapper">
            <!-- 3D Open Tome Container -->
            <div class="magical-open-tome" id="magicalOpenTome">
                <!-- Leather Hardcover Backing & Gilded Metal Corner Plates -->
                <div class="tome-leather-cover">
                    <div class="tome-corner topleft"></div>
                    <div class="tome-corner topright"></div>
                    <div class="tome-corner bottomleft"></div>
                    <div class="tome-corner bottomright"></div>
                </div>

                <!-- Hanging Red Silk Bookmark Ribbon with Gilded Fringe -->
                <div class="tome-silk-bookmark"></div>

                <!-- Two-Page Open Parchment Spread -->
                <div class="tome-spread" id="tomeSpread">
                    <!-- Left Page: The Living Photographic Memory Canvas -->
                    <div class="tome-page left-page">
                        <div class="page-corner-flourish tl"></div>
                        <div class="page-corner-flourish bl"></div>

                        <div class="memory-plate-header">
                            <span class="plate-num" id="bookPlateNum">MEMORIA I</span>
                            <span class="plate-tag" id="bookPlateLocation">Hogsmeade Village</span>
                        </div>

                        <!-- Antique Photo Frame with Gilded Corner Brackets -->
                        <div class="living-photo-frame">
                            <div class="photo-corner pc-tl"></div>
                            <div class="photo-corner pc-tr"></div>
                            <div class="photo-corner pc-bl"></div>
                            <div class="photo-corner pc-br"></div>
                            <img id="bookMemoryImg" src="images/scene-1.jpg" alt="Living Memory" class="living-memory-img" />
                            <div class="photo-ambient-vignette"></div>
                            <div class="photo-magic-sheen"></div>
                        </div>

                        <!-- Photo Caption Plaque -->
                        <div class="memory-caption-box">
                            <div class="caption-title" id="bookMemoryCaption">Hogsmeade Stroll</div>
                            <div class="caption-stamp">ARCHIVUM HOGWARTS • YEAR VI</div>
                        </div>

                        <!-- Page Flip Navigation (Prev / Next & Counter) -->
                        <div class="tome-page-nav">
                            <button class="tome-nav-btn prev" onclick="navigateBookMemory(-1)" title="เปิดดูบันทึกก่อนหน้า (หรือกดลูกศรซ้าย)">
                                <span>‹</span> ก่อนหน้า
                            </button>
                            <span class="tome-page-counter" id="bookPageCounter">1 / 6</span>
                            <button class="tome-nav-btn next" onclick="navigateBookMemory(1)" title="เปิดดูบันทึกถัดไป (หรือกดลูกศรขวา)">
                                ถัดไป <span>›</span>
                            </button>
                        </div>
                    </div>

                    <!-- Center Book Spine Gutter & Binding Stitches -->
                    <div class="tome-spine-gutter">
                        <div class="spine-line"></div>
                        <div class="spine-stitches"></div>
                    </div>

                    <!-- Right Page: The Hand-Inked Field Notes & Story -->
                    <div class="tome-page right-page">
                        <div class="page-corner-flourish tr"></div>
                        <div class="page-corner-flourish br"></div>

                        <!-- Antique Close Tome Wax Seal Button -->
                        <button class="close-tome-btn" onclick="closeEnchantedBook()" title="ปิดสมุดบันทึก (หรือกด ESC)">
                            <span class="close-icon">✕</span>
                            <span class="close-text">ปิดสมุด</span>
                        </button>

                        <div class="journal-header">
                            <div class="journal-latin-sub">FOLIO HISTORIAE • GRYFFINDOR</div>
                            <h3 class="journal-title" id="bookMemoryTitle">Hogsmeade Stroll / เดินเล่นฮอกส์มี้ด</h3>
                            <div class="journal-rule-divider"></div>
                        </div>

                        <!-- Inked Body Text with Illuminated Drop Cap -->
                        <div class="journal-body-content">
                            <div class="illuminated-text-wrap" id="bookMemoryText">
                                <!-- Populated dynamically by JavaScript -->
                            </div>
                        </div>

                        <!-- Journal Footer: Signature & Gryffindor Wax Seal -->
                        <div class="journal-footer">
                            <div class="journal-signature">
                                <span class="sig-label">บันทึกความทรงจำของ</span>
                                <strong class="sig-name">Alexan N. Lake</strong>
                            </div>
                            <div class="tome-wax-seal-badge" title="ตราประทับขี้ผึ้งกริฟฟินดอร์">
                                <img src="images/crest.png" alt="Gryffindor Seal" />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
"""

# Place open_book_modal_html right after scrollModal
scroll_modal_marker = '<!-- ================= PARCHMENT MODAL DIALOG ================= -->'
pos_scroll_modal = html.find(scroll_modal_marker)
if pos_scroll_modal != -1:
    # Find the end of scrollModal div
    end_scroll_modal = html.find('</div>\n    </div>', pos_scroll_modal) + len('</div>\n    </div>')
    html = html[:end_scroll_modal] + "\n" + open_book_modal_html + html[end_scroll_modal:]
    print("[3] Added Enchanted Open Book Modal HTML right after parchment scroll modal")
else:
    # Fallback to before </main>
    html = html.replace('</main>', '</main>\n' + open_book_modal_html)
    print("[3] Added Enchanted Open Book Modal HTML before </main>")

# =========================================================================
# 4. CSS STYLES FOR THE MARAUDER'S MAP & ENCHANTED OPEN BOOK MODAL
# =========================================================================
book_and_map_css = """
        /* ==========================================================================
           ENCHANTED OPEN BOOK (GRIMOIRE) MODAL & PURE MARAUDER'S MAP STYLES
           ========================================================================== */

        /* Marauder's Spell Ribbon Bar */
        .marauder-spell-ribbon-bar {
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 10px auto 25px;
            position: relative;
            z-index: 10;
        }

        .marauder-ribbon-btn {
            background: radial-gradient(ellipse at center, rgba(55, 12, 16, 0.95) 0%, rgba(20, 2, 4, 0.95) 100%);
            border: 2px solid var(--gold-antique);
            border-radius: 40px;
            color: #ffe6a0;
            padding: 10px 28px;
            font-family: 'Noto Serif Thai', serif;
            font-size: 1.35rem;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 12px;
            box-shadow: 
                0 8px 24px rgba(0, 0, 0, 0.85),
                0 0 20px rgba(223, 162, 44, 0.3),
                inset 0 0 15px rgba(255, 215, 0, 0.15);
            transition: all 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            user-select: none;
        }

        .marauder-ribbon-btn:hover {
            transform: translateY(-3px) scale(1.03);
            border-color: var(--gold-bright);
            color: #ffffff;
            box-shadow: 
                0 14px 30px rgba(0, 0, 0, 0.95),
                0 0 35px rgba(223, 162, 44, 0.6),
                inset 0 0 25px rgba(255, 215, 0, 0.3);
        }

        .ribbon-wand-icon {
            font-size: 1.2rem;
            color: var(--gold-bright);
            animation: wandPulse 2s infinite ease-in-out;
        }

        @keyframes wandPulse {
            0%, 100% { transform: scale(1); filter: drop-shadow(0 0 4px #ffd000); }
            50% { transform: scale(1.25); filter: drop-shadow(0 0 12px #fffaaa); }
        }

        .ribbon-sub {
            font-family: 'Cinzel', 'Sarun HarryPotter', cursive, serif;
            font-size: 0.95rem;
            color: #d8be8d;
            font-style: italic;
            border-left: 1px solid rgba(223, 162, 44, 0.4);
            padding-left: 12px;
            margin-left: 4px;
        }

        /* -------------------------------------------------------------
           ENCHANTED OPEN BOOK (GRIMOIRE) MODAL
           ------------------------------------------------------------- */
        .enchanted-book-scrim {
            position: fixed;
            inset: 0;
            background: radial-gradient(circle at center, rgba(14, 2, 4, 0.88) 0%, rgba(4, 0, 1, 0.96) 100%);
            backdrop-filter: blur(10px);
            z-index: 99999;
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
            padding: 20px;
        }

        .enchanted-book-scrim.active {
            opacity: 1;
            pointer-events: auto;
        }

        .book-modal-wrapper {
            perspective: 2200px;
            width: 100%;
            max-width: 960px;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* The Hardcover 3D Open Tome */
        .magical-open-tome {
            position: relative;
            width: 100%;
            border-radius: 12px;
            transform: scale(0.85) rotateX(8deg);
            opacity: 0;
            transition: transform 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.2), opacity 0.4s ease;
            box-shadow: 
                0 35px 80px rgba(0, 0, 0, 0.95),
                0 0 50px rgba(223, 162, 44, 0.25);
        }

        .enchanted-book-scrim.active .magical-open-tome {
            transform: scale(1) rotateX(0deg);
            opacity: 1;
        }

        /* Leather Hardcover Backing */
        .tome-leather-cover {
            position: absolute;
            inset: -14px -16px;
            background: 
                radial-gradient(ellipse at 50% 50%, #3e090f 0%, #1c0205 100%);
            border-radius: 14px;
            border: 2px solid rgba(223, 162, 44, 0.7);
            box-shadow: 
                inset 0 0 40px rgba(0, 0, 0, 0.9),
                0 15px 35px rgba(0, 0, 0, 0.85);
            pointer-events: none;
            z-index: 1;
        }

        /* Gilded Brass Corner Plates on Leather Cover */
        .tome-corner {
            position: absolute;
            width: 38px;
            height: 38px;
            border: 3px solid var(--gold-bright);
            box-shadow: 0 0 10px rgba(255, 215, 0, 0.4);
            pointer-events: none;
        }
        .tome-corner.topleft { top: 6px; left: 6px; border-right: none; border-bottom: none; border-top-left-radius: 8px; }
        .tome-corner.topright { top: 6px; right: 6px; border-left: none; border-bottom: none; border-top-right-radius: 8px; }
        .tome-corner.bottomleft { bottom: 6px; left: 6px; border-right: none; border-top: none; border-bottom-left-radius: 8px; }
        .tome-corner.bottomright { bottom: 6px; right: 6px; border-left: none; border-top: none; border-bottom-right-radius: 8px; }

        /* Hanging Silk Bookmark Ribbon */
        .tome-silk-bookmark {
            position: absolute;
            bottom: -46px;
            left: calc(50% - 14px);
            width: 28px;
            height: 60px;
            background: linear-gradient(to right, #7a0810, #ba1622 45%, #6a050d 100%);
            border-bottom: 2px solid var(--gold-bright);
            clip-path: polygon(0 0, 100% 0, 100% 84%, 50% 100%, 0 84%);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.7);
            z-index: 10;
            pointer-events: none;
        }

        /* Two-Page Open Parchment Spread */
        .tome-spread {
            position: relative;
            z-index: 2;
            display: flex;
            background: #eddcb8;
            border-radius: 6px;
            overflow: hidden;
            min-height: 520px;
            box-shadow: inset 0 0 35px rgba(80, 40, 10, 0.35);
            transition: transform 0.25s ease, opacity 0.25s ease;
        }

        .tome-spread.page-flipping {
            transform: scale(0.985);
            opacity: 0.7;
        }

        /* Individual Page */
        .tome-page {
            flex: 1;
            padding: 34px 38px 28px;
            position: relative;
            background: radial-gradient(ellipse at 50% 30%, #fbf3df 0%, #edd9b2 65%, #ddc497 100%);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .tome-page.left-page {
            box-shadow: inset -22px 0 26px -12px rgba(60, 30, 8, 0.45);
            border-right: 1px solid rgba(138, 92, 40, 0.2);
        }

        .tome-page.right-page {
            box-shadow: inset 22px 0 26px -12px rgba(60, 30, 8, 0.45);
            border-left: 1px solid rgba(138, 92, 40, 0.2);
        }

        /* Center Spine Gutter Crease */
        .tome-spine-gutter {
            position: absolute;
            top: 0;
            bottom: 0;
            left: 50%;
            width: 32px;
            transform: translateX(-50%);
            background: linear-gradient(to right, 
                rgba(35, 15, 5, 0.45) 0%, 
                rgba(20, 8, 2, 0.65) 45%, 
                rgba(10, 3, 0, 0.75) 50%, 
                rgba(20, 8, 2, 0.65) 55%, 
                rgba(35, 15, 5, 0.45) 100%
            );
            pointer-events: none;
            z-index: 8;
        }

        .spine-line {
            position: absolute;
            top: 0;
            bottom: 0;
            left: 50%;
            width: 1px;
            background: rgba(223, 162, 44, 0.4);
        }

        /* Page Corner Ornamental Flourishes */
        .page-corner-flourish {
            position: absolute;
            width: 24px;
            height: 24px;
            border: 1px solid rgba(138, 92, 40, 0.5);
            pointer-events: none;
        }
        .page-corner-flourish.tl { top: 12px; left: 12px; border-right: none; border-bottom: none; }
        .page-corner-flourish.bl { bottom: 12px; left: 12px; border-right: none; border-top: none; }
        .page-corner-flourish.tr { top: 12px; right: 12px; border-left: none; border-bottom: none; }
        .page-corner-flourish.br { bottom: 12px; right: 12px; border-left: none; border-top: none; }

        /* Left Page Content: Photo & Framing */
        .memory-plate-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1.5px solid rgba(138, 92, 40, 0.35);
            padding-bottom: 8px;
            margin-bottom: 16px;
        }

        .plate-num {
            font-family: 'Cinzel', 'Sarun HarryPotter', serif;
            font-size: 1.15rem;
            font-weight: 700;
            letter-spacing: 1.5px;
            color: #7a151e;
        }

        .plate-tag {
            font-family: 'Noto Serif Thai', serif;
            font-size: 0.95rem;
            color: #5c3818;
            font-style: italic;
        }

        /* Living Photo Frame with Antique Photo Mount Corners */
        .living-photo-frame {
            position: relative;
            width: 100%;
            height: 275px;
            border-radius: 4px;
            background: #1a0407;
            padding: 8px;
            box-shadow: 
                0 10px 25px rgba(0, 0, 0, 0.7),
                inset 0 0 20px rgba(0, 0, 0, 0.9);
            border: 1.5px solid rgba(138, 92, 40, 0.6);
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .living-memory-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            border-radius: 2px;
            filter: sepia(18%) contrast(1.1) brightness(0.96);
            transition: filter 0.5s ease, transform 0.5s ease;
        }

        .living-photo-frame:hover .living-memory-img {
            filter: sepia(0%) contrast(1.18) brightness(1.03);
            transform: scale(1.03);
        }

        /* Photo Brass Mount Corners */
        .photo-corner {
            position: absolute;
            width: 18px;
            height: 18px;
            border: 3px solid var(--gold-bright);
            z-index: 5;
            pointer-events: none;
            box-shadow: 0 0 6px rgba(0, 0, 0, 0.7);
        }
        .photo-corner.pc-tl { top: 4px; left: 4px; border-right: none; border-bottom: none; }
        .photo-corner.pc-tr { top: 4px; right: 4px; border-left: none; border-bottom: none; }
        .photo-corner.pc-bl { bottom: 4px; left: 4px; border-right: none; border-top: none; }
        .photo-corner.pc-br { bottom: 4px; right: 4px; border-left: none; border-top: none; }

        .photo-ambient-vignette {
            position: absolute;
            inset: 0;
            box-shadow: inset 0 0 35px rgba(20, 4, 6, 0.7);
            pointer-events: none;
            z-index: 3;
        }

        .photo-magic-sheen {
            position: absolute;
            inset: 0;
            background: linear-gradient(135deg, transparent 40%, rgba(255, 240, 180, 0.18) 50%, transparent 60%);
            background-size: 200% 200%;
            pointer-events: none;
            z-index: 4;
            animation: magicSheen 6s infinite ease-in-out;
        }

        @keyframes magicSheen {
            0% { background-position: -100% -100%; }
            50% { background-position: 100% 100%; }
            100% { background-position: 200% 200%; }
        }

        /* Memory Caption Box */
        .memory-caption-box {
            text-align: center;
            margin-top: 14px;
        }

        .caption-title {
            font-family: 'Sarun HarryPotter', 'Cinzel', serif;
            font-size: 1.55rem;
            color: #3b1b0b;
            letter-spacing: 0.5px;
            margin-bottom: 2px;
        }

        .caption-stamp {
            font-family: 'Cinzel', serif;
            font-size: 0.75rem;
            letter-spacing: 2px;
            color: #8c5722;
            font-weight: 700;
        }

        /* Page Flip Navigation Buttons */
        .tome-page-nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 1.5px solid rgba(138, 92, 40, 0.35);
            padding-top: 10px;
            margin-top: 14px;
        }

        .tome-nav-btn {
            background: rgba(60, 20, 10, 0.08);
            border: 1px solid rgba(138, 92, 40, 0.5);
            border-radius: 6px;
            padding: 5px 14px;
            color: #5c2415;
            font-family: 'Noto Serif Thai', serif;
            font-size: 0.95rem;
            font-weight: 600;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: all 0.25s ease;
        }

        .tome-nav-btn:hover {
            background: #7a151e;
            color: #ffffff;
            border-color: #7a151e;
            transform: translateY(-2px);
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.25);
        }

        .tome-page-counter {
            font-family: 'Cinzel', serif;
            font-size: 0.9rem;
            font-weight: 700;
            color: #8c5722;
            letter-spacing: 1px;
        }

        /* Right Page Content: Journal & Story */
        .close-tome-btn {
            position: absolute;
            top: 14px;
            right: 16px;
            background: #7a151e;
            color: #ffe6a0;
            border: 1.5px solid var(--gold-antique);
            border-radius: 20px;
            padding: 4px 14px;
            font-family: 'Noto Serif Thai', serif;
            font-size: 0.85rem;
            font-weight: bold;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            box-shadow: 0 3px 8px rgba(0, 0, 0, 0.35);
            transition: all 0.25s ease;
            z-index: 10;
        }

        .close-tome-btn:hover {
            background: #a31c28;
            color: #ffffff;
            border-color: var(--gold-bright);
            transform: scale(1.06);
            box-shadow: 0 5px 14px rgba(122, 21, 30, 0.5);
        }

        .journal-header {
            margin-top: 12px;
            margin-bottom: 14px;
        }

        .journal-latin-sub {
            font-family: 'Cinzel', serif;
            font-size: 0.78rem;
            letter-spacing: 2px;
            color: #8c5722;
            font-weight: 700;
            margin-bottom: 4px;
        }

        .journal-title {
            font-family: 'Sarun HarryPotter', 'Cinzel', 'Noto Serif Thai', serif;
            font-size: 1.85rem;
            color: #630c14;
            line-height: 1.25;
            margin: 0;
            text-shadow: 1px 1px 0 rgba(255, 235, 180, 0.4);
        }

        .journal-rule-divider {
            height: 2px;
            background: linear-gradient(to right, #8c5722, rgba(140, 87, 34, 0.2) 80%, transparent 100%);
            margin-top: 8px;
        }

        /* Journal Body Text & Drop Cap */
        .journal-body-content {
            flex: 1;
            overflow-y: auto;
            max-height: 285px;
            padding-right: 6px;
            margin-bottom: 12px;
        }

        .journal-body-content::-webkit-scrollbar {
            width: 5px;
        }
        .journal-body-content::-webkit-scrollbar-thumb {
            background: rgba(138, 92, 40, 0.4);
            border-radius: 4px;
        }

        .illuminated-text-wrap {
            font-family: 'SOV Yoona', 'Noto Serif Thai', serif;
            font-size: 1.35rem;
            color: #271408;
            line-height: 2.05;
            letter-spacing: 0.35px;
            text-align: justify;
        }

        .drop-cap {
            float: left;
            font-family: 'Cinzel', 'Sarun HarryPotter', serif;
            font-size: 3.4rem;
            line-height: 0.78;
            padding-top: 6px;
            padding-right: 12px;
            padding-bottom: 2px;
            color: #800a12;
            font-weight: 900;
            text-shadow: 1px 1px 0 #ebd09e, 2px 2px 4px rgba(0, 0, 0, 0.2);
        }

        /* Journal Footer: Signature & Wax Seal */
        .journal-footer {
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            border-top: 1.5px solid rgba(138, 92, 40, 0.35);
            padding-top: 10px;
        }

        .journal-signature {
            display: flex;
            flex-direction: column;
        }

        .sig-label {
            font-family: 'Noto Serif Thai', serif;
            font-size: 0.82rem;
            color: #7a4a20;
            font-style: italic;
        }

        .sig-name {
            font-family: 'Satisfy', 'Lobster Two', cursive;
            font-size: 1.7rem;
            color: #630c14;
            letter-spacing: 0.5px;
            font-weight: normal;
        }

        .tome-wax-seal-badge {
            width: 48px;
            height: 56px;
            filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.4));
            transition: transform 0.3s ease;
        }

        .tome-wax-seal-badge:hover {
            transform: scale(1.15) rotate(4deg);
        }

        .tome-wax-seal-badge img {
            width: 100%;
            height: 100%;
            object-fit: contain;
        }

        /* -------------------------------------------------------------
           RESPONSIVE OPEN BOOK (Mobile & Tablet)
           ------------------------------------------------------------- */
        @media (max-width: 860px) {
            .tome-spread {
                flex-direction: column;
                min-height: auto;
            }

            .tome-spine-gutter {
                display: none;
            }

            .tome-page.left-page {
                box-shadow: none;
                border-right: none;
                border-bottom: 2px solid rgba(138, 92, 40, 0.4);
                padding: 24px 20px 18px;
            }

            .tome-page.right-page {
                box-shadow: none;
                border-left: none;
                padding: 20px 20px 24px;
            }

            .living-photo-frame {
                height: 220px;
            }

            .journal-body-content {
                max-height: none;
            }

            .marauder-ribbon-btn {
                font-size: 1.15rem;
                padding: 8px 18px;
            }

            .ribbon-sub {
                display: none;
            }
        }
"""

# Replace Map CSS section
start_css_marker = '/* ================= MARAUDER\'S MAP (ENCHANTED 3D BOOK & MAP) ================= */'
pos_css_start = html.find(start_css_marker)
pos_css_about = html.find('/* ===== TAB 4: ABOUT ===== */', pos_css_start)

if pos_css_start != -1 and pos_css_about != -1:
    # Retain the pure 3D map folding CSS and add the new Book modal CSS
    # Let's inspect what is currently between pos_css_start and pos_css_about
    existing_map_css = html[pos_css_start:pos_css_about]
    
    # We will append book_and_map_css right before pos_css_about
    html = html[:pos_css_about] + book_and_map_css + "\n\n        " + html[pos_css_about:]
    print("[4] Added Enchanted Open Book and pure Marauder CSS before TAB 4: ABOUT")
else:
    print("[Warning] Could not find exact CSS anchors, injecting before </style>")
    html = html.replace('</style>', book_and_map_css + '\n    </style>')

# =========================================================================
# 5. NEW JAVASCRIPT CONTROLLERS (Enchanted Book & Smooth Navigation)
# =========================================================================
open_book_js = """
        // ================= Enhanced Gallery Memories (6 Plates) =================
        const galleryStories = [
            {
                plate: "MEMORIA I",
                location: "Hogsmeade Village • The Three Broomsticks",
                captionTitle: "Hogsmeade Stroll",
                title: "Hogsmeade Stroll / เดินเล่นฮอกส์มี้ด",
                desc: "ช็อตช่วงวันหยุดสุดสัปดาห์ในฤดูหนาวที่หมู่บ้านฮอกส์มี้ด อเล็กซ์แอบพาเพื่อนย่องไปซื้อขนมร้านฮันนี่ดุกส์ และนั่งคุยกันข้างเตาผิงร้านไม้กวาดสามอันพร้อมบัตเตอร์เบียร์ฟองนุ่มไออุ่นคลายความหนาว",
                image: "images/scene-1.jpg"
            },
            {
                plate: "MEMORIA II",
                location: "Gryffindor Tower • Northern Battlements",
                captionTitle: "Winter Scarf",
                title: "Winter Scarf / ผ้าพันคอรับลมหนาว",
                desc: "ผ้าพันคอไหมพรมลายทางสีแดงเลือดหมูสลับทองที่ถักเองอย่างเบี้ยวๆ แต่นุ่มอุ่นสบาย ช่วยบังลมหนาวจากยอดหอคอยกริฟฟินดอร์ในวันที่หิมะแรกโปรยปรายทั่วปราสาทฮอกวอตส์",
                image: "images/scene-2.jpg"
            },
            {
                plate: "MEMORIA III",
                location: "Quidditch Stadium • Gryffindor Chaser #07",
                captionTitle: "Quidditch Pitch",
                title: "Quidditch Pitch / สนามควิดดิช",
                desc: "ภาพช่วงก่อนแมตช์การแข่งขันใหญ่กับสลิธีริน อเล็กซ์ถือไม้กวาดไฟเยอร์โบลด์คู่ใจด้วยสีหน้ามุ่งมั่นมั่นใจเต็มร้อย พร้อมจะพาทีมสิงห์ทะยานคว้าชัยชนะกลางเวหา",
                image: "images/scene-3.jpg"
            },
            {
                plate: "MEMORIA IV",
                location: "Gryffindor Common Room • Fireside Lounge",
                captionTitle: "Prank Fireworks",
                title: "Prank Fireworks / จังหวะหน้าแดง",
                desc: "เหตุการณ์ตอนที่ตั้งใจจะจุดประทัดควันดักแกล้งเพื่อนในห้องนั่งเล่นรวม แต่ดันโดนจับได้คาหนังคาเขาจนแก้ตัวไม่ถูกหน้าแดงแจ๋ ท่ามกลางเสียงหัวเราะของเพื่อนร่วมบ้าน",
                image: "images/alexan-profile.jpg"
            },
            {
                plate: "MEMORIA V",
                location: "D.A.D.A. Chambers • Spell Duel Arena",
                captionTitle: "Duel Training",
                title: "Duel Training / หลังการดวลฝึกซ้อม",
                desc: "เสื้อคลุมเปื้อนเขม่าควันคาถาหลังฝึกดวลวิชาป้องกันตัวจากศาสตร์มืดจนเหงื่อท่วม แต่ยังมีรอยยิ้มภาคภูมิใจไม่เคยยอมแพ้ พร้อมจะลุกขึ้นสู้ใหม่เสมอ",
                image: "images/alexan-profile.jpg"
            },
            {
                plate: "MEMORIA VI",
                location: "The Great Hall • Lion's Sanctum",
                captionTitle: "Fierce Resolve",
                title: "Fierce Resolve / จิตวิญญาณกริฟฟินดอร์",
                desc: "แววตาแน่วแน่แม้จะสูญเสียดวงตาข้างซ้ายและขาขวา แต่อเล็กซ์ก็พิสูจน์ให้ทุกคนเห็นว่าหัวใจแห่งความกล้าหาญไม่ได้สูญเสียไปตามร่างกายเลยแม้แต่น้อย",
                image: "images/alexan-profile.jpg"
            }
        ];

        // ================= Marauder's Map Controls =================
        let isMarauderMapActive = true; // Open by default for immediate immersion!

        function toggleMarauderMap() {
            const mapBase = document.getElementById('maraudersMapBase');
            const spellText = document.getElementById('mapSpellText');
            const spellSub = document.getElementById('mapSpellSub');
            if (!mapBase) return;

            isMarauderMapActive = !isMarauderMapActive;
            if (isMarauderMapActive) {
                mapBase.classList.add('active');
                if (spellText) spellText.textContent = "แผนลวงสำเร็จแล้ว";
                if (spellSub) spellSub.textContent = '"Mischief Managed" • แตะเพื่อพับเก็บแผนที่';
            } else {
                mapBase.classList.remove('active');
                if (spellText) spellText.textContent = "ข้าขอสาบานอย่างจริงจังว่าข้านั้นหาความดีมิได้";
                if (spellSub) spellSub.textContent = '"I solemnly swear that I am up to no good" • แตะเพื่อคลี่เปิดแผนที่ 3D';
            }
        }

        function handleMapBaseClick(e) {
            // If map is currently closed and user clicks anywhere on the cover, unfold it!
            if (!isMarauderMapActive) {
                toggleMarauderMap();
            }
        }

        // ================= Enchanted Open Book (Grimoire Modal) Controls =================
        let currentBookIndex = 0;
        let isBookModalOpen = false;

        function openEnchantedBook(index) {
            if (index < 0 || index >= galleryStories.length) index = 0;
            currentBookIndex = index;
            renderBookPage(currentBookIndex);

            const modal = document.getElementById('enchantedBookModal');
            if (modal) {
                modal.classList.add('active');
                isBookModalOpen = true;
            }

            // Play delicate magical page rustle / harp chime
            if (typeof playSpellHarpTone === 'function') {
                playSpellHarpTone(659.25, 0, 0.35);
                playSpellHarpTone(880.00, 0.08, 0.45);
            }

            try {
                if (!window.history.state || !window.history.state.enchantedBookOpen) {
                    window.history.pushState({ enchantedBookOpen: true }, '');
                }
            } catch (e) { }
        }

        function renderBookPage(index) {
            const story = galleryStories[index];
            if (!story) return;

            // Left Page updates
            const plateNum = document.getElementById('bookPlateNum');
            const plateLoc = document.getElementById('bookPlateLocation');
            const memImg = document.getElementById('bookMemoryImg');
            const caption = document.getElementById('bookMemoryCaption');
            const counter = document.getElementById('bookPageCounter');

            if (plateNum) plateNum.textContent = story.plate;
            if (plateLoc) plateLoc.textContent = story.location;
            if (memImg) {
                memImg.src = story.image;
                memImg.alt = story.captionTitle;
            }
            if (caption) caption.textContent = story.captionTitle;
            if (counter) counter.textContent = `${index + 1} / ${galleryStories.length}`;

            // Right Page updates
            const titleEl = document.getElementById('bookMemoryTitle');
            const textEl = document.getElementById('bookMemoryText');

            if (titleEl) titleEl.textContent = story.title;
            if (textEl) {
                const desc = story.desc.trim();
                const firstChar = desc.charAt(0);
                const restOfText = desc.slice(1);
                textEl.innerHTML = `<span class="drop-cap">${firstChar}</span>${restOfText}`;
            }
        }

        function navigateBookMemory(direction) {
            const total = galleryStories.length;
            currentBookIndex = (currentBookIndex + direction + total) % total;

            const spread = document.getElementById('tomeSpread');
            if (spread) {
                spread.classList.add('page-flipping');
                setTimeout(() => {
                    renderBookPage(currentBookIndex);
                    spread.classList.remove('page-flipping');
                }, 120);
            } else {
                renderBookPage(currentBookIndex);
            }

            if (typeof playSpellHarpTone === 'function') {
                playSpellHarpTone(783.99, 0, 0.25);
            }
        }

        function closeEnchantedBook(fromHistory = false) {
            const modal = document.getElementById('enchantedBookModal');
            if (modal) modal.classList.remove('active');

            if (isBookModalOpen && !fromHistory) {
                if (window.history.state && window.history.state.enchantedBookOpen) {
                    window.history.back();
                }
            }
            isBookModalOpen = false;
        }

        function closeBookOnBackdrop(e) {
            if (e.target.id === 'enchantedBookModal') {
                closeEnchantedBook();
            }
        }

        // Backward compatibility: alias openGalleryItem to openEnchantedBook
        function openGalleryItem(index) {
            openEnchantedBook(index);
        }

        // Keyboard navigation for the open book (ESC to close, Arrow keys to flip)
        window.addEventListener('keydown', (e) => {
            if (!isBookModalOpen) return;
            if (e.key === 'Escape') {
                closeEnchantedBook();
            } else if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
                navigateBookMemory(1);
            } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
                navigateBookMemory(-1);
            }
        });
"""

# Replace the old Marauder's Map JS controls in index.html
js_start_marker = '// ================= Marauder\'s Map Controls & Waypoint Navigation ================='
js_end_marker = '// ================= Modal Management & Mobile History Back Navigation ================='

pos_js_start = html.find(js_start_marker)
pos_js_end = html.find(js_end_marker, pos_js_start)

if pos_js_start != -1 and pos_js_end != -1:
    html = html[:pos_js_start] + open_book_js.strip() + "\n\n        " + html[pos_js_end:]
    print("[5] Successfully replaced Gallery & Marauder JS controllers with Open Book system")
else:
    print("[Warning] Could not find JS marker, appending before </script>")
    html = html.replace('</script>', open_book_js + '\n    </script>')

# =========================================================================
# 6. Save the upgraded index.html
# =========================================================================
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("[6] Upgraded index.html written successfully!")
