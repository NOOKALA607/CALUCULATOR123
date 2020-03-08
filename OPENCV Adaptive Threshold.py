import cv2
image=cv2.imread("C:\\Users\\DELL\\Desktop\\OPENCV PYTH\\OPENCV\\four-blank-sudoku-grids-format-letter-141028185938-conversion-gate01-thumbnail-4.jpg")
cv2.imshow("image",image)
ret,thresh=cv2.threshold(image,127,255,cv2.THRESH_BINARY)
cv2.imshow("thresh",thresh)
thresh1=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,20)
cv2.imshow("thresh1",thresh1)

#thresh: it will disappear some unhighlighted content
#adaptive threshold: it make bright unhighlighted content
