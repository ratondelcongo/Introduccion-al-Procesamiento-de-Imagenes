import cv2

src = 'src/img/perros.png'

img = cv2.imread(src)

cv2.imshow('img', img)

cv2.waitKey(0)
