# -*- coding: utf-8 -*-
"""
Apply Harry Potter x Modern Editorial Poster Layout to index.html.
Preserves authentic Gryffindor / Hogwarts character lore for Alexan Nigelus Lake.
Starts from clean index.html.before_poster.bak.
"""

import shutil
import re

# 1. Restore from clean backup
shutil.copyfile('index.html.before_poster.bak', 'index.html')
print("[1] Restored clean base from index.html.before_poster.bak")

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 2. Update Google Fonts in <head>
gfonts_old = 'https://fonts.googleapis.com/css2?family=Alex+Brush&family=Cinzel:wght@700;900&family=Great+Vibes&family=Noto+Serif+Thai:wght@400;600&display=swap'
gfonts_new = 'https://fonts.googleapis.com/css2?family=Alex+Brush&family=Cinzel:wght@700;900&family=Great+Vibes&family=Noto+Serif+Thai:wght@400;600&family=Bebas+Neue&family=Big+Shoulders+Display:wght@700;800;900&family=Outfit:wght@400;500;600;700;800;900&family=Inter:wght@400;600;700;800&display=swap'

if gfonts_old in content:
    content = content.replace(gfonts_old, gfonts_new)
    print("[2] Updated Google Fonts with Bebas Neue, Big Shoulders Display, Outfit, Inter")
else:
    content = content.replace('</head>', f'    <link href="{gfonts_new}" rel="stylesheet">\n</head>')
    print("[2] Injected new Google Fonts into <head>")

