import cv2 as cv
import matplotlib.pyplot as plt 
import numpy as np

green = np.uint8([[[0, 255, 0]]])
hsv_green = cv.cvtColor(green, cv.COLOR_BGR2HSV)
print hsv_green
# print green[0,0,3]