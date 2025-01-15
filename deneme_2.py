#basit foksiyonlar
import cv2
import numpy as np

# img=cv2.imread("diagno.png")

# imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# cv2.imshow("Gray image",imgGray)
# cv2.waitKey(0)

img=cv2.imread("diagno.png")
karnel=np.ones((5,5),np.uint8)

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)               
imgCanny=cv2.Canny(img,150,200)                         #gölgeleri silme ,sadece siyah-beyaz çoğunlukla siyah
imgDialation=cv2.dilate(imgCanny,karnel,iterations=1)   #çizgilerde genişleme
imgEroded=cv2.erode(imgDialation,karnel,iterations=1)   
cv2.imshow("Gray image",imgGray)
cv2.imshow("Blur image",imgBlur)
cv2.imshow("Canny image",imgCanny)
cv2.imshow("Dialation image",imgDialation)
cv2.imshow("Eroded image",imgEroded)
cv2.waitKey(0)
