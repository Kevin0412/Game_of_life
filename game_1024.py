import cv2
import numpy as np
import time
img=np.zeros((1024,1024,3), np.uint8)
h=open("game.csv")
H=h.read()
Hh=H.split("\n")
data=[]
for row in Hh:
    data.append(row.split(","))
    time.sleep(0.01)
for x in range(1024):
    data[x][-1]=int(data[x][1023])
    data[x][1024]=int(data[x][0])
    data[-1][x]=int(data[1023][x])
    data[1024][x]=int(data[0][x])
#0 remain died
#1 remain alive
#2 born
#3 die
def develop(x,y):
    cell=0
    for a in range(3):
        for b in range(3):
            if int(data[x+a-1][y+b-1])==1 or int(data[x+a-1][y+b-1])==3:
                cell+=1
    if int(data[x][y])==1:
        cell-=1
    if cell==3 and int(data[x][y])==0:
        data[x][y]=2
        cv2.rectangle(img,(x,y),(x,y),(255,255,255),-1)
    if cell!=2 and cell!=3 and int(data[x][y])==1:
        data[x][y]=3
        cv2.rectangle(img,(x,y),(x,y),(0,0,0),-1)
def grow():
    for x in range(1024):
        data[x][-1]=int(data[x][1023])
        data[x][1024]=int(data[x][0])
        data[-1][x]=int(data[1023][x])
        data[1024][x]=int(data[0][x])
    for x in range(1024):
        for y in range(1024):
            develop(x,y)
    for x in range(1024):
        for y in range(1024):
            if data[x][y]==2:
                data[x][y]=1
            if data[x][y]==3:
                data[x][y]=0
for x in range(1024):
    for y in range(1024):
        if int(data[x][y])==1:
            cv2.rectangle(img,(x,y),(x,y),(255,255,255),-1)
        if int(data[x][y])==0:
            cv2.rectangle(img,(x,y),(x,y),(0,0,0),-1)
g=0
while(True):
    #cv2.imshow('image',img):
    grow()
    g+=1
    print(g)
    '''if cv2.waitKey(1)&0xFF==27:
        break'''
    cv2.imwrite('Game.jpg',img)
#cv2.destroyAllWindows()