# 3. CSS for Harry Potter Editorial Poster Layout
hp_poster_css = """
        /* ==========================================================================
           HARRY POTTER x MODERN EDITORIAL POSTER (ALEXAN LAKE - HOME TAB)
           Fuses modern graphic poster composition with Gryffindor & Hogwarts identity
           ========================================================================== */

        body.home-hp-poster-active {
            background-color: #120306;
            transition: background-color 0.4s ease;
        }

        /* Subtle atmospheric control on Home: keep soft magic embers & wand trail */
        body.home-hp-poster-active .gryffindor-banner-left,
        body.home-hp-poster-active .gryffindor-banner-right,
        body.home-hp-poster-active .floating-candle,
        body.home-hp-poster-active .bg-lion-watermark {
            opacity: 0.12 !important;
            transition: opacity 0.4s ease;
        }

        body.home-hp-poster-active .top-crest-shield {
            display: none !important;
        }

        /* Palette Theme Modifiers (Controlled via House Aura Widget) */
        body.home-hp-poster-active.aura-obsidian .hp-editorial-canvas {
            background: radial-gradient(circle at 75% 25%, #1e131d 0%, #100a12 65%, #080509 100%);
            border-color: rgba(223, 162, 44, 0.25);
            box-shadow: 0 25px 70px rgba(0, 0, 0, 0.8), 0 0 50px rgba(138, 20, 36, 0.2);
        }
        body.home-hp-poster-active.aura-parchment .hp-editorial-canvas {
            background: radial-gradient(circle at 60% 40%, #f7f1e4 0%, #ece1cd 70%, #dfd1b8 100%);
            border-color: rgba(94, 21, 28, 0.35);
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.45);
        }
        body.home-hp-poster-active.aura-parchment .hp-mega-title-line,
        body.home-hp-poster-active.aura-parchment .hp-sub-house-title,
        body.home-hp-poster-active.aura-parchment .hp-nav-words {
            color: #2b0c10 !important;
            -webkit-text-fill-color: #2b0c10 !important;
        }
        body.home-hp-poster-active.aura-parchment .hp-poster-dot {
            background: #4a131a !important;
        }
        body.home-hp-poster-active.aura-parchment .hp-bottom-caption {
            color: #5c1b24 !important;
        }

        /* Section Container */
        #tab-home {
            position: relative;
            width: 100%;
            max-width: 1360px;
            margin: 0 auto;
            padding: 10px 18px 120px 18px;
            box-sizing: border-box;
            user-select: none;
        }

        #tab-home .parchment-frame {
            background: transparent !important;
            border: none !important;
            outline: none !important;
            box-shadow: none !important;
            padding: 0 !important;
            margin: 0 !important;
        }

        /* Main Editorial Poster Canvas */
        .hp-editorial-canvas {
            position: relative;
            width: 100%;
            min-height: 650px;
            background: radial-gradient(circle at 75% 20%, #2f070e 0%, #1c0307 50%, #0d0103 100%);
            border: 2px solid rgba(223, 162, 44, 0.45);
            border-radius: 30px;
            padding: 24px 38px 40px 38px;
            box-sizing: border-box;
            overflow: hidden;
            box-shadow: 
                0 25px 70px rgba(0, 0, 0, 0.85),
                0 0 45px rgba(223, 162, 44, 0.2),
                inset 0 1px 1px rgba(255, 235, 170, 0.3);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: background 0.4s ease, border-color 0.4s ease, box-shadow 0.4s ease;
        }

        /* Subtle Floating Magic Sparks & Dust Dots */
        .hp-poster-dot {
            position: absolute;
            width: 5px;
            height: 5px;
            background: #dfa22c;
            border-radius: 50%;
            opacity: 0.75;
            box-shadow: 0 0 8px #ffd875;
            pointer-events: none;
            z-index: 2;
            animation: dotGlowPulse 4s ease-in-out infinite alternate;
        }

        @keyframes dotGlowPulse {
            from { opacity: 0.4; transform: scale(0.9); }
            to { opacity: 0.95; transform: scale(1.3); }
        }

        /* ----------------------------------------------------
           1. TOP HEADER: COURAGE  CHIVALRY  •  GRYFFINDOR  PRIDE
           ---------------------------------------------------- */
        .hp-poster-top-header {
            position: relative;
            z-index: 20;
            display: flex;
            align-items: center;
            justify-content: space-between;
            width: 100%;
            padding: 4px 0 16px 0;
        }

        .hp-nav-words {
            display: flex;
            align-items: center;
            gap: 26px;
            font-family: 'Outfit', 'Cinzel', serif;
            font-weight: 800;
            font-size: 1.05rem;
            letter-spacing: 4px;
            color: #ffd875;
            margin-left: 45%;
            text-transform: uppercase;
            text-shadow: 0 2px 8px rgba(0, 0, 0, 0.8), 0 0 15px rgba(223, 162, 44, 0.4);
            transition: color 0.3s ease;
        }

        .hp-nav-dot {
            font-size: 1.25rem;
            color: #dfa22c;
        }

        .hp-top-actions {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .hp-circle-action-btn {
            width: 46px;
            height: 46px;
            border-radius: 50%;
            background: #140205;
            border: 1.5px solid #dfa22c;
            color: #ffd875;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 14px rgba(0, 0, 0, 0.7), 0 0 10px rgba(223, 162, 44, 0.25);
            transition: transform 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275), background 0.3s ease, box-shadow 0.3s ease;
        }

        .hp-circle-action-btn:hover {
            transform: scale(1.12);
            background: #2a050c;
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.85), 0 0 18px rgba(243, 194, 82, 0.55);
            color: #ffffff;
        }

        .hp-circle-action-btn svg {
            width: 22px;
            height: 22px;
            fill: currentColor;
        }

        /* ----------------------------------------------------
           2. TOP "QUIDDITCH ARCHIVE" CAPSULE PILL WIDGET
           ---------------------------------------------------- */
        .hp-gallery-capsule {
            position: absolute;
            top: 66px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 25;
            background: #100103;
            border: 1.5px solid #dfa22c;
            color: #ffd875;
            border-radius: 9999px;
            padding: 6px 14px 6px 16px;
            display: inline-flex;
            align-items: center;
            gap: 14px;
            cursor: pointer;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.8), 0 0 16px rgba(223, 162, 44, 0.35);
            transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.3s ease;
        }

        .hp-gallery-capsule:hover {
            transform: translateX(-50%) translateY(-2px) scale(1.05);
            box-shadow: 0 12px 28px rgba(0, 0, 0, 0.9), 0 0 25px rgba(243, 194, 82, 0.6);
        }

        .hp-capsule-dots {
            font-size: 13px;
            letter-spacing: 2px;
            color: #dfa22c;
            font-weight: 700;
        }

        .hp-capsule-label {
            font-family: 'Outfit', 'Cinzel', serif;
            font-weight: 700;
            font-size: 0.95rem;
            letter-spacing: 1px;
            text-transform: uppercase;
        }

        .hp-capsule-close {
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background: #dfa22c;
            color: #100103;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 11px;
            font-weight: 900;
            cursor: pointer;
            transition: transform 0.2s ease, background 0.2s ease;
        }

        .hp-capsule-close:hover {
            transform: rotate(90deg);
            background: #ffffff;
        }

        /* ----------------------------------------------------
           3. MAIN GRID: LEFT (ALEXAN + WIDGETS) & RIGHT (TYPOGRAPHY)
           ---------------------------------------------------- */
        .hp-poster-grid {
            position: relative;
            z-index: 10;
            display: grid;
            grid-template-columns: 46% 54%;
            min-height: 550px;
            align-items: center;
            width: 100%;
        }

        /* Layered Depth Cards behind Character */
        .hp-bg-card-layer-1 {
            position: absolute;
            left: 20px;
            top: 20px;
            width: 320px;
            height: 480px;
            border-radius: 34px;
            background: rgba(30, 4, 8, 0.75);
            border: 1.5px solid rgba(223, 162, 44, 0.35);
            box-shadow: 0 20px 45px rgba(0, 0, 0, 0.7);
            pointer-events: none;
            z-index: 1;
            transform: rotate(-3deg);
        }

        .hp-bg-card-layer-2 {
            position: absolute;
            left: 5px;
            top: 60px;
            width: 260px;
            height: 400px;
            border-radius: 30px;
            background: #0d0102;
            border: 1px solid rgba(223, 162, 44, 0.2);
            opacity: 0.95;
            box-shadow: 0 25px 60px rgba(0, 0, 0, 0.85);
            pointer-events: none;
            z-index: 2;
            transform: rotate(2deg);
        }

        /* Hero Character Column */
        .hp-hero-column {
            position: relative;
            z-index: 10;
            height: 100%;
            display: flex;
            align-items: flex-end;
            justify-content: center;
        }

        .hp-hero-artwork-frame {
            position: relative;
            width: 100%;
            max-width: 440px;
            height: 590px;
            display: flex;
            align-items: flex-end;
            justify-content: center;
            z-index: 8;
        }

        /* The Hero Image Slot */
        .hp-hero-img {
            max-width: 100%;
            max-height: 100%;
            object-fit: contain;
            object-position: bottom center;
            display: block;
            filter: drop-shadow(0 15px 35px rgba(0, 0, 0, 0.95)) drop-shadow(0 0 20px rgba(223, 162, 44, 0.3));
            transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            pointer-events: auto;
        }

        .hp-hero-artwork-frame:hover .hp-hero-img {
            transform: scale(1.03) translateY(-6px);
        }

        /* ----------------------------------------------------
           4. HARRY POTTER THEMED FLOATING WIDGETS
           ---------------------------------------------------- */

        /* Widget: BRAVE AT HEART (Upper Badge) */
        .hp-widget-brave {
            position: absolute;
            top: 75px;
            left: 350px;
            z-index: 16;
            border: 1.5px solid #dfa22c;
            border-radius: 8px;
            padding: 4px 8px;
            font-family: 'Outfit', 'Cinzel', serif;
            font-size: 0.62rem;
            font-weight: 800;
            letter-spacing: 1.5px;
            line-height: 1.15;
            text-align: center;
            color: #ffd875;
            background: rgba(18, 2, 5, 0.85);
            backdrop-filter: blur(6px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.6), 0 0 8px rgba(223, 162, 44, 0.3);
            pointer-events: none;
        }

        /* Widget: HOUSE AURA (Palette Swatches Card) */
        .hp-widget-aura {
            position: absolute;
            top: 115px;
            left: 310px;
            z-index: 18;
            background: #140205;
            border: 1.5px solid #dfa22c;
            border-radius: 20px;
            padding: 10px 16px 12px 16px;
            box-shadow: 0 14px 35px rgba(0, 0, 0, 0.8), 0 0 15px rgba(223, 162, 44, 0.25);
            display: flex;
            flex-direction: column;
            gap: 8px;
            cursor: default;
            transition: transform 0.3s ease;
        }

        .hp-widget-aura:hover {
            transform: translateY(-3px);
        }

        .hp-aura-head {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            font-family: 'Outfit', 'Cinzel', serif;
            font-size: 0.78rem;
            font-weight: 800;
            color: #ffd875;
            letter-spacing: 1px;
            text-transform: uppercase;
        }

        .hp-aura-menu-icon {
            font-size: 14px;
            color: #dfa22c;
            cursor: pointer;
        }

        .hp-aura-swatches-row {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .hp-swatch-chip {
            width: 22px;
            height: 22px;
            border-radius: 50%;
            border: 2px solid transparent;
            cursor: pointer;
            transition: transform 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.2s ease;
        }

        .hp-swatch-chip:hover {
            transform: scale(1.22);
            box-shadow: 0 0 10px #ffd875;
        }

        .chip-gryffindor {
            background: linear-gradient(135deg, #8b1525 0%, #dfa22c 100%);
            border-color: #ffd875;
        }
        .chip-obsidian {
            background: #110d14;
            border-color: #554460;
        }
        .chip-parchment {
            background: #f7f1e4;
            border-color: #8a2a36;
        }

        /* Widget: Circular Profile / Crest Button */
        .hp-widget-profile-btn {
            position: absolute;
            top: 215px;
            left: 360px;
            z-index: 18;
            width: 54px;
            height: 54px;
            border-radius: 50%;
            background: #190307;
            border: 2px solid #dfa22c;
            color: #ffd875;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.85), 0 0 15px rgba(223, 162, 44, 0.35);
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), background 0.3s ease, box-shadow 0.3s ease;
        }

        .hp-widget-profile-btn:hover {
            transform: scale(1.15) rotate(8deg);
            background: #32060e;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.95), 0 0 25px rgba(243, 194, 82, 0.65);
        }

        .hp-widget-profile-btn svg {
            width: 24px;
            height: 24px;
            fill: currentColor;
        }

        /* Widget: MARAUDER'S LOG & Action Badges */
        .hp-widget-log-cluster {
            position: absolute;
            bottom: 40px;
            left: 270px;
            z-index: 18;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .hp-log-dark-card {
            background: #110204;
            border: 1.5px solid #dfa22c;
            color: #ffffff;
            border-radius: 18px;
            padding: 12px 20px;
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.85), 0 0 15px rgba(223, 162, 44, 0.25);
            cursor: pointer;
            transition: transform 0.25s ease, box-shadow 0.25s ease;
        }

        .hp-log-dark-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 16px 36px rgba(0, 0, 0, 0.95), 0 0 22px rgba(243, 194, 82, 0.45);
        }

        .hp-log-title {
            font-family: 'Outfit', 'Cinzel', serif;
            font-weight: 800;
            font-size: 1.05rem;
            letter-spacing: 1px;
            color: #ffd875;
        }

        .hp-log-date {
            font-family: 'Inter', sans-serif;
            font-size: 0.68rem;
            color: #d4b270;
            margin-top: 1px;
            letter-spacing: 0.8px;
        }

        .hp-log-actions-row {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .hp-reload-spell-btn {
            width: 34px;
            height: 34px;
            border-radius: 50%;
            background: #1a0307;
            color: #dfa22c;
            border: 1.5px solid #dfa22c;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.6);
            transition: transform 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        .hp-reload-spell-btn:hover {
            transform: rotate(-180deg) scale(1.15);
            color: #ffffff;
            border-color: #ffd875;
        }

        .hp-firebolt-pill-badge {
            background: #dfa22c;
            color: #120104;
            border: 2px solid #ffd875;
            border-radius: 9999px;
            padding: 4px 14px;
            font-family: 'Outfit', 'Cinzel', sans-serif;
            font-weight: 900;
            font-size: 0.88rem;
            letter-spacing: 1.5px;
            cursor: pointer;
            box-shadow: 0 4px 14px rgba(0, 0, 0, 0.5), 0 0 10px rgba(223, 162, 44, 0.4);
            transition: transform 0.2s ease, background 0.2s ease;
        }

        .hp-firebolt-pill-badge:hover {
            transform: scale(1.08);
            background: #ffd875;
        }

        .hp-shield-badge {
            width: 30px;
            height: 30px;
            border-radius: 8px;
            background: #140205;
            border: 1.5px solid #dfa22c;
            color: #dfa22c;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.6);
        }

        .hp-shield-badge svg {
            width: 17px;
            height: 17px;
        }

        /* Widget: CHASER #07 & LUMOS PILL (Left Edge) */
        .hp-widget-quidditch-side {
            position: absolute;
            bottom: 60px;
            left: 0;
            z-index: 18;
            display: flex;
            flex-direction: column;
            gap: 4px;
        }

        .hp-side-sub-text {
            font-family: 'Outfit', 'Inter', sans-serif;
            font-size: 0.68rem;
            font-weight: 800;
            color: #dfa22c;
            letter-spacing: 1px;
            text-transform: uppercase;
            padding-left: 4px;
            text-shadow: 0 1px 4px rgba(0, 0, 0, 0.8);
        }

        .hp-side-pill-btn {
            background: #140205;
            color: #ffd875;
            border: 1.5px solid #dfa22c;
            border-radius: 9999px;
            padding: 7px 18px;
            font-family: 'Outfit', 'Cinzel', serif;
            font-weight: 900;
            font-size: 1rem;
            letter-spacing: 1px;
            cursor: pointer;
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.7), 0 0 12px rgba(223, 162, 44, 0.25);
            transition: transform 0.2s ease, background 0.2s ease;
        }

        .hp-side-pill-btn:hover {
            transform: translateX(5px);
            background: #2a050c;
            color: #ffffff;
        }

        /* ----------------------------------------------------
           5. RIGHT COLUMN: GIANT CONDENSED DISPLAY TYPOGRAPHY
           ---------------------------------------------------- */
        .hp-poster-typography {
            position: relative;
            z-index: 10;
            display: flex;
            flex-direction: column;
            justify-content: center;
            padding-left: 10px;
            padding-top: 15px;
        }

        .hp-mega-text-row {
            display: flex;
            align-items: center;
            line-height: 0.82;
            margin: 0;
            padding: 0;
        }

        /* Line 1: ALEXAN & Line 2: LAKE */
        .hp-mega-title-line {
            font-family: 'Bebas Neue', 'Big Shoulders Display', 'Cinzel', sans-serif;
            font-size: clamp(6.2rem, 13.5vw, 12.8rem);
            font-weight: 900;
            letter-spacing: -1px;
            color: #ffd875;
            background: linear-gradient(180deg, #fff2c2 0%, #f3c252 55%, #c2881a 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            filter: drop-shadow(0 4px 16px rgba(0, 0, 0, 0.95)) drop-shadow(0 0 25px rgba(223, 162, 44, 0.45));
            margin: 0;
            padding: 0;
            text-transform: uppercase;
            line-height: 0.84;
            display: block;
        }

        /* Equalizer Rune Capsule Indicator */
        .hp-eq-rune-column {
            display: flex;
            flex-direction: column;
            gap: 8px;
            margin-right: 18px;
        }

        .hp-eq-capsule-unit {
            width: 14px;
            height: 38px;
            border-radius: 9999px;
            background: #140205;
            border: 2px solid #dfa22c;
            box-shadow: 0 0 10px rgba(223, 162, 44, 0.4);
        }

        /* Line 3: GRYFFINDOR */
        .hp-sub-house-title {
            font-family: 'Bebas Neue', 'Big Shoulders Display', 'Cinzel', serif;
            font-size: clamp(2.6rem, 5.2vw, 4.4rem);
            font-weight: 800;
            letter-spacing: 2px;
            color: #e5aa37;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.9), 0 0 18px rgba(229, 170, 55, 0.5);
            margin-top: 8px;
            line-height: 1;
            text-transform: uppercase;
        }

        /* Bottom-Right Motto Caption */
        .hp-bottom-caption {
            align-self: flex-end;
            margin-top: 18px;
            font-family: 'Outfit', 'Cinzel', serif;
            font-size: 0.68rem;
            font-weight: 800;
            letter-spacing: 2px;
            color: #d4b270;
            text-transform: uppercase;
            display: flex;
            align-items: center;
            gap: 6px;
            text-shadow: 0 1px 4px rgba(0, 0, 0, 0.9);
        }

        /* ----------------------------------------------------
           6. DOCK NAVIGATION IN HOME MODE
           ---------------------------------------------------- */
        body.home-hp-poster-active .common-room-dock {
            background: rgba(22, 3, 7, 0.92) !important;
            backdrop-filter: blur(18px) !important;
            -webkit-backdrop-filter: blur(18px) !important;
            border-top: 1.5px solid rgba(223, 162, 44, 0.45) !important;
            box-shadow: 0 -8px 28px rgba(0, 0, 0, 0.92), 0 0 20px rgba(223, 162, 44, 0.2) !important;
            padding: 10px 24px !important;
        }

        body.home-hp-poster-active .dock-link {
            font-family: 'Outfit', 'Cinzel', serif !important;
            font-size: 1.15rem !important;
            font-weight: 700 !important;
            letter-spacing: 1.5px !important;
            color: #dfa22c !important;
            text-transform: uppercase !important;
            padding: 6px 14px !important;
            border-radius: 8px !important;
            transition: all 0.25s ease !important;
        }

        body.home-hp-poster-active .dock-link:hover {
            color: #ffffff !important;
            transform: translateY(-2px) !important;
            text-shadow: 0 0 12px #ffd875 !important;
        }

        body.home-hp-poster-active .dock-link.active {
            color: #ffffff !important;
            background: rgba(223, 162, 44, 0.2) !important;
            box-shadow: 0 0 15px rgba(223, 162, 44, 0.3) !important;
        }

        /* ----------------------------------------------------
           7. RESPONSIVENESS
           ---------------------------------------------------- */
        @media (max-width: 1080px) {
            .hp-nav-words {
                margin-left: 35%;
                gap: 16px;
                font-size: 0.95rem;
            }
            .hp-poster-grid {
                grid-template-columns: 48% 52%;
            }
            .hp-widget-aura {
                left: 260px;
                top: 100px;
            }
            .hp-widget-profile-btn {
                left: 300px;
                top: 190px;
            }
            .hp-widget-brave {
                left: 300px;
                top: 70px;
            }
            .hp-widget-log-cluster {
                left: 220px;
                bottom: 20px;
            }
        }

        @media (max-width: 860px) {
            .hp-editorial-canvas {
                padding: 20px 16px 36px 16px;
            }
            .hp-nav-words {
                margin-left: 0;
                gap: 12px;
                font-size: 0.85rem;
            }
            .hp-gallery-capsule {
                top: 16px;
                left: auto;
                right: 120px;
                transform: none;
                padding: 4px 10px 4px 12px;
            }
            .hp-gallery-capsule:hover {
                transform: translateY(-2px);
            }
            .hp-poster-grid {
                grid-template-columns: 1fr;
                gap: 30px;
            }
            .hp-hero-column {
                order: 2;
            }
            .hp-hero-artwork-frame {
                max-width: 340px;
                height: 460px;
            }
            .hp-poster-typography {
                order: 1;
                text-align: center;
                align-items: center;
                padding-left: 0;
            }
            .hp-mega-text-row {
                justify-content: center;
            }
            .hp-bottom-caption {
                align-self: center;
            }
            .hp-widget-aura {
                left: auto;
                right: 20px;
                top: 60px;
            }
            .hp-widget-profile-btn {
                left: auto;
                right: 40px;
                top: 150px;
            }
            .hp-widget-log-cluster {
                left: auto;
                right: 20px;
                bottom: 20px;
            }
        }

        @media (max-width: 520px) {
            .hp-nav-words {
                gap: 6px;
                font-size: 0.72rem;
                letter-spacing: 1.5px;
            }
            .hp-gallery-capsule {
                display: none;
            }
            .hp-mega-title-line {
                font-size: 5.2rem;
            }
            .hp-sub-house-title {
                font-size: 2.2rem;
            }
            .hp-widget-aura,
            .hp-widget-profile-btn,
            .hp-widget-log-cluster,
            .hp-widget-quidditch-side {
                position: static;
                margin-top: 12px;
            }
            .hp-hero-column {
                flex-direction: column;
                align-items: center;
            }
        }
"""

