from mcpi.minecraft import Minecraft
from mcpi import block
mc=Minecraft.create()
mc.postToChat("Hello world")
mc.player.setPos(0,0,0)
x,y,z=mc.player.getPos()
mc.player.setPos(x,y+100,z)
pos=mc.player.getPos()
#mc.postToChat(pos)
#mc.setBlock(x,y,z,block.DIAMOND_BLOCK.id)
mc.setBlock(x,y,z,block.TNT.id,1)

blockobj=mc.getBlockWithData(x,y,z)
#blocks=mc.getBlocks(x-1,y-1,z-1,x+1,y+1,z+1)
block=mc.getBlock(x,y,z)
print(block)
print(blockobj)
#print(blocks)
print(pos)
print(mc.player.getTilePos())
#direction=mc.player.getRotation()
mc.camera.setFollow(1)

#mc.getBlocks(-1,99,-1,1,101,1,1)




