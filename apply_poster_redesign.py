# -*- coding: utf-8 -*-
"""
Script to apply the editorial character poster design to index.html (Home page).
Matches the provided reference image layout and widgets with high precision.
"""

import os
import re

INDEX_FILE = 'index.html'

with open(INDEX_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Google Fonts in <head>
old_fonts = 'https://fonts.googleapis.com/css2?family=Alex+Brush&family=Cinzel:wght@700;900&family=Great+Vibes&family=Noto+Serif+Thai:wght@400;600&display=swap'
new_fonts = 'https://fonts.googleapis.com/css2?family=Alex+Brush&family=Cinzel:wght@700;900&family=Great+Vibes&family=Noto+Serif+Thai:wght@400;600&family=Anton&family=Bebas+Neue&family=Big+Shoulders+Display:wght@700;800;900&family=Inter:wght@400;500;600;700;800;900&family=Outfit:wght@400;500;600;700;800;900&display=swap'

if old_fonts in content:
    content = content.replace(old_fonts, new_fonts)
    print("[1] Updated Google Fonts URL")
else:
    print("[1] Old fonts link not matched exactly, checking alternate...")
    if 'Bebas+Neue' not in content:
        content = content.replace('</head>', f'    <link href="{new_fonts}" rel="stylesheet">\n</head>')
        print("[1] Injected new Google Fonts into <head>")

# 2. Modern Poster CSS
poster_css = """
        /* ==========================================================================
           MODERN EDITORIAL CHARACTER POSTER STYLES (HOME TAB)
           Matches Reference: Megan Tuto's / Dargahonel Poster Layout & UI Widgets
           ========================================================================== */

        /* When on Home tab, isolate from Hogwarts castle banners & candles for pristine editorial look */
        body.home-poster-active .gryffindor-banner-left,
        body.home-poster-active .gryffindor-banner-right,
        body.home-poster-active .floating-candle,
        body.home-poster-active .bg-lion-watermark,
        body.home-poster-active .top-crest-shield,
        body.home-poster-active .golden-snitch {
            opacity: 0 !important;
            pointer-events: none !important;
            visibility: hidden !important;
            transition: opacity 0.3s ease;
        }

        body.home-poster-active {
            background: #ebebee;
            transition: background-color 0.4s ease;
        }

        /* Poster Themes toggled via Color Styles widget */
        body.home-poster-active.theme-charcoal {
            background: #151518;
        }
        body.home-poster-active.theme-black {
            background: #09090b;
        }
        body.home-poster-active.theme-warm {
            background: #f3efe6;
        }

        /* Section Container */
        #tab-home {
            position: relative;
            width: 100%;
            max-width: 1340px;
            margin: 0 auto;
            padding: 10px 16px 80px 16px;
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

        /* Main Poster Art Canvas */
        .editorial-poster-canvas {
            position: relative;
            width: 100%;
            min-height: 640px;
            background: #ebebee;
            border-radius: 28px;
            padding: 24px 36px 40px 36px;
            box-sizing: border-box;
            overflow: hidden;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.12), 0 1px 3px rgba(0, 0, 0, 0.06);
            transition: background-color 0.4s ease, color 0.4s ease, box-shadow 0.4s ease;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .theme-charcoal .editorial-poster-canvas {
            background: #18181c;
            box-shadow: 0 25px 70px rgba(0, 0, 0, 0.45);
        }

        .theme-black .editorial-poster-canvas {
            background: #0c0c0f;
            box-shadow: 0 25px 70px rgba(0, 0, 0, 0.6);
        }

        .theme-warm .editorial-poster-canvas {
            background: #f6f2e9;
        }

        /* Scattered Aesthetic Floating Dots */
        .poster-floating-dot {
            position: absolute;
            width: 4px;
            height: 4px;
            background: #0a0a0a;
            border-radius: 50%;
            opacity: 0.65;
            pointer-events: none;
            z-index: 2;
            transition: background-color 0.4s ease, opacity 0.4s ease;
        }
        .theme-charcoal .poster-floating-dot,
        .theme-black .poster-floating-dot {
            background: #ffffff;
            opacity: 0.75;
        }

        /* ----------------------------------------------------
           1. TOP HEADER BAR: "IN   HERE   •   FOR   ME" + ICONS
           ---------------------------------------------------- */
        .poster-top-header {
            position: relative;
            z-index: 20;
            display: flex;
            align-items: center;
            justify-content: space-between;
            width: 100%;
            padding: 4px 0 16px 0;
        }

        .poster-nav-spelling {
            display: flex;
            align-items: center;
            gap: 28px;
            font-family: 'Outfit', 'Inter', -apple-system, sans-serif;
            font-weight: 800;
            font-size: 1.12rem;
            letter-spacing: 3.5px;
            color: #0a0a0a;
            margin-left: 45%;
            transition: color 0.3s ease;
        }

        .theme-charcoal .poster-nav-spelling,
        .theme-black .poster-nav-spelling {
            color: #f1f1f3;
        }

        .poster-nav-dot {
            font-size: 1.3rem;
            line-height: 1;
        }

        .poster-top-actions {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .poster-circle-btn {
            width: 44px;
            height: 44px;
            border-radius: 50%;
            background: #0c0c0e;
            color: #ffffff;
            border: none;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 14px rgba(0, 0, 0, 0.22);
            transition: transform 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275), background 0.3s ease;
        }

        .poster-circle-btn:hover {
            transform: scale(1.1);
            background: #232328;
        }

        .poster-circle-btn svg {
            width: 20px;
            height: 20px;
            fill: currentColor;
        }

        .theme-charcoal .poster-circle-btn,
        .theme-black .poster-circle-btn {
            background: #ffffff;
            color: #0c0c0e;
        }
        .theme-charcoal .poster-circle-btn:hover,
        .theme-black .poster-circle-btn:hover {
            background: #dedede;
        }

        /* ----------------------------------------------------
           2. TOP "GALLERY" CAPSULE PILL WIDGET
           ---------------------------------------------------- */
        .poster-gallery-capsule {
            position: absolute;
            top: 22px;
            left: 49%;
            transform: translateX(-50%);
            z-index: 25;
            background: #0a0a0a;
            color: #ffffff;
            border-radius: 9999px;
            padding: 6px 14px 6px 16px;
            display: inline-flex;
            align-items: center;
            gap: 14px;
            cursor: pointer;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.28);
            transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), background-color 0.3s ease;
        }

        .poster-gallery-capsule:hover {
            transform: translateX(-50%) translateY(-2px) scale(1.04);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.38);
        }

        .gallery-pill-dots {
            font-size: 13px;
            letter-spacing: 2px;
            opacity: 0.8;
            font-weight: 700;
        }

        .gallery-pill-label {
            font-family: 'Outfit', 'Inter', sans-serif;
            font-weight: 700;
            font-size: 0.96rem;
            letter-spacing: 0.5px;
        }

        .gallery-pill-close {
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background: #ffffff;
            color: #0a0a0a;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 11px;
            font-weight: 900;
            cursor: pointer;
            transition: transform 0.2s ease;
        }

        .gallery-pill-close:hover {
            transform: rotate(90deg);
        }

        .theme-charcoal .poster-gallery-capsule,
        .theme-black .poster-gallery-capsule {
            background: #f1f1f3;
            color: #0a0a0a;
        }
        .theme-charcoal .gallery-pill-close,
        .theme-black .gallery-pill-close {
            background: #0a0a0a;
            color: #ffffff;
        }

        /* ----------------------------------------------------
           3. POSTER MAIN GRID: LEFT (HERO + WIDGETS) & RIGHT (TYPOGRAPHY)
           ---------------------------------------------------- */
        .poster-main-grid {
            position: relative;
            z-index: 10;
            display: grid;
            grid-template-columns: 46% 54%;
            min-height: 540px;
            align-items: center;
            width: 100%;
        }

        /* Layered Depth Cards behind Character */
        .poster-bg-card-layer-1 {
            position: absolute;
            left: 20px;
            top: 20px;
            width: 320px;
            height: 480px;
            border-radius: 34px;
            background: rgba(255, 255, 255, 0.45);
            border: 1.5px solid rgba(0, 0, 0, 0.08);
            box-shadow: 0 20px 45px rgba(0, 0, 0, 0.05);
            pointer-events: none;
            z-index: 1;
            transform: rotate(-3deg);
            transition: all 0.4s ease;
        }

        .poster-bg-card-layer-2 {
            position: absolute;
            left: 5px;
            top: 60px;
            width: 260px;
            height: 400px;
            border-radius: 30px;
            background: #0f0f12;
            opacity: 0.95;
            box-shadow: 0 25px 60px rgba(0, 0, 0, 0.25);
            pointer-events: none;
            z-index: 2;
            transform: rotate(2deg);
            transition: all 0.4s ease;
        }

        .theme-charcoal .poster-bg-card-layer-1,
        .theme-black .poster-bg-card-layer-1 {
            background: rgba(255, 255, 255, 0.06);
            border-color: rgba(255, 255, 255, 0.12);
        }

        .theme-charcoal .poster-bg-card-layer-2,
        .theme-black .poster-bg-card-layer-2 {
            background: #000000;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        /* Hero Character Column */
        .poster-hero-column {
            position: relative;
            z-index: 10;
            height: 100%;
            display: flex;
            align-items: flex-end;
            justify-content: center;
        }

        .poster-hero-artwork-frame {
            position: relative;
            width: 100%;
            max-width: 440px;
            height: 560px;
            display: flex;
            align-items: flex-end;
            justify-content: center;
            z-index: 8;
        }

        /* The Hero Image Slot */
        .poster-hero-img {
            max-width: 100%;
            max-height: 100%;
            object-fit: contain;
            object-position: bottom center;
            display: block;
            filter: drop-shadow(0 15px 30px rgba(0, 0, 0, 0.35));
            transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            pointer-events: auto;
        }

        .poster-hero-artwork-frame:hover .poster-hero-img {
            transform: scale(1.02) translateY(-4px);
        }

        /* ----------------------------------------------------
           4. FLOATING UI WIDGETS AROUND CHARACTER
           ---------------------------------------------------- */

        /* Widget: PERFECT BEAUTY badge */
        .widget-perfect-beauty {
            position: absolute;
            top: 80px;
            left: 360px;
            z-index: 16;
            border: 1.5px solid #0a0a0a;
            border-radius: 8px;
            padding: 3px 6px;
            font-family: 'Outfit', sans-serif;
            font-size: 0.58rem;
            font-weight: 800;
            letter-spacing: 1px;
            line-height: 1.1;
            text-align: center;
            color: #0a0a0a;
            background: rgba(255, 255, 255, 0.8);
            backdrop-filter: blur(4px);
            pointer-events: none;
        }
        .theme-charcoal .widget-perfect-beauty,
        .theme-black .widget-perfect-beauty {
            border-color: #ffffff;
            color: #ffffff;
            background: rgba(0, 0, 0, 0.6);
        }

        /* Widget: Color Styles Card */
        .widget-color-styles {
            position: absolute;
            top: 115px;
            left: 310px;
            z-index: 18;
            background: #ffffff;
            border-radius: 20px;
            padding: 10px 16px 12px 16px;
            box-shadow: 0 14px 35px rgba(0, 0, 0, 0.14);
            border: 1px solid rgba(0, 0, 0, 0.06);
            display: flex;
            flex-direction: column;
            gap: 8px;
            cursor: default;
            transition: transform 0.3s ease, background-color 0.3s ease;
        }

        .widget-color-styles:hover {
            transform: translateY(-2px);
        }

        .color-styles-head {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            font-family: 'Outfit', sans-serif;
            font-size: 0.76rem;
            font-weight: 800;
            color: #0a0a0a;
            letter-spacing: 0.3px;
        }

        .color-styles-menu-icon {
            font-size: 13px;
            color: #71717a;
            cursor: pointer;
        }

        .color-swatches-row {
            display: flex;
            align-items: center;
            gap: 9px;
        }

        .color-swatch-chip {
            width: 22px;
            height: 22px;
            border-radius: 50%;
            border: 2px solid transparent;
            cursor: pointer;
            transition: transform 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275), border-color 0.2s ease;
        }

        .color-swatch-chip:hover {
            transform: scale(1.18);
        }

        .chip-light {
            background: #d4d4d8;
        }
        .chip-charcoal {
            background: #3f3f46;
        }
        .chip-black {
            background: #09090b;
        }

        .theme-charcoal .widget-color-styles,
        .theme-black .widget-color-styles {
            background: #202025;
            border-color: rgba(255, 255, 255, 0.12);
        }
        .theme-charcoal .color-styles-head,
        .theme-black .color-styles-head {
            color: #f4f4f5;
        }

        /* Widget: Circular Profile Avatar Button */
        .widget-profile-btn {
            position: absolute;
            top: 215px;
            left: 360px;
            z-index: 18;
            width: 54px;
            height: 54px;
            border-radius: 50%;
            background: #0a0a0a;
            color: #ffffff;
            border: none;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.28);
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), background 0.3s ease;
        }

        .widget-profile-btn:hover {
            transform: scale(1.12);
            background: #27272a;
        }

        .widget-profile-btn svg {
            width: 24px;
            height: 24px;
            fill: currentColor;
        }

        .theme-charcoal .widget-profile-btn,
        .theme-black .widget-profile-btn {
            background: #ffffff;
            color: #0a0a0a;
        }

        /* Widget: Notebook Card & Action Badges */
        .widget-notebook-cluster {
            position: absolute;
            bottom: 40px;
            left: 275px;
            z-index: 18;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .notebook-dark-card {
            background: #0a0a0a;
            color: #ffffff;
            border-radius: 18px;
            padding: 12px 20px;
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.3);
            cursor: pointer;
            transition: transform 0.25s ease, box-shadow 0.25s ease;
        }

        .notebook-dark-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 16px 36px rgba(0, 0, 0, 0.4);
        }

        .notebook-title {
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 1.05rem;
            letter-spacing: 0.3px;
        }

        .notebook-date {
            font-family: 'Inter', sans-serif;
            font-size: 0.65rem;
            color: #a1a1aa;
            margin-top: 1px;
            letter-spacing: 0.5px;
        }

        .notebook-actions-row {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .round-reload-btn {
            width: 32px;
            height: 32px;
            border-radius: 50%;
            background: #ffffff;
            color: #0a0a0a;
            border: 1.5px solid #0a0a0a;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        .round-reload-btn:hover {
            transform: rotate(-180deg) scale(1.1);
        }

        .ready-pill-badge {
            background: #ffffff;
            color: #0a0a0a;
            border: 2px solid #0a0a0a;
            border-radius: 9999px;
            padding: 4px 14px;
            font-family: 'Outfit', sans-serif;
            font-weight: 900;
            font-size: 0.88rem;
            letter-spacing: 1px;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s ease, background 0.2s ease;
        }

        .ready-pill-badge:hover {
            transform: scale(1.05);
            background: #f4f4f5;
        }

        .shield-check-badge {
            width: 28px;
            height: 28px;
            border-radius: 8px;
            background: #0a0a0a;
            color: #ffffff;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
        }

        .shield-check-badge svg {
            width: 16px;
            height: 16px;
        }

        .theme-charcoal .notebook-dark-card,
        .theme-black .notebook-dark-card {
            background: #27272a;
            border: 1px solid rgba(255, 255, 255, 0.15);
        }

        /* Widget: To be con... / Come... (Left Edge) */
        .widget-come-cluster {
            position: absolute;
            bottom: 60px;
            left: 0;
            z-index: 18;
            display: flex;
            flex-direction: column;
            gap: 4px;
        }

        .come-sub-text {
            font-family: 'Inter', sans-serif;
            font-size: 0.68rem;
            font-weight: 700;
            color: #52525b;
            letter-spacing: 0.4px;
            padding-left: 2px;
        }

        .come-pill-btn {
            background: #0a0a0a;
            color: #ffffff;
            border-radius: 9999px;
            padding: 7px 18px;
            font-family: 'Outfit', sans-serif;
            font-weight: 900;
            font-size: 1.02rem;
            letter-spacing: 0.5px;
            cursor: pointer;
            box-shadow: 0 6px 16px rgba(0, 0, 0, 0.2);
            transition: transform 0.2s ease, background 0.2s ease;
        }

        .come-pill-btn:hover {
            transform: translateX(4px);
            background: #27272a;
        }

        .theme-charcoal .come-sub-text,
        .theme-black .come-sub-text {
            color: #a1a1aa;
        }
        .theme-charcoal .come-pill-btn,
        .theme-black .come-pill-btn {
            background: #ffffff;
            color: #0a0a0a;
        }

        /* ----------------------------------------------------
           5. RIGHT COLUMN: GIANT CONDENSED TYPOGRAPHY
           ---------------------------------------------------- */
        .poster-typography-stage {
            position: relative;
            z-index: 10;
            display: flex;
            flex-direction: column;
            justify-content: center;
            padding-left: 10px;
            padding-top: 20px;
        }

        /* Big Condensed Titles: MEGAN / TUTO'S */
        .mega-text-row {
            display: flex;
            align-items: center;
            line-height: 0.82;
            margin: 0;
            padding: 0;
        }

        .mega-condensed-headline {
            font-family: 'Bebas Neue', 'Big Shoulders Display', 'Anton', sans-serif;
            font-size: clamp(6.5rem, 14vw, 13.2rem);
            font-weight: 900;
            letter-spacing: -1.5px;
            color: #0a0a0a;
            margin: 0;
            padding: 0;
            text-transform: uppercase;
            line-height: 0.84;
            display: block;
            transition: color 0.4s ease;
        }

        /* Equalizer Capsule Pills next to TUTO'S */
        .eq-pill-column {
            display: flex;
            flex-direction: column;
            gap: 8px;
            margin-right: 18px;
        }

        .eq-capsule-unit {
            width: 14px;
            height: 38px;
            border-radius: 9999px;
            background: #0a0a0a;
            border: 2px solid #ffffff;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
            transition: background-color 0.4s ease, border-color 0.4s ease;
        }

        /* Subtitle: DARGAHONEL */
        .sub-condensed-headline {
            font-family: 'Bebas Neue', 'Big Shoulders Display', sans-serif;
            font-size: clamp(2.6rem, 5.2vw, 4.4rem);
            font-weight: 800;
            letter-spacing: 1px;
            color: #0a0a0a;
            margin-top: 8px;
            line-height: 1;
            text-transform: uppercase;
            transition: color 0.4s ease;
        }

        /* Bottom-Right Caption */
        .poster-bottom-caption {
            align-self: flex-end;
            margin-top: 18px;
            font-family: 'Outfit', 'Inter', sans-serif;
            font-size: 0.65rem;
            font-weight: 800;
            letter-spacing: 1.5px;
            color: #18181b;
            text-transform: uppercase;
            display: flex;
            align-items: center;
            gap: 6px;
            transition: color 0.4s ease;
        }

        .theme-charcoal .mega-condensed-headline,
        .theme-charcoal .sub-condensed-headline,
        .theme-black .mega-condensed-headline,
        .theme-black .sub-condensed-headline {
            color: #f4f4f6;
        }

        .theme-charcoal .eq-capsule-unit,
        .theme-black .eq-capsule-unit {
            background: #f4f4f6;
            border-color: #0a0a0a;
        }

        .theme-charcoal .poster-bottom-caption,
        .theme-black .poster-bottom-caption {
            color: #a1a1aa;
        }

        /* ----------------------------------------------------
           6. RESPONSIVE MEDIA QUERIES FOR POSTER
           ---------------------------------------------------- */
        @media (max-width: 1080px) {
            .poster-nav-spelling {
                margin-left: 35%;
                gap: 18px;
                font-size: 1rem;
            }
            .poster-main-grid {
                grid-template-columns: 48% 52%;
            }
            .widget-color-styles {
                left: 260px;
                top: 100px;
            }
            .widget-profile-btn {
                left: 300px;
                top: 190px;
            }
            .widget-perfect-beauty {
                left: 300px;
                top: 70px;
            }
            .widget-notebook-cluster {
                left: 220px;
                bottom: 20px;
            }
        }

        @media (max-width: 860px) {
            .editorial-poster-canvas {
                padding: 20px 16px 36px 16px;
            }
            .poster-nav-spelling {
                margin-left: 0;
                gap: 14px;
                font-size: 0.9rem;
            }
            .poster-gallery-capsule {
                top: 18px;
                left: auto;
                right: 120px;
                transform: none;
                padding: 4px 10px 4px 12px;
            }
            .poster-gallery-capsule:hover {
                transform: translateY(-2px);
            }
            .poster-main-grid {
                grid-template-columns: 1fr;
                gap: 30px;
            }
            .poster-hero-column {
                justify-content: center;
                order: 2;
            }
            .poster-hero-artwork-frame {
                max-width: 340px;
                height: 440px;
            }
            .poster-typography-stage {
                order: 1;
                text-align: center;
                align-items: center;
                padding-left: 0;
            }
            .mega-text-row {
                justify-content: center;
            }
            .poster-bottom-caption {
                align-self: center;
            }
            .widget-color-styles {
                left: auto;
                right: 20px;
                top: 60px;
            }
            .widget-profile-btn {
                left: auto;
                right: 40px;
                top: 150px;
            }
            .widget-notebook-cluster {
                left: auto;
                right: 20px;
                bottom: 20px;
            }
        }

        @media (max-width: 520px) {
            .poster-nav-spelling {
                gap: 8px;
                font-size: 0.78rem;
                letter-spacing: 1.5px;
            }
            .poster-gallery-capsule {
                display: none; /* Hide compact capsule on small mobile to avoid header overlap */
            }
            .mega-condensed-headline {
                font-size: 5.4rem;
            }
            .sub-condensed-headline {
                font-size: 2.2rem;
            }
            .widget-color-styles,
            .widget-profile-btn,
            .widget-notebook-cluster,
            .widget-come-cluster {
                position: static;
                margin-top: 12px;
            }
            .poster-hero-column {
                flex-direction: column;
                align-items: center;
            }
        }
"""

# Inject CSS before </style>
if 'MODERN EDITORIAL CHARACTER POSTER STYLES' not in content:
    content = content.replace('    </style>', f'{poster_css}\n    </style>')
    print("[2] Injected Poster CSS before </style>")
else:
    print("[2] Poster CSS already present")

# 3. New HTML markup for tab-home
poster_html = """        <!-- ================= TAB 1: HOME (Modern Editorial Poster Layout) ================= -->
        <section id="tab-home" class="tab-content active">
            <div class="editorial-poster-canvas" id="posterCanvas">

                <!-- Scattered Accent Dots matching the reference image -->
                <div class="poster-floating-dot" style="top: 6%; right: 28%;"></div>
                <div class="poster-floating-dot" style="top: 18%; left: 9%;"></div>
                <div class="poster-floating-dot" style="top: 38%; right: 4%;"></div>
                <div class="poster-floating-dot" style="bottom: 12%; right: 26%;"></div>
                <div class="poster-floating-dot" style="bottom: 24%; left: 45%;"></div>

                <!-- 1. TOP HEADER: Spaced Nav Words + Action Icon Buttons -->
                <header class="poster-top-header">
                    <div class="poster-nav-spelling" aria-hidden="true">
                        <span>IN</span>
                        <span>HERE</span>
                        <span class="poster-nav-dot">•</span>
                        <span>FOR</span>
                        <span>ME</span>
                    </div>

                    <div class="poster-top-actions">
                        <button class="poster-circle-btn" id="posterHomeBtn" title="หน้าแรก (Home)" onclick="switchTab('home')" aria-label="Home">
                            <svg viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>
                        </button>
                        <button class="poster-circle-btn" id="posterMenuBtn" title="เมนูข้อมูลตัวละคร (Menu / Information)" onclick="switchTab('information')" aria-label="Menu">
                            <svg viewBox="0 0 24 24"><rect x="4" y="4" width="6.5" height="6.5" rx="2"/><rect x="13.5" y="4" width="6.5" height="6.5" rx="2"/><rect x="4" y="13.5" width="6.5" height="6.5" rx="2"/><rect x="13.5" y="13.5" width="6.5" height="6.5" rx="2"/></svg>
                        </button>
                    </div>
                </header>

                <!-- 2. TOP CENTER "GALLERY" CAPSULE PILL WIDGET -->
                <div class="poster-gallery-capsule" role="button" tabindex="0" onclick="switchTab('gallery')" title="คลิกเพื่อเปิดดูคลังรูปภาพ (Gallery)">
                    <span class="gallery-pill-dots">•••</span>
                    <span class="gallery-pill-label">Gallery</span>
                    <span class="gallery-pill-close" onclick="event.stopPropagation(); switchTab('information');" title="ปิดหรือสลับแท็บ">✕</span>
                </div>

                <!-- 3. MAIN POSTER GRID: LEFT (HERO + WIDGETS) & RIGHT (CONDENSED TYPOGRAPHY) -->
                <div class="poster-main-grid">

                    <!-- LEFT COLUMN: Character Hero Cut-out & Floating Badges -->
                    <div class="poster-hero-column">

                        <!-- Layered Depth Cards behind Character -->
                        <div class="poster-bg-card-layer-1" aria-hidden="true"></div>
                        <div class="poster-bg-card-layer-2" aria-hidden="true"></div>

                        <!-- 🌟 WIDGET 1: PERFECT BEAUTY BADGE -->
                        <div class="widget-perfect-beauty" aria-hidden="true">
                            PERFECT<br>BEAUTY
                        </div>

                        <!-- 🎨 WIDGET 2: COLOR STYLES CARD (Interactive Theme Swatches) -->
                        <div class="widget-color-styles" title="ปรับโทนสีพื้นหลังโปสเตอร์ (Color Styles)">
                            <div class="color-styles-head">
                                <span>Color Styles</span>
                                <span class="color-styles-menu-icon" aria-hidden="true">⋮</span>
                            </div>
                            <div class="color-swatches-row">
                                <button class="color-swatch-chip chip-light" onclick="setPosterTheme('light')" title="โทนสีสว่าง (Light Minimalist)" aria-label="Light theme"></button>
                                <button class="color-swatch-chip chip-charcoal" onclick="setPosterTheme('charcoal')" title="โทนสีเทาดำ (Charcoal Dark)" aria-label="Charcoal theme"></button>
                                <button class="color-swatch-chip chip-black" onclick="setPosterTheme('black')" title="โทนสีดำสนิท (Pitch Black)" aria-label="Pitch Black theme"></button>
                            </div>
                        </div>

                        <!-- 👤 WIDGET 3: CIRCULAR PROFILE AVATAR BUTTON -->
                        <button class="widget-profile-btn" onclick="openScroll('history')" title="คลิกเพื่อดูประวัติและข้อมูลตัวละคร (Alexan Nigelus Lake)" aria-label="Character Profile Bio">
                            <svg viewBox="0 0 24 24"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>
                        </button>

                        <!-- 📓 WIDGET 4: NOTEBOOK CARD & ACTION BADGES -->
                        <div class="widget-notebook-cluster">
                            <div class="notebook-dark-card" onclick="openScroll('history')" role="button" tabindex="0" title="คลิกอ่านบันทึกประวัติ (Notebook Archive)">
                                <div class="notebook-title">Notebook</div>
                                <div class="notebook-date">16 December</div>
                            </div>
                            <div class="notebook-actions-row">
                                <div class="round-reload-btn" onclick="refreshPosterQuote()" role="button" tabindex="0" title="รีเฟรชคำคมเวทมนตร์ (Refresh Quote)">
                                    <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.19"/></svg>
                                </div>
                                <div class="ready-pill-badge" onclick="openScroll('history')" role="button" tabindex="0" title="READY: เปิดดูข้อมูลส่วนตัว">READY</div>
                                <div class="shield-check-badge" title="สถานะพร้อม">
                                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg>
                                </div>
                            </div>
                        </div>

                        <!-- ⏩ WIDGET 5: TO BE CON... / COME... PILL (Left Edge) -->
                        <div class="widget-come-cluster">
                            <div class="come-sub-text">To be con...</div>
                            <div class="come-pill-btn" onclick="switchTab('information')" role="button" tabindex="0" title="ไปยังหน้าข้อมูลส่วนตัว (Information)">Come...</div>
                        </div>

                        <!-- 🖼️ HERO CHARACTER ARTWORK FRAME -->
                        <div class="poster-hero-artwork-frame" id="posterHeroWrapper">
                            <!-- 📷 [จุดใส่รูปตัวละครของคุณ] 
                                 แทนที่ src="images/alexan-profile.jpg?v=3" ด้านล่างนี้ ด้วยไฟล์รูปภาพที่คุณต้องการ
                                 แนะนำเป็นไฟล์ภาพไดคัทพื้นหลังโปร่งใส (.png) เช่น images/my-character.png เพื่อให้เนียนสวยงามเหมือนแบบ 100% -->
                            <img id="posterHeroImg" src="images/alexan-profile.jpg?v=3" alt="Character Portrait" class="poster-hero-img"
                                 onerror="this.onerror=null; this.src='images/hogwarts-logo.png';" />
                        </div>

                    </div>

                    <!-- RIGHT COLUMN: GIANT CONDENSED DISPLAY TYPOGRAPHY -->
                    <div class="poster-typography-stage">
                        
                        <!-- Line 1: MEGAN -->
                        <div class="mega-text-row">
                            <h1 class="mega-condensed-headline" title="Megan / Alexan">MEGAN</h1>
                        </div>

                        <!-- Line 2: TUTO'S with Equalizer Pill indicator -->
                        <div class="mega-text-row">
                            <div class="eq-pill-column" aria-hidden="true">
                                <div class="eq-capsule-unit"></div>
                                <div class="eq-capsule-unit"></div>
                            </div>
                            <div class="mega-condensed-headline" title="Tuto's">TUTO'S</div>
                        </div>

                        <!-- Line 3: DARGAHONEL -->
                        <div class="sub-condensed-headline" title="Dargahonel / House">DARGAHONEL</div>

                        <!-- Bottom-right micro caption -->
                        <div class="poster-bottom-caption">
                            <span>•</span> THE REAL FACE OF WORD
                        </div>

                    </div>

                </div>

            </div>
        </section>"""

# Replace the existing tab-home section
pattern = r'<section id="tab-home".*?</section>'
match = re.search(pattern, content, re.DOTALL)
if match:
    content = content[:match.start()] + poster_html + content[match.end():]
    print("[3] Replaced tab-home with new Poster Layout")
else:
    print("[3] ERROR: Could not find <section id=\"tab-home\">")

# 4. Add JavaScript helper functions
poster_js = """
        // ================= Modern Poster Layout Helper Functions =================
        function setPosterTheme(themeName) {
            document.body.classList.remove('theme-charcoal', 'theme-black', 'theme-warm');
            if (themeName !== 'light') {
                document.body.classList.add('theme-' + themeName);
            }
        }

        const magicQuotes = [
            '"ความเร็วน่ะไม่ใช่แค่เรื่องของการบิน แต่มันคือการตัดสินใจในเสี้ยววินาที" — Alex Lake',
            '"หัวใจแห่งความกล้าหาญของกริฟฟินดอร์ ไม่เคยสูญเสียไปตามร่างกายเลย" — Alexan',
            '"ไม้กวาดไฟเยอร์โบลด์คู่ใจ พร้อมพุ่งทะยานสู่สนามเสมอ" — Quidditch Pitch',
            '"อย่าเข้ามาทางจุดบอดข้างซ้าย... เตือนแล้วนะ!" — Alex Lake'
        ];
        let quoteIndex = 0;

        function refreshPosterQuote() {
            quoteIndex = (quoteIndex + 1) % magicQuotes.length;
            const quote = magicQuotes[quoteIndex];
            const btn = document.querySelector('.round-reload-btn');
            if (btn) {
                btn.style.transform = 'rotate(-360deg) scale(1.15)';
                setTimeout(() => btn.style.transform = '', 350);
            }
            openScrollCustom('Magic Quote / คำคมประจำตัว', `<div style="padding: 10px 0; font-size: 1.4rem; font-style: italic; color: #2a1408; line-height: 1.8;">${quote}</div>`);
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
        function initHomePosterMode() {
            const homeTab = document.getElementById('tab-home');
            if (homeTab && homeTab.classList.contains('active')) {
                document.body.classList.add('home-poster-active');
            }
        }
        window.addEventListener('DOMContentLoaded', initHomePosterMode);
        initHomePosterMode();
"""

# Update switchTab to manage home-poster-active class
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
                    document.body.classList.add('home-poster-active');
                } else {
                    document.body.classList.remove('home-poster-active');
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
    print("[4] Updated switchTab function to toggle home-poster-active")
else:
    print("[4] Note: switchTab pattern match not identical, checking...")

if 'Modern Poster Layout Helper Functions' not in content:
    content = content.replace('    <script>', f'    <script>\n{poster_js}')
    print("[5] Injected Poster JS helper functions")

with open(INDEX_FILE, 'w', encoding='utf-8') as f:
    f.write(content)

print("[DONE] Successfully wrote updated index.html!")
