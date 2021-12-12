import cv2
import numpy as np
import time
import random
img=np.zeros((2400,2400,3), np.uint8)
img2=np.zeros((2400,2400), np.int16)
#video = cv2.VideoWriter("game_colour_7.mp4", cv2.VideoWriter_fourcc('I', '4', '2', '0'), 8,(2160,2160))
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
for x in range(2400):
    d=[]
    for y in range(2400):
        if x==1199 or x==1200 or y==1199 or y==1200:
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
def color(n):
    if n>0:
        n=n-1
        if int((n%765)/255)==0:
            return(255-n%255,n%255,255)
        if int((n%765)/255)==1:
            return(n%255,255,255-n%255)
        if int((n%765)/255)==2:
            return(255,255-n%255,n%255)
    else:
        '''n=abs(n)-1
        if int((n%765)/255)==0:
            return(n%255,255-n%255,0)
        if int((n%765)/255)==1:
            return(255-n%255,0,n%255)
        if int((n%765)/255)==2:
            return(0,n%255,255-n%255)'''
        return(0,0,0)
def grow(n):
    for x in range(1197-n,1200):
        if 2 in data[x] or 3 in data[x]:
            for y in range(11977-n,1200):
                if int(data[x][y])==2:
                    img2[x][y]=n+1
                    img2[y][2399-x]=n+1
                    img2[2399-y][x]=n+1
                    img2[2399-x][2399-y]=n+1
                    data[x][y]=1
                    data[y][2399-x]=1
                    data[2399-y][x]=1
                    data[2399-x][2399-y]=1
                elif int(data[x][y])==3:
                    img2[x][y]=-n-1
                    img2[y][2399-x]=-n-1
                    img2[2399-y][x]=-n-1
                    img2[2399-x][2399-y]=-n-1
                    data[x][y]=0
                    data[y][2399-x]=0
                    data[2399-y][x]=0
                    data[2399-x][2399-y]=0
    for x in range(1198-n,1202+n):
        data[1196-n][x]=data[1197-n][x]
        data[1204-n][x]=data[1203-n][x]
        data[x][1196-n]=data[x][1197-n]
        data[x][1204-n]=data[x][1203-n]
    for x in range(1197-n,1200):
        for y in range(1197-n,1200):
            develop(x,y)
for x in range(2400):
    for y in range(2400):
        if int(data[x][y])==1 or int(data[x][y])==2:
            img2[x][y]=1
            data[x][y]=1
        else:
            img2[x][y]=-1
            data[x][y]=0
k=0
for g in range(1,481+k):
    grow(g)
    for x in range(1198-g,1200):
        for y in range(1198-g,1200):
            if img2[x][y]<g:
                img[x][y]=color(int(img2[x][y]/(g+1)*765))
                img[y][2399-x]=img[x][y]
                img[2399-y][x]=img[x][y]
                img[2399-x][2399-y]=img[x][y]
    print(g)  
    if g>k:
        imgo=img[1200+k-g:1200-k+g,1200+k-g:1200-k+g]
        imgp=cv2.resize(imgo,(1000,1000))
        cv2.imshow('img',imgp)
        #imgp=cv2.resize(imgo,(2160,2160))
        #video.write(imgp)
    if cv2.waitKey(1)&0xFF==27:
        break
cv2.imwrite("game_colour_12.bmp",imgo)
#video.release()
cv2.destroyAllWindows()
'''
100000
010100
001000
000100
001010
000001
'''
