import cv2
import numpy as np
import time
import random
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
img=np.zeros((2160,2160), np.uint8)
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
for x in range(2160):
    d=[]
    for y in range(2160):
        if (x,y)==(1078,1078) or (x,y)==(1078,1079) or (x,y)==(1079,1079) or (x,y)==(1079,1080) or (x,y)==(1080,1079):
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
    l=np.zeros((2160,2160),np.uint8)
    for k in range(4):
        for x in range(2160):
            if 2 in data[x] or 3 in data[x] or 1 in data[x]:
                for y in range(2160):
                    if int(data[x][y])==1 or int(data[x][y])==2:
                        l[x,y]+=2**k
                        img[x,y]=255
                        data[x][y]=1
                    else:
                        img[x,y]=0
                        data[x][y]=0
        for x in range(2,2158):
            if 1 in data[x] or 1 in data[x+1] or 1 in data[x-1]:
                for y in range(2,2158):
                    develop(x,y)
        mc.player.setTilePos(0,239-n,0)
        for x in range(2160):
            for y in range(2160):
                if l[x,y]!=0:
                   mc.setBlock(y-1080,251-n,x-1080,95,l[x,y])
for x in range(2160):
    for y in range(2160):
        if int(data[x][y])==1:
            img[x,y]=255
for x in range(-16,17):
    for y in range(-16,17):
        mc.setBlock(y,-1,x,0)
        time.sleep(0.001)
for g in range(256):
    grow(g)
    print(g)
    imgo=img[540:1620,540:1620]
    '''cv2.imshow('img',imgo)
    if cv2.waitKey(0)&0xFF==27:
        cv2.imwrite('Game.bmp',img)
        break'''
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
