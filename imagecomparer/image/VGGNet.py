import numpy as np
from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input as prreprocess_input_vgg
from numpy import linalg as LA

class VGGNet:
    def __init__(self):
        self.input_shape = (1000,1000,3)
        self.weight = "imagenet"
        self.pooling = None
        self.model_vgg = VGG16(weights=self.weight,
                               input_shape=[self.input_shape[0],self.input_shape[1],self.input_shape[2]],
                               pooling=self.pooling,include_top=False)
        self.model_vgg.predict(np.zeros((1,1000,1000,3)))

    def vgg_extra_feature(self,image_path):
        img = image.load_img(image_path,target_size=(self.input_shape[0],self.input_shape[1],self.input_shape[2]))
        img = image.img_to_array(img)
        img = np.expand_dims(img,axis=0)
        img = prreprocess_input_vgg(img)
        feature = self.model_vgg.predict(img)
        norm_feature = feature[0] / LA.norm(feature[0])
        return norm_feature



