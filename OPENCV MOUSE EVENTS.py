
import cv2
import numpy as np
#events=[i for i in dir(cv2) if "EVENT " in i]
#print(events,end="\n")

def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(str(x)+","+str(y))
        font=cv2.FONT_HERSHEY_SIMPLEX
        text=str(x)+","+str(y)
        cv2.putText(img,text,(x,y),font,0.5,(250,250,0),1)
        cv2.imshow("image",img)
    if event==cv2.EVENT_RBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        font=cv2.FONT_HERSHEY_SIMPLEX
        text=str(blue)+","+str(green)+","+str(red)
        cv2.putText(img,text,(x,y),font,0.5,(250,160,120),2)
        cv2.imshow("image",img)
#img=np.zeros((512,512,3))
img=cv2.imread("C:\\Users\\DELL\\Desktop\\python files\\manu.jpg")
cv2.imshow("image",img)
cv2.setMouseCallback("image",click_event)

