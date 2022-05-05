from PIL import Image, ImageDraw, ImageFont
import nn
import textwrap
import eel
import numpy as np


@eel.expose
def create_meme(topic, count):
    W, H = 1000, 1000
    text = nn.generate_text(topic, 30, count)

    for i in range(0, count):
        img = Image.open(f'www/img/{topic}/{topic}{i}.jpg')
        img = img.resize((W, H), Image.ANTIALIAS)
        d = ImageDraw.Draw(img)
        font = ImageFont.truetype("www/style/fonts/unicode.impact.ttf", 60)

        part = text[i].split()
        part = np.array_split(part, 2)

        part[0] = ' '.join(part[0])
        part[0] = part[0].upper()
        part[0] = textwrap.fill(text=part[0], width=35)

        w, h = d.textsize(part[0], font=font)
        d.text(((W - w) / 2, 50), str(part[0]), fill=(255, 255, 255), font=font, align='center', stroke_fill=(0, 0, 0),
               stroke_width=2)

        part[1] = ' '.join(part[1])
        part[1] = part[1].upper()
        part[1] = textwrap.fill(text=part[1], width=35)

        w, h = d.textsize(part[1], font=font)
        d.text(((W - w) / 2, 800), str(part[1]), fill=(255, 255, 255), font=font, align='center', stroke_fill=(0, 0, 0),
               stroke_width=2)
        img.save(f'www/img/memes/{topic}/{topic}{i}.jpg')


class ImgManager:
    def __init__(self):
        pass
