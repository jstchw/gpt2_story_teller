try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    import Image, ImageDraw

import pytesseract


class ImgManager:

    def __init__(self, input_img, output_img):
        self.txt = None
        self.input_img = 'img/' + input_img
        self.output_img = 'img/' + output_img
        self.img_pil = None

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
        self.img_pil = self.img_pil.resize((200, 200), Image.ANTIALIAS)
        self.img_pil.save(self.output_img)
