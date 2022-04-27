import gpt_2_simple as gpt2
import os
import eel
import tensorflow as tf


@eel.expose
def generate_text(run_name, length, nsamples):
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, run_name=run_name, reuse=tf.compat.v1.AUTO_REUSE)
    texts = gpt2.generate(sess, return_as_list=True, length=length, nsamples=nsamples, model_name='124M',
                          temperature=1, batch_size=nsamples, prefix="")
    for idx, item in enumerate(texts):
        item = item.replace("<|startoftext|>", "")
        item = item.rsplit('.', 1)[0]
        item = item.lstrip()
        while not item[0].isalpha():
            item = item[1:]
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
                      restore_from='latest', overwrite=True, sample_length=sample_length, save_every=100,
                      sample_every=steps)
