import cv2
import numpy as np
import time
import random
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
img=np.zeros((540,540), np.uint8)
'''h=open("game.csv")
H=h.read()
Hh=H.split("\n")
data=[]
for row in Hh:
    data.append(row.split(","))
    time.sleep(0.01)'''
data=[]
#f=[]
#e=[]
'''for y in range(256):
    if 0==random.randint(0,1):
        f.append(1)
        e.append(1)
    else:
        f.append(0)
        e.append(1)'''
for x in range(540):
    d=[]
    for y in range(540):
        if  x==269 and y<270 or x==270 and y>269 or y==269 and x>269 or y==270 and x<270 or x-y==-1 or x+y==538 or x-y==1 or x+y==540:
            #if  x-y==1 and y<270 or x+y==540 and y<271 or x-y==-1 and y>269 or x+y==538 and y>268:
            d.append(1)
        else:
            d.append(0)
    data.append(d)
    '''if x==127 or x==128:
        for y in range(256):
            if y==0 or y==255:
                d.append(0)
            else:
                d.append(1) 
    else:
        for y in range(256):
            if y==127 or y==128:
                d.append(0)
            else:
                d.append(0)'''
    #data.append(d)
    '''if 0==random.randint(0,1):
        data.append(e)
    else:
        data.append(f)'''
#0 remain died
#1 remain alive
#2 born
#3 die
def develop(x,y):
    cell=0
    for a in range(3):
        for b in range(3):
            c=x+a-1
            d=y+b-1
            if c==539:
                c=538
            if c==0:
                c=1
            if d==539:
                d=538
            if d==0:
                d=1
            if int(data[c][d])==1 or int(data[c][d])==3:
                cell+=1
    if int(data[x][y])==1:
        cell-=1
    if cell==3 and int(data[x][y])==0:
        data[x][y]=2
    if cell!=2 and cell!=3 and int(data[x][y])==1:
        data[x][y]=3
def grow(n):
    for x in range(-n,n):
        if int(data[x+270][270-n-1])==1 or int(data[x+270][270-n-1])==2:
            mc.setBlock(-n-1,251-n,x,155)
        else:
            if int(data[x+270][270-n-1])==3:
                mc.setBlock(-n-1,252-n,x,169)
            mc.setBlock(-n-1,251-n,x,20)
        if int(data[x+270][270+n])==1 or int(data[x+270][270+n])==2:
            mc.setBlock(n,251-n,x,155)
        else:
            if int(data[x+270][270+n])==3:
                mc.setBlock(n,252-n,x,169)
            mc.setBlock(n,251-n,x,20)
        if int(data[270-n-1][x+270])==1 or int(data[270-n-1][x+270])==2:
            mc.setBlock(x,251-n,-n-1,155)
        else:
            if int(data[270-n-1][x+270])==3:
                mc.setBlock(x,252-n,-n-1,169)
            mc.setBlock(x,251-n,-n-1,20)
        if int(data[270+n][x+270])==1 or int(data[270+n][x+270])==2:
            mc.setBlock(x,251-n,n,155)
        else:
            if int(data[270+n][x+270])==3:
                mc.setBlock(x,252-n,n,169)
            mc.setBlock(x,251-n,n,20)
        for y in range(-n,n):
            if int(data[x+270][y+270])==1 or int(data[x+270][y+270])==2:
                if int(data[x+270][y+270])==2:
                    mc.setBlock(y,251-n,x,155)
            else:
                if int(data[x+270][y+270])==3:
                    mc.setBlock(y,252-n,x,169)
    for x in range(540):
        for y in range(540):
            if data[x][y]==2 or data[x][y]==1:
                data[x][y]=1
                img[x,y]=255
            if data[x][y]==3 or data[x][y]==0:
                data[x][y]=0
                img[x,y]=0
    for x in range(1,539):
        for y in range(1,539):
            if (x,y)!=(1,1) and (x,y)!=(1,538) and (x,y)!=(538,1) and (x,y)!=(538,538) and (x,y)!=(2,1) and (x,y)!=(2,538) and  (x,y)!=(537,1) and (x,y)!=(537,538) and (x,y)!=(1,2) and (x,y)!=(1,537) and (x,y)!=(538,2) and (x,y)!=(538,537) and (x,y)!=(3,1) and (x,y)!=(3,538) and  (x,y)!=(536,1) and (x,y)!=(536,538) and (x,y)!=(1,3) and (x,y)!=(1,536) and (x,y)!=(538,3) and (x,y)!=(538,536):
                develop(x,y)
for x in range(540):
    for y in range(540):
        if int(data[x][y])==1:
            img[x,y]=255
        mc.setBlock(y-270,-1,x-270,0)
for g in range(256):
    grow(g)
    print(g)
    cv2.imshow('img',img)
    if cv2.waitKey(1)&0xFF==27:
        cv2.imwrite('Game.bmp',img)
        break
cv2.imwrite('Game.bmp',img)
#cv2.destroyAllWindows()
