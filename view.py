from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()

pos=mc.player.getTilePos()

#mc.player.setTilePos(-8036,248,-1127)
mc.player.setTilePos(0,256,0)
time.sleep(10)
for y in range(-16,256):
    mc.player.setTilePos(0,239-y,0)
    time.sleep(0.1)
     
#mc.player.setTilePos(-8-40,248,-8+23*60+23)      
#mc.player.setTilePos(-8-10800,248,-8)
