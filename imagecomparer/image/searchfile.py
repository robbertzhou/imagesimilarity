import h5py
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from imagecomparer.image.VGGNet import VGGNet



def searchfile(img_path):
    model = VGGNet()

    query = img_path
    index = r"C:\Users\Administrator\PycharmProjects\imagecomparer\imagecomparer\image\models\gs_model.h5"
    h5f = h5py.File(index, 'r')
    feats = h5f['dataset_1'][:]
    imageNames = h5f['dataset_2'][:]
    h5f.close()

    # queryImg = mpimg.imread(query)
    # plt.title("Query Image")
    # plt.imshow(queryImg)
    # plt.show()

    queryVec = model.vgg_extra_feature(query)
    scores = np.dot(queryVec, feats.T)
    rand_id = np.argsort(scores)[::-1]
    rank_score = scores[rand_id]

    maxres = 3
    imlist = []
    result = ""
    for i, index in enumerate(rand_id[0:maxres]):
        imlist.append(imageNames[index])
        result += "image names:" + str(imageNames[index]) + " scores :%f" % rank_score[i] + "<br />"
        print("image names:" + str(imageNames[index]) + " scores :%f" % rank_score[i])

    return result

