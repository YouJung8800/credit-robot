from PIL import Image, ImageDraw

W, H = 128, 64


def draw_eyes(mood):
    img = Image.new("1", (W, H), 0)
    d = ImageDraw.Draw(img)
    cx_l, cx_r, cy = 38, 90, 32
    if mood == "안심":
        for cx in (cx_l, cx_r):
            d.arc([cx-16, cy-6, cx+16, cy+26], start=200, end=340, fill=1, width=6)
    elif mood == "양호":
        for cx in (cx_l, cx_r):
            d.rounded_rectangle([cx-14, cy-16, cx+14, cy+16], radius=10, fill=1)
    elif mood == "주의":
        for cx in (cx_l, cx_r):
            d.rounded_rectangle([cx-14, cy-8, cx+14, cy+12], radius=8, fill=1)
        d.line([cx_l-14, cy-16, cx_l+10, cy-10], fill=1, width=3)
        d.line([cx_r+14, cy-16, cx_r-10, cy-10], fill=1, width=3)
    else:
        for cx in (cx_l, cx_r):
            d.ellipse([cx-13, cy-9, cx+13, cy+15], outline=1, width=3)
            d.ellipse([cx-4, cy-1, cx+4, cy+7], fill=1)
        d.line([cx_l-14, cy-20, cx_l+12, cy-12], fill=1, width=3)
        d.line([cx_r+14, cy-20, cx_r-12, cy-12], fill=1, width=3)
    return img


def draw_blink():
    img = Image.new("1", (W, H), 0)
    d = ImageDraw.Draw(img)
    cx_l, cx_r, cy = 38, 90, 32
    for cx in (cx_l, cx_r):
        d.line([cx-15, cy, cx+15, cy], fill=1, width=4)
    return img


def score_to_mood(score):
    if score <= 25: return "위험"
    elif score <= 45: return "주의"
    elif score <= 70: return "양호"
    else: return "안심"


def show_on_device(img):
    try:
        from luma.core.interface.serial import i2c
        from luma.oled.device import ssd1306
        serial = i2c(port=1, address=0x3C)
        device = ssd1306(serial)
        device.display(img)
    except Exception:
        img.resize((W*4, H*4), Image.NEAREST).save("face_preview.png")
