import cv2

src = 'src/img/perros.png'

img = cv2.imread(src)

(channel_b, channel_g, channel_r) = cv2.split(img)

cv2.imshow('img', img)
cv2.imshow('channel_b', channel_b)
cv2.imshow('channel_g', channel_g)
cv2.imshow('channel_r', channel_r)

cv2.waitKey(0)
