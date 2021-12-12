import cv2
import numpy as np
import time
import random
import math
img=np.zeros((1,1),np.uint8)
data=[[1,0,0]]
#img[0][1]=255
img[0][0]=255
x=1
while(True):
    d=[]
    for y in range(x+1):
        if y==0:
            if int(data[x-1][y+1])==1:
                d.append(1)
            else:
                d.append(0)
            '''if int(data[x-1][y])==1:
                if int(data[x-1][y+1])==0 and int(data[x-1][y])==0:
                    d.append(1)
                else:
                    d.append(0)
            else:
                if int(data[x-1][y])==0 and int(data[x-1][y+1])==1 or int(data[x-1][y])==1 and int(data[x-1][y+1])==0:
                    d.append(1)
                else:
                    d.append(0)
            '''
        else:
            if int(data[x-1][y])==1:
                if int(data[x-1][y+1])==0 and int(data[x-1][y-1])==0:
                    d.append(1)
                else:
                    d.append(0)
            else:
                if int(data[x-1][y-1])==0 and int(data[x-1][y+1])==1 or int(data[x-1][y-1])==1 and int(data[x-1][y+1])==0:
                    d.append(1)
                else:
                    d.append(0)
    m=0
    d.append(0)
    d.append(0)
    data.append(d)
    #cv2.imshow('image',img)
    print('\r',math.log(x,2))
    if math.modf(math.log(x,2))[0]==0.0:
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
        break    
    '''if cv2.waitKey(1)&0xFF==27:
        break'''
    x+=1
#cv2.destroyAllWindows()
