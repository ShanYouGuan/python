from PIL import Image, ImageDraw, ImageFont
import random

msgNum = str(random.randint(1,99))

# Read image
im = Image.open('kxrr.jpg')
w, h = im.size
wDraw = 0.8 * w
hDraw = 0.1 * w

# Draw image
draw = ImageDraw.Draw(im)
draw.text((wDraw,hDraw), msgNum, fill=(255,33,33))

# Save image
im.save('kxrr_msg.jpg')