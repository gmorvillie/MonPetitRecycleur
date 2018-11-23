import cv2 as cv
import numpy as np

im=cv.imread('plat2.jpg')

#for i in range(0,1):
	#im = cv.GaussianBlur(im,(3,3),0)


#imgray = cv.Laplacian(im,cv.CV_8U) #petit Laplacien

imgray = cv.Canny(im, 50, 500) #petit Canny

cv.imshow('plat',imgray)
cv.waitKey(0)

#for i in range(0,1):
#	imgray = cv.GaussianBlur(imgray,(5,5),0)



ret, thresh = cv.threshold(imgray, 127, 255, cv.THRESH_BINARY)
ret2,otsu = cv.threshold(imgray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
adamean = cv.adaptiveThreshold(imgray,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,2) #etudier les deux derniers paramètres
adagauss = cv.adaptiveThreshold(imgray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,2)



#différents threshold
bw, contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE) #Simple thresholding
#bw, contours, hierarchy = cv.findContours(adamean, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) #Adaptative with Mean
#bw, contours, hierarchy = cv.findContours(adagauss, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) #Adaptative with Gaussian
#bw, contours, hierarchy = cv.findContours(otsu, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) #Otsu binarization


cv.drawContours(im, contours, -1, (0,255,0), 2)	#-1 c'est pour tous les contours, les arguments suivants c'est la forme du dessin

#mieux pour un contour spécifique
#cnt = contours[4]
#cv2.drawContours(img, [cnt], 0, (0,255,0), 3)

cv.imshow('plat',im)
cv.waitKey(0)
cv.destroyAllWindows()

