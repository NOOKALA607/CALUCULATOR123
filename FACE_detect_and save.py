import cv2
import numpy as np
from imutils.object_detection import non_max_suppression


cap=cv2.VideoCapture(r"E:\OPENCV PYTH\OPENCV\Human_counting\Face detection with human count\army_for_opencv.mp4")
#cap=cv2.VideoCapture(r"E:\OPENCV PYTH\OPENCV\Human_counting\Face detection with human count\human_counting.mp4")
classifier=cv2.CascadeClassifier("E:\OPENCV PYTH\OPENCV\XML files\haarcascade_frontalface_alt2.xml")
hog=cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

count=0
while cap.isOpened():
    ret,frame=cap.read()
    
    
    rect=classifier.detectMultiScale(frame)
        
    hog_rect,_=hog.detectMultiScale(frame,winStride=(2,2),padding=(8,8))
    hog_rect_pick=np.array([[x,y,x+w,y+h] for x,y,w,h in hog_rect])
        #pick=np.array([[x,y,x+w,y+h] for x,y,w,h in rect])
    rect=non_max_suppression(rect,overlapThresh=0.6)
    cv2.imshow("frame",frame)


    if cv2.waitKey(1)==ord("q"):
        break
    for x,y,w,h in rect:
        img=frame[y-10:y+h+10,x-10:x+w+10]
        resize=cv2.resize(img,(250,250))
        blur=cv2.medianBlur(resize,5)
        cv2.imwrite(r"E:\OPENCV PYTH\OPENCV\Human_counting\faces{}".format(count)+".jpg",blur)
        
        image=cv2.imread(r"E:\OPENCV PYTH\OPENCV\Human_counting\faces{}".format(count)+".jpg",)
        cv2.imshow("captured:{}".format(count),image)
        count+=1
        #count+=1
        #cv2.imwrite("E:\OPENCV PYTH\OPENCV\Human_counting\faces{}".format(count)+".jpg",img)
        #image=cv2.imread("E:\OPENCV PYTH\OPENCV\Human_counting.{}".format(count)+".jpg",img)
        #cv2.imshow("captured{}".format(count),image)
        

cap.release()
cv2.destroyAllWindows()
            
        
