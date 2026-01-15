"""Videos:collection of images is called video
Videocapture is used to read the first frame of the video"""

import numpy as np
import cv2

cap = cv2.VideoCapture("C:\\Users\\Mounika Reddy\\OneDrive\\Desktop\\opencv\\images\\video.mp4")

print(cap.read()) #it is used to read the frame values in the video
# cap is stored one  frame data from the video

#to show a single frame
res , frame = cap.read()
print(res)
print(frame)


# for multiple frames
count = 0
print(cap.get(3)) # to get width of the frame
print(cap.get(4)) # to get height of the frame
while True:
    res , frame = cap.read()
    if res == True:
        cv2.imshow("frame" , frame)
        count = count + 1
        if cv2.waitKey(18) == ord("q"):

            break
    else:
        break
print(f"count of total frames: {count}")
cap.release()
cv2.destroyAllWindows()

#Every frame has same height and width
