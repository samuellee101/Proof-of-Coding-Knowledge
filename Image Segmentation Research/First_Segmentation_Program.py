from skimage.color import rgb2gray
import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy import ndimage

image = plt.imread('task_1.png')
image.shape
plt.imshow(image)

gray = rgb2gray(image)
plt.imshow(gray, cmap='gray')

x, bin_edges = np.histogram(gray, bins=256, range=(0, 1))

plt.figure()
plt.title("Pixels per Grayscale Value")
plt.xlabel("grayscale value")
plt.ylabel("pixels")
plt.xlim([0.0, 1.0])
plt.plot(bin_edges[0:-1], x)
plt.show()

originalImage = cv2.imread('task_1.png')

#0.0721 0.59294116 0.2125 0.7154

#gray_r = gray.reshape(30*30)
gray_r=np.zeros([30,30])
for i in range(gray.shape[0]):
    for j in range(gray.shape[1]):
        if (gray[i,j] <= 0.21 or gray[i,j] >= 0.22):
            #print(gray[i,j])
            gray_r[i,j] = 0
        else:
            gray_r[i,j] = 1
# gray = gray_r.reshape(gray.shape[0],gray.shape[1])
plt.imshow(gray_r, cmap='gray')

array = np.array(gray)
print('These are all the pixel values of the image: \n')
print(array)

unique_array = np.unique(array)
print("\n These are your unique values: ")
print(unique_array)

# unique finds the unique values in an array
