import cv2

src = 'src/img/perros.png'

img = cv2.imread(src)

center = (240, 225)
radio = 200
color = (0, 0, 255)
thickness = 2

cv2.circle(img, center, radio, color, thickness)

cv2.imshow('img', img)

cv2.waitKey(0)
