"""Reading and writing image with opencv-cv2"""
import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread("C:\\Users\\Mounika Reddy\\OneDrive\\Desktop\\opencv\\images\\henas.jpg",0)

"""Here imread helps us to read the values of the image whereas
imshow helpus to create a image from the read pixel values .
-- Here flag = 0 becoz we are reading gray_scale image so flag value 0
for color image flag value is 1"""
print(image)

print(image.shape)

cv2.imshow('lena_image' , image)
"we need to use window name while showing image"


cv2.waitKey() # will completely wait to pop a image
cv2.destroyAllWindows() # used to remove the image pop up by using keypad buttons