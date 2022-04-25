import nn
import imgmanager
from interface import Interface
from nn import NN
import time
import numpy as np

# network = NN('124M')

# network.train_model(file_name='datasets/alice/alice-preprocess.txt', run_name='alice-preprocess', steps=12000, sample_length=100)

# network.train_model(file_name='datasets/catcher/catcher-in-the-rye-new-format.txt', run_name='catcher', steps=3000,
# sample_length=100)

# network.train_model(file_name='datasets/the_iliad/the_iliad.txt', run_name='the_iliad', steps=10000,
# sample_length=100)

# start_time = time.time()
# nn.generate_text(run_name='the_iliad', length=100, nsamples=6)
# print("--- %s seconds ---" % (time.time() - start_time))

# Creates an instance of a browser using Eel.
gui = Interface()

# Create the window
gui.create_window()
# text = nn.generate_text(run_name='the_iliad', length=20, nsamples=2)
# print(text)
# # print(text[0])
# # print(text[1])
#
# for i in range(0, 2):
#     part = text[i].split()
#     part = np.array_split(part, 2)
#     print(part[0])
#     print(part[1])
#
