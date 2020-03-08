import cv2
import numpy as np
img=cv2.imread("C:\\Users\\DELL\\Desktop\\OPENCV PYTH\\howle.jpg")
img2=cv2.imread("C:\\Users\\DELL\\Desktop\\lion.webp")
#copying some sort of image from one place to another
#REGION OF INTEREST[ROI]
eye=img[350:450,500:600]
img[300:400,600:700]=eye
#RESIZING IMAGES
img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))
#ADDING IMAGES TO A SINGLE IMAGE
dst=cv2.add(img,img2)
cv2.imshow("image",dst)
cv2.imwrite("Mixed_lion_manu.jpg",dst)
#addWeighted() to give priority to images

dst=cv2.addWeighted(img,0.3,img2,.7,0)#0.9+0.1=1
cv2.imshow("image",dst)
cv2.imwrite("manu_lion.jpg",dst)
