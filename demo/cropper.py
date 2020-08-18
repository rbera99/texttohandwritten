import sys,os
from PIL import Image
import os
im=Image.open(r"C:\Users\Riddhik\Desktop\demo\handimg\abc.jpeg")
for i in range(0,240,24):
    area = (i,0,i+24,52)
    cim=im.crop(area)
    
    new_im = Image.new('RGB', (24,52))
    new_im.paste(cim)
    new_im.save(r'C:\Users\Riddhik\Desktop\demo\handimg\wst.jpg')
    
    os.chdir('C:\\Users\\Riddhik\Desktop\\demo\\handimg')
    src='wst.jpg'
    #dst=chr(ord('A')+int(i/24))+'123.jpg'
    dst=str(int(i/24))+ '.jpg'
    os.rename(src,dst)



    

