from imgmanager import ImgManager
from interface import Interface
from nn import NN
from mememanager import MemeManager

# Manages the memes
# im = ImgManager(input_img='meme0.jpg', output_img='test_img.gif', )
# im.reformat_image()

# network = NN('124M')


# Creates an instance of a browser using Eel.
gui = Interface()

mm = MemeManager(client_id=gui.credentials['client_id'], client_secret=gui.credentials['client_secret'],
                 user_agent=gui.credentials['user_agent'], username=gui.credentials['username'],
                 password=gui.credentials['password'], limit='10', subreddits_list=gui.credentials['list'])

gui.create_window()
# text = im.read_text()

# im.write_text()
