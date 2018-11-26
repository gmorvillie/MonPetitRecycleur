from sklearn.cluster import KMeans
import cv2 #openCV works with BGR 
import numpy as np
import argparse
import utils.utilitaries as ut

image = cv2.imread("image/brown_plate.jpg")
parser = argparse.ArgumentParser(description='Separate the images pixel following the kMean algorithm.')
parser.add_argument('kmean', help='the number of classes you need (< 5)', type=int)
args = parser.parse_args()

k_meanValue = args.kmean
cv2.imshow('original',image)
cv2.waitKey(0)

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #pour que numpy fonctionne
blurredImage = ut.gaussian(image) #filtre gaussien
satImage = cv2.convertScaleAbs(blurredImage, alpha=1.2, beta=40) #alpha is for contrast, beta for brightness
cv2.imshow('satImage', satImage)

image2 = satImage.reshape((satImage.shape[0] * satImage.shape[1], 3))



'''
pour essayer correction gamma :
    lookUpTable = np.empty((1,256), np.uint8)
    for i in range(256):
        lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
    res = cv.LUT(img_original, lookUpTable)
'''


#essayer de mettre arbitrairement des valeurs pour les centroïdes (celle du plateau par exemple)
clt = KMeans(n_clusters = k_meanValue, init = 'k-means++', algorithm = 'auto') 


cluster_index = clt.fit_predict(image2) #tableau des cluster de chaque pixel (0, ou 1)

listed = cluster_index.tolist() #pour parcourir
for indice, valeur in enumerate(listed):
	if valeur == 1:
		image2[indice] = [0, 255, 0] #itemset pour le traitement des pixels sinon ça prend 1000 ans
	elif valeur == 0 :		
		image2[indice] = [0, 0, 255]
	elif valeur == 2:
		image2[indice] = [255, 0, 0]
	elif valeur == 3:
		image2[indice] = [0, 255, 0]
	else : 
		image2[indice] = [144, 144, 144]
		
image3 = image2.reshape(image.shape[0], image.shape[1], 3)
image3 = cv2.cvtColor(image3, cv2.COLOR_RGB2BGR)

cv2.imshow('twocolors',image3)
cv2.waitKey(0)



