import cv2
import numpy as np
img=cv2.imread("C:\\Users\\DELL\\Desktop\\OPENCV PYTH\\howle.jpg")
print("image_shape:",img.shape)# return no.rows,no.cols,no.channels
print("image_size:",img.size)#total number of pixels
print("image_datatype:",img.dtype)
b,g,r=cv2.split(img)
#img=cv2.merge((b,g,r))
cv2.imshow("image",img)
