import cv2
import numpy as np
import time
import random
img=cv2.imread('communist_party.jpeg')
img=cv2.resize(img,(1024,1024))
img=cv2.inRange(img,(0,0,0),(200,255,255))
#video = cv2.VideoWriter("game.mp4", cv2.VideoWriter_fourcc('I', '4', '2', '0'), 8,(2160,2160))
'''h=open("game.csv")
H=h.read()
Hh=H.split("\n")
data=[]
for row in Hh:
    data.append(row.split(","))
    time.sleep(0.01)'''
data=np.zeros((2340,2340), np.uint8)
data[658:1682,658:1682]=img
imgp=cv2.resize(data,(1024,1024))
cv2.imshow('img',imgp)
cv2.waitKey(0)
img=np.zeros((2340,2340),np.uint8)
imgp=cv2.resize(img,(1024,1024))
#f=[]
#e=[]
'''for y in range(256):
    if 0==random.randint(0,1):
        f.append(1)
        e.append(1)
    else:
        f.append(0)
        e.append(1)'''
'''for x in range(2160):
    d=[]
    for y in range(2160):
        if  x==y or x+y==539 or x-y==2 and y<269 or x+y==541 and y<271 or x-y==-2 and y>270 or x+y==537 and y>268:
            d.append(1)
        else:
            d.append(0)
    data.append(d)'''
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
            if int(data[c][d])==255 or int(data[c][d])==3:
                cell+=1
    if int(data[x][y])==255:
        cell-=1
    if cell==3 and int(data[x][y])==0:
        data[x][y]=2
    if cell!=2 and cell!=3 and int(data[x][y])==255:
        data[x][y]=3
def grow(n):
    for x in range(2340):
        for y in range(2340):
            if int(data[x][y])==255 or int(data[x][y])==2:
                cv2.rectangle(img,(4*x,4*y),(4*x+2,4*y+2),255,-1)
                data[x][y]=255
            else:
                cv2.rectangle(img,(4*x,4*y),(4*x+2,4*y+2),0,-1)
                data[x][y]=0
    for x in range(2,2338):
        if 2 in data[x] or 3 in data[x] or 255 in data[x] or 2 in data[x-1] or 3 in data[x-1] or 255 in data[x-1] or 2 in data[x+1] or 3 in data[x+1] or 255 in data[x+1]:
            for y in range(2,2338):
                develop(x,y)
for g in range(256):
    print(g)
    grow(g)
    imgp=cv2.resize(img,(1024,1024))
    cv2.imshow('img',imgp)
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
