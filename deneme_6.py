#resim ekleme
import cv2
import numpy as np 

#imgHor=np.hstack((img,img)) #yatayda bir eşini daha yapmak
#imgVer=np.vstack((img,img))#dikeyde bir eşini daha yapmak

#cv2.imshow("Horizontal",imgHor)
#cv2.imshow("Vertical",imgVer)

#işlem sonrası görüntü yeniden boyutlandılamaz,olduğu gibi gelecektir
#Eğer görüntüler ayn sayıda kanala sahip değilse, yani her ikisi de RGB değilse veya belki biri gri biri RGB ise işe yaramayacaktır.

#ölçeklendirme için  aşağıdaki fonksiyonu kullanıcağız

def stackImages(scale,imgArray):
    rows=len(imgArray)
    cols=len(imgArray[0])
    rowsAvaible=isinstance(imgArray[0],list)
    width=imgArray[0][0].shape[1]
    height=imgArray[0][0].shape[0]
    if rowsAvaible:
        for x in range(0,rows):
            for y in range(0,cols):
                if imgArray[x][y].shape[:2]==imgArray[0][0].shape [:2]:
                    imgArray[x][y]=cv2.resize(imgArray[x][y],(0,0),None,scale)
                else:
                    imgArray[x][y]=cv2.resize(imgArray[x][y],(imgArray[0][0]))
                if len(imgArray[x][y].shape)==2: imArray[x][y]=cv2.cvtColor(imgArray)
        imageBlank=np.zeros((height,width,3),np.uint8)
        hor=[imageBlank]*rows
        hor_con=[imageBlank]*rows
        for x in range(0,rows):
            hor[x]=np.hhstack(imgArray[x])
        ver=np.vstack(hor)
    else:
        for x in range(0,rows):
            if imgArray[x].shape[:2]==imgArray[0].shape[:2]:
                imgArray[x]=cv2.resize(imgArray[x],(0,0),None,scale,scale)
            else:
                imgArray[x]=cv2.resize(imgArray[x],(imgArray[0].shape[1],))
            if len(imgArray[x].shape)==2: imgArray[x]=cv2.cvtcolor(imgArray)
        hor=np.hstack(imgArray)
        ver=hor
    return ver

    img=cv2.imread("kedi.png")
    imgGray=cv2.cvtColor(img,cvt2.COLOR_BGR2GRAY)

    imgStack= stackImages(0.5,([img,imgGray,img],[img,img,img]))

    cv2.imshow("ImageStack",imgStack)

cv2.waitKey(0)