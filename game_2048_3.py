import cv2
import numpy as np
import time
import random
img=np.zeros((2048,2048,3), np.uint8)
h=open("game.csv")
H=h.read()
Hh=H.split("\n")
data=[]
for row in Hh:
    data.append(row.split(","))
    time.sleep(0.01)
'''data=[]
for x in range(1024):
    d=[]
    for y in range(1024):
        if 0==random.randint(0,1):
            d.append(1)
        else:
            d.append(0)
    data.append(d)'''
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
            if c==2048:
                c=0
            if c==-1:
                c=2047
            if d==2048:
                d=0
            if d==-1:
                d=2047
            if int(data[c][d])==1 or int(data[c][d])==3:
                cell+=1
    if int(data[x][y])==1:
        cell-=1
    if cell==3 and int(data[x][y])==0:
        data[x][y]=2
    if cell!=2 and cell!=3 and int(data[x][y])==1:
        data[x][y]=3
def grow():
    for x in range(2048):
        for y in range(2048):
            develop(x,y)
    for x in range(2048):
        for y in range(2048):
            if data[x][y]==2:
                data[x][y]=1
            if data[x][y]==3:
                data[x][y]=0
    for x in range(2048):
        for y in range(2048):
            if int(data[x][y])==1:
                cv2.rectangle(img,(x,y),(x,y),(255,255,255),-1)
            if int(data[x][y])==0:
                cv2.rectangle(img,(x,y),(x,y),(0,0,0),-1)
g=0
'''while(True):
    cv2.imshow('image',img)
    grow()
    g+=1
    print(g)
    if cv2.waitKey(1)&0xFF==27:
        cv2.imwrite('Game.jpg',img)
        break
cv2.destroyAllWindows()'''
while(True):
    for n in range(10):
        grow()
        g+=1
        print(g)
        cv2.imwrite('Game.jpg',img)
    File=open("game.csv","w")
    for x in range(2048):
        for y in range(2048):
            File.write(str(data[x][y]))
            File.write(',')
        File.write('\n')
    File.close()
