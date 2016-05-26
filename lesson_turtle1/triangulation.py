from turtle import *
from math import *
innerangles=[45,85,50]
turnangles=[180-45,180-85,180-50]
length=[sin(radians(85)),sin(radians(50)),sin(radians(45))]
for i in range(3):
   fd(100*length[i])
   lt(turnangles[i])
