from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io
from model import load_model, preprocess_image, predict

app = FastAPI()

# Load the model globally
model = load_model()

@app.post("/predict/")
async def classify_image(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read()))
    processed_image = preprocess_image(image)
    prediction = predict(model, processed_image)
    return {"prediction": prediction}