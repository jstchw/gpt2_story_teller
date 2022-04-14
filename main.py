import nn
import imgmanager
from interface import Interface
from nn import NN
import interface
import time

#network = NN('124M')

# network.train_model(file_name='datasets/alice/alice-preprocess.txt', run_name='alice-preprocess', steps=1000, sample_length=100)

# network.train_model(file_name='datasets/alice.txt', run_name='alice-no-dot', steps=200,
# sample_length=124)

# network.train_model(file_name='datasets/catcher/catcher-in-the-rye-new-format.txt', run_name='catcher', steps=3000,
# sample_length=100)

# network.train_model(file_name='datasets/the_iliad/the_iliad.txt', run_name='the_iliad', steps=10000,
# sample_length=100)

# print(network.generate_text(run_name='alice-preprocess',))
# start_time = time.time()
# nn.generate_text(run_name='the_iliad', length=100, nsamples=6)
# print("--- %s seconds ---" % (time.time() - start_time))

# print(network.generate_text(run_name='iliad'))

# imgmanager.create_meme('the_iliad', 6)

# Creates an instance of a browser using Eel.
gui = Interface()

# Create the window
gui.create_window()
