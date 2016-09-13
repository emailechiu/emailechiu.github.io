from mcpi.minecraft import Minecraft
from mcpi import block
from math import *
mc=Minecraft.create()
x,y,z=mc.player.getPos()
mc.camera.setNormal()
mc.postToChat("Hello world")
if 1:
    mc.player.setPos(-3,0,-3)
    size=3
    for x in range(size):
        for z in range(size):
            if (x-size/2)**2 + (z-size/2)**2<=(size/2)**2:
                print(x,z)
                mc.setBlock(x,20,z,47)
    mc.player.setPos(x,y,z)



