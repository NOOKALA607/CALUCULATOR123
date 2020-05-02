import cv2
import numpy as np
import time
cap=cv2.VideoCapture(r'E:\OPENCV PYTH\OPENCV\Human_counting\Face detection with human count\human_counting_at_man_hole.mp4')
carros=0
cent_points=[]
bgs=cv2.bgsegm.createBackgroundSubtractorMOG()
print(cap.isOpened())
while cap.isOpened():
  ret,frame=cap.read()
  time.sleep(0.01)
  if ret==True:
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(3,3),5)

    img=bgs.apply(blur)
    cv2.imshow("img",img)
    dilate=cv2.dilate(img,np.ones((5,5)))
    kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    morph=cv2.morphologyEx(dilate,cv2.MORPH_CLOSE,kernel)
    dilatada=cv2.morphologyEx(morph,cv2.MORPH_CLOSE,kernel)
    contours,images=cv2.findContours(dilatada,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    for contour in contours:
      x,y,w,h=cv2.boundingRect(contour)
      if not (w>=80 and h>=80):
        continue

      cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
      
      centroids=((x+w//2),(y+h//2))
      cv2.circle(frame,centroids,2,(0,0,255),2)
      
      cv2.putText(frame,".",centroids,cv2.FONT_HERSHEY_SIMPLEX,10,(0,0,255),1)
      cent_points.append(centroids)
    for x,y in cent_points:
      if y<206 and y>194:
        carros+=1
        cv2.line(frame,(25,200),(2000,200),(0,255,0),2)
        cent_points.remove((x,y))
                  

    cv2.putText(frame, "VEICULOS: "+str(carros), (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),5)  
    
    cv2.imshow("imshow",frame)

  if cv2.waitKey(1)==27:
    break

cap.release()
cv2.destroyAllWindows()
    
