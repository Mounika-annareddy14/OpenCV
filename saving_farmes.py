import numpy as np
import cv2
"""saving farmes"""

cap = cv2.VideoCapture("C:\\Users\\Mounika Reddy\\OneDrive\\Desktop\\opencv\\images\\video.mp4")

print(cap.get(3))
print(cap.get(4))
count = 1
while True:
    res , frame = cap.read()
    if res == True:
        """To put a text (h,w) on each frame"""
        height , width = frame.shape[0] , frame.shape[1]
        targetd_text = "height:" + str(height) + " width:"+str(width)
        font_style = cv2.FONT_HERSHEY_COMPLEX_SMALL
        cv2.putText(frame , targetd_text , (120,100) , font_style , 2,(0,0,255) , 2)
        cv2.imshow("Each_frame" , frame)
        cv2.imwrite("C:\\Users\\Mounika Reddy\\OneDrive\\Desktop\\opencv\\frames\\" +str(count)+'.jpg',frame)
        count+=1
        if cv2.waitKey(22) == ord("q"):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()