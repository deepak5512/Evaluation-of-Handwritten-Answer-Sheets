import cv2 as cv 
import numpy as np 
import os

filenames = os.listdir('C:/Users/Prajjwal Dixit/OneDrive/Desktop/Train_Samples_V0/Train_Samples_V0/')

def reshapeImg(img, scale = 0.1): 
    width = int(img.shape[1]*scale)
    height = int(img.shape[0]*(scale))
    dimensions = (width,height)
    return cv.resize(img,dimensions,interpolation=cv.INTER_AREA)



img = cv.imread('C:/Users/Prajjwal Dixit/OneDrive/Desktop/Train_Samples_V0/Train_Samples_V0/'+filenames[10])

img_reshape = reshapeImg(img)
img_gray = cv.cvtColor(img_reshape,cv.COLOR_BGR2GRAY)

adaptive_img = cv.adaptiveThreshold(img_gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,51,10)

kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(1,1))

sharpened_image = cv.filter2D(adaptive_img, -1, kernel)

cv.imshow("Final Image",sharpened_image)
cv.waitKey(0)