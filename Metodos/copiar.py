import cv2

src = '../img/dog1.jpeg'

image = cv2.imread(src)

copy = image.copy()

cv2.imshow("Imagen", image)
cv2.imshow("Copia", copy)

cv2.waitKey(0)