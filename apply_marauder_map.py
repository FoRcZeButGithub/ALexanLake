import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Google Fonts in <head>
google_fonts_old = '<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+Thai:wght@300;400;600;700&display=swap"\n        rel="stylesheet">'
google_fonts_new = '<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+Thai:wght@300;400;600;700&family=Satisfy&family=Lobster+Two:ital,wght@0,400;0,700;1,400&family=Cinzel:wght@600;700;900&family=Comfortaa:wght@400;700&display=swap"\n        rel="stylesheet">'

if google_fonts_old in content:
    content = content.replace(google_fonts_old, google_fonts_new)
    print("Google Fonts updated.")
else:
    print("Warning: Google fonts pattern not found exactly, searching regex...")
    content = re.sub(
        r'<link href="https://fonts\.googleapis\.com/css2\?family=Noto\+Serif\+Thai[^"]+"\s+rel="stylesheet">',
        google_fonts_new,
        content
    )
    print("Google Fonts regex replaced.")

# 2. Add Marauder's Map CSS after .gallery-inspect-pill block
map_css = """
        /* ================= MARAUDER'S MAP (ENCHANTED 3D BOOK & MAP) ================= */
        :root {
            --map-brown: #615349;
            --map-brown-dark: #3b2c21;
        }

        /* Gallery View Mode Switcher */
        .gallery-view-mode-bar {
            display: flex;
            justify-content: center;
            gap: 12px;
            margin: 15px auto 28px;
            flex-wrap: wrap;
        }

        .view-mode-btn {
            background: rgba(30, 4, 7, 0.85);
            border: 1.5px solid var(--gold-antique);
            color: #e5cb9d;
            font-family: 'Sarun HarryPotter', 'Cinzel', serif;
            font-size: 1.35rem;
            padding: 8px 22px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.6);
        }

        .view-mode-btn:hover {
            border-color: var(--gold-bright);
            color: #fff;
            transform: translateY(-2px);
        }

        .view-mode-btn.active {
            background: linear-gradient(135deg, rgba(120, 20, 25, 0.95), rgba(60, 8, 12, 0.95));
            border-color: var(--gold-bright);
            color: var(--gold-bright);
            box-shadow: 0 6px 18px rgba(243, 199, 102, 0.35);
        }

        .gallery-view-section {
            display: none;
            animation: fadeInView 0.4s ease forwards;
        }

        .gallery-view-section.active {
            display: block;
        }

        @keyframes fadeInView {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Marauder's Map Stage */
        .marauder-map-stage {
            position: relative;
            width: 100%;
            padding: 30px 10px 50px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background: radial-gradient(circle at center, rgba(46, 4, 7, 0.65) 0%, rgba(15, 2, 4, 0.96) 100%);
            border: 2px solid var(--gold-antique);
            border-radius: 12px;
            box-shadow: inset 0 0 50px rgba(0,0,0,0.85), 0 12px 35px rgba(0,0,0,0.7);
            margin-bottom: 30px;
            overflow: hidden;
        }

        /* Incantation Header */
        .map-incantation-panel {
            text-align: center;
            margin-bottom: 22px;
            z-index: 20;
        }

        .map-spell-prompt {
            font-family: 'Sarun HarryPotter', 'Cinzel', serif;
            font-size: 1.55rem;
            color: var(--gold-bright);
            text-shadow: 0 2px 8px rgba(0,0,0,0.9);
            margin-bottom: 12px;
            letter-spacing: 0.8px;
        }

        .toggle-map-btn {
            border: 2px solid var(--gold-bright);
            background: linear-gradient(135deg, rgba(80, 10, 15, 0.92), rgba(30, 4, 7, 0.98));
            font-family: 'Sarun HarryPotter', 'Lobster Two', 'Cinzel', cursive, serif;
            font-size: 1.95rem;
            color: #fff;
            padding: 10px 32px;
            cursor: pointer;
            position: relative;
            border-radius: 4px;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.6), 0 0 18px rgba(243, 199, 102, 0.25);
            transition: all 0.35s ease;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
        }

        .toggle-map-btn::before {
            content: "";
            position: absolute;
            width: calc(100% - 8px);
            height: calc(100% - 8px);
            left: 2px;
            top: 2px;
            border: 1px solid rgba(255, 235, 170, 0.4);
            pointer-events: none;
            transition: all 0.3s ease;
        }

        .toggle-map-btn:hover {
            background: linear-gradient(135deg, rgba(120, 20, 25, 0.96), rgba(50, 8, 12, 0.98));
            color: var(--gold-bright);
            box-shadow: 0 8px 28px rgba(0, 0, 0, 0.85), 0 0 25px rgba(243, 199, 102, 0.6);
            transform: translateY(-2px);
        }

        .toggle-map-btn:hover::before {
            left: -2px;
            top: -2px;
            width: calc(100% + 2px);
            height: calc(100% + 2px);
            border-color: var(--gold-bright);
        }

        .map-sub-spell-text {
            font-family: 'Cinzel', 'Satisfy', serif;
            font-size: 1.15rem;
            color: #d1b47c;
            margin-top: 8px;
            font-style: italic;
            letter-spacing: 1px;
            text-shadow: 0 2px 4px #000;
        }

        /* Map Navigation Bar ("แต่นำทางแต่รูปภาพเหมือนแผนที่") */
        .map-navigator-bar {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 8px;
            margin: 12px 0 20px;
            z-index: 20;
            max-width: 950px;
        }

        .map-nav-btn {
            background: rgba(26, 4, 7, 0.85);
            border: 1px solid var(--gold-antique);
            color: #e5cb9d;
            font-family: 'Sarun HarryPotter', 'Cinzel', serif;
            font-size: 1.25rem;
            padding: 5px 14px;
            border-radius: 20px;
            cursor: pointer;
            transition: all 0.25s ease;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.5);
        }

        .map-nav-btn:hover, .map-nav-btn.active-target {
            background: var(--crimson-crest);
            border-color: var(--gold-bright);
            color: #fff;
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(243, 199, 102, 0.4);
        }

        /* 3D Viewport & Scaling */
        .map-viewport-wrapper {
            width: 100%;
            min-height: 660px;
            display: flex;
            justify-content: center;
            align-items: center;
            perspective: 1600px;
            overflow-x: auto;
            overflow-y: hidden;
            padding: 20px 10px 30px;
        }

        .map-scale-container {
            position: relative;
            width: 306px;
            height: 600px;
            transform-origin: center center;
            transition: transform 0.4s ease;
        }

        @media (max-width: 1100px) {
            .map-scale-container {
                transform: scale(0.85);
            }
        }

        @media (max-width: 820px) {
            .map-scale-container {
                transform: scale(0.68);
            }
            .map-viewport-wrapper {
                min-height: 520px;
            }
        }

        @media (max-width: 540px) {
            .map-scale-container {
                transform: scale(0.55);
            }
            .map-viewport-wrapper {
                min-height: 440px;
            }
        }

        /* Map Base */
        .map-base {
            width: 306px;
            height: 600px;
            margin: auto;
            background: url("https://meowlivia.s3.us-east-2.amazonaws.com/codepen/map/9.png") center center / cover;
            position: relative;
            display: inline-block;
            box-shadow: 0 15px 35px rgba(0,0,0,0.85);
            border-radius: 2px;
        }

        /* Flaps (Cover Top & Bottom) */
        .map-flap {
            transform-style: preserve-3d;
            position: absolute;
            width: 100%;
            height: 25%;
            margin: auto;
            left: 0;
            right: 0;
            transition: 0.5s ease;
            top: 25%;
            z-index: 5;
        }

        .map-flap__front,
        .map-flap__back {
            backface-visibility: hidden;
            width: 100%;
            height: 100%;
            position: absolute;
        }

        .map-flap__back {
            transform: scale(-1) rotateY(180deg);
        }

        .map-flap.flap--1 {
            box-shadow: 0 -1px 6px rgba(97, 83, 73, 0.5);
            top: 25%;
        }

        .map-flap.flap--1 .map-flap__front {
            background: url("https://meowlivia.s3.us-east-2.amazonaws.com/codepen/map/mini-1.png") center left / cover;
        }

        .map-flap.flap--1 .map-flap__back {
            background: url("https://meowlivia.s3.us-east-2.amazonaws.com/codepen/map/mini-3.png") -3px 0 / cover;
        }

        .map-flap.flap--2 {
            box-shadow: 0 1px 6px rgba(97, 83, 73, 0.5);
            top: 50%;
        }

        .map-flap.flap--2 .map-flap__front {
            background: url("https://meowlivia.s3.us-east-2.amazonaws.com/codepen/map/mini-2.png") center left / cover;
        }

        .map-flap.flap--2 .map-flap__back {
            background: url("https://meowlivia.s3.us-east-2.amazonaws.com/codepen/map/mini-4.png") -3px 0 / cover;
        }

        /* Map Sides (Wings) */
        .map-side {
            height: 600px;
            width: 152px;
            position: absolute;
            transform-style: preserve-3d;
            transition: 0.3s ease;
            top: 0;
        }

        .map-side .front,
        .map-side .back {
            width: 100%;
            height: 100%;
            position: absolute;
            background-repeat: no-repeat;
            background-position: left top;
            background-size: cover;
            background-image: var(--image);
            backface-visibility: hidden;
        }

        .map-side .back {
            background-image: url("https://meowlivia.s3.us-east-2.amazonaws.com/codepen/map/back.png");
        }

        .map-side.side-1 {
            left: 0;
            margin-left: 1.5px;
            z-index: 4;
        }

        .map-side.side-2 {
            left: 50%;
            margin-left: -2px;
            z-index: 4;
        }

        .map-side.side-3 {
            left: 0;
            margin-left: 3px;
            z-index: 3;
        }

        .map-side.side-3 .back {
            transform: rotateY(180deg);
        }

        .map-side.side-4 {
            left: 50%;
            margin-left: -1px;
            z-index: 3;
        }

        .map-side.side-4 .back {
            transform: rotateY(180deg);
        }

        .map-side.side-5 {
            left: 0;
            z-index: 6;
        }

        .map-side.side-5 .back {
            background-image: url("https://meowlivia.s3.us-east-2.amazonaws.com/codepen/map/1.png");
        }

        .map-side.side-6 {
            left: 50%;
            z-index: 6;
        }

        .map-side.side-6 .front {
            background-size: 99.5%;
        }

        .map-side.side-6 .back {
            background-image: url("https://meowlivia.s3.us-east-2.amazonaws.com/codepen/map/17.png");
        }

        /* Scroll Names & Footsteps */
        .scroll-name {
            position: absolute;
            bottom: 105px;
            left: -60px;
            width: 150px;
            height: 30px;
            font-family: 'Satisfy', 'Sarun HarryPotter', cursive;
            font-size: 14px;
            text-align: center;
            background: url("https://meowlivia.s3.us-east-2.amazonaws.com/codepen/map/scroll.svg") center center / cover;
            z-index: 10;
            color: var(--map-brown);
            cursor: default;
            opacity: 0;
            pointer-events: none;
        }

        .scroll-name p {
            display: inline-block;
            margin: 4px 0 0 15px;
            font-weight: bold;
        }

        .footstep {
            position: absolute;
            background: var(--map-brown);
            width: 6px;
            height: 12px;
            border-radius: 80% 80% 70% 70% / 130% 130% 25% 25%;
            z-index: 10;
            opacity: 0;
            pointer-events: none;
        }

        .footstep::before {
            content: "";
            position: absolute;
            width: 5px;
            height: 5px;
            top: 110%;
            left: 0px;
            background: var(--map-brown);
            border-radius: 0 0 100% 100%;
        }

        .footstep.left {
            transform: rotate(5deg);
        }

        .footstep.right {
            transform: rotate(-3deg) translateY(15px) translateX(10px);
        }

        .footsteps-1 .footstep.left {
            bottom: 150px;
            left: 18px;
            transform: rotate(35deg);
        }

        .footsteps-1 .footstep.right {
            bottom: 150px;
            left: 28px;
            transform: rotate(30deg);
        }

        .footsteps-2 .footstep.left {
            bottom: 285px;
            left: 280px;
            transform: rotate(-90deg);
        }

        .footsteps-2 .footstep.right {
            bottom: 275px;
            left: 285px;
            transform: rotate(-85deg);
        }

        .footsteps-2 .scroll-name {
            bottom: 300px;
            left: 220px;
        }

        /* Map Active (Unfolded State) */
        .map-base.active .flap--1 {
            transform: rotateX(180deg);
            transform-origin: top center;
            transition: 0.6s transform 1.5s;
        }

        .map-base.active .flap--2 {
            transform: rotateX(180deg);
            transform-origin: bottom center;
            transition: 0.6s transform 1.8s;
        }

        .map-base.active .side-1 {
            transform-origin: center left;
            transform: rotateY(180deg) skewY(2deg);
            transition: 0.5s all ease-in-out 0.6s;
        }

        .map-base.active .side-1 .front {
            transform: rotateY(180deg);
        }

        .map-base.active .side-2 {
            transform-origin: center right;
            transform: rotateY(180deg) skewY(-2deg);
            transition: 0.5s all ease-in-out 0.6s;
        }

        .map-base.active .side-2 .front {
            transform: rotateY(180deg);
        }

        .map-base.active .side-3 {
            left: -50%;
            transform: skewY(2deg) translateX(-100%);
            top: 8px;
            transition: 0.5s transform ease 0.8s, 0.3s left ease 0.8s, 0.5s top ease 0.8s;
        }

        .map-base.active .side-4 {
            left: 100%;
            transform: skewY(-2deg) translateX(100%);
            top: 8px;
            margin-left: -7px;
            transition: 0.5s transform ease 0.8s, 0.3s left ease 0.8s, 0.5s top ease 0.8s, 0.5s margin ease 0.8s;
        }

        .map-base.active .side-5 {
            left: -100%;
            transform-origin: center left;
            transform: rotateY(180deg);
            transition: 0.5s transform, 0.7s left 0.8s, 0.2s margin 0.8s;
            top: 0px;
            margin-left: 4px;
        }

        .map-base.active .side-5 .front {
            transform: rotateY(180deg);
            transition: 0.1s transform;
        }

        .map-base.active .side-6 {
            left: 150%;
            transform: rotateY(180deg);
            transform-origin: center right;
            margin-left: -8px;
            transition: 0.5s transform 0.3s, 0.7s left 0.8s, 0.5s top 0.8s, 0.5s margin 0.8s;
        }

        .map-base.active .side-6 .front {
            transform: rotateY(180deg);
            transition: 0.1s transform;
        }

        .map-base.active .footstep,
        .map-base.active .scroll-name {
            opacity: 1;
            transition: 0.5s opacity 2.5s;
        }

        .map-base.active .footsteps-1 .footstep {
            animation: 15s footsteps-1 ease 3s forwards;
        }

        .map-base.active .footsteps-1 .scroll-name {
            animation: 15s scroll-1 ease 3s forwards;
        }

        .map-base.active .footsteps-2 .footstep {
            animation: 15s footsteps-2 ease 3.2s forwards;
        }

        .map-base.active .footsteps-2 .scroll-name {
            animation: 15s scroll-2 ease 3.2s forwards;
        }

        /* Keyframes */
        @keyframes footsteps-1 {
            10% { transform: translate(8px, -15px) rotate(30deg); }
            20% { transform: translate(30px, -45px) rotate(30deg); }
            30% { transform: translate(40px, -75px) rotate(20deg); }
            40% { transform: translate(45px, -100px) rotate(10deg); }
            50% { transform: translate(50px, -125px) rotate(10deg); }
            60% { transform: translate(50px, -135px) rotate(10deg); }
            100% { transform: translate(50px, -135px) rotate(20deg); }
        }

        @keyframes footsteps-2 {
            0% { }
            80% { transform: translate(-170px, -25px) rotate(-90deg); }
            100% { transform: translate(-180px, -25px) rotate(-90deg); }
        }

        @keyframes scroll-1 {
            10% { transform: translate(8px, -15px); }
            20% { transform: translate(30px, -45px); }
            30% { transform: translate(40px, -75px); }
            40% { transform: translate(45px, -100px); }
            50% { transform: translate(50px, -125px); }
            60% { transform: translate(50px, -135px); }
            100% { transform: translate(50px, -135px); }
        }

        @keyframes scroll-2 {
            0% { }
            80% { transform: translate(-170px, -25px); }
            100% { transform: translate(-180px, -25px); }
        }

        /* ================= MAP MEMORY TOKENS (PICTURES ON THE MAP) ================= */
        .map-memory-token {
            position: absolute;
            z-index: 25;
            display: flex;
            flex-direction: column;
            align-items: center;
            cursor: pointer;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.5s ease 2.2s, transform 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            user-select: none;
        }

        .map-base.active .map-memory-token {
            opacity: 1;
            pointer-events: auto;
        }

        .map-memory-token:hover,
        .map-memory-token.focused-token {
            transform: scale(1.18) translateY(-6px);
            z-index: 35;
        }

        .token-seal-frame {
            width: 58px;
            height: 58px;
            border-radius: 50%;
            border: 2px solid var(--gold-bright);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.9), 0 0 10px rgba(223, 162, 44, 0.6);
            overflow: hidden;
            position: relative;
            background: #1a0507;
        }

        .token-seal-frame img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            filter: sepia(35%) contrast(1.1);
            transition: filter 0.3s ease, transform 0.3s ease;
        }

        .map-memory-token:hover .token-seal-frame img,
        .map-memory-token.focused-token .token-seal-frame img {
            filter: sepia(0%) contrast(1.2);
            transform: scale(1.12);
        }

        .token-compass-pulse {
            position: absolute;
            inset: -6px;
            border-radius: 50%;
            border: 1.5px dashed var(--gold-bright);
            pointer-events: none;
            animation: rotateCompass 12s linear infinite;
        }

        @keyframes rotateCompass {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }

        .token-banner-label {
            margin-top: 5px;
            background: rgba(30, 8, 10, 0.92);
            border: 1px solid var(--gold-antique);
            color: #ffe6a0;
            font-family: 'Sarun HarryPotter', 'Cinzel', serif;
            font-size: 0.95rem;
            padding: 2px 8px;
            border-radius: 8px;
            white-space: nowrap;
            box-shadow: 0 3px 8px rgba(0,0,0,0.8);
            pointer-events: none;
            letter-spacing: 0.5px;
        }

        .token-inspect-hint {
            font-size: 0.75rem;
            color: #e5cb9d;
            opacity: 0;
            transition: opacity 0.2s ease;
            background: rgba(0, 0, 0, 0.85);
            padding: 1px 6px;
            border-radius: 4px;
            margin-top: 2px;
        }

        .map-memory-token:hover .token-inspect-hint,
        .map-memory-token.focused-token .token-inspect-hint {
            opacity: 1;
        }

        /* Coordinates of the 6 memories across the unfolded panels */
        /* Side 5 (Leftmost Wing: Hogsmeade Village) */
        .map-side.side-5 .map-memory-token.token-0 {
            top: 220px;
            left: 36px;
        }

        /* Side 3 (North Tower / Gryffindor Quarters) */
        .map-side.side-3 .map-memory-token.token-1 {
            top: 360px;
            left: 34px;
        }

        /* Side 1 (Inner Common Room / Courtyard) */
        .map-side.side-1 .map-memory-token.token-3 {
            top: 140px;
            left: 40px;
        }

        /* Side 2 (Central Classrooms / Training Grounds) */
        .map-side.side-2 .map-memory-token.token-4 {
            top: 380px;
            left: 38px;
        }

        /* Side 4 (Quidditch Pitch / South Grounds) */
        .map-side.side-4 .map-memory-token.token-2 {
            top: 240px;
            left: 40px;
        }

        /* Side 6 (Rightmost Wing: Great Hall / Hogwarts Sanctum) */
        .map-side.side-6 .map-memory-token.token-5 {
            top: 160px;
            left: 36px;
        }
"""

