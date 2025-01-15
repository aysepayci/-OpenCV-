#resim ve video ekleme ve kamera acma
import cv2

# print('i love myself')
#resim ekleme

#                  -Dosya yolu-
# img=cv2.imread("kedi.png") --!!!!png formatında olmalı!!!!--

# cv2.imshow("Output",img)
# cv2.waitKey(0)    
#waitKey'i 0 yapmak beklemeden direkt başlamasını sağlar.

#video ekleme
# cap=cv2.VideoCapture("video.mp4")

# while True:
#     success,img =cap.read()
#     cv2.imshow("video",img)
#     if cv2.waitKey(1)& 0xFF==ord('q'):
#         break

#kamera açma
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    success,img =cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1)& 0xFF==ord('q'):
        break