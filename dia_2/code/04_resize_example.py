import cv2

src = 'src/img/perros.png'

img = cv2.imread(src)

aspect_ratio = img.shape[0]/img.shape[1]

print(aspect_ratio)

dim = (200, int(200*aspect_ratio))
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

cv2.imshow('img', img)
cv2.imshow('resized', resized)

cv2.waitKey(0)
