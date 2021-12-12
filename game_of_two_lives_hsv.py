import cv2
import numpy as np
import time
import random
k=1200
hsv=np.zeros((k*2,k*2,3), np.uint8)
img2=np.zeros((k*2,k*2), np.int16)
img3=np.zeros((k*2,k*2), np.int16)
cv2.rectangle(hsv,(0,0),(k*2,k*2),(0,0,127),-1)
video = cv2.VideoWriter("game_of_two_lives_1.mp4", cv2.VideoWriter_fourcc('I', '4', '2', '0'), 30,(2160,2160))
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
        if x==k-3 and y<k or x==k-2 and y<k or x==k-1 and y>k-1 or y==k and x<k:
            d.append(1)
        elif x==k+2 and y>k-1 or x==k+1 and y>k-1 or x==k and y<k or y==k-1 and x>k-1:
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
m=3
def color(n,m):
    if n>0:
        n=(-abs(n))%180
        #m=int(m/2+128)
        #m=255-m
        return(n,m,255)
    elif n==0:
        return(0,0,127)
    else:
        #n=(abs(n)+90)%180
        n=(-abs(n))%180
        #m=int(128-m/2)
        #m=255-m
        return(n,255,m)
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
    global m
    for x in range(k-n-2-m,k+n+2+m):
        for y in range(k-n-2-m,k+n+2+m):
            develop(x,y,n)
    '''for x in range(k-n-2-m,k+n+2+m):
        for y in range(k-n-2-m,k+n+2+m):
            if int(data[x][y])==2:
                data[x][y]=1
            if int(data[x][y])==3:
                data[x][y]=0
            if int(data[x][y])==-2:
                data[x][y]=-1
            if int(data[x][y])==-3:
                data[x][y]=0'''
    for x in range(k-n-2-m,k+n+2+m):
        for y in range(k-n-2-m,k+n+2+m):
            if int(data[x][y])==2 or int(data[x][y])==-3:
                img2[x][y]=n+1
                img3[x][y]=0
                if data[x][y]>0:
                    data[x][y]=1
                else:
                    data[x][y]=0
            elif int(data[x][y])==3 or int(data[x][y])==-2:
                img2[x][y]=-n-1
                img3[x][y]=0
                if data[x][y]<0:
                    data[x][y]=-1
                else:
                    data[x][y]=0
            else:
                img3[x][y]+=1
    '''for x in range(k-n-1-m,k+n+1+m):
        img2[x][k-n-2-m]=img2[x][k-n-1-m]
        img2[x][k+n+1+m]=img2[x][k+n+m]
        img3[x][k-n-2-m]=img3[x][k-n-1-m]
        img3[x][k+n+1+m]=img3[x][k+n+m]
    for x in range(k-n-2-m,k+n+2+m):
        img2[k-n-2-m][x]=img2[k-n-1-m][x]
        img2[k+n+1+m][x]=img2[k+n+m][x]
        img3[k-n-2-m][x]=img3[k-n-1-m][x]
        img3[k+n+1+m][x]=img3[k+n+m][x]'''
    for x in range(k-n-2-m,k+n+2+m):
        img2[x][k-n-3-m]=img2[x][k-n-2-m]
        img2[x][k+n+2+m]=img2[x][k+n+1+m]
        img3[x][k-n-3-m]=img3[x][k-n-2-m]
        img3[x][k+n+2+m]=img3[x][k+n+1+m]
        data[x][k-n-3-m]=data[x][k-n-2-m]
        data[x][k+n+2+m]=data[x][k+n+1+m]
    for x in range(k-n-3-m,k+n+3+m):
        img2[k-n-3-m][x]=img2[k-n-2-m][x]
        img2[k+n+2+m][x]=img2[k+n+1+m][x]
        img3[k-n-3-m][x]=img3[k-n-2-m][x]
        img3[k+n+2+m][x]=img3[k+n+1+m][x]
        data[k-n-3-m][x]=data[k-n-2-m][x]
        data[k+n+2+m][x]=data[k+n+1+m][x]
    '''for x in range(k-n-3-m,k+n+3+m):
        img2[x][k-n-4-m]=img2[x][k-n-3-m]
        img2[x][k+n+3+m]=img2[x][k+n+2+m]
        img3[x][k-n-4-m]=img3[x][k-n-3-m]
        img3[x][k+n+3+m]=img3[x][k+n+2+m]
    for x in range(k-n-4-m,k+n+4+m):
        img2[k-n-4-m][x]=img2[k-n-3-m][x]
        img2[k+n+3+m][x]=img2[k+n+2+m][x]
        img3[k-n-4-m][x]=img3[k-n-3-m][x]
        img3[k+n+3+m][x]=img3[k+n+2+m][x]'''
    #m+=1
for g in range(1080):
    grow(g)
    for x in range(k-m-g,k+m+g):
        for y in range(k-m-g,k+m+g):
            if abs(x-k+0.5)<abs(y-k+0.5):
                l=int(img3[x][y]/(g-int(abs(x-k+0.5))+m+1)*255)
            else:
                l=int(img3[x][y]/(g-int(abs(y-k+0.5))+m+1)*255)
            hsv[x][y]=color(int(img2[x][y]/(g+1)*180),l)
    print(g)
    img=cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
    imgo=img[k-g-1:k+g+1,k-g-1:k+g+1]
    imgp=cv2.resize(imgo,(1000,1000))
    cv2.imshow('img',imgp)
    imgp=cv2.resize(imgo,(2160,2160))
    video.write(imgp)
    #video.write(img)
    if g==479 or g==779:
        q=1
        img=cv2.imread("game_of_two_lives_colour_"+str(q)+".png")
        while isinstance(img,np.ndarray):
            q=q+1
            img=cv2.imread("game_of_two_lives_colour_"+str(q)+".png")
        cv2.imwrite("game_of_two_lives_colour_"+str(q)+".png",imgo)
    if cv2.waitKey(1)&0xFF==27:
        break
q=1
img=cv2.imread("game_of_two_lives_colour_"+str(q)+".png")
while isinstance(img,np.ndarray):
    q=q+1
    img=cv2.imread("game_of_two_lives_colour_"+str(q)+".png")
cv2.imwrite("game_of_two_lives_colour_"+str(q)+".png",imgo)
cv2.destroyAllWindows()
video.release()
#cv2.destroyAllWindows()
'''
100000
010100
001000
000100
001010
000001
'''