# Inject CSS before the main </style> tag (at line ~1832)
# We find the last </style> tag in the head
last_style_idx = content.rfind('</style>')
if last_style_idx != -1:
    content = content[:last_style_idx] + f'{hp_poster_css}\n    ' + content[last_style_idx:]
    print("[3] Injected Harry Potter Editorial Poster CSS before </style>")

# 4. HTML markup for tab-home
hp_poster_html = """        <!-- ================= TAB 1: HOME (Harry Potter x Modern Editorial Poster) ================= -->
        <section id="tab-home" class="tab-content active">
            <div class="hp-editorial-canvas" id="hpPosterCanvas">

                <!-- Subtle Hogwarts Golden Dust & Magic Sparks -->
                <div class="hp-poster-dot" style="top: 8%; right: 26%;"></div>
                <div class="hp-poster-dot" style="top: 20%; left: 9%; animation-delay: 1s;"></div>
                <div class="hp-poster-dot" style="top: 42%; right: 4%; animation-delay: 2s;"></div>
                <div class="hp-poster-dot" style="bottom: 14%; right: 28%; animation-delay: 1.5s;"></div>
                <div class="hp-poster-dot" style="bottom: 26%; left: 44%; animation-delay: 0.5s;"></div>

                <!-- 1. TOP HEADER: COURAGE  CHIVALRY  •  GRYFFINDOR  PRIDE + ICON BUTTONS -->
                <header class="hp-poster-top-header">
                    <div class="hp-nav-words" aria-hidden="true">
                        <span>COURAGE</span>
                        <span>CHIVALRY</span>
                        <span class="hp-nav-dot">•</span>
                        <span>GRYFFINDOR</span>
                        <span>PRIDE</span>
                    </div>

                    <div class="hp-top-actions">
                        <button class="hp-circle-action-btn" id="hpHomeBtn" title="หน้าแรก (Gryffindor Common Room)" onclick="switchTab('home')" aria-label="Home">
                            <svg viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>
                        </button>
                        <button class="hp-circle-action-btn" id="hpMenuBtn" title="เมนูข้อมูลและสถิติเวทมนตร์ (Information)" onclick="switchTab('information')" aria-label="Information Menu">
                            <svg viewBox="0 0 24 24"><rect x="4" y="4" width="6.5" height="6.5" rx="2"/><rect x="13.5" y="4" width="6.5" height="6.5" rx="2"/><rect x="4" y="13.5" width="6.5" height="6.5" rx="2"/><rect x="13.5" y="13.5" width="6.5" height="6.5" rx="2"/></svg>
                        </button>
                    </div>
                </header>

                <!-- 2. TOP CENTER "QUIDDITCH ARCHIVE" CAPSULE PILL WIDGET -->
                <div class="hp-gallery-capsule" role="button" tabindex="0" onclick="switchTab('gallery')" title="คลิกเพื่อเปิดดูคลังภาพความทรงจำฮอกวอตส์ (Gallery Archive)">
                    <span class="hp-capsule-dots">•••</span>
                    <span class="hp-capsule-label">Quidditch Archive</span>
                    <span class="hp-capsule-close" onclick="event.stopPropagation(); switchTab('information');" title="สลับไปยังหน้าข้อมูลส่วนตัว">✕</span>
                </div>

                <!-- 3. MAIN GRID: LEFT (ALEXAN LAKE + WIDGETS) & RIGHT (CONDENSED TYPOGRAPHY) -->
                <div class="hp-poster-grid">

                    <!-- LEFT COLUMN: Character Hero & Floating Gryffindor Badges -->
                    <div class="hp-hero-column">

                        <!-- Layered Depth Cards behind Alexan -->
                        <div class="hp-bg-card-layer-1" aria-hidden="true"></div>
                        <div class="hp-bg-card-layer-2" aria-hidden="true"></div>

                        <!-- 🦁 WIDGET 1: BRAVE AT HEART BADGE -->
                        <div class="hp-widget-brave" aria-hidden="true">
                            BRAVE AT<br>HEART
                        </div>

                        <!-- 🎨 WIDGET 2: HOUSE AURA CARD (Interactive Theme Swatches) -->
                        <div class="hp-widget-aura" title="ปรับโทนสีบรรยากาศห้อง (House Aura)">
                            <div class="hp-aura-head">
                                <span>House Aura</span>
                                <span class="hp-aura-menu-icon" aria-hidden="true">⋮</span>
                            </div>
                            <div class="hp-aura-swatches-row">
                                <button class="hp-swatch-chip chip-gryffindor" onclick="setHouseAura('gryffindor')" title="สีกริฟฟินดอร์เลือดหมู-ทอง (Gryffindor Crimson & Gold)" aria-label="Gryffindor Theme"></button>
                                <button class="hp-swatch-chip chip-obsidian" onclick="setHouseAura('obsidian')" title="สีรัตติกาลปราสาทฮอกวอตส์ (Midnight Obsidian)" aria-label="Obsidian Dark Theme"></button>
                                <button class="hp-swatch-chip chip-parchment" onclick="setHouseAura('parchment')" title="สีกระดาษคัมภีร์เวทมนตร์ (Antique Parchment)" aria-label="Parchment Theme"></button>
                            </div>
                        </div>

                        <!-- 👤 WIDGET 3: CIRCULAR PROFILE CREST BUTTON -->
                        <button class="hp-widget-profile-btn" onclick="openScroll('history')" title="คลิกเพื่ออ่านประวัติ Alexan Nigelus Lake" aria-label="Character Bio">
                            <svg viewBox="0 0 24 24"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>
                        </button>

                        <!-- 📓 WIDGET 4: MARAUDER'S LOG & ACTION BADGES -->
                        <div class="hp-widget-log-cluster">
                            <div class="hp-log-dark-card" onclick="openScroll('history')" role="button" tabindex="0" title="คลิกเปิดบันทึกประวัติ (Marauder's Log Archive)">
                                <div class="hp-log-title">Marauder's Log</div>
                                <div class="hp-log-date">16 December • Quidditch Pitch</div>
                            </div>
                            <div class="hp-log-actions-row">
                                <div class="hp-reload-spell-btn" onclick="refreshMagicQuote()" role="button" tabindex="0" title="ร่ายคำคมเวทมนตร์ (Cast Quote Spell)">
                                    <svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.19"/></svg>
                                </div>
                                <div class="hp-firebolt-pill-badge" onclick="openScroll('magic')" role="button" tabindex="0" title="คลิกดูข้อมูลไม้กวาดไฟเยอร์โบลด์ (Firebolt)">FIREBOLT</div>
                                <div class="hp-shield-badge" title="Gryffindor House Crest">
                                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg>
                                </div>
                            </div>
                        </div>

                        <!-- 🧹 WIDGET 5: CHASER #07 & LUMOS PILL (Left Edge) -->
                        <div class="hp-widget-quidditch-side">
                            <div class="hp-side-sub-text">Chaser #07</div>
                            <div class="hp-side-pill-btn" onclick="switchTab('information')" role="button" tabindex="0" title="ไปยังหน้าข้อมูลตัวละคร (Information)">Lumos...</div>
                        </div>

                        <!-- 🖼️ HERO CHARACTER ARTWORK FRAME -->
                        <div class="hp-hero-artwork-frame" id="hpPosterHeroWrapper">
                            <!-- 📷 [จุดใส่รูปตัวละครของคุณ] 
                                 แทนที่ src="images/alexan-profile.jpg?v=4" ด้วยไฟล์รูปภาพของคุณ
                                 แนะนำเป็นภาพไดคัทพื้นหลังโปร่งใส (.png) เช่น images/my-character.png เพื่อให้ตัวละครลอยซ้อนทับเลเยอร์เหมือนต้นแบบอย่างสมบูรณ์แบบ -->
                            <img id="hpPosterHeroImg" src="images/alexan-profile.jpg?v=4" alt="Alexan Nigelus Lake" class="hp-hero-img"
                                 onerror="this.onerror=null; this.src='images/hogwarts-logo.png';" />
                        </div>

                    </div>

                    <!-- RIGHT COLUMN: BESPOKE HARRY POTTER DISPLAY TYPOGRAPHY -->
                    <div class="hp-poster-typography">
                        
                        <!-- Line 1: ALEXAN -->
                        <div class="hp-mega-text-row">
                            <h1 class="hp-mega-title-line" title="Alexan">ALEXAN</h1>
                        </div>

                        <!-- Line 2: LAKE with Equalizer Rune Indicator -->
                        <div class="hp-mega-text-row">
                            <div class="hp-eq-rune-column" aria-hidden="true">
                                <div class="hp-eq-capsule-unit"></div>
                                <div class="hp-eq-capsule-unit"></div>
                            </div>
                            <div class="hp-mega-title-line" title="Lake">LAKE</div>
                        </div>

                        <!-- Line 3: GRYFFINDOR -->
                        <div class="hp-sub-house-title" title="Gryffindor House">GRYFFINDOR</div>

                        <!-- Bottom-right Latin Motto Caption -->
                        <div class="hp-bottom-caption">
                            <span>•</span> FORTI ANIMI INVENTORES • HOGWARTS CASTLE
                        </div>

                    </div>

                </div>

            </div>
        </section>"""

