import cv2
import numpy as np
import time
import random
video = cv2.VideoWriter("game_between_USSR&NAZI_3.mp4", cv2.VideoWriter_fourcc('I', '4', '2', '0'), 30,(4320,2160))#储存为视频，4K分辨率
img=cv2.imread("USSR.jpg")#读取苏联旗
img=cv2.resize(img,(180,180))
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
USSR=cv2.inRange(hsv,(11,0,0),(34,255,255))#保留核心部分
img=cv2.imread("NAZI.jpg")#读取纳粹旗
img=cv2.resize(img,(180,180))
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
NAZI=cv2.inRange(hsv,(0,0,0),(180,255,46))#保留核心部分
img2=np.zeros((360,180), np.int16)#记录各个格子变化的时刻，正负表示不同的变化
img3=np.zeros((360,180), np.int16)#记录各个格子多久没发生变化
img4=np.zeros((360,180), np.int16)#记录各个格子由那种细胞控制
showcells=True#是否显示细胞
'''h=open("game.csv")
H=h.read()
Hh=H.split("\n")
data=[]
for row in Hh:
    data.append(row.split(","))
    time.sleep(0.01)'''
data=[]#生命游戏计算用的是这个列表
#f=[]
#e=[]
'''for y in range(256):
    if 0==random.randint(0,1):
        f.append(1)
        e.append(1)
    else:
        f.append(0)
        e.append(1)'''
for y in range(180):
    d=[]
    for x in range(180):
        if USSR[x][y]==255:
            d.append(1)
        else:
            d.append(0)
    data.append(d)
for y in range(180):
    d=[]
    for x in range(180):
        if NAZI[x][y]==255:
            d.append(-1)
        else:
            d.append(0)
    data.append(d)#读入二旗
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
def develop(x,y):#对(x,y)坐标上的细胞进行计算
    #data中标记生死：
    #0 已死
    #±1 活
    #±2 分娩
    #±3 将死
    cell=0
    for a in range(3):
        for b in range(3):
            c=x+a-1
            d=y+b-1
            if c==360:
                c=0
            if c==-1:
                c=359
            if d==180:
                d=179
                c+=180
                c=c%360
            if d==-1:
                d=0
                c+=180
                c=c%360
            if int(data[c][d])==1 or int(data[c][d])==3:
                cell+=1
            if int(data[c][d])==-1 or int(data[c][d])==-3:
                cell-=1
    if int(data[x][y])==1:
        cell-=1
    if int(data[x][y])==-1:
        cell+=1
    #变量cell计细胞数
    if cell==3 and int(data[x][y])==0:#正三且死，正生
        data[x][y]=2
    if cell!=2 and cell!=3 and int(data[x][y])==1:#非正二三且正活，正死
        data[x][y]=3
    if cell==-3 and int(data[x][y])==0:#负三且死，负生
        data[x][y]=-2
    if cell!=-2 and cell!=-3 and int(data[x][y])==-1:#非负二三且负活，负死
        data[x][y]=-3
def color(n,m,o):#颜色处理函数，hsv模型，n为颜色值（正负表示生和死），m为颜色深浅，o表示该格之前由那种细胞控制
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
def grow(n):#下一代细胞
    for x in range(360):
        for y in range(180):
            if int(data[x][y])==2 or int(data[x][y])==-3:
                img3[x][y]=0
                if int(data[x][y])==2:
                    data[x][y]=1
                    if showcells:
                        img2[x][y]=-n-1
                    else:
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
                    if showcells:
                        img2[x][y]=n+1
                    else:
                        img2[x][y]=-n-1
                    data[x][y]=-1
                    img4[x][y]=-1
            else:
                img3[x][y]+=1
    for x in range(360):#先记录后发展
        for y in range(180):
            develop(x,y)
g=0
hsv=np.zeros((2160,4320,3), np.uint8)#写入的图片
#while(True):
for g in range(180*44):
    grow(g)
    g+=1
    for x in range(360):
        for y in range(180):
            m=int((img3[x][y])/g*256)#计算没变化的时间占比，换算为深度
            cv2.rectangle(hsv,(x*12,y*12),(x*12+11,y*12+11),color(int(img2[x][y]/g*180+0.5),m,img4[x][y]),-1)#在hsv上记录数据
    print(g)
    img=cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)#hsv到bgr
    video.write(img)#视频写入图片
    imgp=cv2.resize(img,(720,360))#缩小后方便显示
    cv2.imshow('image',imgp)#显示
    if g%180==0:
        q=1
        img=cv2.imread("game_"+str(q)+".bmp")
        while isinstance(img,np.ndarray):
            q=q+1
            img=cv2.imread("game_"+str(q)+".bmp")
        img=cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
        cv2.imwrite("game_"+str(q)+".bmp",img)#保存关键帧
    if cv2.waitKey(1)&0xFF==27:
        break
video.release()
cv2.destroyAllWindows()
