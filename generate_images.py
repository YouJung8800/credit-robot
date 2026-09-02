import os
from PIL import Image, ImageDraw
from robot_face_eyes import draw_eyes, draw_blink, W, H

os.makedirs("images", exist_ok=True)


def flatten(rgba_img, size):
    bg = Image.new("RGBA", size, (255, 255, 255, 255))
    return Image.alpha_composite(bg, rgba_img).convert("RGB")


moods = ["위험", "주의", "양호", "안심"]
scale = 3
cell_w, cell_h = W * scale, H * scale + 24
grid = Image.new("RGB", (cell_w * 2, cell_h * 2), "white")
for i, mood in enumerate(moods):
    eye_img = draw_eyes(mood).resize((cell_w, H * scale), Image.NEAREST)
    eye_rgb = Image.new("RGB", eye_img.size, "black")
    eye_rgb.paste((255, 255, 255), mask=eye_img)
    row, col = i // 2, i % 2
    grid.paste(eye_rgb, (col * cell_w, row * cell_h + 24))
grid.save("images/face_expressions_preview.png")

draw_blink().resize((W * 4, H * 4), Image.NEAREST).save("images/eyes_blink.png")

base = Image.new("RGBA", (380, 400), (0, 0, 0, 0))
d = ImageDraw.Draw(base)
d.ellipse([78, 359, 302, 385], fill=(0, 0, 0, 24))
d.rounded_rectangle([90, 40, 290, 350], radius=95, fill=(184, 230, 213, 255), outline=(143, 203, 176, 255), width=2)
d.ellipse([186, 64, 194, 72], fill=(111, 207, 151, 255))
d.ellipse([181, 59, 199, 77], fill=(111, 207, 151, 60))
d.ellipse([104, 75, 160, 109], fill=(255, 255, 255, 100))
d.ellipse([110, 79, 134, 93], fill=(255, 255, 255, 160))
d.rounded_rectangle([113, 130, 267, 230], radius=22, fill=(26, 28, 36, 255))
d.rounded_rectangle([121, 138, 259, 222], radius=16, fill=(43, 46, 56, 255))
d.polygon([(132,140),(142,140),(124,220),(114,220)], fill=(255,255,255,22))
d.polygon([(150,140),(157,140),(139,220),(132,220)], fill=(255,255,255,14))
d.arc([158, 168, 186, 196], start=200, end=340, fill=(245, 247, 250, 255), width=6)
d.arc([194, 168, 222, 196], start=200, end=340, fill=(245, 247, 250, 255), width=6)
d.ellipse([140, 246, 165, 267], fill=(255, 201, 201, 120))
d.ellipse([216, 246, 241, 267], fill=(255, 201, 201, 120))
flatten(base, (380, 400)).save("images/hero_shot.png")

base2 = Image.new("RGBA", (380, 300), (0, 0, 0, 0))
d2 = ImageDraw.Draw(base2)
d2.rectangle([0, 205, 380, 300], fill=(232, 220, 200, 255))
d2.line([0, 205, 380, 205], fill=(216, 200, 168, 255), width=2)
d2.ellipse([40, 197, 100, 209], fill=(0, 0, 0, 20))
d2.rounded_rectangle([52, 168, 88, 202], radius=4, fill=(245, 240, 230, 255), outline=(216, 200, 168, 255), width=2)
d2.arc([78, 174, 106, 198], start=280, end=80, fill=(216, 200, 168, 255), width=3)
d2.ellipse([52, 163, 88, 173], fill=(107, 74, 50, 255))
d2.ellipse([294, 194, 346, 206], fill=(0, 0, 0, 18))
d2.polygon([(300, 200), (308, 160), (332, 160), (340, 200)], fill=(201, 123, 95, 255))
d2.ellipse([312, 132, 328, 168], fill=(123, 174, 127, 255))
d2.ellipse([298, 141, 318, 171], fill=(143, 195, 147, 255))
d2.ellipse([322, 141, 342, 171], fill=(143, 195, 147, 255))
d2.ellipse([138, 201, 242, 219], fill=(0, 0, 0, 26))
d2.rounded_rectangle([150, 105, 230, 220], radius=38, fill=(184, 230, 213, 255), outline=(143, 203, 176, 255), width=2)
d2.ellipse([161, 122, 183, 134], fill=(255, 255, 255, 130))
d2.rounded_rectangle([160, 148, 220, 188], radius=10, fill=(43, 46, 56, 255))
d2.polygon([(172,150),(178,150),(168,186),(162,186)], fill=(255,255,255,20))
d2.arc([171, 158, 189, 176], start=200, end=340, fill=(245, 247, 250, 255), width=4)
d2.arc([197, 158, 215, 176], start=200, end=340, fill=(245, 247, 250, 255), width=4)
d2.ellipse([163, 191, 175, 202], fill=(255, 201, 201, 120))
d2.ellipse([205, 191, 217, 202], fill=(255, 201, 201, 120))
flatten(base2, (380, 300)).save("images/home_context.png")
print("이미지 4장 생성 완료")
