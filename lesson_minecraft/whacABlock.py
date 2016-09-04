from mcpi.minecraft import *
from mcpi.block import *
from random import *
from time import *
mc = Minecraft.create()
mc.postToChat("Minecraft Whac-a-Block")
mc.postToChat("Get ready ...")
mc.postToChat("Go")
mc.player.setPos(-10,0,10)
pos=mc.player.getTilePos()
mc.postToChat(pos)
mc.saveCheckpoint()
#What is around me?
(x,y,z)=mc.player.getTilePos()
mc.setBlocks(x-1,y,z+2,x+1,y+3,z+2,STONE)
blocksLit=0
points=0
while blocksLit<12:
    sleep(1)  
    (xPos,yPos,zPos)=(x+randint(-1,1),y+randint(0,3),z+2)
    print(blocksLit,points,xPos,yPos,zPos)
    if mc.getBlock(xPos,yPos,zPos)==STONE.id:
        mc.setBlock(xPos,yPos,zPos,GLOWSTONE_BLOCK)
        blocksLit+=1
    for hitBlock in mc.events.pollBlockHits():
        pos=hitBlock.pos
        if mc.getBlock(pos.x,pos.y,pos.z)==GLOWSTONE_BLOCK.id:       
            mc.setBlock(pos.x,pos.y,pos.z,STONE)
            blocksLit-=1
            points+=1
            print(blocksLit,points)
            mc.postToChat(points)
mc.postToChat("Game Over, You Earned")
