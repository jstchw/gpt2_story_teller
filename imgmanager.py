try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    import Image, ImageDraw, ImageFont

import os
import nn
import textwrap
import eel


@eel.expose
def create_meme(topic, count):
    W, H = 1000, 1000
    text = nn.generate_text(topic, 20, count * 2)

    for i in range(0, count):
        img = Image.open(f'www/img/{topic}/{topic}{i}.jpg')
        img = img.resize((W, H), Image.ANTIALIAS)
        d = ImageDraw.Draw(img)
        font = ImageFont.truetype("www/style/fonts/unicode.impact.ttf", 60)
        text[i] = text[i].upper()
        text[i] = textwrap.fill(text=text[i], width=35)
        w, h = d.textsize(text[i], font=font)
        d.text(((W-w)/2, 50), text[i], fill=(255, 255, 255), font=font, align='center', stroke_fill=(0, 0, 0),
               stroke_width=2)
        text[i+6] = text[i+6].upper()
        text[i+6] = textwrap.fill(text=text[i+6], width=35)
        w, h = d.textsize(text[i+6], font=font)
        d.text(((W-w)/2, 800), text[i+6], fill=(255, 255, 255), font=font, align='center', stroke_fill=(0, 0, 0),
               stroke_width=2)
        img.save(f'www/img/memes/{topic}/{topic}{i}.jpg')


class ImgManager:

    # def __init__(self, input_img, output_img):
    def __init__(self):
        self.img_pil = None
        self.meme_dir = os.fsdecode('www/img/memes/')
        self.output_img = self.meme_dir + 'testing.jpg'

    # Takes a string as a value

    def reformat_image(self):
        self.img_pil = Image.open(self.input_img)
        self.img_pil = self.img_pil.resize((350, 350), Image.ANTIALIAS)
        self.img_pil.save(self.output_img)