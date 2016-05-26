import pygame,sys
from pygame.locals import *
pygame.init()
MYDISPLAY=pygame.display.set_mode((400,200))
MYDISPLAY.fill((255,255,255))
pygame.draw.line(MYDISPLAY,(0,255,0),(50,50),(100,100))
while 1:
   for event in pygame.event.get():
       if event.type==QUIT:
           pygame.quite()
           sys.exit()
   pygame.display.update()   


