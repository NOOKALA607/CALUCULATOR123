
import numpy as np
import cv2
def nothing(x):
    print(x)
#img=np.zeros((512,512,3),np.uint8)
img=cv2.imread("C:\\Users\\DELL\\Desktop\\OPENCV PYTH\\OPENCV\\manu_lion.jpg")
cv2.namedWindow("image")
cv2.createTrackbar("CP","image",10,400,nothing)

switch="color/gray"
cv2.createTrackbar(switch,"image",0,1,nothing)
while True:
    img=cv2.imread("C:\\Users\\DELL\\Desktop\\OPENCV PYTH\\OPENCV\\manu_lion.jpg")

    pos=cv2.getTrackbarPos("CP","image")
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,str(pos),(50,150),font,4,(0,0,250),3)
    s=cv2.getTrackbarPos(switch,"image")
    if cv2.waitKey(1)==27:
        break
    if s==0:
        pass
    else:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img=cv2.imshow("image",img)
cv2.destroyAllWindows()
