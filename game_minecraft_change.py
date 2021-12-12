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
        if x==y or x+y==539 or x-y==2 and y<269 or x+y==541 and y<271 or x-y==-2 and y>270 or x+y==537 and y>268:
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
            if int(data[c][d])==1 or int(data[c][d])==3:
                cell+=1
    if int(data[x][y])==1:
        cell-=1
    if cell==3 and int(data[x][y])==0:
        data[x][y]=2
    if cell!=2 and cell!=3 and int(data[x][y])==1:
        data[x][y]=3
def grow(n):
    for x in range(540):
        if 2 in data[x] or 3 in data[x] and n!=0:
            block=mc.getBlockWithData(random.randint(-270,269),251-n,x-270)
            if block.id!=0:
                for y in range(540):
                    mc.setBlock(y-270,251-n,x-270,0)
            for y in range(540):
                if int(data[x][y])==1 or int(data[x][y])==2:
                    '''if int(data[x][y])==1:
                        mc.setBlock(y-270,251-n,x-270,155)'''
                    if int(data[x][y])==2:
                        mc.setBlock(y-270,251-n,x-270,155)
                    img[x,y]=255
                    data[x][y]=1
                else:
                    if int(data[x][y])==3:
                        mc.setBlock(y-270,252-n,x-270,20)
                    img[x,y]=0
                    data[x][y]=0
    for x in range(2,538):
        for y in range(2,538):
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
'''
100000
010100
001000
000100
001010
000001
'''
