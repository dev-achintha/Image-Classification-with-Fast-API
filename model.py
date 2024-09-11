from PIL import Image
import numpy as np
import tensorflow as tf

def load_model():
    model = tf.keras.applications.MobileNetV2(weights='imagenet')
    return model

def preprocess_image(image: Image.Image):
    img = image.resize((224, 224))
    img = np.array(img)
    if img.shape[-1] == 4:
        img = img[:, :, :3]
    img = img.reshape((1, 224, 224, 3)) / 255.0
    return img

def predict(model, img):
    preds = model.predict(img)
    decoded = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=1)
    return decoded