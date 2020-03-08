import cv2
image=cv2.imread("C:\\Users\\DELL\\Desktop\\OPENCV PYTH\\OPENCV\\th.jfif")
cv2.imshow("image",image)
ret,thresh1=cv2.threshold(image,50,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
ret,thresh4=cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
ret,thresh5=cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow("thresh1",thresh1)
cv2.imshow("thresh2",thresh2)
cv2.imshow("thresh3",thresh3)
cv2.imshow("thresh4",thresh4)
cv2.imshow("thresh5",thresh5)
