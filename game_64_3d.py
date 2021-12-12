import cv2
import numpy as np
import time
import random
img=np.zeros((512,512), np.uint8)
'''h=open("game.csv")
H=h.read()
Hh=H.split("\n")
data=[]
for row in Hh:
    data.append(row.split(","))
    time.sleep(0.01)'''
data=[]
for x in range(64):
    '''d=[]
    for y in range(64):
        if 0==random.randint(0,y):
            d.append(1)
        else:
            d.append(0)
    data.append(d)'''
    '''d=[]
    if x==32 or x==31:
        for y in range(64):
            if y==0 or y==63:
                d.append(1)
            else:
                d.append(1) 
    else:
        for y in range(64):
            if y==31 or y==32:
                d.append(1)
            else:
                d.append(0)'''
    d=[]
    for y in range(64):
        D=[]
        for z in range(64):
            if x==y or x==31 or x==32:
                D.append(1)
            else:
                D.append(0)
        d.append(D)
    data.append(d)
#0 remain died
#1 remain alive
#2 born
#3 die
def develop(x,y,z):
    cell=0
    for a in range(3):
        for b in range(3):
            for c in range(3):
                d=x+a-1
                e=y+b-1
                f=z+c-1
                if d==64:
                    d=0
                if d==-1:
                    d=63
                if e==64:
                    e=0
                if e==-1:
                    e=63
                if f==64:
                    f=0
                if f==-1:
                    f=63
                if int(data[d][e][f])==1 or int(data[d][e][f])==3:
                    cell+=1
    if int(data[x][y][z])==1:
        cell-=1
    if 8<cell<11 and int(data[x][y][z])==0:
        data[x][y][z]=2
        img[x+z%8*64,y+int(z/8)*64]=255
    if cell!=9 and cell!=10 and cell!=11 and cell!=8 and int(data[x][y][z])==1:
        data[x][y][z]=3
        img[x+z%8*64,y+int(z/8)*64]=0
def grow():
    for x in range(64):
        for y in range(64):
            for z in range(64):
                if data[x][y][z]==2:
                    data[x][y][z]=1
                if data[x][y][z]==3:
                    data[x][y][z]=0
    for x in range(64):
        for y in range(64):
            for z in range(64):
                develop(x,y,z)
for x in range(64):
    for y in range(64):
        for z in range(64):
            if int(data[x][y][z])==1:
                img[x+z%8*64,y+int(z/8)*64]=255
            if int(data[x][y][z])==0:
                img[x+z%8*64,y+int(z/8)*64]=0
def breaked(data):
    result=True
    for ds in data:
        for d in ds:
            if 2 in d or 3 in d:
                result=False
    return result
g=0
while(True):
    cv2.imshow('image',img)
    if cv2.waitKey(1)&0xFF==27:
        break
    print(g)
    g+=1
    grow()
    if breaked(data):
        cv2.imwrite('Game.jpg',img)
        break
    #print(data)
cv2.destroyAllWindows()