# Replace existing tab-home section
pattern = r'<section id="tab-home".*?</section>'
match = re.search(pattern, content, re.DOTALL)
if match:
    content = content[:match.start()] + hp_poster_html + content[match.end():]
    print("[4] Replaced tab-home with bespoke Harry Potter Editorial Poster markup")

# 5. JavaScript Helper Functions
hp_poster_js = """
        // ================= Harry Potter Editorial Poster Helpers =================
        function setHouseAura(auraName) {
            document.body.classList.remove('aura-obsidian', 'aura-parchment');
            if (auraName === 'obsidian') {
                document.body.classList.add('aura-obsidian');
            } else if (auraName === 'parchment') {
                document.body.classList.add('aura-parchment');
            }
        }

        const hpCharacterQuotes = [
            '"ความเร็วน่ะไม่ใช่แค่เรื่องของการบิน แต่มันคือการตัดสินใจในเสี้ยววินาที" — Alex Lake',
            '"หัวใจแห่งความกล้าหาญของกริฟฟินดอร์ ไม่เคยสูญเสียไปตามร่างกายเลย" — Alexan Nigelus Lake',
            '"ไม้กวาดไฟเยอร์โบลด์คู่ใจ พร้อมพุ่งทะยานสู่สนามเสมอ" — Quidditch Pitch',
            '"อย่าเข้ามาข้างหลังทางจุดบอดด้านซ้ายเด็ดขาด... เตือนแล้วนะ!" — Alex Lake',
            '"ระเบิดควันแกล้งคนน่ะเหรอ? ผมแค่ทดลองคาถาศาสตร์มืดในแบบของผมเองต่างหาก!" — Alex Lake'
        ];
        let hpQuoteIdx = 0;

        function refreshMagicQuote() {
            hpQuoteIdx = (hpQuoteIdx + 1) % hpCharacterQuotes.length;
            const quote = hpCharacterQuotes[hpQuoteIdx];
            const btn = document.querySelector('.hp-reload-spell-btn');
            if (btn) {
                btn.style.transform = 'rotate(-360deg) scale(1.2)';
                setTimeout(() => btn.style.transform = '', 350);
            }
            openScrollCustom('คำคมเวทมนตร์ประจำตัว (Character Quote)', `<div style="padding: 12px 4px; font-family: 'SOV Yoona', serif; font-size: 1.45rem; color: #320c10; line-height: 2; letter-spacing: 0.35px;">${quote}</div>`);
        }

        function openScrollCustom(title, htmlContent) {
            const header = document.getElementById('scrollHeader');
            const contentEl = document.getElementById('scrollContent');
            const modal = document.getElementById('scrollModal');
            if (header && contentEl && modal) {
                header.innerHTML = title;
                contentEl.innerHTML = htmlContent;
                modal.classList.add('active');
                isModalOpen = true;
            }
        }

        // Initialize Home Poster Mode on DOM Ready
        function initHpPosterMode() {
            const homeTab = document.getElementById('tab-home');
            if (homeTab && homeTab.classList.contains('active')) {
                document.body.classList.add('home-hp-poster-active');
            }
        }
        window.addEventListener('DOMContentLoaded', initHpPosterMode);
        initHpPosterMode();
"""

