import numpy as np
import cv2

cap = cv2.VideoCapture("C:\\Users\\Mounika Reddy\\OneDrive\\Desktop\\opencv\\images\\video.mp4")

count=0
print(cap.get(3))
print(cap.get(4))

while True:
    res , frame = cap.read()
    if res == True:
        """To put a text (h,w) on each frame"""
        height , width = frame.shape[0] , frame.shape[1]
        targetd_text = "height:" + str(height) + " width:"+str(width)
        font_style = cv2.FONT_HERSHEY_COMPLEX_SMALL

        """To put a frame count"""
        targeted_txt = "Frame:" + str(count)
        font_sty = cv2.FONT_HERSHEY_SIMPLEX

        cv2.putText(frame , targetd_text , (120,100) , font_style , 2,(0,0,255) , 2)
        cv2.putText(frame , targeted_txt , (120,140) , font_sty , 2,(0,0,0) , 2)
        cv2.imshow("Each_frame" , frame)
        count = count + 1
        if cv2.waitKey(22) == ord("q"):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()