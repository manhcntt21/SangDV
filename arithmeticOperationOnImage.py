import numpy as np 
import cv2 as cv 

x= np.uint8([250])
y = np.uint8([10])

print cv.add(x,y)

print x + y

img1 = cv.imread("bird.jpg")
img2 = cv.imread("train.jpg")
# phai cung kich thuoc moi long anh vaoo nhau theo addweighted dc
# dst = cv.addWeighted(img1, 0.3, img2, 0.7, 0)

# cv.imshow("aaa",dst)

# lay kich thuong cua anh bird
rows, cols, chanel = img1.shape

roi = img1[0:rows, 0:cols]

img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
# threshhold: tham so 1: la 1 anh xam, 2: gia tri nguong, 3: gia tri duoc gan neu pixel lon hon gia tri nguong
# 4: phan loai nguong
ret, mark =  cv.threshold(img2gray, 100, 255, cv.THRESH_BINARY_INV)
mark_inv = cv.bitwise_not(mark)

cv.imshow("aa", mark_inv)

cv.imwrite("aaaaa.jpg",mark_inv)

k = cv.waitKey(0)

if k == 27:
    cv.destroyAllWindows()