import cv2
import numpy as np

size = 200, 200
m = np.zeros(size, dtype=np.uint8)
n = np.ones(size, dtype=np.uint8)*255

cv2.imshow('n', n)
cv2.imshow('m', m)

cv2.waitKey(0)
