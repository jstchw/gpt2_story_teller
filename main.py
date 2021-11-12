from imgmanager import ImgManager
from interface import Interface

im = ImgManager(input_img='meme0.jpg', output_img='test_img.gif', )
im.reformat_image()


gui = Interface(x_size=1024, y_size=768, title='GPT-2 Meme Generator')


#text = im.read_text()

#im.write_text()
