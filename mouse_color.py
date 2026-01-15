"""mouse handling for color image"""
import cv2
import numpy as np


def click(event, x, y, flags,patterns):
    if event == cv2.EVENT_LBUTTONDOWN:
        b = color_image[x,y , 0] # blue_channel becoz color image works on 3channels
        g = color_image[x,y,1] # green channel
        r = color_image[x,y , 2]
        print(b,g,r)
        targeted_text = 'b'+str(b)+ " "+ 'g'+str(g) + " "+ 'r'+str(r)
        style = cv2.FONT_HERSHEY_SIMPLEX
        # cv2.putText(color_image, targeted_text, (x, y), style, 1, (0, 0, 255), 1)
        # cv2.imshow('color', color_image)
        cv2.putText(black_image, targeted_text, (x,y), style, 1, (0,0,255), 1 )
        cv2.imshow('black' , black_image)

black_image = np.zeros((512,512,3) , np.float64)
color_image = cv2.imread("images\dog.jpg")

cv2.imshow('color' , color_image)
cv2.imshow('black' , black_image)

cv2.setMouseCallback('color' , click)

cv2.waitKey()
cv2.destroyAllWindows()