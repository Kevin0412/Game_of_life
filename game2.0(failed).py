import cv2
import numpy as np
import random
img=np.zeros((1024,1024),np.uint8)
for x in range(1024):
    for y in range(1024):
        if 0==random.randint(0,3):
            img[x][y]=255
for g in range(100):
    cv2.imshow('img',img)
    cv2.waitKey(0)
    imgo=cv2.blur(img,(3,3))
    alive=cv2.inRange(img,255,255)
    cell3=cv2.inRange(imgo,84,86)
    '''cv2.imshow('img',cell3)
    cv2.waitKey(0)'''
    cell4=cv2.inRange(imgo,112,114)
    '''cv2.imshow('img',cell4)
    cv2.waitKey(0)'''
    new_generation=cell3+~(~cell4+~alive)
    img=new_generation