anchor_css = ".gallery-frame-item:hover .gallery-inspect-pill {\n            background: var(--crimson-crest);\n            color: #fff;\n        }"
if anchor_css in content:
    content = content.replace(anchor_css, anchor_css + "\n" + map_css)
    print("Map CSS added successfully.")
else:
    print("Warning: CSS anchor not found, searching with regex...")
    content = re.sub(r'(\.gallery-frame-item:hover \.gallery-inspect-pill\s*\{[^}]+\})', r'\1\n' + map_css, content)
    print("Map CSS added via regex.")

# 3. Replace Section HTML for #tab-gallery
new_gallery_html = """        <!-- ================= TAB 3: GALLERY ================= -->
        <section id="tab-gallery" class="tab-content">
            <h2 class="section-ribbon-title">Enchanted Gallery / สมุดภาพแผนที่ตัวกวน</h2>

            <!-- Gallery View Mode Controls -->
            <div class="gallery-view-mode-bar">
                <button id="viewModeMapBtn" class="view-mode-btn active" onclick="switchGalleryView('map')" title="เปิดมุมมองแผนที่ตัวกวน 3 มิติ">
                    <span class="mode-icon">🗺️</span>
                    <span class="mode-text">แผนที่เวทมนตร์ 3D (Marauder's Map)</span>
                </button>
                <button id="viewModeGridBtn" class="view-mode-btn" onclick="switchGalleryView('grid')" title="เปิดมุมมองสมุดภาพตาราง">
                    <span class="mode-icon">📜</span>
                    <span class="mode-text">สมุดภาพตาราง (Archive Grid)</span>
                </button>
            </div>

            <!-- ===== 3D MARAUDER'S MAP VIEW ===== -->
            <div id="galleryMapView" class="gallery-view-section active">
                <div class="marauder-map-stage">
                    <!-- Spells Incantation Trigger -->
                    <div class="map-incantation-panel">
                        <div class="map-spell-prompt">✦ แตะร่ายคาถาเปิด-ปิด แผนที่ตัวกวนเพื่อสำรวจความทรงจำ ✦</div>
                        <button id="toggleMapBtn" class="toggle-map-btn" onclick="toggleMarauderMap()" title="ร่ายคาถาเปิดแผนที่">
                            <span class="spell-wand-icon">⚡</span>
                            <span id="mapSpellText">ข้าขอสาบานอย่างจริงจังว่าข้านั้นหาความดีมิได้</span>
                        </button>
                        <div class="map-sub-spell-text" id="mapSpellSub">"I solemnly swear that I am up to no good"</div>
                    </div>

                    <!-- Map Memory Compass Navigator ("แต่นำทางแต่รูปภาพเหมือนแผนที่") -->
                    <div class="map-navigator-bar">
                        <button class="map-nav-btn" onclick="navigateToMapMemory(0)" title="นำทางไปยัง Hogsmeade">
                            <span class="pin-symbol">📍</span> Hogsmeade Stroll
                        </button>
                        <button class="map-nav-btn" onclick="navigateToMapMemory(1)" title="นำทางไปยัง North Tower">
                            <span class="pin-symbol">📍</span> Winter Scarf
                        </button>
                        <button class="map-nav-btn" onclick="navigateToMapMemory(2)" title="นำทางไปยัง Quidditch Pitch">
                            <span class="pin-symbol">📍</span> Quidditch Pitch
                        </button>
                        <button class="map-nav-btn" onclick="navigateToMapMemory(3)" title="นำทางไปยัง Gryffindor Room">
                            <span class="pin-symbol">📍</span> Prank Fireworks
                        </button>
                        <button class="map-nav-btn" onclick="navigateToMapMemory(4)" title="นำทางไปยัง Duel Chambers">
                            <span class="pin-symbol">📍</span> Duel Training
                        </button>
                        <button class="map-nav-btn" onclick="navigateToMapMemory(5)" title="นำทางไปยัง The Great Hall">
                            <span class="pin-symbol">📍</span> Fierce Resolve
                        </button>
                    </div>

                    <!-- 3D Stage & Viewport -->
                    <div class="map-viewport-wrapper">
                        <div class="map-scale-container">
                            <div class="map-base" id="maraudersMapBase">
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

                                <!-- Flaps (Center Top & Bottom Folds) -->
                                <div class="map-flap flap--1">
                                    <div class="map-flap__front"></div>
                                    <div class="map-flap__back"></div>
                                </div>
                                <div class="map-flap flap--2">
                                    <div class="map-flap__front"></div>
                                    <div class="map-flap__back"></div>
                                </div>

                                <!-- Side 1: Inner Left Wing (Common Room) -->
                                <div class="map-side side-1" style="--image: url('https://meowlivia.s3.us-east-2.amazonaws.com/codepen/map/8.png')">
                                    <div class="front">
                                        <!-- Memory Pin 3: Prank Fireworks -->
                                        <div class="map-memory-token token-3" id="mapToken-3" onclick="openGalleryItem(3)" title="ตรวจดูภาพ: Prank Fireworks">
                                            <div class="token-compass-pulse"></div>
                                            <div class="token-seal-frame">
                                                <img src="images/alexan-profile.jpg" alt="Prank Fireworks" />
                                            </div>
                                            <div class="token-banner-label">Prank Fireworks</div>
                                            <div class="token-inspect-hint">✦ แตะเปิดดู</div>
                                        </div>
                                    </div>
                                    <div class="back"></div>
                                </div>

                                <!-- Side 2: Inner Right Wing (Duel Classrooms) -->
                                <div class="map-side side-2" style="--image: url('https://meowlivia.s3.us-east-2.amazonaws.com/codepen/map/10.png')">
                                    <div class="front">
                                        <!-- Memory Pin 4: Duel Training -->
                                        <div class="map-memory-token token-4" id="mapToken-4" onclick="openGalleryItem(4)" title="ตรวจดูภาพ: Duel Training">
                                            <div class="token-compass-pulse"></div>
                                            <div class="token-seal-frame">
                                                <img src="images/alexan-profile.jpg" alt="Duel Training" />
                                            </div>
                                            <div class="token-banner-label">Duel Training</div>
                                            <div class="token-inspect-hint">✦ แตะเปิดดู</div>
                                        </div>
                                    </div>
                                    <div class="back"></div>
                                </div>

                                <!-- Side 3: Middle Left Wing (Tower Corridor) -->
                                <div class="map-side side-3" style="--image: url('https://meowlivia.s3.us-east-2.amazonaws.com/codepen/map/7.png')">
                                    <div class="front">
                                        <!-- Memory Pin 1: Winter Scarf -->
                                        <div class="map-memory-token token-1" id="mapToken-1" onclick="openGalleryItem(1)" title="ตรวจดูภาพ: Winter Scarf">
                                            <div class="token-compass-pulse"></div>
                                            <div class="token-seal-frame">
                                                <img src="images/scene-2.jpg" alt="Winter Scarf" />
                                            </div>
                                            <div class="token-banner-label">Winter Scarf</div>
                                            <div class="token-inspect-hint">✦ แตะเปิดดู</div>
                                        </div>
                                    </div>
                                    <div class="back"></div>
                                </div>

                                <!-- Side 4: Middle Right Wing (Quidditch Grounds) -->
                                <div class="map-side side-4" style="--image: url('https://meowlivia.s3.us-east-2.amazonaws.com/codepen/map/11.png')">
                                    <div class="front">
                                        <!-- Memory Pin 2: Quidditch Pitch -->
                                        <div class="map-memory-token token-2" id="mapToken-2" onclick="openGalleryItem(2)" title="ตรวจดูภาพ: Quidditch Pitch">
                                            <div class="token-compass-pulse"></div>
                                            <div class="token-seal-frame">
                                                <img src="images/scene-3.jpg" alt="Quidditch Pitch" />
                                            </div>
                                            <div class="token-banner-label">Quidditch Pitch</div>
                                            <div class="token-inspect-hint">✦ แตะเปิดดู</div>
                                        </div>
                                    </div>
                                    <div class="back"></div>
                                </div>

                                <!-- Side 5: Outer Left Wing (Hogsmeade Village) & Front Cover Left -->
                                <div class="map-side side-5" style="--image: url('https://meowlivia.s3.us-east-2.amazonaws.com/codepen/map/2.png')">
                                    <div class="front">
                                        <!-- Memory Pin 0: Hogsmeade Stroll -->
                                        <div class="map-memory-token token-0" id="mapToken-0" onclick="openGalleryItem(0)" title="ตรวจดูภาพ: Hogsmeade Stroll">
                                            <div class="token-compass-pulse"></div>
                                            <div class="token-seal-frame">
                                                <img src="images/scene-1.jpg" alt="Hogsmeade Stroll" />
                                            </div>
                                            <div class="token-banner-label">Hogsmeade Stroll</div>
                                            <div class="token-inspect-hint">✦ แตะเปิดดู</div>
                                        </div>
                                    </div>
                                    <div class="back"></div>
                                </div>

                                <!-- Side 6: Outer Right Wing (Great Hall Sanctum) & Front Cover Right -->
                                <div class="map-side side-6" style="--image: url('https://meowlivia.s3.us-east-2.amazonaws.com/codepen/map/16.png')">
                                    <div class="front">
                                        <!-- Memory Pin 5: Fierce Resolve -->
                                        <div class="map-memory-token token-5" id="mapToken-5" onclick="openGalleryItem(5)" title="ตรวจดูภาพ: Fierce Resolve">
                                            <div class="token-compass-pulse"></div>
                                            <div class="token-seal-frame">
                                                <img src="images/alexan-profile.jpg" alt="Fierce Resolve" />
                                            </div>
                                            <div class="token-banner-label">Fierce Resolve</div>
                                            <div class="token-inspect-hint">✦ แตะเปิดดู</div>
                                        </div>
                                    </div>
                                    <div class="back"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ===== CLASSIC MOSAIC GRID VIEW ===== -->
            <div id="galleryGridView" class="gallery-view-section">
                <div class="gallery-mosaic-grid">
                    <div class="gallery-frame-item" role="button" tabindex="0" aria-label="ตรวจดูภาพ Hogsmeade Stroll"
                        onclick="openGalleryItem(0)">
                        <svg class="gallery-svg-icon" viewBox="0 0 24 24">
                            <path
                                d="M11 2v4.07l-2.7-1.56-.99 1.73L10 7.8v2.2L7.8 8.87l1.43-2.48-1.73-.99L6.07 8.1 2 6v2l3.46 2L2 12v2l3.46-2L2 14v2l4.07-2.1 1.43 2.48 1.73-.99-1.27-2.2H10v2.2l-2.69 1.56.99 1.73L11 17.93V22h2v-4.07l2.7 1.56.99-1.73L14 16.2v-2.2l2.2 1.13-1.43 2.48 1.73.99 1.43-2.7L22 18v-2l-3.46-2L22 12v-2l-3.46 2L22 10V8l-4.07 2.1-1.43-2.48-1.73.99 1.27 2.2H14V8.8l2.69-1.56-.99-1.73L13 6.07V2h-2z" />
                        </svg>
                        <div class="gallery-art-title">Hogsmeade Stroll</div>
                        <div class="gallery-art-desc">เดินเล่นฮอกส์มี้ดกับเพื่อน จิบเบียร์บัตเตอร์อุ่นๆ หน้าร้านไม้กวาดสามอัน</div>
                        <div class="gallery-inspect-pill">ตรวจดูภาพ ✦ INSPECT</div>
                    </div>
                    <div class="gallery-frame-item" role="button" tabindex="0" aria-label="ตรวจดูภาพ Winter Scarf"
                        onclick="openGalleryItem(1)">
                        <svg class="gallery-svg-icon" viewBox="0 0 24 24">
                            <path
                                d="M12 3C7 3 3 6 3 9c0 2 2 3.5 5 4.5V21l4-2 4 2v-7.5c3-1 5-2.5 5-4.5 0-3-4-6-9-6zm-2 14.5l-2 1v-4.8c.6.2 1.3.4 2 .6v3.2zm6 0v-3.2c.7-.2 1.4-.4 2-.6v4.8l-2-1z" />
                        </svg>
                        <div class="gallery-art-title">Winter Scarf</div>
                        <div class="gallery-art-desc">พอร์ตเทรตผ้าพันคอรับลมหนาวสีแดงเลือดหมูสลับทองลายกริฟฟินดอร์</div>
                        <div class="gallery-inspect-pill">ตรวจดูภาพ ✦ INSPECT</div>
                    </div>
                    <div class="gallery-frame-item" role="button" tabindex="0" aria-label="ตรวจดูภาพ Quidditch Pitch"
                        onclick="openGalleryItem(2)">
                        <svg class="gallery-svg-icon" viewBox="0 0 24 24">
                            <path
                                d="M19.36 2.64a1.5 1.5 0 0 0-2.12 0L8.2 11.68l-3.54-.71a1.5 1.5 0 0 0-1.63.79l-1 1.73a1.5 1.5 0 0 0 .34 1.83l3.54 3.54-3.62 3.62 1.41 1.41 3.62-3.62 3.54 3.54a1.5 1.5 0 0 0 1.83.34l1.73-1a1.5 1.5 0 0 0 .79-1.63l-.71-3.54 9.04-9.04a1.5 1.5 0 0 0 0-2.12l-1.42-1.42z" />
                        </svg>
                        <div class="gallery-art-title">Quidditch Pitch</div>
                        <div class="gallery-art-desc">ทีมสควอดสนามควิดดิชและไม้กวาดไฟเยอร์โบลด์คู่ใจ</div>
                        <div class="gallery-inspect-pill">ตรวจดูภาพ ✦ INSPECT</div>
                    </div>
                    <div class="gallery-frame-item" role="button" tabindex="0" aria-label="ตรวจดูภาพ Prank Fireworks"
                        onclick="openGalleryItem(3)">
                        <svg class="gallery-svg-icon" viewBox="0 0 24 24">
                            <path d="M12 2l2.4 7.2h7.6l-6 4.8 2.3 7.2-6.3-4.6-6.3 4.6 2.3-7.2-6-4.8h7.6z" />
                        </svg>
                        <div class="gallery-art-title">Prank Fireworks</div>
                        <div class="gallery-art-desc">ภาพจังหวะหน้าแดงแจ๋ตอนโดนจับได้ว่าแอบจุดประทัดควันแกล้งคน</div>
                        <div class="gallery-inspect-pill">ตรวจดูภาพ ✦ INSPECT</div>
                    </div>
                    <div class="gallery-frame-item" role="button" tabindex="0" aria-label="ตรวจดูภาพ Duel Training"
                        onclick="openGalleryItem(4)">
                        <svg class="gallery-svg-icon" viewBox="0 0 24 24">
                            <path
                                d="M14.5 2.5L13 4l1.5 1.5L16 4l-1.5-1.5zm-5 0L8 4l1.5 1.5L11 4l-1.5-1.5zM7 8l-4 4 1.4 1.4L7 10.8V21h2v-8.2l2.6 2.6 1.4-1.4L7 8zm10 0l-6 6 1.4 1.4L15 12.8V21h2v-8.2l2.6 2.6 1.4-1.4L17 8z" />
                        </svg>
                        <div class="gallery-art-title">Duel Training</div>
                        <div class="gallery-art-desc">รอยยิ้มหลังการฝึกดวลวิชาป้องกันตัวจากศาสตร์มืดและคราบเขม่า</div>
                        <div class="gallery-inspect-pill">ตรวจดูภาพ ✦ INSPECT</div>
                    </div>
                    <div class="gallery-frame-item" role="button" tabindex="0" aria-label="ตรวจดูภาพ Fierce Resolve"
                        onclick="openGalleryItem(5)">
                        <img src="images/hogwarts-logo.png" class="gallery-svg-icon" alt="Hogwarts"
                            style="object-fit: contain;" />
                        <div class="gallery-art-title">Fierce Resolve</div>
                        <div class="gallery-art-desc">แววตาดุเดือดสู้ศึกและจิตวิญญาณความกล้าหาญแห่งกริฟฟินดอร์</div>
                        <div class="gallery-inspect-pill">ตรวจดูภาพ ✦ INSPECT</div>
                    </div>
                </div>
            </div>
        </section>"""

