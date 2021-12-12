import cv2
import numpy as np
import time
import random
hsv=np.zeros((2400,2400,3), np.uint8)
img2=np.zeros((2400,2400), np.int16)
img3=np.zeros((2400,2400), np.int16)
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
        if x==y or x+y==2399 or x-y==2 and y<1199 or x+y==2401 and y<1201 or x-y==-2 and y>1200 or x+y==2397 and y>1198:
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
def color(n,m):
    if n>0:
        n=(-abs(n))%180
        #m=int(m/2+128)
        #m=255-m
        return(n,m,255)
    else:
        #n=(abs(n)+90)%180
        n=(-abs(n))%180
        #m=int(128-m/2)
        #m=255-m
        return(n,255,m)
def grow(n):
    for x in range(1197-n,1200):
        for y in range(1197-n,1200):
            if int(data[x][y])==2:
                img2[x][y]=n+1
                img2[y][2399-x]=n+1
                img2[2399-y][x]=n+1
                img2[2399-x][2399-y]=n+1
                img3[x][y]=0
                img3[y][2399-x]=0
                img3[2399-y][x]=0
                img3[2399-x][2399-y]=0
                data[x][y]=1
                data[y][2399-x]=1
                data[2399-y][x]=1
                data[2399-x][2399-y]=1
            elif int(data[x][y])==3:
                img2[x][y]=-n-1
                img2[y][2399-x]=-n-1
                img2[2399-y][x]=-n-1
                img2[2399-x][2399-y]=-n-1
                img3[x][y]=0
                img3[y][2399-x]=0
                img3[2399-y][x]=0
                img3[2399-x][2399-y]=0
                data[x][y]=0
                data[y][2399-x]=0
                data[2399-y][x]=0
                data[2399-x][2399-y]=0
            else:
                img3[x][y]+=1
                img3[y][2399-x]+=1
                img3[2399-y][x]+=1
                img3[2399-x][2399-y]+=1
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
for g in range(1,586+k):
    grow(g)
    for x in range(1198-g,1200):
        for y in range(1198-g,1200):
            if abs(x-1199.5)>abs(y-1199.5):
                m=int(img3[x][y]/(g-int(abs(x-1199.5)+1)+3)*255)
            else:
                m=int(img3[x][y]/(g-int(abs(y-1199.5)+1)+3)*255)
            hsv[x][y]=color(int(img2[x][y]/(g+1)*180),m)
            hsv[y][2399-x]=hsv[x][y]
            hsv[2399-y][x]=hsv[x][y]
            hsv[2399-x][2399-y]=hsv[x][y]
    print(g)
    img=cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
    if g>k:
        imgo=img[1200+k-g:1200-k+g,1200+k-g:1200-k+g]
        imgp=cv2.resize(imgo,(1000,1000))
        cv2.imshow('img',imgp)
        #imgp=cv2.resize(imgo,(2160,2160))
        #video.write(imgp)
    if cv2.waitKey(1)&0xFF==27:
        break
q=1
img=cv2.imread("game_colour_"+str(q)+".bmp")
while isinstance(img,np.ndarray):
    q=q+1
    img=cv2.imread("game_colour_"+str(q)+".bmp")
cv2.imwrite("game_colour_"+str(q)+".bmp",imgo)
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
