# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Hide sparks canvas in home poster mode
old_hide = """        body.home-poster-active .gryffindor-banner-left,
        body.home-poster-active .gryffindor-banner-right,
        body.home-poster-active .floating-candle,
        body.home-poster-active .bg-lion-watermark,
        body.home-poster-active .top-crest-shield,
        body.home-poster-active .golden-snitch {"""

new_hide = """        body.home-poster-active #magicCanvas,
        body.home-poster-active #wandTrailCanvas,
        body.home-poster-active .gryffindor-banner-left,
        body.home-poster-active .gryffindor-banner-right,
        body.home-poster-active .floating-candle,
        body.home-poster-active .bg-lion-watermark,
        body.home-poster-active .top-crest-shield,
        body.home-poster-active .golden-snitch {"""

if old_hide in content:
    content = content.replace(old_hide, new_hide)
    print("Updated body.home-poster-active hidden elements to include canvases")

# 2. Modern Dock Navigation styling for Home mode
dock_home_css = """
        /* Modern Sleek Glass Dock when on Home Poster */
        body.home-poster-active .common-room-dock {
            background: rgba(16, 16, 20, 0.88) !important;
            backdrop-filter: blur(20px) !important;
            -webkit-backdrop-filter: blur(20px) !important;
            border-top: 1px solid rgba(255, 255, 255, 0.12) !important;
            box-shadow: 0 -10px 30px rgba(0, 0, 0, 0.35) !important;
            padding: 10px 24px !important;
        }

        body.home-poster-active .dock-bg-sketches {
            display: none !important;
        }

        body.home-poster-active .dock-link {
            font-family: 'Outfit', 'Inter', sans-serif !important;
            font-size: 1.15rem !important;
            font-weight: 700 !important;
            letter-spacing: 1.5px !important;
            color: #9ca3af !important;
            text-transform: uppercase !important;
            text-shadow: none !important;
            padding: 6px 14px !important;
            border-radius: 8px !important;
            transition: all 0.25s ease !important;
        }

        body.home-poster-active .dock-link:hover {
            color: #ffffff !important;
            transform: translateY(-2px) !important;
            background: rgba(255, 255, 255, 0.08) !important;
        }

        body.home-poster-active .dock-link.active {
            color: #ffffff !important;
            background: rgba(255, 255, 255, 0.15) !important;
            border-bottom: none !important;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.25) !important;
        }

        body.home-poster-active .dock-pipe-divider {
            color: #4b5563 !important;
            font-family: sans-serif !important;
            font-size: 1.1rem !important;
        }
"""

if 'Modern Sleek Glass Dock when on Home Poster' not in content:
    content = content.replace('    </style>', f'{dock_home_css}\n    </style>')
    print("Added modern dock styling for Home mode")

# 3. Increase bottom padding on #tab-home so canvas never gets blocked by dock
old_tab_home = """        #tab-home {
            position: relative;
            width: 100%;
            max-width: 1340px;
            margin: 0 auto;
            padding: 10px 16px 80px 16px;
            box-sizing: border-box;
            user-select: none;
        }"""

new_tab_home = """        #tab-home {
            position: relative;
            width: 100%;
            max-width: 1360px;
            margin: 0 auto;
            padding: 16px 18px 120px 18px;
            box-sizing: border-box;
            user-select: none;
        }"""

if old_tab_home in content:
    content = content.replace(old_tab_home, new_tab_home)
    print("Updated #tab-home padding")

# 4. Refine hero image container and blend
old_hero_frame = """        .poster-hero-artwork-frame {
            position: relative;
            width: 100%;
            max-width: 440px;
            height: 560px;
            display: flex;
            align-items: flex-end;
            justify-content: center;
            z-index: 8;
        }"""

new_hero_frame = """        .poster-hero-artwork-frame {
            position: relative;
            width: 100%;
            max-width: 460px;
            height: 600px;
            display: flex;
            align-items: flex-end;
            justify-content: center;
            z-index: 8;
        }"""

if old_hero_frame in content:
    content = content.replace(old_hero_frame, new_hero_frame)
    print("Updated poster-hero-artwork-frame height to 600px")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Polish script finished successfully!")
