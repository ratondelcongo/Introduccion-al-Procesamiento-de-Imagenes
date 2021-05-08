import cv2

src = 'src/img/perros.png'

img = cv2.imread(src)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(img.shape)
print(gray.shape)