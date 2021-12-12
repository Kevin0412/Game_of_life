import random
File=open("game.csv","w")
for x in range(1024):
    for y in range(1024):
        if x==511 and y<512 or x==512 and y>511 or y==511 and x>511 or y==512 and x<512:
            File.write('1,')
        else:
            File.write('0,')
    File.write('\n')
File.close()
