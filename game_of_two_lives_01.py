import cv2
import numpy as np
import time
import random
k=270
img=np.zeros((k*2,k*2), np.uint8)
#video = cv2.VideoWriter("game.mp4", cv2.VideoWriter_fourcc('I', '4', '2', '0'), 8,(2160,2160))
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
for x in range(k*2):
    d=[]
    for y in range(k*2):
        #if  x==y or x+y==539 or x-y==2 and y<269 or x+y==541 and y<271 or x-y==-2 and y>270 or x+y==537 and y>268:
        if x==k-2 or x==k-1 and y<k-2 or y==k-1 and x<k-1:
            d.append(1)
        elif x==k+1 or x==k and y>k+1 or y==k and x>k:
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
m=2
def develop(x,y,n):
    cell=0
    for a in range(3):
        for b in range(3):
            c=x+a-1
            d=y+b-1
            if c==k-3-n-m or c==k-2-n-m:
                c=k-n-1-m
            if d==k-3-n-m or d==k-2-n-m:
                d=k-n-1-m
            if c==k+n+2+m or c==k+n+1+m:
                c=k+n+m
            if d==k+n+2+m or d==k+n+1+m:
                d=k+n+m
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
def grow(n):
    for x in range(k-n-2-m,k+n+2+m):
        for y in range(k-n-2-m,k+n+2+m):
            develop(x,y,n)
    for x in range(2*k):
        for y in range(2*k):
            if int(data[x][y])==2:
                data[x][y]=1
            if int(data[x][y])==3:
                data[x][y]=0
            if int(data[x][y])==-2:
                data[x][y]=-1
            if int(data[x][y])==-3:
                data[x][y]=0
    for x in range(2*k):
        for y in range(2*k):
            if int(data[x][y])==1:
                cv2.rectangle(img,(x,y),(x,y),(255,255,255),-1)
            if int(data[x][y])==-1:
                cv2.rectangle(img,(x,y),(x,y),(0,0,0),-1)
            if int(data[x][y])==0:
                cv2.rectangle(img,(x,y),(x,y),(127,127,127),-1)
for g in range(256):
    grow(g)
    print(g)
    cv2.imshow('img',img)
    #video.write(img)
    if cv2.waitKey(1)&0xFF==27:
        break
#video.release()
#cv2.destroyAllWindows()
'''
100000
010100
001000
000100
001010
000001
'''
