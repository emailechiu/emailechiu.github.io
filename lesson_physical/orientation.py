#!/usr/bin/python3
from sense_hat import *
from math import *
from time import sleep
sense=SenseHat()
sense.clear()
#sense.set_pixel(0,0,255,0,0)
#roll 90->y=7, 270->y=0
#pitch 270->x=7, 90->x=0
sense.set_imu_config(False,True,False)
x=0
y=0
z=0
gx=0
gy=0
pitch_index=[3,2,1,1,0,0,0,0,7,7,7,7,6,6,5,4]
roll_index=pitch_index.copy()
roll_index.reverse()
yaw_index=[0,1,2,3,4,5,6,7,15,23,31,39,47,55,63,62,61,60,59,58,57,56,48,40,32,24,16,8]
while True:
    o=sense.get_orientation()
    a=sense.get_accelerometer()
    g=sense.get_gyroscope()
    gr=sense.get_gyroscope_raw()
    #print(o)
    #print(a)
    print(gr)
    pitch=g['pitch']
    roll=g['roll']
    yaw=g['yaw']
    if (pitch>360) | (roll>360) | (yaw>360): break
    print(round(yaw),' ',round(pitch),' ',round(roll))
    if x!=pitch_index[int(pitch//22.5)]  |y!=roll_index[int(roll//22.5)] :
        sense.set_pixel(x,y,0,0,0)
        x=pitch_index[int(pitch//22.5)]
        y=roll_index[int(roll//22.5)]
        sense.set_pixel(x,y,0,255,255)
    if z!=yaw_index[int(yaw//28)]:
        sense.set_pixel(z%8,z//8,0,0,0)
        z=yaw_index[int(yaw//28)]
        sense.set_pixel(z%8,z//8,0,255,255)

#   Gyroscopic detector
    if gx!=-int(gr['y']*8)+3 |gy!=int(gr['x']*8)+3:       
        sense.set_pixel(gx,gy,0,0,0)
        gx=-int(gr['y']*8)+3
        gy=int(gr['x']*8)+3
        if gx>7 : gx=7
        if gx<0 : gx=0
        if gy>7 : gy=7
        if gy<0 : gy=0
        sense.set_pixel(gx,gy,255,0,0)
    
 
