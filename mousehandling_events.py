import cv2
import numpy as np

print(len(dir(np)))
print(len(dir(cv2)))

event = [len(i) for i in dir(cv2) if 'EVENT' in i]
events = [i for i in dir(cv2) if 'EVENT' in i]
print(event)
print(events)

def fun(event , x , y , c, b): # event for waht event happend
    #x , y coordinates for the that event
    # c, b are alpha gamma values which are internal mathemetics
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        targeted_text = 'x:' + str(x) +' '+ 'y:' + str(y)
        style = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(black_image , targeted_text , (x,y) , style ,1,(0,0,255) , 1)
        cv2.imshow('image', black_image)

#blacimage
black_image = np.zeros((512,512,3), np.float64)

cv2.imshow('image' , black_image)

cv2.setMouseCallback('image' , fun)

cv2.waitKey()
cv2.destroyAllWindows()


