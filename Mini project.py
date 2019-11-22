import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

 # reading an image 
im_path = "./femi.jpg"
test_image = None
# TODO read in the image with name femi.jpg
test_image = cv2.imread("femi.jpg")
plt.imshow(test_image)
 
# CONVERTING THE BGR TO RGB 

convert_RGB = cv2.cvtColor(test_image, cv2.COLOR_BGR2RGB)
plt.imshow(convert_RGB)

# CONVERTING THE convert_RGB TO HSV 
# H = 0-20 , S= 48-255 and V = 80-255

convert_HSV = cv2.cvtColor(convert_RGB, cv2.COLOR_RGB2HSV)

plt.imshow(convert_HSV)

#  SKIN DETECTION,  skin color range in hsv

Lower = np.array([0, 48, 80], dtype = "uint8")
upper = np.array([20, 255, 255], dtype = "uint8")

#TODO detect the skin pixels in the test images.# for hsv to be qualified as pixel is has 
# have an array of H 0-20 ,S 0-255 and V 0-255 
# i.e colors outside the range above
# use cv2.inRange function

skin_pixels = None

mask = cv2.inRange(convert_HSV,Lower,upper)
plt.imshow(mask)

# CONVERTING THE BGR (COLOR)  TO GRAY SCALE USING THE using ApplyColorMap 

# Read the colored image
color_im_path = "./teju.jpg"
colored_im = cv2.imread(color_im_path)

# Convert the colored image to greyscale
gray_im = cv2.cvtColor(colored_im, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_im, cmap='gray', vmin = 0, vmax = 255)





