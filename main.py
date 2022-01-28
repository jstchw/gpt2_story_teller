from imgmanager import ImgManager
from interface import Interface
from nn import NN

# Manages the memes
im = ImgManager(input_img='meme0.jpg', output_img='test_img.gif', )
im.reformat_image()

network = NN('124M')

# Creates an instance of a browser using Eel.
gui = Interface()

# text = im.read_text()

# im.write_text()
