import cv2
import numpy as np


faceDetect=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #face detection
cap=cv2.VideoCapture(0)


while True :
    ret,frame=cap.read()
    cv2.imshow("image",frame)
    cv2.waitKey(1000000)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)    
    faces=faceDetect.detectMultiScale(gray,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
        
    cv2.imshow("frame",gray)  
    if cv2.waitKey(1)==ord("q"):    
        break

cap.release()
cv2.destroyAllWindows()
    
