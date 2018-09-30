import numpy as np 
import cv2 as cv 
import matplotlib.pyplot as plt 

x= np.uint8([250])
y = np.uint8([10])

print cv.add(x,y)

print x + y

img1 = cv.imread("train.jpg")
img2 = cv.imread("bkhn.png")


img3 = cv.imread("./img/9.JPG")
img4 = cv.imread("./img/10.JPG")
img5 = cv.imread("./img/11.JPG")
img6 = cv.imread("./img/16.JPG")

# phai cung kich thuoc moi long anh vaoo nhau theo addweighted dc
# dst = cv.addWeighted(img1, 0.3, img2, 0.7, 0)
# cv.imshow("aaa",dst)

# lay kich thuong cua anh bkhn.jpg
rows, cols, chanel = img2.shape
roi = img1[0:rows, 0:cols]
# chuyen sang anh xam
img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

img3gray = cv.cvtColor(img3, cv.COLOR_BGR2GRAY)
img4gray = cv.cvtColor(img4, cv.COLOR_BGR2GRAY)
img5gray = cv.cvtColor(img5, cv.COLOR_BGR2GRAY)
img6gray = cv.cvtColor(img6, cv.COLOR_BGR2GRAY)

# cv.imshow("a", img3gray)
# threshhold: tham so 1: la 1 anh xam, 2: gia tri nguong, 3: gia tri duoc gan neu pixel lon hon gia tri nguong
# 4: phan loai nguong
ret, mask =  cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)

ret, mask1 =  cv.threshold(img3gray, 200, 255, cv.THRESH_TOZERO_INV)
ret, mask2 =  cv.threshold(img4gray, 200, 255, cv.THRESH_TOZERO_INV)
ret, mask3 =  cv.threshold(img5gray, 200, 255, cv.THRESH_TOZERO_INV)
ret, mask4 =  cv.threshold(img6gray, 200, 255, cv.THRESH_TOZERO_INV)

titles = ['9','10','11','16']
images = [ mask1, mask2, mask3, mask4]

for i in xrange(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

# cv.imshow("aa", mask1)
# cv.imwrite("kim1.jpg",mask1)
# ham nay dung de doi mau vi du anh gray: den thanh trang va nguoc lai
mask_inv = cv.bitwise_not(mask)
img_bg = cv.bitwise_and(roi, roi, mask= mask_inv)
img_fg = cv.bitwise_and(img2,img2, mask=mask)
dst = cv.add(img_bg,img_fg)
img1[0:rows, 0:cols] = dst

# cv.imshow("aa", img1)

# cv.imwrite("aaaaa.jpg",mark_inv)

# # tao 1 anh xam
# # in cac gia tri cua no voi cac threshhold khac nhau
# X = np.random.random((200,200))

# ret,thresh1 = cv.threshold(X,127,255,cv.THRESH_BINARY)
# ret,thresh2 = cv.threshold(X,127,255,cv.THRESH_BINARY_INV)
# ret,thresh3 = cv.threshold(X,127,255,cv.THRESH_TRUNC)
# ret,thresh4 = cv.threshold(X,127,255,cv.THRESH_TOZERO)
# ret,thresh5 = cv.threshold(X,127,255,cv.THRESH_TOZERO_INV)

# titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# images = [X, thresh1, thresh2, thresh3, thresh4, thresh5]

# for i in xrange(6):
#     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()



k = cv.waitKey(0)

if k == 27:
    cv.destroyAllWindows()