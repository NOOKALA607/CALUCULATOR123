import cv2
import numpy as np

def click_event(event,x,y,flag,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        #cv2.circle(img,(x,y),3,(0,0,250),-1)
        mycolorimage=np.zeros((512,512,3),dtype=np.uint8)
        mycolorimage[:]=[blue,green,red]
        cv2.imshow("color",mycolorimage)

img=cv2.imread("C:\\Users\\DELL\\Desktop\\OPENCV PYTH\\howle.jpg")

cv2.imshow("image",img)
cv2.setMouseCallback("image",click_event)
