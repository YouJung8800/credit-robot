import os
from PIL import Image, ImageDraw
from robot_face_eyes import draw_eyes, draw_blink, W, H

os.makedirs("images", exist_ok=True)
moods = ["위험", "주의", "양호", "안심"]
scale = 3
cell_w, cell_h = W*scale, H*scale+24
grid = Image.new("RGB", (cell_w*2, cell_h*2), "white")
for i, mood in enumerate(moods):
    eye_img = draw_eyes(mood).resize((cell_w, H*scale), Image.NEAREST)
    eye_rgb = Image.new("RGB", eye_img.size, "black")
    eye_rgb.paste((255,255,255), mask=eye_img)
    row, col = i//2, i%2
    grid.paste(eye_rgb, (col*cell_w, row*cell_h+24))
grid.save("images/face_expressions_preview.png")
draw_blink().resize((W*4, H*4), Image.NEAREST).save("images/eyes_blink.png")

W2, H2 = 380, 400
concept = Image.new("RGB", (W2, H2), (255, 255, 255))
dc = ImageDraw.Draw(concept)
dc.ellipse([95, 345, 285, 365], fill=(230, 230, 230))
dc.rounded_rectangle([95, 65, 285, 345], radius=95, fill=(184, 230, 213), outline=(143, 203, 176), width=2)
dc.ellipse([118, 100, 162, 128], fill=(255, 255, 255))
dc.rounded_rectangle([128, 150, 252, 232], radius=18, fill=(43, 46, 56))
for cx in (165, 215):
    dc.arc([cx - 16, 176, cx + 16, 208], start=200, end=340, fill=(245, 247, 250), width=6)
dc.ellipse([140, 253, 160, 273], fill=(255, 201, 201))
dc.ellipse([220, 253, 240, 273], fill=(255, 201, 201))
concept.save("images/finished_concept.png")
print("[1/4] 이미지 3장 생성 완료")
