# TODO:
# - Conduct a survey - do people like it?
# - Restructure the report
# - Write an explanation of the testing in the apendices

import nn
import imgmanager
from interface import Interface
from nn import NN
import time
import numpy as np

network = NN('124M')

# network.train_model(file_name='datasets/alice/alice-preprocess.txt', run_name='alice-preprocess', steps=12000,
# sample_length=100)

# network.train_model(file_name='datasets/catcher/catcher-in-the-rye-new-format.txt', run_name='catcher', steps=8000,
                    # sample_length=100)

# network.train_model(file_name='datasets/the_iliad/the_iliad.txt', run_name='the_iliad', steps=10000,
# sample_length=100)

# start_time = time.time()
# text = nn.generate_text(run_name='catcher', length=100, nsamples=6)
# print("--- %s seconds ---" % (time.time() - start_time))

# Creates an instance of a browser using Eel.
gui = Interface()

# Create the window
gui.create_window()
