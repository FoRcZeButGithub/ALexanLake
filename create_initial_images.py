import os
import math
from PIL import Image, ImageDraw, ImageFilter

os.makedirs('images', exist_ok=True)

# Colors
BURGUNDY_DARK = (30, 4, 8)
BURGUNDY_MID = (75, 12, 22)
BURGUNDY_LIGHT = (110, 20, 35)
GOLD_BRIGHT = (255, 218, 121)
GOLD_DEEP = (212, 163, 55)
GOLD_SHADOW = (130, 90, 20)
SILVER_BORDER = (190, 195, 205)
DARK_FRAME = (18, 4, 8)

# 1. Generate crest.png (Shield with Lion)
def create_crest():
    size = (400, 480)
    img = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    w, h = size
    shield_pts = [
        (40, 60),
        (w//2, 40),
        (w - 40, 60),
        (w - 40, int(h * 0.65)),
        (w//2, h - 30),
        (40, int(h * 0.65)),
    ]
    
    # Outer silver ornate border
    draw.polygon(shield_pts, fill=(160, 165, 175, 255))
    # Inner border
    inner_pts = [
        (48, 68),
        (w//2, 50),
        (w - 48, 68),
        (w - 48, int(h * 0.64)),
        (w//2, h - 42),
        (48, int(h * 0.64)),
    ]
    draw.polygon(inner_pts, fill=(60, 65, 75, 255))
    
    # Crimson core
    core_pts = [
        (56, 76),
        (w//2, 60),
        (w - 56, 76),
        (w - 56, int(h * 0.63)),
        (w//2, h - 54),
        (56, int(h * 0.63)),
    ]
    draw.polygon(core_pts, fill=(100, 15, 25, 255))
    
    # Draw ornate golden lion in center
    cx, cy = w//2, int(h * 0.48)
    # Head & Mane
    draw.ellipse([cx - 55, cy - 70, cx + 45, cy + 30], fill=GOLD_DEEP)
    draw.ellipse([cx - 45, cy - 60, cx + 35, cy + 20], fill=GOLD_BRIGHT)
    # Snout
    draw.polygon([(cx + 10, cy - 40), (cx + 65, cy - 25), (cx + 55, cy + 5), (cx + 10, cy - 10)], fill=GOLD_BRIGHT)
    # Crown/Ears
    draw.polygon([(cx - 30, cy - 85), (cx - 10, cy - 65), (cx - 45, cy - 65)], fill=GOLD_DEEP)
    draw.polygon([(cx - 5, cy - 85), (cx + 15, cy - 65), (cx - 20, cy - 65)], fill=GOLD_DEEP)
    # Eye
    draw.ellipse([cx + 22, cy - 36, cx + 32, cy - 26], fill=(50, 5, 10, 255))
    draw.ellipse([cx + 26, cy - 33, cx + 29, cy - 30], fill=(255, 255, 255, 255))
    # Roaring jaw
    draw.polygon([(cx + 25, cy + 5), (cx + 55, cy + 12), (cx + 40, cy + 28), (cx + 15, cy + 20)], fill=GOLD_DEEP)
    draw.polygon([(cx + 30, cy - 5), (cx + 45, cy + 5), (cx + 20, cy + 5)], fill=(30, 0, 0, 255))
    # Forepaw raised
    draw.polygon([(cx + 10, cy + 25), (cx + 70, cy + 45), (cx + 60, cy + 70), (cx - 5, cy + 55)], fill=GOLD_DEEP)
    draw.ellipse([cx + 55, cy + 40, cx + 80, cy + 65], fill=GOLD_BRIGHT)
    
    # Mane spikes
    for angle in range(120, 260, 20):
        rad = math.radians(angle)
        sx = cx + int(70 * math.cos(rad))
        sy = cy - 20 + int(70 * math.sin(rad))
        draw.polygon([(sx, sy), (sx + 20, sy - 10), (sx - 10, sy + 15)], fill=GOLD_SHADOW)
        
    img.save('images/crest.png')
    print("Created images/crest.png")

# 2. Generate alexan-profile.png (Circular Portrait matching the blushing anime sketch)
def create_profile():
    size = (600, 600)
    img = Image.new('RGB', size, (245, 238, 230))
    draw = ImageDraw.Draw(img)
    cx, cy = 300, 300
    
    draw.rectangle([0, 0, 600, 600], fill=(245, 240, 235))
    
    # Shoulders
    draw.polygon([(100, 600), (220, 430), (380, 430), (500, 600)], fill=(215, 175, 175))
    # Neck & collar
    draw.polygon([(240, 440), (300, 490), (360, 440), (330, 360), (270, 360)], fill=(255, 250, 245))
    draw.polygon([(285, 450), (300, 520), (315, 450)], fill=(140, 20, 30))
    draw.line([(290, 470), (310, 470)], fill=GOLD_BRIGHT, width=3)
    
    # Head contour (anime boy jawline)
    jaw_pts = [
        (210, 250), (220, 320), (250, 380), (300, 420), (350, 380), (380, 320), (390, 250)
    ]
    draw.polygon(jaw_pts, fill=(255, 242, 235))
    draw.line(jaw_pts, fill=(40, 30, 30), width=4)
    
    # Ears
    draw.polygon([(190, 280), (215, 250), (215, 330), (195, 310)], fill=(255, 230, 225), outline=(40, 30, 30))
    draw.polygon([(410, 280), (385, 250), (385, 330), (405, 310)], fill=(255, 230, 225), outline=(40, 30, 30))
    
    # Cheeks blush
    draw.ellipse([225, 300, 285, 345], fill=(255, 190, 195))
    for x_b in range(235, 280, 8):
        draw.line([(x_b, 335), (x_b + 12, 310)], fill=(210, 60, 80), width=3)
    draw.ellipse([315, 300, 375, 345], fill=(255, 190, 195))
    for x_b in range(325, 370, 8):
        draw.line([(x_b, 335), (x_b + 12, 310)], fill=(210, 60, 80), width=3)
    draw.polygon([(205, 270), (215, 285), (200, 290)], fill=(200, 230, 255), outline=(40, 40, 50))
    
    # Smiling Mouth with slight fang
    mouth_pts = [(265, 360), (300, 400), (335, 360)]
    draw.polygon(mouth_pts, fill=(30, 10, 15))
    draw.line(mouth_pts + [(265, 360)], fill=(20, 10, 10), width=4)
    draw.ellipse([285, 375, 315, 398], fill=(235, 90, 105))
    draw.polygon([(270, 360), (282, 370), (294, 360)], fill=(255, 255, 255))
    
    # Eyes
    draw.line([(240, 280), (260, 272), (280, 282)], fill=(30, 25, 25), width=5)
    draw.ellipse([248, 280, 272, 300], fill=(45, 30, 25))
    draw.ellipse([254, 283, 262, 290], fill=(255, 255, 255))
    draw.line([(320, 282), (340, 272), (360, 280)], fill=(30, 25, 25), width=5)
    draw.ellipse([328, 280, 352, 300], fill=(45, 30, 25))
    draw.ellipse([334, 283, 342, 290], fill=(255, 255, 255))
    
    # Eyebrows
    draw.line([(235, 260), (260, 252), (282, 262)], fill=(30, 25, 25), width=4)
    draw.line([(318, 262), (340, 252), (365, 260)], fill=(30, 25, 25), width=4)
    
    # Nose
    draw.line([(298, 320), (303, 332)], fill=(40, 30, 30), width=3)
    
    # Messy Black Hair
    hair_color = (25, 20, 28)
    draw.ellipse([180, 90, 420, 300], fill=hair_color)
    
    bangs = [
        [(210, 240), (225, 200), (230, 260)],
        [(228, 260), (242, 195), (255, 270)],
        [(252, 270), (270, 190), (285, 285)],
        [(280, 285), (300, 185), (315, 275)],
        [(310, 275), (330, 190), (345, 280)],
        [(340, 280), (355, 200), (370, 260)],
        [(365, 260), (380, 210), (395, 245)],
    ]
    for b in bangs:
        draw.polygon(b, fill=hair_color)
        
    tufts = [
        [(220, 140), (200, 90), (260, 120)],
        [(250, 110), (270, 60), (310, 95)],
        [(300, 95), (335, 65), (360, 105)],
        [(350, 105), (390, 80), (400, 140)],
    ]
    for t in tufts:
        draw.polygon(t, fill=hair_color)
        
    for hx in range(210, 390, 15):
        draw.line([(hx, 160), (hx + 8, 180)], fill=(120, 110, 130), width=3)
        draw.line([(hx + 3, 168), (hx + 6, 174)], fill=(220, 215, 230), width=2)
        
    img.save('images/alexan-profile.png')
    print("Created images/alexan-profile.png")

# 3. Generate 3 scene images: scene-1.jpg, scene-2.jpg, scene-3.jpg (16:10 ratio)
def create_scenes():
    w, h = 500, 320
    
    # Scene 1: Alexan & friend in Hogsmeade winter
    s1 = Image.new('RGB', (w, h), (35, 30, 45))
    d1 = ImageDraw.Draw(s1)
    d1.polygon([(20, h), (80, 100), (140, h)], fill=(45, 40, 60))
    d1.polygon([(120, h), (200, 80), (280, h)], fill=(55, 50, 70))
    d1.polygon([(260, h), (340, 110), (420, h)], fill=(45, 40, 60))
    d1.ellipse([210, 130, 240, 160], fill=(255, 230, 140))
    d1.ellipse([110, 100, 210, 200], fill=(20, 18, 25))
    d1.polygon([(130, 170), (190, 170), (160, 230)], fill=(240, 220, 210))
    d1.polygon([(80, 210), (220, 210), (240, h), (60, h)], fill=(30, 25, 35))
    d1.ellipse([270, 110, 370, 210], fill=(25, 20, 25))
    d1.polygon([(290, 170), (350, 170), (320, 230)], fill=(250, 230, 220))
    d1.line([(305, 195), (315, 195)], fill=(220, 70, 80), width=2)
    d1.line([(325, 195), (335, 195)], fill=(220, 70, 80), width=2)
    d1.polygon([(240, 220), (380, 220), (400, h), (220, h)], fill=(120, 30, 40))
    for sx, sy in [(50, 40), (120, 80), (280, 50), (390, 70), (460, 120), (180, 230), (340, 280), (80, 290)]:
        d1.ellipse([sx, sy, sx + 4, sy + 4], fill=(255, 255, 255))
    s1.save('images/scene-1.jpg', quality=95)
    print("Created images/scene-1.jpg")
    
    # Scene 2: Alexan portrait in snowy village with thick scarf
    s2 = Image.new('RGB', (w, h), (40, 35, 55))
    d2 = ImageDraw.Draw(s2)
    d2.ellipse([100, 60, 150, 110], fill=(180, 140, 220))
    d2.ellipse([340, 80, 390, 130], fill=(200, 160, 240))
    cx = w // 2
    d2.ellipse([cx - 80, 40, cx + 80, 180], fill=(25, 20, 28))
    d2.polygon([(cx - 50, 120), (cx + 50, 120), (cx, 190)], fill=(250, 235, 225))
    d2.line([(cx - 35, 135), (cx - 15, 135)], fill=(30, 20, 25), width=3)
    d2.line([(cx + 15, 135), (cx + 35, 135)], fill=(30, 20, 25), width=3)
    d2.ellipse([cx - 28, 140, cx - 22, 148], fill=(230, 100, 110))
    d2.ellipse([cx + 22, 140, cx + 28, 148], fill=(230, 100, 110))
    d2.ellipse([cx - 90, 175, cx + 90, 255], fill=(135, 25, 35))
    d2.line([(cx - 80, 200), (cx + 80, 200)], fill=GOLD_BRIGHT, width=8)
    d2.line([(cx - 75, 225), (cx + 75, 225)], fill=GOLD_BRIGHT, width=8)
    d2.polygon([(cx - 160, h), (cx - 90, 240), (cx + 90, 240), (cx + 160, h)], fill=(45, 35, 40))
    for sx, sy in [(80, 50), (140, 120), (370, 70), (430, 140), (90, 260), (410, 270)]:
        d2.ellipse([sx, sy, sx + 5, sy + 5], fill=(255, 255, 255))
    s2.save('images/scene-2.jpg', quality=95)
    print("Created images/scene-2.jpg")
    
    # Scene 3: Alexan with Quidditch squad holding beaters' bats
    s3 = Image.new('RGB', (w, h), (30, 25, 35))
    d3 = ImageDraw.Draw(s3)
    d3.polygon([(40, h), (60, 40), (80, h)], fill=(45, 38, 50))
    d3.polygon([(420, h), (440, 50), (460, h)], fill=(45, 38, 50))
    d3.ellipse([80, 120, 140, 180], fill=(20, 18, 25))
    d3.polygon([(70, 180), (150, 180), (160, h), (60, h)], fill=(60, 45, 55))
    d3.line([(140, 140), (160, 80)], fill=(120, 90, 60), width=6)
    
    d3.ellipse([360, 120, 420, 180], fill=(20, 18, 25))
    d3.polygon([(350, 180), (430, 180), (440, h), (340, h)], fill=(60, 45, 55))
    d3.line([(340, 140), (320, 80)], fill=(120, 90, 60), width=6)
    
    cx = w // 2
    d3.ellipse([cx - 70, 70, cx + 70, 190], fill=(25, 20, 25))
    d3.polygon([(cx - 45, 140), (cx + 45, 140), (cx, 210)], fill=(250, 235, 225))
    d3.line([(cx - 30, 155), (cx - 10, 160)], fill=(30, 20, 25), width=3)
    d3.line([(cx + 10, 160), (cx + 30, 155)], fill=(30, 20, 25), width=3)
    d3.polygon([(cx - 15, 180), (cx + 15, 180), (cx, 195)], fill=(30, 10, 15))
    d3.polygon([(cx - 110, h), (cx - 60, 210), (cx + 60, 210), (cx + 110, h)], fill=(110, 20, 25))
    d3.line([(cx + 40, 280), (cx + 140, 180)], fill=(150, 110, 70), width=16)
    d3.line([(cx + 120, 200), (cx + 140, 180)], fill=(190, 150, 90), width=18)
    s3.save('images/scene-3.jpg', quality=95)
    print("Created images/scene-3.jpg")

# 4. Generate bg-lion.png (Silhouette Watermark)
def create_bg_lion():
    size = (700, 700)
    img = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    cx, cy = 350, 350
    gold_watermark = (220, 170, 60, 160)
    
    draw.ellipse([cx - 180, cy - 180, cx + 140, cy + 140], fill=gold_watermark)
    draw.polygon([(cx - 40, cy - 100), (cx + 220, cy - 50), (cx + 160, cy + 80), (cx - 20, cy + 30)], fill=gold_watermark)
    draw.polygon([(cx + 40, cy + 40), (cx + 180, cy + 80), (cx + 120, cy + 150), (cx - 10, cy + 80)], fill=gold_watermark)
    draw.polygon([(cx + 60, cy - 10), (cx + 140, cy + 40), (cx + 50, cy + 40)], fill=(0, 0, 0, 0))
    draw.polygon([(cx - 240, cy + 100), (cx + 80, cy + 100), (cx + 20, cy + 320), (cx - 260, cy + 320)], fill=gold_watermark)
    
    img = img.filter(ImageFilter.GaussianBlur(4))
    img.save('images/bg-lion.png')
    print("Created images/bg-lion.png")

# 5. Generate bg-sketches.png (Faded manga sketch strip for bottom bar)
def create_bg_sketches():
    w, h = 1200, 160
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    sketch_color = (255, 230, 200, 45)
    
    for x_offset in [80, 280, 520, 760, 980]:
        draw.ellipse([x_offset, 20, x_offset + 90, 110], outline=sketch_color, width=2)
        draw.line([(x_offset + 10, 40), (x_offset + 30, 10), (x_offset + 50, 45)], fill=sketch_color, width=2)
        draw.line([(x_offset + 45, 30), (x_offset + 70, 12), (x_offset + 85, 45)], fill=sketch_color, width=2)
        draw.line([(x_offset - 30, 140), (x_offset + 20, 110), (x_offset + 70, 110), (x_offset + 120, 140)], fill=sketch_color, width=2)
        draw.line([(x_offset - 20, 150), (x_offset + 110, 10)], fill=sketch_color, width=2)
        
    img.save('images/bg-sketches.png')
    print("Created images/bg-sketches.png")

if __name__ == '__main__':
    create_crest()
    create_profile()
    create_scenes()
    create_bg_lion()
    create_bg_sketches()
    print("All initial images created successfully!")
