import cv2

src = 'src/img/perros.png'

img = cv2.imread(src)

dim = (200, 300)
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

cv2.imshow('img', img)
cv2.imshow('resized', resized)

cv2.waitKey(0)