old_gallery_pattern = r'<!-- ================= TAB 3: GALLERY ================= -->\s*<section id="tab-gallery" class="tab-content">.*?</section>'
match = re.search(old_gallery_pattern, content, re.DOTALL)
if match:
    content = content[:match.start()] + new_gallery_html + content[match.end():]
    print("Gallery section HTML replaced successfully.")
else:
    print("ERROR: old_gallery_pattern not found.")
    sys.exit(1)

# 4. Update JavaScript (galleryStories and Marauder's Map controllers)
old_stories = """        const galleryStories = [
            {
                title: "Hogsmeade Stroll / เดินเล่นฮอกส์มี้ด",
                desc: "ช็อตช่วงวันหยุดสุดสัปดาห์ในฤดูหนาวที่หมู่บ้านฮอกส์มี้ด อเล็กซ์แอบพาเพื่อนย่องไปซื้อขนมร้านฮันนี่ดุกส์ และนั่งคุยกันข้างเตาผิงร้านไม้กวาดสามอันพร้อมบัตเตอร์เบียร์ฟองนุ่ม",
                image: "images/scene-1.jpg"
            },
            {
                title: "Winter Scarf / ผ้าพันคอรับลมหนาว",
                desc: "ผ้าพันคอไหมพรมลายทางสีแดงเลือดหมูสลับทองที่ถักเองอย่างเบี้ยวๆ แต่นุ่มอุ่นสบาย ช่วยบังลมหนาวจากยอดหอคอยกริฟฟินดอร์",
                image: "images/scene-2.jpg"
            },
            {
                title: "Quidditch Pitch / สนามควิดดิช",
                desc: "ภาพช่วงก่อนแมตช์การแข่งขันใหญ่กับสลิธีริน อเล็กซ์ถือไม้กวาดและไม้ตีบลัดเจอร์ด้วยสีหน้ามั่นใจเต็มร้อย พร้อมจะพาทีมคว้าชัยชนะ",
                image: "images/scene-3.jpg"
            },
            {
                title: "Prank Fireworks / จังหวะหน้าแดง",
                desc: "เหตุการณ์ตอนที่ตั้งใจจะจุดประทัดควันดักแกล้งเพื่อนในห้องนั่งเล่นรวม แต่โดนจับได้จนแก้ตัวไม่ถูกจนหน้าแดงแจ๋",
                image: "images/alexan-profile.png"
            },
            {
                title: "Duel Training / หลังการดวลฝึกซ้อม",
                desc: "เสื้อคลุมเปื้อนเขม่าควันคาถาหลังฝึกดวลวิชาป้องกันตัวจากศาสตร์มืดจนเหงื่อท่วม แต่ยังมีรอยยิ้มภาคภูมิใจไม่เคยยอมแพ้",
                image: "images/alexan-profile.png"
            },
            {
                title: "Fierce Resolve / จิตวิญญาณกริฟฟินดอร์",
                desc: "แววตาแน่วแน่แม้จะสูญเสียดวงตาข้างซ้ายและขาขวา แต่อเล็กซ์ก็พิสูจน์ให้ทุกคนเห็นว่าหัวใจแห่งความกล้าหาญไม่ได้สูญเสียไปตามร่างกายเลย",
                image: "images/alexan-profile.png"
            }
        ];"""

