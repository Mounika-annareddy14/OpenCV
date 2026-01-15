"""Region of Intrest"""
import cv2
import numpy as np

def click(event , x , y , flags , pattern):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        targetedtext = str(x) + str(y)
        style = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(messi , targetedtext , (x,y) , style , 1,(0,0,255) , 1)
        cv2.imshow('messi' , messi)
messi = cv2.imread("images\messi.jpg")

#162 , 143
#204,175  ball image pixels

#203 , 25
#251 , 71 position pixels
cv2.imshow('messi',messi)
cv2.setMouseCallback('messi' , click)
cv2.waitKey()
cv2.destroyAllWindows()