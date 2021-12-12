import random
File=open("game.csv","w")
for x in range(2048):
    for y in range(2048):
        if x==2047 or x==0 or x==y or x+y==2047:
            File.write('1,')
        else:
            File.write('0,')
    File.write('\n')
File.close()
