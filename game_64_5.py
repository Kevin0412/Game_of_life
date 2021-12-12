import cv2
import numpy as np
import time
import random
from mido import Message, MidiFile, MidiTrack
def play_note(note, length, track, base_num=0, delay=0, velocity=1.0, channel=0):
    meta_time = 60 * 60 * 10 / bpm
    major_notes = [0, 2, 2, 1, 2, 2, 2, 1]
    base_note = 60
    track.append(
        Message('note_on', note=base_note + base_num * 12 + sum(major_notes[0:note]), velocity=round(64 * velocity),
                time=round(delay * meta_time), channel=channel))
    track.append(
        Message('note_off', note=base_note + base_num * 12 + sum(major_notes[0:note]), velocity=round(64 * velocity),
                time=round(meta_time * length), channel=channel))
img=np.zeros((64,64,3), np.uint8)
'''h=open("game.csv")
H=h.read()
Hh=H.split("\n")
data=[]
for row in Hh:
    data.append(row.split(","))
    time.sleep(0.01)'''
data=[]
for x in range(64):
    '''d=[]
    for y in range(64):
        if 0==random.randint(0,y):
            d.append(1)
        else:
            d.append(0)
    data.append(d)'''
    '''d=[]
    if x==32 or x==31:
        for y in range(64):
            if y==0 or y==63:
                d.append(1)
            else:
                d.append(1) 
    else:
        for y in range(64):
            if y==31 or y==32:
                d.append(1)
            else:
                d.append(0)'''
    d=[]
    for y in range(64):
        if x==31 and y<32 or x==32 and y>31 or y==31 and x>31 or y==32 and x<32:
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
            if c==64:
                c=0
            if c==-1:
                c=63
            if d==64:
                d=0
            if d==-1:
                d=63
            if int(data[c][d])==1 or int(data[c][d])==3:
                cell+=1
    if int(data[x][y])==1:
        cell-=1
    if cell==3 and int(data[x][y])==0:
        data[x][y]=2
        cv2.rectangle(img,(x,y),(x,y),(255,255,255),-1)
    if cell!=2 and cell!=3 and int(data[x][y])==1:
        data[x][y]=3
        cv2.rectangle(img,(x,y),(x,y),(0,0,0),-1)
def grow():
    for x in range(64):
        for y in range(64):
            develop(x,y)
    b=0
    d=0
    for x in range(64):
        for y in range(64):
            if data[x][y]==2:
                data[x][y]=1
                b+=1
            if data[x][y]==3:
                data[x][y]=0
                d+=1
    print(b,d)
    play_note(b%7+1, 1, track)
    for x in range(64):
        for y in range(64):
            if int(data[x][y])==1:
                cv2.rectangle(img,(x,y),(x,y),(255,255,255),-1)
            if int(data[x][y])==0:
                cv2.rectangle(img,(x,y),(x,y),(0,0,0),-1)
g=0
mid = MidiFile()  # 创建MidiFile对象
track = MidiTrack()  # 创建音轨
mid.tracks.append(track)  # 把音轨加到MidiFile对象中
bpm = 75
# 向音轨添加
#    Message对象（包括program_change、note_on、note_off等）
#    MetaMessage对象（用以表示MIDI文件的节拍、速度、调式等属性）
track.append(Message('program_change', program=12, time=0))
track.append(Message('note_on', note=64, velocity=64, time=32))
track.append(Message('note_off', note=64, velocity=127, time=32))
while(True):
    cv2.imshow('image',img)
    grow()
    g+=1
    print(g)
    if cv2.waitKey(1)&0xFF==27:
        cv2.imwrite('Game.jpg',img)
        break
cv2.destroyAllWindows()
mid.save('new_song.mid')
