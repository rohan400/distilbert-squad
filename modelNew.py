from pathlib import Path
import requests
import os
from transformers import pipeline

def download_model(s3_url, model_name):
    path = "./model"
    path_to_model = os.path.join(path, model_name)
    if not os.path.exists(path_to_model):
        print("Model weights not found, downloading from S3...")
        print(f"URL:{s3_url}")
        os.makedirs(os.path.join(path), exist_ok=True)
        filename = Path(path_to_model)
        r = requests.get(s3_url)
        filename.write_bytes(r.content)

    return path_to_model

def load_model():

    s3_model_url = 'https://storage.googleapis.com/bertpepper/pepperqa/pytorch_model.bin'

    path_to_model = download_model(s3_model_url, model_name="pytorch_model.bin")
    qa_pipeline = pipeline("question-answering",model="model",tokenizer="model")

   
    return qa_pipeline



class Model:

    def __init__(self, path: str):
        self.model = self.model_load(path)


    def model_load(self, path):

        s3_model_url = 'https://storage.googleapis.com/bertpepper/pepperqa/pytorch_model.bin'
        path_to_model = download_model(s3_model_url, model_name="pytorch_model.bin")

        qa_pipeline = pipeline("question-answering",model="model",tokenizer="model")

        return qa_pipeline

    def predict(self, context, question):
        answer =qa_pipeline({'context': context,'question': question})


        return answer

model = Model('model')
    
    
    
    