# Update switchTab
old_switchTab = """        function switchTab(tabId) {
            document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.dock-link').forEach(el => el.classList.remove('active'));

            const target = document.getElementById(`tab-${tabId}`);
            if (target) {
                target.classList.add('active');
                if (tabId === 'information') {
                    animateStatBars();
                }
            }

            // Query active dock button by data-tab attribute
            const activeBtn = document.querySelector(`.dock-link[data-tab="${tabId}"]`);
            if (activeBtn) activeBtn.classList.add('active');

            window.scrollTo({ top: 0, behavior: 'smooth' });
        }"""

new_switchTab = """        function switchTab(tabId) {
            document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.dock-link').forEach(el => el.classList.remove('active'));

            const target = document.getElementById(`tab-${tabId}`);
            if (target) {
                target.classList.add('active');
                if (tabId === 'home') {
                    document.body.classList.add('home-hp-poster-active');
                } else {
                    document.body.classList.remove('home-hp-poster-active');
                }
                if (tabId === 'information') {
                    animateStatBars();
                }
            }

            // Query active dock button by data-tab attribute
            const activeBtn = document.querySelector(`.dock-link[data-tab="${tabId}"]`);
            if (activeBtn) activeBtn.classList.add('active');

            window.scrollTo({ top: 0, behavior: 'smooth' });
        }"""

if old_switchTab in content:
    content = content.replace(old_switchTab, new_switchTab)
    print("[5] Updated switchTab to toggle home-hp-poster-active")

if 'Harry Potter Editorial Poster Helpers' not in content:
    content = content.replace('    <script>', f'    <script>\n{hp_poster_js}')
    print("[6] Injected Harry Potter Editorial Poster JS helpers")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("[DONE] Successfully generated index.html with Harry Potter x Modern Editorial Poster!")
