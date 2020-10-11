from pathlib import Path
import requests
import os
from transformers import pipeline
from download import download_model





class Model:

    def __init__(self, path: str):
        self.model = self.model_load(path)
        print('******************************************')


    def model_load(self, path):

        s3_model_url = 'https://storage.googleapis.com/bertpepper/pepperqa/pytorch_model.bin'
        print('******************************************')
        path_to_model = download_model(s3_model_url, model_name="pytorch_model.bin")

        #qa_pipeline = pipeline("question-answering",model=path,tokenizer=path)

        return path_to_model

    def predict(self, context, question):
        answer =self.model({'context': context,'question': question})


        return answer

model = Model('model')
    
    
    
    
