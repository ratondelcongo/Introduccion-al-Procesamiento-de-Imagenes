import cv2

src = 'src/img/perros.png'

img = cv2.imread(src)

# imagen en escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# imagen en esquema HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('img', img)
cv2.imshow('gray', gray)
cv2.imshow('hsv', hsv)

cv2.waitKey(0)
