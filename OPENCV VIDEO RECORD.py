import cv2

"""
img=cv2.imread("D:\my certificates\IMG_20190424_183346 (1).jpg",0)

print(img)
cv2.imshow("Manohar",img)
"""
"""
cap=cv2.VideoCapture(0)#    Commanding To Camera
while True:
    ret, frame =cap.read()     #read the image from camera
    cv2.imshow("frame",frame)   #show the image 
    if cv2.waitKey(1)==ord("q"):    
        break
cap.release()
cv2.destroyAllWindows()
"""

cap=cv2.VideoCapture(0)#    Commanding To Camera
fourcc=cv2.VideoWriter_fourcc(*"XVID")
out=cv2.VideoWriter("man.jpg",fourcc,20.0,(640,480))
while (cap.isOpened()):    
    ret, frame =cap.read()     #read the image from camera
    if ret==True:
        
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH) ) #to get width
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) )  #to get height
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)    # read the image into black and white 
        out.write(frame)
        cv2.imshow("frame",gray)   #show the image 
        if cv2.waitKey(1)==ord("q"):    
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
