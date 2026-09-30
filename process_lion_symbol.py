import os
import cv2
import numpy as np
from PIL import Image

src_path = r"C:\Users\HP\.gemini\antigravity-ide\brain\449ba929-5630-4a90-8823-4c2fb143bd62\.user_uploaded\media_1790762588328.jpg"
out_dir = r"c:\Users\HP\Documents\Webapp project\images"
os.makedirs(out_dir, exist_ok=True)

# 1. Load original image
orig_img = Image.open(src_path)

# Bounding box of the lion is roughly Y: 151 to 431, X: 178 to 422
# Crop with a slight balanced margin
crop = orig_img.crop((168, 142, 432, 442)) # 264 x 300
w, h = crop.size

# 2. High-resolution 2x upscale with Lanczos for smooth sub-pixel anti-aliasing
target_w, target_h = w * 2, h * 2 # 528 x 600
crop_hd = crop.resize((target_w, target_h), Image.Resampling.LANCZOS)

# 3. Create precision alpha channel
# Grayscale conversion
gray_arr = np.array(crop_hd.convert('L'), dtype=np.float32)

# Map white background (>=242) to alpha 0 (transparent)
# Map black lion (<=30) to alpha 255 (solid)
# Use smooth cubic Hermite curve for anti-aliased edges
norm = np.clip((242.0 - gray_arr) / (242.0 - 30.0), 0.0, 1.0)
smooth_alpha = (norm * norm * (3.0 - 2.0 * norm) * 255.0).astype(np.uint8)

# 4. Color: Gryffindor Royal Burnished Gold
# Diagonal gradient matching the site's gold theme
yy, xx = np.mgrid[0:target_h, 0:target_w]
grad_factor = 0.3 * (xx / target_w) + 0.7 * (yy / target_h)

# Gryffindor Gold Stops:
# 0.0: Light Radiant Gold Highlight (#fff0a6)
# 0.5: Rich Vibrant Gold (#f3c252 / #dfa22c)
# 1.0: Deep Burnished Antique Gold (#9e6312)
c_top = np.array([255, 240, 166], dtype=np.float32)
c_mid = np.array([243, 194, 82], dtype=np.float32)
c_bot = np.array([160, 102, 18], dtype=np.float32)

rgb_gold = np.zeros((target_h, target_w, 3), dtype=np.uint8)
for i in range(3):
    channel = np.where(
        grad_factor < 0.5,
        c_top[i] + (c_mid[i] - c_top[i]) * (grad_factor / 0.5),
        c_mid[i] + (c_bot[i] - c_mid[i]) * ((grad_factor - 0.5) / 0.5)
    )
    rgb_gold[:, :, i] = np.clip(channel, 0, 255).astype(np.uint8)

rgba_gold = np.dstack([rgb_gold, smooth_alpha])
img_gold = Image.fromarray(rgba_gold, 'RGBA')
lion_png_path = os.path.join(out_dir, "lion-symbol.png")
img_gold.save(lion_png_path, "PNG", optimize=True)
print(f"Saved: {lion_png_path} ({img_gold.size})")

# 5. Flat Gold Version
rgb_flat_gold = np.zeros((target_h, target_w, 3), dtype=np.uint8)
rgb_flat_gold[:, :] = [255, 216, 117] # #ffd875
img_flat_gold = Image.fromarray(np.dstack([rgb_flat_gold, smooth_alpha]), 'RGBA')
img_flat_gold.save(os.path.join(out_dir, "lion-symbol-gold.png"), "PNG", optimize=True)

# 6. White Version
rgb_white = np.full((target_h, target_w, 3), 255, dtype=np.uint8)
img_white = Image.fromarray(np.dstack([rgb_white, smooth_alpha]), 'RGBA')
img_white.save(os.path.join(out_dir, "lion-symbol-white.png"), "PNG", optimize=True)

# 7. Generate clean SVG vector version
crop_cv = cv2.imread(src_path)[142:442, 168:432]
scale = 4
crop_large = cv2.resize(crop_cv, (w * scale, h * scale), interpolation=cv2.INTER_LANCZOS4)
gray_large = cv2.cvtColor(crop_large, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray_large, (5, 5), 1.0)
_, thresh = cv2.threshold(blurred, 180, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_L1)

paths = []
for c in contours:
    if cv2.contourArea(c) < 300:
        continue
    approx = cv2.approxPolyDP(c, 0.7, True)
    pts = approx.reshape(-1, 2)
    if len(pts) < 3:
        continue
    d = f"M {pts[0][0]} {pts[0][1]} " + " ".join(f"L {p[0]} {p[1]}" for p in pts[1:]) + " Z"
    paths.append(d)

vb_w, vb_h = w * scale, h * scale
svg_code = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vb_w} {vb_h}" width="100%" height="100%" fill="none">
  <defs>
    <linearGradient id="gryffindorGold" x1="20%" y1="0%" x2="80%" y2="100%">
      <stop offset="0%" stop-color="#fff0a6" />
      <stop offset="45%" stop-color="#f3c252" />
      <stop offset="80%" stop-color="#dfa22c" />
      <stop offset="100%" stop-color="#a06612" />
    </linearGradient>
  </defs>
  <path fill-rule="evenodd" fill="url(#gryffindorGold)" d="{' '.join(paths)}" />
</svg>'''

svg_path = os.path.join(out_dir, "lion-symbol.svg")
with open(svg_path, "w", encoding="utf-8") as f:
    f.write(svg_code)
print(f"Saved: {svg_path}")

print("Processing complete!")
