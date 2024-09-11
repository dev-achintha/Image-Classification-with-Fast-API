import tensorflow as tf

def load_model():
    model = tf.keras.applications.MobileNetV2(weights='imagenet')
    return model

def preprocess_image(image):
    img = image.resize((224, 224))  # MobileNet expects 224x224 input
    img = tf.keras.preprocessing.image.img_to_array(img)
    img = tf.keras.applications.mobilenet_v2.preprocess_input(img)
    img = img.reshape((1, 224, 224, 3))
    return img

def predict(model, img):
    preds = model.predict(img)
    decoded = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=1)
    return decoded