########################################################################################
# Davi Frossard, 2016                                                                  #
# VGG16 implementation in TensorFlow                                                   #
# Details:                                                                             #
# http://www.cs.toronto.edu/~frossard/post/vgg16/                                      #
#                                                                                      #
# Model from https://gist.github.com/ksimonyan/211839e770f7b538e2d8#file-readme-md     #
# Weights from Caffe converted using https://github.com/ethereon/caffe-tensorflow      #
########################################################################################

import tensorflow as tf
import numpy as np
import datetime
from scipy.misc import imread, imresize, imsave
from imagenet_classes import class_names
from os import listdir
from os.path import isfile, join
import pickle

if __name__ == '__main__':
    imgPath = '/home/ubuntu/works/imageNet/ImageNet_Utils/n02123159/n02123159_urlimages/'
    imageFiles = [f for f in listdir(imgPath) if isfile(join(imgPath, f))]
    imgVec = []

    for f in imageFiles:
        try:
            img1 = imread(join(imgPath, f), mode='RGB')
            if img1.shape[0] > img1.shape[1]:
                margin = (img1.shape[0] - img1.shape[1]) / 2
                img1 = img1[margin:-margin,:,:]
            else:
                margin = (img1.shape[1] - img1.shape[0]) / 2
                img1 = img1[:,margin:-margin,:]

            img1 = imresize(img1, (224, 224))
            imsave(join("./preprocessImg/", f), img1)
               

        except:
            continue
