import cv2
import numpy as np
import time
import random
img=np.zeros((512,512,3), np.uint8)
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
for x in range(512):
    d=[]
    for y in range(512):
        if  x==255 and y<256 or x==256 and y>255 or y==256 and x<256 or y==255 and x>255:
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
            if c==512:
                c=0
            if c==-1:
                c=511
            if d==512:
                d=0
            if d==-1:
                d=511
            if int(data[c][d])==1 or int(data[c][d])==3:
                cell+=1
    if int(data[x][y])==1:
        cell-=1
    if cell==3 and int(data[x][y])==0:
        data[x][y]=2
    if cell!=2 and cell!=3 and int(data[x][y])==1:
        data[x][y]=3
def grow(n):
    for x in range(512):
        for y in range(512):
            develop(x,y)
    for x in range(512):
        for y in range(512):
            if int(data[x][y])==2:
                data[x][y]=1
            if int(data[x][y])==3:
                data[x][y]=0
    for x in range(512):
        for y in range(512):
            if int(data[x][y])==1:
                if int((n%1530)/255)==0:
                    img[x,y]=(0,n%255,255)
                if int((n%1530)/255)==1:
                    img[x,y]=(0,255,255-n%255)
                if int((n%1530)/255)==2:
                    img[x,y]=(n%255,255,0)
                if int((n%1530)/255)==3:
                    img[x,y]=(255,255-n%255,0)
                if int((n%1530)/255)==4:
                    img[x,y]=(255,0,n%255)
                if int((n%1530)/255)==5:
                    img[x,y]=(255-n%255,0,255)
for g in range(1530*2):
    cv2.imshow('image',img)
    grow(g)
    print(g)
    if cv2.waitKey(1)&0xFF==27:
        cv2.imwrite('Game.jpg',img)
        break
cv2.imwrite('Game.jpg',img)
cv2.destroyAllWindows()
