#!/usr/bin/python3
from pi3d import *

display=Display.create(x=100,y=100)
display.set_background(0,0,0,1)
ball=Sphere(z=10)
#ball.set_material((1,0,0))
shader=Shader('uv_light')
texture=Texture('worldmap.png')
texture1=Texture('worldmap1.png')
texture2=Texture('worldmap2.png')
while display.loop_running():
	ball.draw(shader,[texture,texture1,texture2])
