import cv2

img=cv2.imread("my.jpg",1)

#resize image
#img = cv2.resize(img, (200,200))
img =cv2.resize(img, (0,0),fx =0.2,fy=0.2)
#xoay anh
img=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
# xuat anh
cv2.imshow("Show",img)
k =cv2.waitKey(1000)


