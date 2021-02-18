import os

import h5py
from imagecomparer.image.VGGNet import VGGNet
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def get_imlist(path):
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

if __name__ == "__main__":
    database = "database"
    index = 'models/gs_model.h5'
    img_list = get_imlist("G:\\testdata\\gsimages")
    print("------------------------------------------")
    print("          feature extraction starts       ")
    print("------------------------------------------")

    feats = []
    names = []
    model = VGGNet()
    for i , img_path in enumerate(img_list):
        norm_feature = model.vgg_extra_feature(img_path)
        image_name = os.path.split(img_path)[1]
        feats.append(norm_feature)
        names.append(image_name)

    feats = np.array(feats)
    output = index
    h5f = h5py.File(output,'w')
    h5f.create_dataset('dataset_1',data=feats)
    h5f.create_dataset('dataset_2',data=np.string_(names))
    h5f.close()
