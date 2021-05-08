import cv2
import numpy as np

src = 'src/img/perros.png'

img = cv2.imread(src)

(channel_b, channel_g, channel_r) = cv2.split(img)

zeros = np.zeros(img.shape[:2], dtype="uint8")

imgMerged = cv2.merge((channel_b, channel_g, channel_r))

cv2.imshow('img', imgMerged)

cv2.waitKey(0)
