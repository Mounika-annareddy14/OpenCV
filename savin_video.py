import cv2
import numpy as np
"""saving video"""

cap = cv2.VideoCapture("C:\\Users\\Mounika Reddy\\OneDrive\\Desktop\\opencv\\images\\video.mp4")
driver = cv2.VideoWriter_fourcc(*'mp4v') #XVId these are drivers
w = int(cap.get(3))
h = int(cap.get(4))
out = cv2.VideoWriter('output.mp4', driver, 20.0, (w,h))

count = 1
while True:
    res , frame = cap.read()
    if res == True:
        targeted_text = "frame:" + str(count)
        font_style = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame , targeted_text , (120,100) ,  font_style , 2 , [0,0,255] , 2)
        cv2.imshow("video" , frame)
        count+=1
        out.write(frame)
        if cv2.waitKey(27) == ord("q"):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()

"""Face Detection:-it is used to detect only the face 
Fece recognition:- it is used to identify the features also
eg:ofc login"""