from PIL import Image
import os, sys

path = ('./resize/')

dirs = os.listdir( path )

def resize():
    i = 0
    for item in dirs:
        i = i +1
        
        #if os.path.isfile(path+item):
        print("bonn")
        im = Image.open(path+item)
        width, height = im.size
        f, e = os.path.splitext(path+item)
        imResize = im.resize((int(width/5),int(height/5)), Image.ANTIALIAS)
        print("f " +f)
        imResize.save(path + 'resized-'+str(i)+e, 'JPEG', quality=90)

resize()
