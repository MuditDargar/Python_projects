# first solution

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
 
# image = cv2.imread(r"E:\Desktop\Python Project\projects\images.jpg", 1)
# # Loading the image
 
# half = cv2.resize(image, (0, 0), fx = 0.1, fy = 0.1)
# bigger = cv2.resize(image, (1050, 1610))
 
# stretch_near = cv2.resize(image, (780, 540),
#                interpolation = cv2.INTER_LINEAR)
 
 
# Titles =["Original", "Half", "Bigger", "Interpolation Nearest"]
# images =[image, half, bigger, stretch_near]
# count = 4
 
# for i in range(count):
#     plt.subplot(2, 2, i + 1)
#     plt.title(Titles[i])
#     plt.imshow(images[i])
 
# plt.show()




#Second solution


# Importing Image class from PIL module
from PIL import Image
 
# Opens a image in RGB mode
im = Image.open(r"E:\Desktop\Python Project\projects\images.jpg")
 
# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size
 
# Setting the points for cropped image
left = 4
top = height / 5
right = 154
bottom = 3 * height / 5
 
# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))
newsize = (300, 300)
im1 = im1.resize(newsize)
# Shows the image in image viewer
im1.show()