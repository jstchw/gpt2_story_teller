# import gpt_2_simple as gpt2
# import os
# import requests
#
#
# class NN:
#
#     # Model name could either be '124M' (500MB) or '355M' (1.5GB)
#     def __init__(self, model_name):
#         self.model_name = model_name
#
#     def download_model(self):
#         if not os.path.isdir(os.path.join("models", self.model_name)):
#             print(f"Downloading {self.model_name} model...")
#             gpt2.download_gpt2(model_name=self.model_name)
