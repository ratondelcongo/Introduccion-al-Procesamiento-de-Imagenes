import cv2

src = 'src/img/perros.png'

img = cv2.imread(src)

(channel_b, channel_g, channel_r) = cv2.split(img)
imgMerged = cv2.merge((channel_b, channel_g, channel_r))

cv2.imshow('img', imgMerged)

cv2.waitKey(0)
