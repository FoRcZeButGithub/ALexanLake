# -*- coding: utf-8 -*-
"""
Update Enchanted Open Book typography to match the rest of the site (SOV Yoona & Sarun HarryPotter),
and implement the rich 3D page-turning flip animation with sound and dynamic shadows.
"""
import shutil
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# =========================================================================
# 1. UPGRADE CSS FOR FONTS & 3D PAGE-TURNING ANIMATION
# =========================================================================
# Find the start of the book modal CSS
marker_start = '/* ==========================================================================\n           ENCHANTED OPEN BOOK (GRIMOIRE) MODAL & PURE MARAUDER\'S MAP STYLES'
marker_end = '/* ===== TAB 4: ABOUT ===== */'

pos_start = html.find(marker_start)
pos_end = html.find(marker_end)

if pos_start == -1:
    # Try alternate match
    pos_start = html.find('ENCHANTED OPEN BOOK (GRIMOIRE) MODAL')
    pos_start = html.rfind('/*', 0, pos_start)

print("Found CSS start at:", pos_start, "and end at:", pos_end)

new_book_css = """/* ==========================================================================
           ENCHANTED OPEN BOOK (GRIMOIRE) MODAL & PURE MARAUDER'S MAP STYLES
           Consistent Typography (SOV Yoona & Sarun HarryPotter) + 3D Page Turn Animation
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
            padding: 10px 30px;
            font-family: 'Sarun HarryPotter', 'SOV Yoona', 'Noto Serif Thai', cursive, serif;
            font-size: 1.55rem;
            letter-spacing: 0.5px;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 14px;
            box-shadow: 
                0 8px 24px rgba(0, 0, 0, 0.85),
                0 0 20px rgba(223, 162, 44, 0.35),
                inset 0 0 15px rgba(255, 215, 0, 0.15);
            transition: all 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            user-select: none;
        }

        .marauder-ribbon-btn:hover {
            transform: translateY(-3px) scale(1.03);
            border-color: var(--gold-bright);
            color: #ffffff;
            box-shadow: 
                0 14px 32px rgba(0, 0, 0, 0.95),
                0 0 35px rgba(223, 162, 44, 0.65),
                inset 0 0 25px rgba(255, 215, 0, 0.3);
        }

        .ribbon-wand-icon {
            font-size: 1.3rem;
            color: var(--gold-bright);
            animation: wandPulse 2s infinite ease-in-out;
        }

        @keyframes wandPulse {
            0%, 100% { transform: scale(1); filter: drop-shadow(0 0 4px #ffd000); }
            50% { transform: scale(1.25); filter: drop-shadow(0 0 12px #fffaaa); }
        }

        .ribbon-sub {
            font-family: 'Sarun HarryPotter', 'Cinzel', cursive, serif;
            font-size: 1.1rem;
            color: #d8be8d;
            font-style: italic;
            border-left: 1.5px solid rgba(223, 162, 44, 0.4);
            padding-left: 14px;
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
            perspective: 2500px;
            width: 100%;
            max-width: 980px;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* The Hardcover 3D Open Tome */
        .magical-open-tome {
            position: relative;
            width: 100%;
            border-radius: 12px;
            transform: scale(0.85) rotateX(10deg);
            opacity: 0;
            transition: transform 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.2), opacity 0.4s ease;
            box-shadow: 
                0 35px 85px rgba(0, 0, 0, 0.95),
                0 0 55px rgba(223, 162, 44, 0.3);
        }

        .enchanted-book-scrim.active .magical-open-tome {
            transform: scale(1) rotateX(0deg);
            opacity: 1;
            animation: tomeOpenFromSpine 0.55s cubic-bezier(0.175, 0.885, 0.32, 1.15) forwards;
        }

        @keyframes tomeOpenFromSpine {
            0% {
                opacity: 0;
                transform: perspective(2500px) scale(0.7) rotateX(14deg) rotateY(-8deg);
            }
            70% {
                opacity: 1;
                transform: perspective(2500px) scale(1.02) rotateX(-2deg) rotateY(1deg);
            }
            100% {
                opacity: 1;
                transform: perspective(2500px) scale(1) rotateX(0deg) rotateY(0deg);
            }
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

        /* Two-Page Open Parchment Spread with 3D Perspective Gutter */
        .tome-spread {
            position: relative;
            z-index: 2;
            display: flex;
            background: #eddcb8;
            border-radius: 6px;
            overflow: hidden;
            min-height: 530px;
            box-shadow: inset 0 0 35px rgba(80, 40, 10, 0.35);
            perspective: 1800px;
            transform-style: preserve-3d;
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
            transform-style: preserve-3d;
            backface-visibility: hidden;
        }

        .tome-page.left-page {
            box-shadow: inset -22px 0 26px -12px rgba(60, 30, 8, 0.45);
            border-right: 1px solid rgba(138, 92, 40, 0.2);
            transform-origin: right center;
        }

        .tome-page.right-page {
            box-shadow: inset 22px 0 26px -12px rgba(60, 30, 8, 0.45);
            border-left: 1px solid rgba(138, 92, 40, 0.2);
            transform-origin: left center;
        }

        /* =============================================================
           3D REALISTIC PAGE-TURNING ANIMATIONS (NEXT & PREV FLIP)
           ============================================================= */

        /* FLIP NEXT (Turning right page towards left) */
        .tome-spread.flip-next .right-page {
            animation: flipRightPageNext 0.48s cubic-bezier(0.55, 0.055, 0.675, 0.19) forwards;
        }
        .tome-spread.flip-next .left-page {
            animation: settleLeftPageNext 0.48s cubic-bezier(0.215, 0.61, 0.355, 1) forwards;
        }

        @keyframes flipRightPageNext {
            0% {
                transform: rotateY(0deg);
                box-shadow: inset 22px 0 26px -12px rgba(60, 30, 8, 0.45);
                filter: brightness(1);
            }
            45% {
                transform: rotateY(-60deg) scale(0.96);
                box-shadow: inset 60px 0 45px rgba(35, 12, 4, 0.65);
                filter: brightness(0.85);
            }
            100% {
                transform: rotateY(-90deg) scale(0.92);
                box-shadow: inset 100px 0 60px rgba(20, 5, 0, 0.85);
                opacity: 0.15;
                filter: brightness(0.7);
            }
        }

        @keyframes settleLeftPageNext {
            0% {
                opacity: 0.5;
                transform: scale(0.97) translateX(10px);
                filter: brightness(0.9);
            }
            100% {
                opacity: 1;
                transform: scale(1) translateX(0);
                filter: brightness(1);
            }
        }

        /* FLIP PREV (Turning left page towards right) */
        .tome-spread.flip-prev .left-page {
            animation: flipLeftPagePrev 0.48s cubic-bezier(0.55, 0.055, 0.675, 0.19) forwards;
        }
        .tome-spread.flip-prev .right-page {
            animation: settleRightPagePrev 0.48s cubic-bezier(0.215, 0.61, 0.355, 1) forwards;
        }

        @keyframes flipLeftPagePrev {
            0% {
                transform: rotateY(0deg);
                box-shadow: inset -22px 0 26px -12px rgba(60, 30, 8, 0.45);
                filter: brightness(1);
            }
            45% {
                transform: rotateY(60deg) scale(0.96);
                box-shadow: inset -60px 0 45px rgba(35, 12, 4, 0.65);
                filter: brightness(0.85);
            }
            100% {
                transform: rotateY(90deg) scale(0.92);
                box-shadow: inset -100px 0 60px rgba(20, 5, 0, 0.85);
                opacity: 0.15;
                filter: brightness(0.7);
            }
        }

        @keyframes settleRightPagePrev {
            0% {
                opacity: 0.5;
                transform: scale(0.97) translateX(-10px);
                filter: brightness(0.9);
            }
            100% {
                opacity: 1;
                transform: scale(1) translateX(0);
                filter: brightness(1);
            }
        }

        /* Settle In Glow effect upon page arrival */
        .tome-spread.page-settled .tome-page {
            animation: pageArriveGlow 0.4s ease-out;
        }

        @keyframes pageArriveGlow {
            0% {
                box-shadow: inset 0 0 40px rgba(243, 199, 102, 0.45);
            }
            100% {
                box-shadow: inset 0 0 0px transparent;
            }
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
            border: 1.5px solid rgba(138, 92, 40, 0.5);
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
            font-family: 'Sarun HarryPotter', 'Cinzel', cursive, serif;
            font-size: 1.35rem;
            font-weight: 700;
            letter-spacing: 2px;
            color: #7a151e;
            text-shadow: 0 1px 2px rgba(0, 0, 0, 0.15);
        }

        .plate-tag {
            font-family: 'SOV Yoona', 'Noto Serif Thai', serif;
            font-size: 1.1rem;
            color: #5c3818;
            letter-spacing: 0.3px;
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
            font-family: 'Sarun HarryPotter', 'Harry Potter', cursive;
            font-size: 1.95rem;
            color: #3b1b0b;
            letter-spacing: 0.5px;
            margin-bottom: 2px;
            text-shadow: 0 1px 2px rgba(255, 235, 180, 0.5);
        }

        .caption-stamp {
            font-family: 'Cinzel', 'Sarun HarryPotter', serif;
            font-size: 0.8rem;
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
            padding-top: 12px;
            margin-top: 14px;
        }

        .tome-nav-btn {
            background: rgba(60, 20, 10, 0.08);
            border: 1.5px solid rgba(138, 92, 40, 0.55);
            border-radius: 8px;
            padding: 6px 16px;
            color: #5c2415;
            font-family: 'SOV Yoona', 'Sarun HarryPotter', serif;
            font-size: 1.15rem;
            font-weight: 600;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: all 0.25s ease;
            user-select: none;
        }

        .tome-nav-btn:hover {
            background: #7a151e;
            color: #ffffff;
            border-color: #7a151e;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        }

        .tome-page-counter {
            font-family: 'Cinzel', 'Sarun HarryPotter', serif;
            font-size: 1.05rem;
            font-weight: 700;
            color: #8c5722;
            letter-spacing: 1.5px;
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
            padding: 5px 16px;
            font-family: 'SOV Yoona', 'Sarun HarryPotter', serif;
            font-size: 1.05rem;
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
            margin-top: 10px;
            margin-bottom: 12px;
        }

        .journal-latin-sub {
            font-family: 'Cinzel', 'Sarun HarryPotter', serif;
            font-size: 0.85rem;
            letter-spacing: 2px;
            color: #8c5722;
            font-weight: 700;
            margin-bottom: 4px;
        }

        .journal-title {
            font-family: 'Sarun HarryPotter', 'Harry Potter', cursive;
            font-size: 2.2rem;
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

        /* Journal Body Text & Drop Cap matching Information & Home tab */
        .journal-body-content {
            flex: 1;
            overflow-y: auto;
            max-height: 285px;
            padding-right: 8px;
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
            font-family: 'SOV Yoona', 'Samphan Condensed', 'Noto Serif Thai', serif;
            font-size: 1.4rem;
            color: #1f0f04;
            line-height: 2.15;
            letter-spacing: 0.35px;
            text-align: justify;
        }

        .drop-cap {
            float: left;
            font-family: 'Sarun HarryPotter', 'Cinzel', cursive, serif;
            font-size: 3.6rem;
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
            font-family: 'SOV Yoona', 'Noto Serif Thai', serif;
            font-size: 0.95rem;
            color: #7a4a20;
            font-style: italic;
        }

        .sig-name {
            font-family: 'Satisfy', 'Lobster Two', 'Cinzel', cursive;
            font-size: 1.85rem;
            color: #630c14;
            letter-spacing: 0.5px;
            font-weight: normal;
        }

        .tome-wax-seal-badge {
            width: 50px;
            height: 58px;
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
                font-size: 1.25rem;
                padding: 8px 20px;
            }

            .ribbon-sub {
                display: none;
            }
        }
"""

