import argparse
import cv2 

# ap = argparse.ArgumentParser()

# ap.add_argument("-i", "--image", required = True,
#                 help = "Path to the image")
# args = vars(ap.parse_args())

image = cv2.imread("train.jpg", 0)
print "width: %d pixels" % (image.shape[1])
print "height: %d pixels" % (image.shape[0])
print "channels: %d channels" % (image.shape[2])

cv2.imshow("Image", image)
cv2.imwrite("new.jpg", image)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()

