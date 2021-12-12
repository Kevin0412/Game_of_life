import os
import cv2
import numpy as np

path = 'game9/'
filelist = os.listdir(path)

fps = 25 #视频每秒24帧
size = (512,512) #需要转为视频的图片的尺寸
#可以使用cv2.resize()进行修改

video = cv2.VideoWriter("game9.mp4", cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)
#视频保存在当前目录下

for item in filelist:
    if item.endswith('.jpg'): 
    #找到路径中所有后缀名为.png的文件，可以更换为.jpg或其它
        item = path + item
        print(item)
        img = cv2.imread(item)
        video.write(img)

video.release()
cv2.destroyAllWindows()
