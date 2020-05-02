import cv2

import numpy as np

cap=cv2.VideoCapture(r'E:\OPENCV PYTH\OPENCV\Human_counting\Face detection with human count\human_counting_at_man_hole.mp4')

bgs=cv2.createBackgroundSubtractorMOG2()
offset=100

up=0
down=0
def man_entry(y,entry_val,exit_val):
  absdiff=abs(y-entry_val)
  if absdiff<=2 and y<exit_val:
    return 1
  else:
    return 0
  
def man_exit(y,entry_val,exit_val):
  absdiff=abs(y-exit_val)
  if absdiff<=2 and y>entry_val:
    return 1
  else:
    return 0
while cap.isOpened():
  
  ret,frame=cap.read()
  
  if ret==True:
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(19,19),5)
    im_frame=bgs.apply(blur)
    dilate=cv2.dilate(im_frame,(5,5))
    erode=cv2.erode(dilate,(5,5))
    
    
    kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    morph_ele=cv2.morphologyEx(erode,cv2.MORPH_CLOSE,kernel)
    second_morph=cv2.morphologyEx(morph_ele,cv2.MORPH_CLOSE,kernel)
    contours,image=cv2.findContours(second_morph,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame,contours,-1,(0,255,0),3)
    entry1=np.size(frame,0)/2-offset
    print(np.size(frame,1),np.size(frame,0))
    exit1=np.size(frame,0)/2+offset
    for contour in contours:
      x,y,w,h=cv2.boundingRect(contour)
      if cv2.contourArea(contour)<=10000:
        
        continue
      cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
      cent_x,cent_y=((x+x+w)//2,(y+y+h)//2)
      cv2.circle(frame,(cent_x,cent_y),5,(0,0,255),2)
      if man_entry(cent_y,entry1,exit1):
        up+=1
      if man_exit(cent_y,entry1,exit1):
        down+=1

    cv2.line(frame,(0,int(entry1)),(int(np.size(frame,1)),int(entry1)),(0,255,0),2)
    cv2.line(frame,(0,int(exit1)),(int(np.size(frame,1)),int(exit1)),(0,255,0),2)
    cv2.putText(frame,"IN:"+str(up),(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.putText(frame,"OUT:"+str(down),(50,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        
        
    cv2.imshow("frame",frame)
  if cv2.waitKey(1)==27:
    break

cap.release()
cv2.destroyAllWindows()
