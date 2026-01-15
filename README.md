# OpenCV
This repository contains my OpenCV learning notes and practice implementations, created while preparing for computer vision and image processing interviews.
The focus is on core concepts, practical usage, and interview-ready explanations.

📌 What I Practiced

Image reading & visualization

Color spaces (RGB vs BGR)

Grayscale conversion

Image operations

Drawing geometric shapes

Video processing
Frame extraction & saving

Region of Interest (ROI)

Mouse events

Bitwise operations
1️⃣ Image Basics

Image is a matrix of pixel values

Pixel intensity range: 0–255

0 → Black

255 → White

Image Types
Type	Dimensions
Grayscale Image	2D (H, W)
Color Image	3D (H, W, 3)

2️⃣ Reading Images
Using Matplotlib

plt.imread()

Reads image in RGB format

Mainly used for visualization

Using OpenCV

cv2.imread(path, flag)

Flags:

0 → Grayscale

1 → Color (default)

-1 → Alpha channel

OpenCV reads images in BGR format

⚠️ Interview Tip:

Matplotlib → RGB
OpenCV → BGR

3️⃣ Displaying Images

Matplotlib:

plt.imshow(image)
plt.show()


OpenCV:

cv2.imshow("window_name", image)
cv2.waitKey()
cv2.destroyAllWindows()

4️⃣ Color Channels

Color image has 3 channels: Red, Green, Blue

Each channel is a grayscale image

image[:,:,0]  # Red channel
image[:,:,1]  # Green channel
image[:,:,2]  # Blue channel

BGR → RGB Conversion
rgb = image[:,:,::-1]

5️⃣ Grayscale Conversion

Color → Grayscale is possible

Grayscale → Color is not reversible

gray = cv2.imread(path, 0)

6️⃣ Image Shape & Flattening

Image shape:

Grayscale → (H, W)

Color → (H, W, 3)

Convert image to 1D array:

flat_image = image.ravel()

7️⃣ Image Addition
Direct Addition
cv2.add(img1, img2)


✔ Images must have the same shape

Weighted Addition
cv2.addWeighted(img1, 0.6, img2, 0.4, 1)


Used for image blending

8️⃣ Drawing Geometric Shapes

Commonly used for object detection & annotation

Line

cv2.line(img, pt1, pt2, color, thickness)


Rectangle

cv2.rectangle(img, pt1, pt2, color, thickness)


Circle

cv2.circle(img, center, radius, color, thickness)


Text

cv2.putText(img, text, org, font, scale, color, thickness)

9️⃣ Video Basics

Video = collection of frames

All frames have same height & width

Read Video
cap = cv2.VideoCapture("video.mp4")
res, frame = cap.read()


res → Frame read success (True/False)

frame → Image array

🔟 Frame Properties
cap.get(3)  # Frame width
cap.get(4)  # Frame height

1️⃣1️⃣ Saving Frames
cv2.imwrite("frame.jpg", frame)


Used for:

Dataset creation

Training data generation

1️⃣2️⃣ Saving Video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("output.mp4", fourcc, 20.0, (w, h))

1️⃣3️⃣ Region of Interest (ROI)

Extract specific part of image

roi = image[y1:y2, x1:x2]


Used in:

Face detection

Object tracking

Feature extraction

1️⃣4️⃣ Mouse Events

Capture pixel coordinates on click

cv2.setMouseCallback(window_name, function)


Used for:

ROI selection

Manual annotation

1️⃣5️⃣ Bitwise Operations

cv2.bitwise_and

cv2.bitwise_or

cv2.bitwise_not

cv2.bitwise_xor

Used for:

Masking

Background removal

Image segmentation

1️⃣6️⃣ Face Detection vs Face Recognition
Feature	Description
Face Detection	Detects face location
Face Recognition	Identifies the person
🔥 Extra Interview Notes

OpenCV images are NumPy arrays

Pixel access:

pixel = image[y, x]


waitKey() controls video playback speed

OpenCV is widely used for real-time computer vision applications



👩‍💻 Author

Mounika Annareddy
📌 OpenCV & Computer Vision Learner
🎯 Preparing for DataScience Interviews

