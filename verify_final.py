import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("File size:", len(text))
print("Has <style>:", text.count('<style>'))
print("Has </style>:", text.count('</style>'))
print("Has Cinzel:", 'Cinzel' in text)
print("Has Noto Serif Thai:", 'Noto Serif Thai' in text)
print("Has Great Vibes:", 'Great Vibes' in text)
print("Has data-tab=\"home\":", 'data-tab="home"' in text)
print("Has a11y waxSeal:", 'id="waxSeal"' in text)
print("Has chapter flow:", 'parchment-history-flow' in text)
print("Has adaptive embers:", 'loopEmbers' in text)
print("Has visibilitychange listener:", 'visibilitychange' in text)
print("Has crest image:", 'images/crest.png' in text)
print("Has profile image:", 'images/alexan-profile.png' in text)
print("Has scene images:", 'images/scene-1.jpg' in text and 'images/scene-2.jpg' in text and 'images/scene-3.jpg' in text)
print("Has lion watermark:", 'images/bg-lion.png' in text)
print("Has sketch strip:", 'images/bg-sketches.png' in text)

# Let's check lines 1 to 25 of index.html
print("\n--- FIRST 25 LINES ---")
print('\n'.join(text.split('\n')[:25]))

# Let's check the dock navigation
print("\n--- DOCK NAVIGATION ---")
dock_start = text.find('<nav class="common-room-dock"')
print(text[dock_start:dock_start+450])

