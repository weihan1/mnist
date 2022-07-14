#Preprocess the input data 
import tensorflow as tf
import numpy as np
import cv2

def preprocess(img_path):
    img=cv2.imread(img_path)
    rescaled_image = tf.image.resize(img, (256,256))
    processed_image = np.expand_dims(rescaled_image/255, 0)
    return processed_image


def load_model():
    return tf.keras.models.load_model("models/imageclassifier_vgg16_best.h5")


