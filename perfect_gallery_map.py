import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update token styles to be automatically centered with left: 50% and transform: translateX(-50%)
token_css_old_pattern = r'/\* Coordinates of the 6 memories across the unfolded panels.*?(?=\*/\n\s*</style>|\*/\s*</style>|\n\s*</style>)'

token_css_new = """/* Coordinates of the 6 memories across the unfolded panels (dead-center on each 152px wing) */
        .map-memory-token {
            position: absolute;
            z-index: 25;
            display: flex;
            flex-direction: column;
            align-items: center;
            cursor: pointer;
            opacity: 0;
            pointer-events: none;
            left: 50%;
            transform: translateX(-50%);
            transition: opacity 0.5s ease 2.2s, transform 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            user-select: none;
            width: 90px;
        }

        .map-base.active .map-memory-token {
            opacity: 1;
            pointer-events: auto;
        }

        .map-memory-token:hover,
        .map-memory-token.focused-token {
            transform: translateX(-50%) translateY(-8px) scale(1.18);
            z-index: 35;
        }

        .token-seal-frame {
            width: 62px;
            height: 62px;
            border-radius: 50%;
            border: 2px solid var(--gold-bright);
            box-shadow: 0 4px 14px rgba(0, 0, 0, 0.95), 0 0 14px rgba(223, 162, 44, 0.7);
            overflow: hidden;
            position: relative;
            background: #1a0507;
        }

        .token-seal-frame img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            filter: sepia(20%) contrast(1.15);
            transition: filter 0.3s ease, transform 0.3s ease;
        }

        .map-memory-token:hover .token-seal-frame img,
        .map-memory-token.focused-token .token-seal-frame img {
            filter: sepia(0%) contrast(1.25);
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
            background: rgba(30, 8, 10, 0.95);
            border: 1px solid var(--gold-antique);
            color: #ffe6a0;
            font-family: 'Noto Serif Thai', serif;
            font-size: 0.85rem;
            padding: 2px 8px;
            border-radius: 8px;
            white-space: nowrap;
            box-shadow: 0 3px 8px rgba(0,0,0,0.85);
            pointer-events: none;
            letter-spacing: 0.3px;
            text-align: center;
        }

        .token-banner-label .label-en {
            font-family: 'Cinzel', 'Sarun HarryPotter', cursive, serif;
            font-size: 0.88rem;
            display: block;
            font-weight: 600;
        }

        .token-inspect-hint {
            font-family: 'Noto Serif Thai', serif;
            font-size: 0.8rem;
            color: #fff;
            opacity: 0;
            transition: opacity 0.2s ease;
            background: rgba(80, 10, 15, 0.95);
            border: 1px solid var(--gold-bright);
            padding: 2px 7px;
            border-radius: 4px;
            margin-top: 3px;
            white-space: nowrap;
            box-shadow: 0 2px 6px rgba(0,0,0,0.8);
        }

        .map-memory-token:hover .token-inspect-hint,
        .map-memory-token.focused-token .token-inspect-hint {
            opacity: 1;
        }

        /* Vertical Top coordinates for each wing */
        .map-side.side-5 .map-memory-token.token-0 { top: 180px; }
        .map-side.side-3 .map-memory-token.token-1 { top: 290px; }
        .map-side.side-1 .map-memory-token.token-3 { top: 160px; }
        .map-side.side-2 .map-memory-token.token-4 { top: 360px; }
        .map-side.side-4 .map-memory-token.token-2 { top: 200px; }
        .map-side.side-6 .map-memory-token.token-5 { top: 300px; }
"""

# Replace in CSS
old_token_block = re.search(r'/\* ================= MAP MEMORY TOKENS \(PICTURES ON THE MAP\) ================= \*/.*?(?=/\* ===== TAB 4: ABOUT ================= \*/|</style>)', content, re.DOTALL)
if old_token_block:
    content = content[:old_token_block.start()] + "/* ================= MAP MEMORY TOKENS (PICTURES ON THE MAP) ================= */\n        " + token_css_new.strip() + "\n\n        " + content[old_token_block.end():]
    print("Token CSS replaced with centered coords.")

# 2. Update toggle-map-btn, map-spell-prompt, and view-mode-btn to use 'Noto Serif Thai'
content = re.sub(
    r'(\.toggle-map-btn\s*\{[^}]*font-family:\s*)[^;]+;',
    r"\1'Noto Serif Thai', serif;",
    content
)

content = re.sub(
    r'(\.map-spell-prompt\s*\{[^}]*font-family:\s*)[^;]+;',
    r"\1'Noto Serif Thai', serif;",
    content
)

content = re.sub(
    r'(\.map-nav-btn\s*\{[^}]*font-family:\s*)[^;]+;',
    r"\1'Noto Serif Thai', serif;",
    content
)

content = re.sub(
    r'(\.view-mode-btn\s*\{[^}]*font-family:\s*)[^;]+;',
    r"\1'Noto Serif Thai', serif;",
    content
)

# 3. Give toggle-map-btn a slightly larger font size for Thai text
content = re.sub(
    r'(\.toggle-map-btn\s*\{[^}]*font-size:\s*)[^;]+;',
    r"\1 1.45rem;",
    content
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html perfected successfully!")
