import cv2
import numpy as np


faceDetect=cv2.CascadeClassifier("C:\\Users\\DELL\\Desktop\\OPENCV PYTH\\OPENCV\\XML files\\haarcascade_frontalface_default.xml") 
cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*"XVID")
faceidentification=cv2.VideoWriter("face_identification.avi",fourcc,20.0,(640,480))

while True :
    ret,frame=cap.read()
    if ret==True:
    
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)    
        faces=faceDetect.detectMultiScale(frame,1.1,4)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
            cv2.imshow("frame",frame)
        faceidentification.write(frame)
    if cv2.waitKey(1)==ord("q"):    
        break

cap.release()
cv2.destroyAllWindows()
    
