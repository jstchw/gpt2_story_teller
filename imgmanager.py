try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    import Image, ImageDraw

import pytesseract
import os
import subprocess


class ImgManager:

    # def __init__(self, input_img, output_img):
    def __init__(self):
        self.txt = None
        # self.input_img = 'img/' + input_img
        # self.output_img = 'img/' + output_img
        self.img_pil = None
        self.meme_dir = os.fsdecode('www/img/memes')

    # Returns a string
    def read_text(self):
        pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract\tesseract.exe"
        self.txt = pytesseract.image_to_string(Image.open(self.input_img))

    # Takes a string as a value
    def write_text(self):
        img = Image.new('RGB', (400, 400), color=(255, 255, 255))
        d = ImageDraw.Draw(img)
        font = ImageFont.truetype("fonts/ZenKakuGothicAntique-Regular.ttf", 15)
        d.text((100, 100), self.txt, fill=(0, 0, 0), font=font)
        img.save(self.output_img)

    def reformat_image(self):
        self.img_pil = Image.open(self.input_img)
        self.img_pil = self.img_pil.resize((350, 350), Image.ANTIALIAS)
        self.img_pil.save(self.output_img)

    # Images will be the same if reddit hot is not updated
    def get_images(self):
        counter = 0
        for file in os.listdir(self.meme_dir):
            if os.path.isfile(os.path.join(self.meme_dir, file)):
                counter += 1

        subprocess.call(['python', 'imagescraper.py', '-s', 'memes', '-n', '60', '-o', 'hot'])

        for file in os.listdir(self.meme_dir):
            filename = os.fsdecode(file)
            if filename.endswith(".jpg") and 'meme' not in filename:
                os.rename(f"{self.meme_dir}/{filename}", f"{self.meme_dir}/meme{counter}.jpg")
                counter = counter + 1