new_stories_and_map_js = """        const galleryStories = [
            {
                title: "Hogsmeade Stroll / เดินเล่นฮอกส์มี้ด",
                desc: "ช็อตช่วงวันหยุดสุดสัปดาห์ในฤดูหนาวที่หมู่บ้านฮอกส์มี้ด อเล็กซ์แอบพาเพื่อนย่องไปซื้อขนมร้านฮันนี่ดุกส์ และนั่งคุยกันข้างเตาผิงร้านไม้กวาดสามอันพร้อมบัตเตอร์เบียร์ฟองนุ่ม",
                image: "images/scene-1.jpg"
            },
            {
                title: "Winter Scarf / ผ้าพันคอรับลมหนาว",
                desc: "ผ้าพันคอไหมพรมลายทางสีแดงเลือดหมูสลับทองที่ถักเองอย่างเบี้ยวๆ แต่นุ่มอุ่นสบาย ช่วยบังลมหนาวจากยอดหอคอยกริฟฟินดอร์",
                image: "images/scene-2.jpg"
            },
            {
                title: "Quidditch Pitch / สนามควิดดิช",
                desc: "ภาพช่วงก่อนแมตช์การแข่งขันใหญ่กับสลิธีริน อเล็กซ์ถือไม้กวาดและไม้ตีบลัดเจอร์ด้วยสีหน้ามั่นใจเต็มร้อย พร้อมจะพาทีมคว้าชัยชนะ",
                image: "images/scene-3.jpg"
            },
            {
                title: "Prank Fireworks / จังหวะหน้าแดง",
                desc: "เหตุการณ์ตอนที่ตั้งใจจะจุดประทัดควันดักแกล้งเพื่อนในห้องนั่งเล่นรวม แต่โดนจับได้จนแก้ตัวไม่ถูกจนหน้าแดงแจ๋",
                image: "images/alexan-profile.jpg"
            },
            {
                title: "Duel Training / หลังการดวลฝึกซ้อม",
                desc: "เสื้อคลุมเปื้อนเขม่าควันคาถาหลังฝึกดวลวิชาป้องกันตัวจากศาสตร์มืดจนเหงื่อท่วม แต่ยังมีรอยยิ้มภาคภูมิใจไม่เคยยอมแพ้",
                image: "images/alexan-profile.jpg"
            },
            {
                title: "Fierce Resolve / จิตวิญญาณกริฟฟินดอร์",
                desc: "แววตาแน่วแน่แม้จะสูญเสียดวงตาข้างซ้ายและขาขวา แต่อเล็กซ์ก็พิสูจน์ให้ทุกคนเห็นว่าหัวใจแห่งความกล้าหาญไม่ได้สูญเสียไปตามร่างกายเลย",
                image: "images/alexan-profile.jpg"
            }
        ];

        // ================= Marauder's Map Controls & Waypoint Navigation =================
        let isMarauderMapActive = false;

        function toggleMarauderMap() {
            const mapBase = document.getElementById('maraudersMapBase');
            const spellText = document.getElementById('mapSpellText');
            const spellSub = document.getElementById('mapSpellSub');
            if (!mapBase) return;

            isMarauderMapActive = !isMarauderMapActive;
            if (isMarauderMapActive) {
                mapBase.classList.add('active');
                if (spellText) spellText.textContent = "แผนลวงสำเร็จแล้ว";
                if (spellSub) spellSub.textContent = '"Mischief Managed"';
            } else {
                mapBase.classList.remove('active');
                if (spellText) spellText.textContent = "ข้าขอสาบานอย่างจริงจังว่าข้านั้นหาความดีมิได้";
                if (spellSub) spellSub.textContent = '"I solemnly swear that I am up to no good"';
            }
        }

        function openMarauderMap() {
            const mapBase = document.getElementById('maraudersMapBase');
            const spellText = document.getElementById('mapSpellText');
            const spellSub = document.getElementById('mapSpellSub');
            if (mapBase && !mapBase.classList.contains('active')) {
                mapBase.classList.add('active');
                isMarauderMapActive = true;
                if (spellText) spellText.textContent = "แผนลวงสำเร็จแล้ว";
                if (spellSub) spellSub.textContent = '"Mischief Managed"';
            }
        }

        function navigateToMapMemory(index) {
            // If in grid view, switch to map view
            switchGalleryView('map');

            // Open the map if closed
            openMarauderMap();

            // Highlight active waypoint badge and button
            document.querySelectorAll('.map-memory-token').forEach(el => el.classList.remove('focused-token'));
            document.querySelectorAll('.map-nav-btn').forEach(el => el.classList.remove('active-target'));

            const targetToken = document.getElementById(`mapToken-${index}`);
            const navBtns = document.querySelectorAll('.map-nav-btn');
            if (navBtns[index]) {
                navBtns[index].classList.add('active-target');
            }

            if (targetToken) {
                targetToken.classList.add('focused-token');
            }

            // Open inspection modal after a brief suspense
            setTimeout(() => {
                openGalleryItem(index);
            }, 400);
        }

        function switchGalleryView(mode) {
            const mapView = document.getElementById('galleryMapView');
            const gridView = document.getElementById('galleryGridView');
            const mapBtn = document.getElementById('viewModeMapBtn');
            const gridBtn = document.getElementById('viewModeGridBtn');

            if (mode === 'map') {
                if (mapView) mapView.classList.add('active');
                if (gridView) gridView.classList.remove('active');
                if (mapBtn) mapBtn.classList.add('active');
                if (gridBtn) gridBtn.classList.remove('active');
            } else {
                if (mapView) mapView.classList.remove('active');
                if (gridView) gridView.classList.add('active');
                if (mapBtn) mapBtn.classList.remove('active');
                if (gridBtn) gridBtn.classList.add('active');
            }
        }"""

if old_stories in content:
    content = content.replace(old_stories, new_stories_and_map_js)
    print("JS logic & galleryStories updated.")
else:
    print("Warning: old_stories exact match not found, searching regex...")
    content = re.sub(
        r'const galleryStories\s*=\s*\[.*?\];',
        new_stories_and_map_js,
        content,
        flags=re.DOTALL
    )
    print("JS logic replaced via regex.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html written successfully!")
