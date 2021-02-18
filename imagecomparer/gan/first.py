import tensorflow as tf
from  tensorflow.keras import layers
import matplotlib.pyplot as plt
import numpy as np
import glob
import os

(train_images,train_labels),(_,_) = tf.keras.datasets.mnist.load_data()
print(train_images.shape,train_images.dtype)
train_images = train_images.astype('float32')
train_images = (train_images -127.5) / 127.5
BATCH_SIZE =256
BUFFER_SIZE =60000

datasets =tf.data.Dataset.from_tensor_slices(train_images)
datasets = datasets.shuffle(BUFFER_SIZE).batch(BATCH_SIZE)

def generate_model():
    model = tf.keras.Sequential()
    model.add(layers.Dense(256,input_shape=(100,),use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    model.add(layers.Dense(512,  use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    model.add(layers.Dense(28*28*1,use_bias=False,activation="tanh"))

    model.add(layers.BatchNormalization())

    model.add(layers.Reshape((28,28,1)))
    return model

def discriminator_model():
    model = tf.keras.Sequential()

    model.add(layers.Flatten())

    model.add(layers.Dense(512,use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    model.add(layers.Dense(512, use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    model.add(layers.Dense(1))


cross_entropy = tf.keras.losses.BinaryCrossentropy(from_logits=True)

def discriminator_loss(real_image,fake_image):
    read_loss = cross_entropy(tf.ones_like(),real_image)
    fake_loss = cross_entropy(tf.zeros_like(), fake_image)
    return read_loss + fake_loss

def generator_loss(fake_image):
    return cross_entropy(tf.ones_like(fake_image), fake_image)


generator_opt = tf.keras.optimizers.Adam(learning_rate=1e-4)
discriminator_opt = tf.keras.optimizers.Adam(learning_rate=1e-4)


EPOCHS = 20
noise_dim = 100
num_exp_to_generate = 16
seed = tf.random.normal([num_exp_to_generate,noise_dim])

generator = generate_model()
discriminator = discriminator_model()

def train_step(images):
    noise = tf.random.normal([BATCH_SIZE,noise_dim])
    with tf.GradientTape() as gen_tape,tf.GradientTape() as disciminator_tape:
        real_output =  discriminator(images,training =True)
        

