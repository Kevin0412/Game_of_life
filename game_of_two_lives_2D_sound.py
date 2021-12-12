import cv2
import numpy as np
import time
import random
import math
import soundfile as sf
#img=np.zeros((1,1),np.uint8)
data=[1,0,0]
sounds=[]
#img[0][1]=255
#img[0][0]=255
x=1
while(True):
    d=[]
    for y in range(x+1):
        if y==0:
            '''
            if int(data[y+1])==1:
                d.append(1)
            else:
                d.append(0)
            '''
            if int(data[y])==1:
                if int(data[y+1])==0 and int(data[y])==0:
                    d.append(1)
                else:
                    d.append(0)
            else:
                if int(data[y])==0 and int(data[y+1])==1 or int(data[y])==1 and int(data[y+1])==0:
                    d.append(1)
                else:
                    d.append(0)
            
        else:
            if int(data[y])==1:
                if int(data[y+1])==0 and int(data[y-1])==0:
                    d.append(1)
                else:
                    d.append(0)
            else:
                if int(data[y-1])==0 and int(data[y+1])==1 or int(data[y-1])==1 and int(data[y+1])==0:
                    d.append(1)
                else:
                    d.append(0)
    m=0
    d.append(0)
    d.append(0)
    sounds.append(sum(d)-sum(data))
    data=d
    #cv2.imshow('image',img)
    #print('\r',math.log(x,2))
    '''if math.modf(math.log(x,2))[0]==0.0:
        #print(str(int(math.log(x,2))))
        #img=np.ones((x,2*x),np.uint8)*127
        img=np.zeros((x,x),np.uint8)
        for m in range(x):
            for n in range(m+1):
                if int(data[m][n])==1:
                    img[m][n]=255
                    #img[m][x-n-1]=255
        cv2.imwrite('pyramid#'+str(int(math.log(x,2)))+'.png',img)
        print(x,'                ')
    if int(math.log(x,2))==16:
        break    '''
    '''if cv2.waitKey(1)&0xFF==27:
        break'''
    x+=1
    #sounds.append(int(sum(data)/x*4/3*65536))
    if math.modf(math.log(x,2))[0]==0.0:
        print(math.log(x,2))
    if x==2**15+2:
        break
sound=[]
for n in range(10):
    for s in reversed(sounds):
        sound.append(s)
sf.write('game_of_life.wav',np.array(sounds),44100)
#cv2.destroyAllWindows()
