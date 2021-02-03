import cv2 as cv
import numpy as np

img = cv.imread("box_QR.jpg", -1)
cv.imshow('box', img)
cv.waitKey(0)