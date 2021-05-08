import cv2

src = 'src/img/perros.png'

img = cv2.imread(src)

pi = (60, 60)
pf = (420, 390)
color = (0, 0, 255)
thickness = 2

cv2.rectangle(img,pi, pf, color, thickness)

cv2.imshow('img', img)

cv2.waitKey(0)
