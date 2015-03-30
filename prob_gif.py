from images2gif import writeGif
from PIL import Image, ImageDraw, ImageColor
from random import randint
from copy import copy
import os

frames_number = 2

pics_dir = 'pics'
file_name = 'original-firefox-logo.jpg'
orig_im = Image.open(os.path.join(pics_dir, file_name))

images = []
for i in range(frames_number):
    im = copy(orig_im)
    draw = ImageDraw.Draw(im)
    (width, height) = im.size
    for i in range(width):
        for j in range(height):
            r, g, b = im.getpixel((i, j))
            color_str = '#'
            for c in [r, g, b]:
                if randint(0, 255) < c:
                    color_str += 'ff'
                else:
                    color_str += '00'
            draw.point((i, j), ImageColor.getcolor(color_str, 'RGB'))
    images.append(im)
            
    #draw = ImageDraw.Draw(im)
    #r, g, b = im.getpixel((10, 10))
    #print r, g, b
    #draw.point((10, 10), ImageColor.getcolor('#00ff00', 'RGB'))
    #r, g, b = im.getpixel((10, 10))
    #print r, g, b
    
images[0].save("pic.jpeg", "JPEG")

if frames_number > 1:
    filename = "gif.gif"
    writeGif(filename, images, duration=0.01)
