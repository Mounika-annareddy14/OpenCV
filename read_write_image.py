import cv2
''' image -  it is a combination of rows and columns and it is made up with pixel values
pixel value ranges between 0-256 ie 0 for black and 255 for white
and image is a two types 
color image (3d) and 
gray_scale_image - 2d'''
import matplotlib.pyplot as plt
import numpy as np

image = plt.imread("C:\\Users\\Mounika Reddy\\OneDrive\\Desktop\\opencv\\images\\henas.jpg")
print(image)
print(image.shape)

plt.imshow(image)
plt.show()

