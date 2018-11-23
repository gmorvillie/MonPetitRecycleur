from sklearn.cluster import KMeans
import cv2 #openCV works with BGR 
import numpy as np

image = cv2.imread("image/color_plat.jpg")
cv2.imshow('original',image)
cv2.waitKey(0)

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #pour que numpy fonctionne
#print(image)

image2 = image.reshape((image.shape[0] * image.shape[1], 3))
#print(image2)

clt = KMeans(n_clusters = 3)
cluster_index = clt.fit_predict(image2) #tableau des cluster de chaque pixel (0, ou 1)

#print(cluster_index)

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
		
#print(image2)
image3 = image2.reshape(image.shape[0], image.shape[1], 3)
image3 = cv2.cvtColor(image3, cv2.COLOR_RGB2BGR)


#print(image3)
cv2.imshow('twocolors',image3)
cv2.waitKey(0)

