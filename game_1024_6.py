import cv2
import numpy as np
import time
import random
img=cv2.imread("communist_party.jpeg")
img=cv2.resize(img,(512,512))
img=cv2.inRange(img,(0,0,0),(200,255,255))
'''h=open("game.csv")
H=h.read()
Hh=H.split("\n")
data=[]
for row in Hh:
    data.append(row.split(","))
    time.sleep(0.01)'''
data=[]
for x in range(1024):
    d=[]
    for y in range(1024):
        if x>255 and y>255 and x<768 and y<768:
            if img[x-256][y-256]==255:
                d.append(1)
            else:
                d.append(0)
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
            if c==1024:
                c=0
            if c==-1:
                c=1023
            if d==1024:
                d=0
            if d==-1:
                d=1023
            if int(data[c][d])==1 or int(data[c][d])==3:
                cell+=1
    if int(data[x][y])==1:
        cell-=1
    if cell==3 and int(data[x][y])==0:
        data[x][y]=2
    if cell!=2 and cell!=3 and int(data[x][y])==1:
        data[x][y]=3
def grow(n):
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
                if int((n%1530)/255)==0:
                    img[x,y]=(0,n%255,255)
                if int((n%1530)/255)==1:
                    img[x,y]=(0,255,255-n%255)
                if int((n%1530)/255)==2:
                    img[x,y]=(n%255,255,0)
                if int((n%1530)/255)==3:
                    img[x,y]=(255,255-n%255,0)
                if int((n%1530)/255)==4:
                    img[x,y]=(255,0,n%255)
                if int((n%1530)/255)==5:
                    img[x,y]=(255-n%255,0,255)
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
q=1
img=cv2.imread("game_"+str(q)+".bmp")
while isinstance(img,np.ndarray):
    q=q+1
    print(q)
    img=cv2.imread("game_"+str(q)+".bmp")
img=np.zeros((1024,1024,3), np.uint8)
for g in range(1530):
    grow(g)
    print(g)
    cv2.imwrite("game_"+str(q)+".bmp",img)
    #File=open("game.csv","w")
    '''for x in range(1024):
        for y in range(1024):
            File.write(str(data[x][y]))
            File.write(',')
        File.write('\n')
    File.close()'''
