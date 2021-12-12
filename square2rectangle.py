import cv2
import numpy as np
img=cv2.imread('game_of_two_lives_colour_36_1.png')
imgo=np.zeros((img.shape[1],img.shape[0]*2,3),np.uint8)
for x in range(img.shape[1]):
    for y in range(img.shape[0]):
        imgo[x][y+int(img.shape[0]*10/13)]=img[x][y]
        imgo[x][y-int(img.shape[0]*3/13)]=img[x][y]
    print(x)
cv2.imwrite('game_of_two_lives_colour_36_2.png',imgo)
