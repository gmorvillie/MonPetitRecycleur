# import the necessary packages
import numpy as np
import cv2 as cv

def gaussian(im):
	for i in range(0,1):
		blurredIm = cv.GaussianBlur(im,(3,3),0)
	return blurredIm


