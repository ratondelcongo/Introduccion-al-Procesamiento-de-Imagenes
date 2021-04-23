import cv2

src = '../img/dog1.jpeg'

image = cv2.imread(src)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow("Imagen", image)
cv2.imshow("Blanco y Negro", gray)
cv2.imshow("HSV", hsv)

cv2.waitKey(0)