import cv2
import numpy as np

messi = cv2.imread('images\messi.jpg')
#where ball loacted
ball_pixels = messi[143:175 , 162:204]  #y1:y2 , x1:x2


#to new location
x,y = 203 , 61
h,w = ball_pixels.shape[:2]

messi[y:y+h , x:x+w] = ball_pixels #some other location


cv2.imshow('messi' , messi)
cv2.waitKey()
cv2.destroyAllWindows()