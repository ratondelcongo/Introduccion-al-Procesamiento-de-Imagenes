import cv2

src1 = 'src/img/perro2.png'
src2 = 'src/img/perro1.png'


img1 = cv2.imread(src1)
img2 = cv2.imread(src2)

vcon = cv2.vconcat([img1, img2])
hcon = cv2.hconcat([img1, img2])

cv2.imshow('vcon', vcon)
cv2.imshow('hcon', hcon)

cv2.waitKey(0)
