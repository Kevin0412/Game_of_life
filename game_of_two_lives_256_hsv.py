import cv2
import numpy as np
import time
import random
video = cv2.VideoWriter("game_between_USSR&NAZI.mp4", cv2.VideoWriter_fourcc('I', '4', '2', '0'), 18,(256,256))
img=cv2.imread("USSR.jpg")
img=cv2.resize(img,(256,256))
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
USSR=cv2.inRange(hsv,(11,0,0),(34,255,255))
img=cv2.imread("NAZI.jpg")
img=cv2.resize(img,(256,256))
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
NAZI=cv2.inRange(hsv,(0,0,0),(180,255,46))
img2=np.zeros((256,256), np.int16)
img3=np.zeros((256,256), np.int16)
img4=np.zeros((256,256), np.int16)
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
for x in range(256):
    d=[]
    for y in range(256):
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
def color(n,m,o):
    if o==0:
        return(0,0,127)
    elif n>0:
        if o==1:
            n=(-abs(n)+30)%180
        else:
            n=(-abs(n)-90+30)%180
        return(n,m,255)
    else:
        if o==1:
            n=(-abs(n)+30)%180
        else:
            n=(-abs(n)-90+30)%180
        return(n,255,m)
def grow(n):
    for x in range(256):
        for y in range(256):
            if int(data[x][y])==2 or int(data[x][y])==-3:
                img3[x][y]=0
                if int(data[x][y])==2:
                    data[x][y]=1
                    #img2[x][y]=-n-1
                    img2[x][y]=n+1
                    img4[x][y]=1
                else:
                    data[x][y]=0
                    img2[x][y]=-n-1
                    img4[x][y]=-1
            elif int(data[x][y])==3 or int(data[x][y])==-2:
                img3[x][y]=0
                if int(data[x][y])==3:
                    img2[x][y]=n+1
                    data[x][y]=0
                    img4[x][y]=1
                else:
                    #img2[x][y]=n+1
                    img2[x][y]=-n-1
                    data[x][y]=-1
                    img4[x][y]=-1
            else:
                img3[x][y]+=1
    for x in range(256):
        for y in range(256):
            develop(x,y)
g=0
hsv=np.zeros((256,256,3), np.uint8)
#while(True):
for g in range(180*100):
    grow(g)
    g+=1
    for x in range(256):
        for y in range(256):
            m=int((img3[x][y])/g*256)
            hsv[x][y]=color(int(img2[x][y]/g*180+0.5),m,img4[x][y])
    print(g)
    img=cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
    cv2.imshow('img',img)
    video.write(img)
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
video.release()
cv2.destroyAllWindows()
