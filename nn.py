import gpt_2_simple as gpt2
import os
import eel
import tensorflow as tf
import re


# sess = None

# @eel.expose
# def load_model(run_name):
#     sess = gpt2.start_tf_sess()
#     gpt2.load_gpt2(sess, run_name=run_name)
#     print(sess)


# TESTED WITH LENGTH 10 - TOO SHORT (NOT EVEN A SENTENCE)
# FIRST TEST - LENGTH 1023 and NSAMPLES 1 (TIME IS OKAY)
# SECOND TEST - LENGTH 500 and NSAMPLES 6 (TOO LONG TO PROCESS)
# SOME NUMBER OF SAMPLES JUST CUT THE TEXT AND NOTHING IS CLEAR
# THIRD TEST - LENGTH 64, NSAMPLES 2, BATCH SIZE 2 - STILL CUTS THE TEXT
# THIRD TEST - LENGTH 60, NSAMPLES 2, BATCH SIZE 2 - STILL CUTS THE TEXT
# FOURTH TEST - LENGTH 60, NSAMPLES 2, BATCH SIZE 1 - STILL CUTS THE TEXT
# FIFTH TEST - LENGTH 70, NSAMPLES 2, BATCH SIZE 1 - STILL CUTS THE TEXT
# THIS IS TRAINED ON 1023 SAMPLE SIZE
# NETWORK WASN'T FINETUNED TO THE SAMPLE SIZE ----------------------
# ALL TRAINED WITH ADAM
@eel.expose
def generate_text(run_name, length, nsamples):
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, run_name=run_name, reuse=tf.compat.v1.AUTO_REUSE)
    texts = gpt2.generate(sess, return_as_list=True, length=length, nsamples=nsamples, model_name='124M')
    for idx, item in enumerate(texts):
        # STAYS FOR NOW
        item = item.rsplit('.', 1)[0]
        if not item[0].isupper() and item[0].isalpha():
            item = '...' + item + '...'
        else:
            item = item + '...'
        texts[idx] = item
    return texts


class NN:

    # Model name could either be '124M' (500MB) or '355M' (1.5GB)
    def __init__(self, model_name):
        self.model_name = model_name
        self.sess = None
        self.run_name = None

    def download_model(self):
        if not os.path.isdir(os.path.join("models", self.model_name)):
            print(f"Downloading {self.model_name} model...")
            gpt2.download_gpt2(model_name=self.model_name)

    def train_model(self, run_name, file_name, steps, sample_length):
        sess = gpt2.start_tf_sess()
        gpt2.finetune(sess, file_name, model_name=self.model_name, steps=steps, run_name=run_name,
                      restore_from='latest', overwrite=True, sample_length=sample_length, save_every=100)
