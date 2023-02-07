import cv2 as cv
import os

galaxy = os.path.join(os.getcwd(), "general-resources", "galaxy.jpg")

img = cv.imread(galaxy, -1)
# print(img)
resized_img = cv.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv.imshow("Galaxy", resized_img)
cv.waitKey(0)
cv.destroyAllWindows()