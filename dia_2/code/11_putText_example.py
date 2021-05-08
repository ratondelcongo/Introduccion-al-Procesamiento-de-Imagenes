import cv2

src = 'src/img/perros.png'

img = cv2.imread(src)

text = "Comsoc"
pt = (10, 30)
font = cv2.FONT_HERSHEY_SIMPLEX
scale = 1
color = (0, 0, 255)
thickness = 2

cv2.putText(img, text, pt, font, scale, color, thickness)

cv2.imshow('img', img)

cv2.waitKey(0)
