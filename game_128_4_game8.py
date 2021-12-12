import cv2
import numpy as np
import time
import random
img=np.zeros((128,128,3), np.uint8)
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
for x in range(128):
    d=[]
    for y in range(128):
        if x==63 and y<64 or y==64 and x<64 or x==64 and y>63 or y==63 and x>63:
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
for x in range(128):
    for y in range(128):
        if int(data[x][y])==1:
            cv2.rectangle(img,(x,y),(x,y),(255,255,255),-1)
        if int(data[x][y])==0:
            cv2.rectangle(img,(x,y),(x,y),(0,0,0),-1)
cv2.imwrite('game8/00001.jpg',img)
def develop(x,y):
    cell=0
    for a in range(3):
        for b in range(3):
            c=x+a-1
            d=y+b-1
            if c==128:
                c=0
            if c==-1:
                c=127
            if d==128:
                d=0
            if d==-1:
                d=127
            if int(data[c][d])==1 or int(data[c][d])==3:
                cell+=1
    if int(data[x][y])==1:
        cell-=1
    if cell==3 and int(data[x][y])==0:
        data[x][y]=2
    if cell!=2 and cell!=3 and int(data[x][y])==1:
        data[x][y]=3
def grow():
    for x in range(128):
        for y in range(128):
            develop(x,y)
    for x in range(128):
        for y in range(128):
            if int(data[x][y])==2:
                data[x][y]=1
            if int(data[x][y])==3:
                data[x][y]=0
    for x in range(128):
        for y in range(128):
            if int(data[x][y])==1:
                cv2.rectangle(img,(x,y),(x,y),(255,255,255),-1)
            if int(data[x][y])==0:
                cv2.rectangle(img,(x,y),(x,y),(0,0,0),-1)
g=1
while(True):
    cv2.imshow('image',img)
    grow()
    g+=1
    print(g)
    if g<10:
        G='0000'+str(g)
    elif g<100:
        G='000'+str(g)
    elif g<1000:
        G='00'+str(g)
    elif g<10000:
        G='0'+str(g)
    elif g<100000:
        G=str(g)
    cv2.imwrite('game8/'+G+'.jpg',img)
    if cv2.waitKey(1)&0xFF==27:
        #cv2.imwrite('Game.jpg',img)
        break
cv2.destroyAllWindows()
