"""In this mini-project i am working on frame processing , roi selection and annotations
 and i have used a general google chrome opening video"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

input_path = r"C:\Users\Mounika Reddy\OneDrive\Desktop\opencv\mini_project\input_video.mp4.mp4"
output_path = r"C:\Users\Mounika Reddy\OneDrive\Desktop\opencv\mini_project\output_video.mp4"
frames_folder = r"C:\Users\Mounika Reddy\OneDrive\Desktop\opencv\mini_project\frames"

#making frames floder
os.makedirs(frames_folder, exist_ok=True)

#Reading the video
cap = cv2.VideoCapture(input_path) #input
w = int(cap.get(3)) # Width
h = int(cap.get(4)) #Height
fps = cap.get(cv2.CAP_PROP_FPS)
# w,h = frame.shape[:2]
print(f"Video width:{w} height:{h} fps:{fps}")

#VideoWriter to save output
driver = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path , driver , fps , (w,h))


#Mouse handling events to select region of intrest
roi_points = []
def click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(roi_points) < 2:  # Only allow max 2 clicks
            roi_points.append((x, y))
            print("Clicked:", x, y)
cv2.namedWindow('video_frames')
cv2.setMouseCallback('video_frames' , click)


#Displaying the frames
#frame properties by getting width and height
frame_count = 1
while True:
    res , frame = cap.read()
    if res == True:
        "Frame properties"
        targeted_text = 'width:'+str(w) +' ' + 'height:'+str(h) +" " + "Frane_count:" + str(frame_count)
        style = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame , targeted_text , (120,100) , style , 1 , (0,0,255) , 2)

        #draw circle
        for point in roi_points:
            cv2.circle(frame , point , 5 ,(0,0,0) , -1)

        #drawing rectangle
        if len(roi_points) == 2:
            (x1,y1),(x2,y2) = roi_points
            cv2.rectangle(frame , (x1,y1) , (x2,y2) , (0,0,255) , 1)

            #croping the roi
            (x1,y1) , (x2,y2) = roi_points
            x1,x2 = min(x1,x2) , max(x1,x2)
            y1,y2 = min(y1,y2) , max(y1,y2)
            roi = frame[y1:y2 , x1:x2]

            #Converting roi to gray scale
            roi_gray = cv2.cvtColor(roi , cv2.COLOR_BGR2GRAY)
            cv2.imshow('ROI grayscale' , roi_gray)

            #creating mask and bitwise
            mask = np.zeros(frame.shape[:2] , np.uint8)
            cv2.rectangle(mask , roi_points[0] , roi_points[1] , 255 , -1)
            roi_bitwise = cv2.bitwise_or(frame , frame , mask=mask)
            cv2.imshow('ROI bitwise' , roi_bitwise)

        """Showing the frames"""
        cv2.imshow('video_frames' , frame)

        #saving frames
        cv2.imwrite(os.path.join(frames_folder , f"Frame{frame_count}.jpg"),frame)
        frame_count+=1

        # saving video
        out.write(frame)

        """holding the frame for a while"""
        key = cv2.waitKey(27)
        if key == ord('q'):
             break
        elif key == ord('r'):
            roi_points.clear()
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
