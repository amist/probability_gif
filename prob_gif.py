from images2gif import writeGif
from PIL import Image, ImageDraw, ImageColor
from random import randint
import os

#pics_dir = os.path.join(os.getcwd(), 'pics')
pics_dir = 'pics'
file_names = sorted((os.path.join(pics_dir, fn) for fn in os.listdir(pics_dir) if fn.endswith('.jpg')))
#print file_names

images = [Image.open(fn) for fn in file_names]
#print images

#size = (150,150)
#for im in images:
#    im.thumbnail(size, Image.ANTIALIAS)

for im in images:
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
            
    #draw = ImageDraw.Draw(im)
    #r, g, b = im.getpixel((10, 10))
    #print r, g, b
    #draw.point((10, 10), ImageColor.getcolor('#00ff00', 'RGB'))
    #r, g, b = im.getpixel((10, 10))
    #print r, g, b
    
    
filename = "gif.gif"
writeGif(filename, images, duration=0.2)
