"""bitwise operators"""
import cv2
import numpy as np

from mousehandling_events import black_image

image = np.zeros((512,512) , np.float64)
cv2.rectangle(image , (0,0) , (int(image.shape[1]/2),512) , (255,255,255) ,-1)
black_image = np.zeros((512,512) , np.float64)

#bit_or
f = cv2.bitwise_or(image,black_image)

#bit_and
g = cv2.bitwise_and(image , black_image)

cv2.imshow('image' , image)
cv2.imshow('black' , black_image)
cv2.imshow('or' ,f )
cv2.imshow('and' , g)




cv2.waitKey()
cv2.destroyAllWindows()

