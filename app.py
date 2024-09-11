from fastapi import FastAPI, UploadFile, File
from model import preprocess_image, load_model
import numpy as np
from PIL import Image
import json
import requests

app = FastAPI()

model = load_model()

url = "https://storage.googleapis.com/download.tensorflow.org/data/imagenet_class_index.json"
class_labels = requests.get(url).json()

@app.post("/predict/")
async def classify_image(image: UploadFile = File(...)):
    img = Image.open(image.file)
    processed_image = preprocess_image(img)
    prediction = model.predict(processed_image)
    predicted_class = np.argmax(prediction, axis=1)[0]
    confidence = float(prediction[0][predicted_class])
    class_id, class_name = class_labels[str(predicted_class)]
    return {
        "predicted_class": class_name,
        "confidence": confidence
    }
