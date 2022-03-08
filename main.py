from imgmanager import ImgManager
from interface import Interface
from nn import NN

# Manages the memes
# im = ImgManager(input_img='meme0.jpg', output_img='test_img.gif', )
# im.reformat_image()

# network = NN('124M')

# network.download_model()


# Creates an instance of a browser using Eel.
gui = Interface()

# Create an instance of ImgManager class
img_manager = ImgManager()

print(img_manager.read_text('www/img/memes/meme3.jpg'))

# Get images from Reddit
# img_manager.get_images()

# Create the window
# gui.create_window()

# text = im.read_text()

# im.write_text()
