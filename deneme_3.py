#yeniden boyutlandırma
import cv2

import numpy as np

img=cv2.imread("diagno.png")
print(img.shape)

imgResize=cv2.resize(img,(800,450))        #genişlik,yükseklik

cv2.imshow("image",img)
cv2.imshow("image",imgResize)
cv2.waitKey(0)