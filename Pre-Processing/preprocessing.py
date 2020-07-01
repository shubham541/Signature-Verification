from PIL import Image
from IPython.display import display
import matplotlib.pyplot as plt
import cv2
import numpy as np
#from google.colab.patches import cv2_imshow
#import os
#import glob 
#%matplotlib inline

# load image
im = Image.open("sign.jpg")
display(im)

# Resize image
width, height = im.size
# print(width,height)
aspect_ratio = width/height
# print(aspect_ratio)
# let height is 60
im_height = 60
im_width = int(im_height * aspect_ratio)
resized_im = im.resize((im_width,im_height), Image.ANTIALIAS)
display(resized_im)

# change image mode using pillow
# print(resized_im.mode)
img = resized_im.convert('LA')
plt.hist(img.histogram())
plt.show()
 
# change image mode using cv2
im_cv = cv2.imread('sign.jpg')
gray_im_cv = cv2.cvtColor(im_cv, cv2.COLOR_BGR2GRAY)
rsz_im_cv = cv2.resize(gray_im_cv, None, fx=0.05, fy=0.05)
plt.hist(rsz_im_cv)
plt.show()

#******** Code Using OpenCv**********

# Read
im3 = cv2.imread('sign.jpg') 
#cv2.imshow(im3,0)
cv2.imshow('Test image',im3)




