html = html[:pos_start] + new_book_css + "\n\n        " + html[pos_end:]
print("[1] Updated CSS with consistent fonts and 3D page flip animation rules.")

# =========================================================================
# 2. UPGRADE JAVASCRIPT FOR 3D PAGE FLIP ANIMATION & SOUND
# =========================================================================
js_func_marker = 'function navigateBookMemory(direction) {'
pos_js = html.find(js_func_marker)
pos_close_book = html.find('function closeEnchantedBook', pos_js)

new_navigate_js = """let isPageFlipping = false;

        function playPageTurnSound() {
            if (!audioCtx) {
                const AudioContext = window.AudioContext || window.webkitAudioContext;
                if (AudioContext) audioCtx = new AudioContext();
            }
            if (!audioCtx) return;
            try {
                // Soft paper flutter noise
                const bufferSize = Math.floor(audioCtx.sampleRate * 0.14);
                const buffer = audioCtx.createBuffer(1, bufferSize, audioCtx.sampleRate);
                const data = buffer.getChannelData(0);
                for (let i = 0; i < bufferSize; i++) {
                    data[i] = (Math.random() * 2 - 1) * Math.exp(-i / (bufferSize * 0.35));
                }
                const noise = audioCtx.createBufferSource();
                noise.buffer = buffer;
                const filter = audioCtx.createBiquadFilter();
                filter.type = 'bandpass';
                filter.frequency.value = 1400;
                filter.Q.value = 1.2;
                const gain = audioCtx.createGain();
                gain.gain.setValueAtTime(0.09, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.14);
                noise.connect(filter);
                filter.connect(gain);
                gain.connect(audioCtx.destination);
                noise.start();

                // Gentle enchanted harp chime
                playSpellHarpTone(783.99, 0.04, 0.3);
            } catch(e) {}
        }

        function navigateBookMemory(direction) {
            if (isPageFlipping) return; // Prevent spamming while animating
            isPageFlipping = true;

            const total = galleryStories.length;
            currentBookIndex = (currentBookIndex + direction + total) % total;

            const spread = document.getElementById('tomeSpread');
            const animClass = direction > 0 ? 'flip-next' : 'flip-prev';

            playPageTurnSound();

            if (spread) {
                spread.classList.remove('flip-next', 'flip-prev', 'page-settled');
                // Trigger reflow to restart animation cleanly
                void spread.offsetWidth;
                spread.classList.add(animClass);

                // At the halfway mark (240ms), update the content while the page is edge-on
                setTimeout(() => {
                    renderBookPage(currentBookIndex);
                }, 240);

                // Animation finishes: remove flip class, trigger golden settle glow
                setTimeout(() => {
                    spread.classList.remove(animClass);
                    spread.classList.add('page-settled');
                    isPageFlipping = false;
                }, 490);
            } else {
                renderBookPage(currentBookIndex);
                isPageFlipping = false;
            }
        }"""

if pos_js != -1 and pos_close_book != -1:
    html = html[:pos_js] + new_navigate_js.strip() + "\n\n        " + html[pos_close_book:]
    print("[2] Updated navigateBookMemory with 3D animation timing and sound.")
else:
    print("[Warning] Could not find navigateBookMemory function position!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("[3] Successfully updated index.html with new fonts and animations!")
