import cv2
import numpy as np
import time
import random
img=cv2.imread("USSR.jpg")
img=cv2.resize(img,(256,256))
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img=cv2.inRange(hsv,(11,0,0),(34,255,255))
img2=np.zeros((256,256), np.int16)
img3=np.zeros((256,256), np.int16)
'''h=open("game.csv")
H=h.read()
Hh=H.split("\n")
data=[]
for row in Hh:
    data.append(row.split(","))
    time.sleep(0.01)'''
data=[]
for x in range(256):
    d=[]
    for y in range(256):
        if img[x][y]==255:
            d.append(1)
        else:
            d.append(0)
    data.append(d)
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
    if int(data[x][y])==1:
        cell-=1
    if cell==3 and int(data[x][y])==0:
        data[x][y]=2
    if cell!=2 and cell!=3 and int(data[x][y])==1:
        data[x][y]=3
def color(n,m):
    if n>0:
        n=(-abs(n)+30)%180
        return(n,m,255)
    else:
        n=(-abs(n)+30)%180
        return(n,255,m)
def grow(n):
    for x in range(256):
        for y in range(256):
            if int(data[x][y])==2:
                img2[x][y]=n+1
                img3[x][y]=0
                data[x][y]=1
            elif int(data[x][y])==3:
                img2[x][y]=-n-1
                img3[x][y]=0
                data[x][y]=0
            else:
                img3[x][y]+=1
    for x in range(256):
        '''m=x-1
        if m==-1:
            m=1023
        n=x+1
        if n==1024:
            n=0
        if 1 in data[m] or 1 in data[x] or 1 in data[n]:'''
        for y in range(256):
            develop(x,y)
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
hsv=np.zeros((256,256,3), np.uint8)
while(True):
    grow(g)
    g+=1
    for x in range(256):
        for y in range(256):
            m=int((img3[x][y])/g*256)
            hsv[x][y]=color(int(img2[x][y]/g*180),m)
    print(g)
    img=cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
    cv2.imshow('img',img)
    if g%180==0:
        q=1
        img=cv2.imread("game_"+str(q)+".bmp")
        while isinstance(img,np.ndarray):
            q=q+1
            img=cv2.imread("game_"+str(q)+".bmp")
        img=cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
        cv2.imwrite("game_"+str(q)+".bmp",img)
    if cv2.waitKey(1)&0xFF==27:
        break
    #File=open("game.csv","w")
    '''for x in range(1024):
        for y in range(1024):
            File.write(str(data[x][y]))
            File.write(',')
        File.write('\n')
    File.close()'''
