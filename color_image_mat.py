"""Color image : is made up of with 3 channels
R G B colors
But individually they are gray color only
color image
in matplotlib it read had RGB
but in opencv it read it has BGR"""

import matplotlib.pyplot as plt
import numpy as np
import cv2

color_image = plt.imread("C:\\Users\\Mounika Reddy\\OneDrive\\Desktop\\opencv\\images\\cube.jpg")
print(color_image)
print(color_image.shape)

plt.imshow(color_image)
plt.show()

plt.subplot(2,2,1)
plt.title('R-Channel')
plt.imshow(color_image[:,:,0])
plt.show()

plt.subplot(2,2,2)
plt.title('g-Channel')
plt.imshow(color_image[:,:,1])
plt.show()

plt.subplot(2,2,3)
plt.title('B-channel')
plt.imshow(color_image[:,:,2])
plt.show()

plt.subplot(2,2,4)
plt.title('color-image')
plt.imshow(color_image)
plt.show()