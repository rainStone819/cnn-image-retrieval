from feature import vgg16FeatureCode
import numpy as np
import os
import sklearn
import sklearn.neighbors
from sklearn.externals import joblib

index_dir = './index'
imagePath = "/htdocs/image-retrieval-UI/database_images"
features_file="%s/img_name_ftr.npz" % index_dir
kdtree_index_file="%s/kdtree_index.data" % index_dir

model_file='./vgg16_weights.npz'
print "load vgg16 weights from: %s..." % model_file
vgg16FeatureCode.loadModel(model_file)

if not os.path.exists(index_dir):
    os.makedirs(index_dir)

def extract_feature():
    print "extract images' feature from dir: %s ..." % imagePath
    idx = 0
    fileNames = []
    imageVectors = []
    for f in os.listdir(imagePath):
        fileNames.append(f)
        fileName = "%s/%s" % (imagePath, f)
        vector=vgg16FeatureCode.getImgVecFc2(fileName)
        imageVectors.append(vector)
        idx += 1
        print idx

    np.savez(features_file, fileNames, imageVectors)

class Searcher:

    def __init__(self):
        self.kd = None
        self.fileNames=None

    def buildIndex(self):
        print "building kd tree ..."
        embedding = np.load(features_file)
        self.fileNames = embedding['arr_0']
        vectors = embedding['arr_1']

        euclideanMetrics = sklearn.neighbors.DistanceMetric.get_metric('euclidean')
        self.kd = sklearn.neighbors.KDTree(vectors, metric=euclideanMetrics)
        joblib.dump(self.kd, kdtree_index_file, compress=9)

    def loadIndex(self):
        self.kd = joblib.load(kdtree_index_file)
        embedding = np.load(features_file)
        self.fileNames = embedding['arr_0']

    def search(self,query_imgpath):
        qvector=vgg16FeatureCode.getImgVecFc2(query_imgpath)
        distances, idxs = self.kd.query(qvector, k=40)

        similar_imgs=[]
        for i in xrange(len(distances[0])):
            img_name = self.fileNames[idxs[0][i]]
            similar_imgs.append(img_name)
        return similar_imgs,distances[0]

if __name__=='__main__':
    extract_feature()

    searcher = Searcher()
    searcher.buildIndex()

    # searcher.loadIndex()
    # similar_imgs,distances=searcher.search('./images/0.jpg')
    print "end"
