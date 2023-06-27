import random
import cv2

img = cv2.imread("my.jpg",-1)
#img =cv2.resize(img, (0,0),fx =0.2,fy=0.2)
# print(img)
print(type(img))
print(img.shape)
# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

vungchon = img[100:200, 500:700]
img[200:300, 900:1100] = vungchon

cv2.imshow('anh', img)
k =cv2.waitKey()