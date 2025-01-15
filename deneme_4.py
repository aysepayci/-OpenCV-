#shapes and text
import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8) #siyah ortam oluşturma (boyut belirleme)

print(img)

# img[200:400,100:400]=255,0,0 #blue,green,red renklendirme işlemi 

#print(img.shape)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) #çubuk çekmek (değişken ismi,merkezi konum,cisim şekli,cisim rengi,kalınlığı)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED) #dikdörtgen çekmek için fiiled doldurmak için kullunılır
cv2.circle(img,(400,50),30,(255,255,0),5) #merkez noktası, yarıçap,renk,kalınlık
cv2.putText(img,"OPENCV ",(300,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)

cv2.imshow("image",img)


cv2.waitKey(0)