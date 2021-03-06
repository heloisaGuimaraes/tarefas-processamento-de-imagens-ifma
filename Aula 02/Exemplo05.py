import cv2
img = cv2.imread('../files/logo-if.jpg')

# Conversão entre sistema de cores
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


cv2.imshow('HSV', hsv)
cv2.imshow('RGB', rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()
