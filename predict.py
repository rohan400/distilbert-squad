from pathlib import Path
import requests
import os

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

   
    return path_to_model
    
    
    
