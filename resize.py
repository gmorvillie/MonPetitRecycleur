from PIL import Image
import os, sys

path = ('./resize/')

dirs = os.listdir( path )

def resize():
    for item in dirs:
        
        
        #if os.path.isfile(path+item):
        print("bonn")
        im = Image.open(path+item)
        width, height = im.size
        f, e = os.path.splitext(path+item)
        imResize = im.resize((int(width/5),int(height/5)), Image.ANTIALIAS)
        imResize.save('resized'+f+'.jpg', 'JPEG', quality=90)

resize()
