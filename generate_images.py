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
print("이미지 생성 완료")
