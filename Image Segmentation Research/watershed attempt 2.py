from sys import exit
from scipy import ndimage as ndi
import matplotlib.pyplot as plt
from skimage.morphology import watershed, disk
from skimage import data
from skimage.io import imread
from skimage.filters import rank
from skimage.color import rgb2gray
from skimage.util import img_as_ubyte
import cv2

img = cv2.imread('task_2.png')
#img = cv2.imread('PinClipart.com_mix-clipart_5641149.png')
img_gray = rgb2gray(img)

image = img_as_ubyte(img_gray)

markers = rank.gradient(image, disk(5)) < 20
markers = ndi.label(markers)[0]

gradient = rank.gradient(image,disk(2))

fig, axes = plt.subplots(nrows=2,ncols=2,figsize=(8,8), sharex=True,
sharey=True,subplot_kw={'adjustable':'box'})
ax = axes.ravel()

ax[0].imshow(image, cmap=plt.cm.gray, interpolation='nearest')
ax[0].set_title("Original")

ax[1].imshow(gradient,cmap=plt.cm.Spectral, interpolation ='nearest')
ax[1].set_title("Local Gradient")

ax[2].imshow(markers,cmap=plt.cm.Spectral, interpolation ='nearest')
ax[2].set_title("Local Gradient")

ax[3].imshow(image, cmap=plt.cm.gray, interpolation='nearest')
ax[3].imshow(gradient,cmap=plt.cm.Spectral, interpolation ='nearest',alpha=0.7)
ax[3].set_title("Segmented")

for a in ax:
    a.axis('off')

fig.tight_layout()
plt.imshow()
    