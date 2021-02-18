# -*- coding: UTF-8 -*-
from skimage import measure
import matplotlib.pyplot as plt
import numpy as np
import cv2
import tensorflow as tf
import scipy.misc


def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err


def crop_or_pad(filePath):
    filename = [filePath]
    filename_queue = tf.train.string_input_producer(filename)
    reader = tf.WholeFileReader()
    key, value = reader.read(filename_queue)
    images = tf.image.decode_jpeg(value)  # tf.image.decode_png(value)
    CP_H = 180
    CP_W = 270
    # 裁切图片
    with tf.Session() as sess:
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(coord=coord)
        reshapeimg = tf.image.resize_image_with_crop_or_pad(images, CP_H, CP_W)
        # reimg1的类型是<class 'numpy.ndarray'>
        reimg1 = reshapeimg.eval()
        scipy.misc.imsave('/root/PycharmProjects/ImageIdentification/Image/crop_or_pad1.jpg', reimg1)
        coord.request_stop()
        coord.join(threads)
        print('crop_or_pad successful!')


def compare_images(imageA, imageB, title):
    m = mse(imageA, imageB)
    s = measure.compare_ssim(imageA, imageB)
    # setup the figure
    fig = plt.figure(title)  # 创建一个窗口
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
    # show first image
    ax = fig.add_subplot(1, 2, 1)  # 将窗口划分为1行两列的子图当前为第1个子图
    plt.imshow(imageA, cmap=plt.cm.gray)  # 图片的绘制，plt.cm.gray显示为灰度图
    plt.axis("off")  # 不显示坐标尺寸

    # show the second image
    ax = fig.add_subplot(1, 2, 2)  # 将窗口划分为1行两列的子图当前为第2个子图
    plt.imshow(imageB, cmap=plt.cm.gray)
    plt.axis("off")

    # show the images
    plt.show()  # 显示窗口


if __name__ == '__main__':
    # 图片格式转化,转化成长和宽一致的图片
    crop_or_pad('/root/PycharmProjects/ImageIdentification/Image/image2.jpg')
    # 图片加载
    original = cv2.imread("/root/PycharmProjects/ImageIdentification/Image/crop_or_pad.jpg")
    contrast = cv2.imread("/root/PycharmProjects/ImageIdentification/Image/crop_or_pad1.jpg")
    shopped = cv2.imread("/root/PycharmProjects/ImageIdentification/Image/crop_or_pad.jpg")
    # 图片的灰阶转化
    # convert the images to grayscale
    original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)
    shopped = cv2.cvtColor(shopped, cv2.COLOR_BGR2GRAY)
    # 彩色图片的灰阶转化：对于彩色图片也可以通过灰阶实现
    # Gray = R * 0.299 + G * 0.587 + B * 0.114
    fig = plt.figure("Images")
    images = ("Original", original), ("Contrast", contrast), ("Photoshopped", shopped)
    # loop over the images
    for (i, (name, image)) in enumerate(images):
        # show the image
        ax = fig.add_subplot(1, 3, i + 1)
        ax.set_title(name)
        plt.imshow(image, cmap=plt.cm.gray)
        plt.axis("off")
    # show the figure
    plt.show()

    # compare the images
    compare_images(original, original, "Original vs. Original")
    compare_images(original, contrast, "Original vs. Contrast")
    compare_images(original, shopped, "Original vs. Photoshopped")