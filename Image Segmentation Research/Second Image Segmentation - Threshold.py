from skimage.color import rgb2gray
import numpy as np
import cv2
import matplotlib.pyplot as plt

image = plt.imread('new_task_2.png')
image.shape
plt.imshow(image)

gray = rgb2gray(image)
plt.imshow(gray, cmap='gray')

array = np.unique(gray)
print(array)

#[0.25442234 0.28053334 0.35910276 0.39215687 0.92789996]

gray_r=np.zeros([256,256])
for i in range(gray.shape[0]):
    for j in range(gray.shape[1]):
        if (gray[i,j] <= 0.92 or gray[i,j] >= 0.93):
            #print(gray[i,j])
            gray_r[i,j] = 0
        else:
            gray_r[i,j] = 1
plt.imshow(gray_r, cmap='gray')