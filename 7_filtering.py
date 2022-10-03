import cv2
import numpy as np

img = cv2.imread("assets/cat.jpg")
# filter2D
blur_filter = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
])
blur_filter = blur_filter / 9
blur_img = cv2.filter2D(img, ddepth=-1, 
        kernel=blur_filter)

# NO FILTER // BRIGHTNESS
no_filter = np.array([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
])
no_filter = no_filter * 2
bright_img = cv2.filter2D(img, ddepth=-1, 
        kernel=no_filter)

# BLUR
blur_img = cv2.blur(img, ksize=(111, 111))

# GAUSSIAN BLUR
gaus_img = cv2.GaussianBlur(img, ksize=(11, 11),
            sigmaX=30, sigmaY=300)

# SHARPEN
sharpen_filter = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])
sharp_img = cv2.filter2D(img, ddepth=-1, 
        kernel=sharpen_filter)

# EDGE DETECTION // LAPLACIAN
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_img = cv2.GaussianBlur(img, ksize=(3, 3),
            sigmaX=1, sigmaY=1)
edges = cv2.Laplacian(gray_img, ddepth=-1)

cv2.imshow("Cat!", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

