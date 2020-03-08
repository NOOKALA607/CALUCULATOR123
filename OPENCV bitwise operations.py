import cv2
import numpy as np
img1=np.zeros((512,512,3),np.uint8)
img2=cv2.rectangle(img1,(100,0),(300,100),(255,255,255),-1)
#bitand=cv2.bitwise_and(img1,img2)
#bitor=cv2.bitwise_or(img1,img2)
#bitxor=cv2.bitwise_xor(img1,img2)
bitnot=cv2.bitwise_not(img1,img2)
#cv2.imshow("image",bitand)
#cv2.imshow("image",bitxor)
cv2.imshow("image",bitnot)
#cv2.imshow("image",bitor)
cv2.imshow("image1",img1)
cv2.imshow("image2",img2)
