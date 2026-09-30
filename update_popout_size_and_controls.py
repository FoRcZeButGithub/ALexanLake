# -*- coding: utf-8 -*-
"""
Fine-tune the Out-of-Frame Pop-Out effect so the character's head visibly and
dramatically pops out above the top gold border, and provide clean CSS variables
so the user can easily adjust the size and position in one place.
"""
import shutil

shutil.copyfile('index.html', 'index.html.before_finetune.bak')
print("[1] Backup created: index.html.before_finetune.bak")

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '/* ==========================================================================\n           POPOUT CHARACTER CARD FRAME (ABOUT TAB)'
pos_start = html.find(start_marker)
pos_end = html.find('</style>', pos_start)

new_popout_css = """/* ==========================================================================
           POPOUT CHARACTER CARD FRAME (ABOUT TAB)
           ตัวละครทะลุล้นออกจากกรอบ (3D Pop-Out Breakout)
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
            /* =========================================================================
               🎛️ จุดปรับแต่งขนาดและตำแหน่งภาพล้นกรอบ (POPOUT CONTROLS)
               คุณสามารถปรับเปลี่ยนตัวเลข 4 ค่านี้เพื่อปรับแต่งได้ตามใจชอบเลยครับ:
               ========================================================================= */
            --popout-card-top: 100px;         /* 🎴 ระดับความสูงขอบบนของการ์ด (เพิ่มเพื่อให้ตัวการ์ดย่อลง ภาพจะดูทะลุล้นออกมามากขึ้น) */
            --popout-img-height: 520px;       /* 📏 ความสูง/ขนาดของรูปตัวละคร (ค่าเริ่มต้น 520px, ลอง 500px - 560px) */
            --popout-img-scale: 1.15;         /* 🔍 สเกลซูมขยายภาพตัวละคร (1.0 = ปกติ, 1.15 = ขยาย 15%) */
            --popout-img-bottom: 0px;         /* ⬆️ เลื่อนรูปขึ้นหรือลง (ค่าบวก = ดันตัวละครขึ้นล้นขอบบนมากขึ้น) */

            position: relative;
            width: 100%;
            max-width: 320px;
            height: 480px;
            margin-top: 40px; /* เว้นระยะด้านบนเพื่อให้หัวตัวละครมีพื้นที่ล้นออกมาอย่างโดดเด่น */
            overflow: visible !important;
            background: transparent !important;
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
            top: var(--popout-card-top, 100px);
            bottom: -10px;
            left: -12px;
            right: -12px;
            background: radial-gradient(circle at 50% 50%, rgba(223, 162, 44, 0.45) 0%, rgba(138, 14, 25, 0.3) 50%, transparent 75%);
            filter: blur(20px);
            border-radius: 35px;
            pointer-events: none;
            z-index: 0;
            opacity: 0.8;
            transition: opacity 0.4s ease;
        }

        .character-portrait-box:hover .popout-ambient-glow {
            opacity: 1;
            filter: blur(26px);
        }

        /* The Rounded Card Frame (Starts down at --popout-card-top) */
        .popout-card-frame {
            position: absolute;
            top: var(--popout-card-top, 100px);
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

        /* Character Pop-out Layer (Top allows 140px overflow, Bottom clips at 28px rounded radius) */
        .popout-character-layer {
            position: absolute;
            top: -140px; /* ยื่นขึ้นไปด้านบน 140px เพื่อให้หัวล้นออกมาได้อย่างอิสระ */
            bottom: 0;
            left: 0;
            right: 0;
            /* ตัดเฉพาะขอบมุมล่างมน 28px ตามขอบการ์ด ด้านบนปล่อยทะลุ 100% */
            clip-path: inset(0px 0px 0px 0px round 0 0 28px 28px);
            -webkit-clip-path: inset(0px 0px 0px 0px round 0 0 28px 28px);
            overflow: visible;
            z-index: 3;
            pointer-events: none;
        }

        .popout-character-img {
            position: absolute;
            bottom: var(--popout-img-bottom, 0px);
            left: 50%;
            transform: translateX(-50%) scale(var(--popout-img-scale, 1.15));
            transform-origin: bottom center;
            height: var(--popout-img-height, 520px);
            width: auto;
            max-width: none;
            object-fit: contain;
            object-position: bottom center;
            filter: drop-shadow(0 14px 28px rgba(0, 0, 0, 0.85));
            transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.2), filter 0.4s ease;
        }

        .character-portrait-box:hover .popout-character-img {
            transform: translateX(-50%) translateY(-6px) scale(calc(var(--popout-img-scale, 1.15) * 1.025));
            filter: drop-shadow(0 20px 35px rgba(0, 0, 0, 0.98)) drop-shadow(0 0 20px rgba(223, 162, 44, 0.45));
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

html = html[:pos_start] + new_popout_css + "\n\n        " + html[pos_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("[2] Successfully updated index.html with fine-tuned popout controls!")
