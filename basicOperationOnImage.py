import cv2 as cv
import numpy as np 

# truy cap va chinh sua gia tri pixel


img = cv.imread("train.jpg")

img2 = cv.imread("hung.jpg")

print img.shape

print img.size

print img.dtype

print img2.shape

print img2.size

print img2.dtype
# flower = img[400:450, 450:550]

# img[100: 150, 200:300] = flower

# # cv.imshow("imagell",img)
# cv.imwrite("testcatanh.jpg",img)


b, g, r = img2[:,:,0], img2[:,:,1] , img2[:,:,1]

# thay doi mau cua anh

img2 = cv.merge((r,b,r))

cv.imshow("ab",img2)



k = cv.waitKey(0)
if k == 27:
    cv.destroyAllWindows()
