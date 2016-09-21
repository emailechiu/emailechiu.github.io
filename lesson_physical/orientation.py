from sense_hat import *
from math import *
sense=SenseHat()
sense.clear()
#sense.set_pixel(0,0,255,0,0)
#roll 90->y=7, 270->y=0
#pitch 270->x=7, 90->x=0
#sense.set_imu_config(False,True,False)
while True:
    o=sense.get_orientation_degrees()
    #print(o)
    pitch=o['pitch']
    roll=o['roll']
    yaw=o['yaw']
    sense.set_pixel(4+floor((pitch-180)/45),3,255,0,0)
    sense.set_pixel(3,3-floor((pitch-180)/45),0,0,255)
    print(round(yaw),' ',round(pitch),' ',round(roll))
    if (pitch>360) | (roll>360) | (yaw>360): break

