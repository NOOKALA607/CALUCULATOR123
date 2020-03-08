import cv2

facedetect=cv2.CascadeClassifier("C:\\Users\\DELL\\Desktop\\OPENCV PYTH\\OPENCV\\XML files\\haarcascade_frontalface_default.xml")
eyedetect=cv2.CascadeClassifier("C:\\Users\\DELL\\Desktop\\OPENCV PYTH\\OPENCV\\XML files\\haarcascade_eye_tree_eyeglasses.xml")
fourcc=cv2.VideoWriter_fourcc(*"XVID")
face_and_eye=cv2.VideoWriter("face_and_eye.avi",fourcc,20.0,(640,480))
cap=cv2.VideoCapture(0)

while cap.isOpened():
    ret,frame=cap.read()
    if ret==True:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=facedetect.detectMultiScale(gray,1.1,4)
        
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
            eye_gray=gray[y:y+h,x:x+w]
            eye_color=frame[y:y+h,x:x+w]
            eyes=eyedetect.detectMultiScale(eye_gray)
            for (xe,ye,we,he) in eyes:
                cv2.rectangle(eye_color,(xe,ye),(xe+we,ye+he),(0,0,250),5)
        cv2.imshow("frame",frame)
        face_and_eye.write(frame)
    if cv2.waitKey(1)==27:
        break
cap.release()
cv2.destroyAllWindows()
