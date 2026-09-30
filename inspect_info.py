import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'@font-face\s*\{([^}]+)\}', text):
    font_block = m.group(1)
    name_m = re.search(r'font-family:\s*[\'"]?([^\'";]+)[\'"]?', font_block)
    if name_m:
        print("Font name:", name_m.group(1).strip())



