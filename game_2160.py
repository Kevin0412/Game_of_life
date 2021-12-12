import cv2
import numpy as np
import time
import random
img=np.zeros((2160,2160), np.uint8)
video = cv2.VideoWriter("game.mp4", cv2.VideoWriter_fourcc('I', '4', '2', '0'), 8,(2160,2160))
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
        if  x==y or x+y==2159 or x-y==2 and y<1079 or x+y==2161 and y<1081 or x-y==-2 and y>1080 or x+y==2157 and y>1078:
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
    for x in range(1077-n,1083+n):
        if 2 in data[x] or 3 in data[x]:
            for y in range(1077-n,1083+n):
                if int(data[x][y])==1 or int(data[x][y])==2:
                    img[x][y]=255
                    data[x][y]=1
                else:
                    img[x][y]=0
                    data[x][y]=0
    for x in range(1077-n,1083+n):
        for y in range(1077-n,1083+n):
            develop(x,y)
for x in range(2160):
    for y in range(2160):
        if int(data[x][y])==1 or int(data[x][y])==2:
            img[x][y]=255
            data[x][y]=1
        else:
            img[x][y]=0
            data[x][y]=0
for g in range(1024):
    grow(g)
    print(g)
    imgo=img[540:1620,540:1620]
    cv2.imshow('img',imgo)
    video.write(img)
    if cv2.waitKey(1)&0xFF==27:
        break
cv2.imwrite("game.bmp",img)
video.release()
cv2.destroyAllWindows()
'''
100000
010100
001000
000100
001010
000001
'''
