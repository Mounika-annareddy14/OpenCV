"""Geometric shapes through opencv for object detection"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

car_image = cv2.imread("C:\\Users\\Mounika Reddy\\OneDrive\\Desktop\\opencv\\images\\car.jpg")
print(car_image.shape)
# # Line
cv2.line(car_image , (107 ,43) ,  (67 ,100) ,  [0,0,255] , 2)

# arrowedline
cv2.arrowedLine(car_image , (170,103) , (67,100) , [255,255,0] , 1 )

#circle
cv2.circle(car_image , (102,115) , 15 , [255 , 0 , 0] , 2)

#rectangle
cv2.rectangle(car_image, (10, 30), (250, 140), (0, 0, 255), 1)

#text
small_rectangle = cv2.rectangle(car_image , (10,14) , (56,31) , [0,255,0] , -1)
cv2.putText(small_rectangle , "CAR",(10,30),cv2.FONT_HERSHEY_SIMPLEX , 0.8 , [0,0,255] , 2 )


"""In open cv we can convert 3d image or 2d image into 1d by using ravel function"""
car = cv2.imread("C:\\Users\\Mounika Reddy\\OneDrive\\Desktop\\opencv\\images\\car.jpg")  #3d
small = car.ravel()
print(car.shape)
print(small.shape)



cv2.imshow("car" , car_image)

cv2.waitKey()
cv2.destroyAllWindows()