import cv2
import numpy as np

#image=cv2.imread("C:\\Users\\DELL\\Desktop\\OPENCV PYTH\\OPENCV\\th.jfif")
cap=cv2.VideoCapture(0)
#cv2.imshow("img",image)

def nothing(x):
    pass
cv2.namedWindow("readingcolors")
cv2.createTrackbar("LH","readingcolors",0,255,nothing)
cv2.createTrackbar("LS","readingcolors",0,255,nothing)
cv2.createTrackbar("LV","readingcolors",0,255,nothing)

cv2.createTrackbar("HH","readingcolors",255,255,nothing)
cv2.createTrackbar("HS","readingcolors",255,255,nothing)
cv2.createTrackbar("HV","readingcolors",255,255,nothing)
while True:
    ret,image=cap.read()
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray",hsv)
    l_h=cv2.getTrackbarPos("LH","readingcolors")
    l_s=cv2.getTrackbarPos("LS","readingcolors")
    l_v=cv2.getTrackbarPos("LV","readingcolors")

    h_h=cv2.getTrackbarPos("HH","readingcolors")
    h_s=cv2.getTrackbarPos("HS","readingcolors")
    h_v=cv2.getTrackbarPos("HV","readingcolors")
    l_range=np.array([l_h,l_s,l_v])
    h_range=np.array([h_h,h_s,h_v])
    
    mask=cv2.inRange(image,l_range,h_range)
    res=cv2.bitwise_and (image,image,mask=mask)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
