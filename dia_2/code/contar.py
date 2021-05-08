import cv2

src = 'src/img/tetris.png'

img = cv2.imread(src)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edge = cv2.Canny(gray, 30, 150)

thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]

cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

output = cv2.drawContours(img.copy(), cnts, -1, (0, 0, 255), 2)

cv2.imshow('img', img)
cv2.imshow('gray', gray)
cv2.imshow('edge', edge)
cv2.imshow('thresh', thresh)
cv2.imshow('output', output)


cv2.waitKey(0)

print("TOTAL DE FIGURAS: ", len(cnts))