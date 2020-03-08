import cv2
import numpy as np
def click_mouse(event,x,y,flag,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        cv2.imshow("image",img)
        """
        points.append((x,y))
        if len(points)>=2:
            cv2.line(img,points[-1],points[-2],(255,0,0),5)
            cv2.imshow("image",img)
        """
img=np.zeros((512,512,3))
points=[]
#img=cv2.imread("C:\\Users\\DELL\\Desktop\\OPENCV PYTH\\howle.jpg",1)
cv2.imshow("image",img)
cv2.setMouseCallback("image",click_mouse)
