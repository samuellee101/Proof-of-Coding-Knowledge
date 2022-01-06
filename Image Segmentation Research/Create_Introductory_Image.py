from PIL import Image, ImageDraw

img = Image.new('RGB', (30 , 30), color = 'blue')
img1 = ImageDraw.Draw(img)

img1.rectangle((0, 0, 20, 25), fill=(0, 192, 192), outline=(0, 192, 192))
img2 = ImageDraw.Draw(img)

img2.ellipse((10, 10, 15, 15), fill=(255, 0, 0), outline=(255, 0, 0))
img3 = ImageDraw.Draw(img)

img3.ellipse((1, 1, 5, 5), fill=(0, 255, 0), outline=(0, 255, 0))
img.save('task_1.png')
