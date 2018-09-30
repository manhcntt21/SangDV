import cv2 as cv
import numpy as np 

img = cv.imread("train.jpg", 0)
# dich
rows, cols = img.shape
M = np.float32([[1, 0, -10], [0, 1, 50]])
dst = cv.warpAffine(img, M, (cols, rows))
cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindowns()

# xoay
# res = cv.resize(img, None, fx=2, fy=2, interpolation = cv.INTER_CUBIC)

# height, width = img.shape[:2]

# res = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)