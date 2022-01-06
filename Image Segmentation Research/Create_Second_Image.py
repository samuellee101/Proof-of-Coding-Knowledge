from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np


img = Image.new('RGB', (256 , 256), color = 'green')
img1 = ImageDraw.Draw(img)

img1.rectangle((40, 40, 100, 100), fill=(55, 55, 192), outline=(55, 55, 192))
img2 = ImageDraw.Draw(img)

img2.ellipse((30, 30, 90, 90), fill=(60, 60, 220), outline=(60, 60, 220))
img3 = ImageDraw.Draw(img)

img3.pieslice((100, 100, 200, 200), start=0, end=270, fill=(255, 255, 0), outline=(0, 0, 0))
img4 = ImageDraw.Draw(img)

img4.polygon(((10, 200), (200, 100), (250, 50), (100,70)), fill=(100, 100, 100), outline=(0, 0, 0))
img5 = ImageDraw.Draw(img)

img.save('task_2.png')

plt.imshow(img)

#pillow used for simplicity