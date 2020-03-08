import cv2
import datetime
cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc('X','V','I','D')
save=cv2.VideoWriter("E.avi",fourcc,20.0,(640,480))
while (cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        date1=datetime.datetime.now()
        frame=cv2.putText(frame,str(date1),(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(250,190,67),2,cv2.LINE_AA)
        save.write(frame)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        cv2.imshow("frame",frame)
        if cv2.waitKey(1)==ord("q"):
            break
    else:
        break
cap.release()
save.release()
cv2.destroyAllWindows()

