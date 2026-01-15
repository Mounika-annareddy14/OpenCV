"""Color image using open-cv"""
import matplotlib.pyplot as plt
import numpy as np
import cv2

color_image = cv2.imread("C:\\Users\\Mounika Reddy\\OneDrive\\Desktop\\opencv\\images\\dog.jpg",1)
print(color_image)
print(color_image.shape)

cv2.imshow('Dog' , color_image)

cv2.waitKey()
cv2.destroyAllWindows()


"""We can read image through matplotlib and we can show image through opencv
we can convert the color image to black and white but not a black and white image to color
matplotlib read image in the RGB form where 
opencv read image in the BGR form"""

color_to_gray = cv2.imread("C:\\Users\\Mounika Reddy\\OneDrive\\Desktop\\opencv\\images\\dog.jpg",0)
cv2.imshow('color_to_gray' , color_to_gray)

cv2.waitKey()
cv2.destroyAllWindows()


image = plt.imread("C:\\Users\\Mounika Reddy\\OneDrive\\Desktop\\opencv\\images\\dog.jpg")
cv2.imshow('image through mat-cv', image[:,:,::-1])
cv2.waitKey()
cv2.destroyAllWindows()


"""In open cv we can add two images also"""
image1 = cv2.imread("C:\\Users\\Mounika Reddy\\OneDrive\\Desktop\\opencv\\images\\dog.jpg")
image2 = cv2.imread("C:\\Users\\Mounika Reddy\\OneDrive\\Desktop\\opencv\\images\\car.jpg")

print(f"Image1 shape is : {image1.shape}")
print(f"Image2 shape is : {image2.shape}")
# becoz while adding the shape of the both images must be same
cv2.imshow("img1" , image1)
cv2.imshow("img2" , image2)

# there are two different sizes so resizing the image2
resized_img = cv2.resize(image2 , (237,213)) # width , height while giving
print(resized_img.shape)

joined_image = cv2.add(image1 , resized_img)

"""We can add through weightage also"""
weigthed_img = cv2.addWeighted(image1 , 0.6 , resized_img,0.4 ,1)


cv2.imshow("joined_image" , joined_image)
cv2.imshow("weighted_image" , weigthed_img)


cv2.waitKey()
cv2.destroyAllWindows()