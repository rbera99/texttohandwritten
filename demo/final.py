import sys
from PIL import Image
import os
#libraries
def create(f):
    new_im = Image.new('RGB', (1200,52),(255, 255, 255))
    os.chdir('C:\\Users\\Riddhik\Desktop\\demo\\handimg')
#for all the symbols which can't be used in file naming
    Dict = {'?': '1.3','*':'1.4','<':'1.5','>':'1.6','root':'1.7','\"':'1.1','\'':'1.2'}
    list_im = os.listdir()
    n=0
    for i in f:
    #for symbols which can't be include in naming file
        if i in Dict:
            fnm= str(Dict[i])+'.jpg'
            im=Image.open(fnm)
            new_im.paste(im,(n,0))
            n+=24
            continue
   
    #for small letters
        if(ord(i)>=97 and ord(i)<=122):
            fnm= i +'.jpg'
            im=Image.open(fnm)
            new_im.paste(im,(n,0))
            n+=24
            continue
    #for capital letters
        elif(ord(i)>=65 and ord(i)<=90):
            fnm= i +'1.jpg'
            im=Image.open(fnm)
            new_im.paste(im,(n,0))
            n+=24
            continue

    #for all the symbols whose ascII value can be generated
        fnm= i +'.jpg'
        im=Image.open(fnm)
        new_im.paste(im,(n,0))
        n+=24
    return new_im

#image saver
def  saver(new_im,u):
    q=r'C:\Users\Riddhik\Desktop\demo\pg' + str(u)+'.jpg'
    new_im.save(q)
#main
fn=open(r'C:\Users\Riddhik\Desktop\demo\typed.txt','r')
b=fn.read()
a=''
for i in b:
    a=a+i
a=a+ ' asdfgh'

z=''
print(a)
new_im= Image.new('RGB', (1200,1560),(255, 255,255))
n=0
u=0
for i in a:
    if(i=='\n'):
        n=int((n//50)+1)*50
        continue
    if(i != ' '): 
        z=z+str(i)
        n+=1
        continue
    '''if(i==' '):
        n=n+1'''
    
    '''if(a[n%50 -1]==' 'and i==' '):
        n=n+1
        continue'''
    
        
    n1=n-len(z)
    imga = Image.new('RGB', (1200,52),(255, 255, 255))
    imga = create(z)
    
    if n/1500>1:
        n=0
        saver(new_im,u)
        new_im= Image.new('RGB', (1200,1560),(255, 255,255))
        u=u+1


    if ((n%50)>(n1%50)):
        new_im.paste(imga,((n1%50)*24,(n1//50)*52))
    else:
        n1=((n//50))*50
        new_im.paste(imga,(0,(n1//50)*52))
        n = n1+ len(z)
        
    
    if(i==' '):
        n=n+1
        z=''
    
saver(new_im,u)   

#q=r'C:\Users\Riddhik\Desktop\demo\pg1234567' + '.jpg'
#new_im.save(q)








