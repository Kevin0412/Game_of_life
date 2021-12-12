import cv2
import numpy as np
import time
import random
video = cv2.VideoWriter("game_between_USSR&NAZI_2.mp4", cv2.VideoWriter_fourcc('I', '4', '2', '0'), 18,(256,256))
img=cv2.imread("USSR.jpg")
img=cv2.resize(img,(256,256))
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
USSR=cv2.inRange(hsv,(11,0,0),(34,255,255))
img=cv2.imread("NAZI.jpg")
img=cv2.resize(img,(256,256))
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
NAZI=cv2.inRange(hsv,(0,0,0),(180,255,46))
img=np.ones((256,256,3),np.uint8)*127
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
for y in range(256):
    d=[]
    for x in range(256):
        if USSR[x][y]==255 and NAZI[x][y]==0:
            d.append(1)
        elif USSR[x][y]==0 and NAZI[x][y]==255:
            d.append(-1)
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
            if c==256:
                c=0
            if c==-1:
                c=255
            if d==256:
                d=0
            if d==-1:
                d=255
            if int(data[c][d])==1 or int(data[c][d])==3:
                cell+=1
            if int(data[c][d])==-1 or int(data[c][d])==-3:
                cell-=1
    if int(data[x][y])==1:
        cell-=1
    if int(data[x][y])==-1:
        cell+=1
    if cell==3 and int(data[x][y])==0:
        data[x][y]=2
    if cell!=2 and cell!=3 and int(data[x][y])==1:
        data[x][y]=3
    if cell==-3 and int(data[x][y])==0:
        data[x][y]=-2
    if cell!=-2 and cell!=-3 and int(data[x][y])==-1:
        data[x][y]=-3
def grow():
    for x in range(256):
        for y in range(256):
            develop(x,y)
    for x in range(256):
        for y in range(256):
            if int(data[x][y])==2:
                data[x][y]=1
            if int(data[x][y])==3:
                data[x][y]=0
            if int(data[x][y])==-2:
                data[x][y]=-1
            if int(data[x][y])==-3:
                data[x][y]=0
    for x in range(256):
        for y in range(256):
            if int(data[x][y])==1:
                cv2.rectangle(img,(x,y),(x,y),(255,255,255),-1)
            if int(data[x][y])==-1:
                cv2.rectangle(img,(x,y),(x,y),(0,0,0),-1)
            if int(data[x][y])==0:
                cv2.rectangle(img,(x,y),(x,y),(127,127,127),-1)
for x in range(256):
    for y in range(256):
        if int(data[x][y])==1:
            cv2.rectangle(img,(x,y),(x,y),(255,255,255),-1)
        if int(data[x][y])==-1:
            cv2.rectangle(img,(x,y),(x,y),(0,0,0),-1)
        if int(data[x][y])==0:
            cv2.rectangle(img,(x,y),(x,y),(127,127,127),-1)
g=0
#while(True):
for g in range(180*9):
    cv2.imshow('image',img)
    video.write(img)
    grow()
    g+=1
    print(g)
    if cv2.waitKey(1)&0xFF==27:
        cv2.imwrite('Game2.bmp',img)
        break
video.release()
cv2.destroyAllWindows()
