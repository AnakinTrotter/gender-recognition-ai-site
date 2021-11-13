import tensorflow as tf
from tensorflow import keras
import face_recognition as fr
from django.contrib.staticfiles import finders
from django.conf import settings
import numpy as np

model_path = finders.find('files/model.h5')
model = tf.keras.models.load_model(model_path)
model.summary()


def predict(image_path):
    image = fr.load_image_file(settings.MEDIA_ROOT + '/' + image_path)
    face_encoding = fr.face_encodings(image)
    if len(face_encoding) <= 0:
        return 'None'
    predict = model.predict(np.array(face_encoding).reshape(1, 128))
    if predict[0] > 0.5:
        return 'Male'
    return 'Female'
