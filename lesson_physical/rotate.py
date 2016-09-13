#!/usr/bin/python3
from sense_hat import SenseHat
import math
import pi3d
from time import sleep
pitch=0
roll=0
yaw=0
try:
    sense = SenseHat()
except:
    sense=0

display = pi3d.Display.create()
cam = pi3d.Camera.instance()
cam.position((0, 20, 0))
cam.point_at((0, -1, 40))
texture1=pi3d.Texture("./worldmap1.png")
texture2=pi3d.Texture("./worldmap2.png")
shader = pi3d.Shader("mat_light")
#model = pi3d.Model( file_string="apollo-soyuz.obj",name="model", x=0, y=-1, z=40, sx=1, sy=1, sz=1)
model = pi3d.Model( file_string="teapot.obj",name="model", x=0, y=-1, z=40, sx=1, sy=1, sz=1)
#model.set_shader(shader)
#model.set_textures([texture1,texture2])
keyb = pi3d.Keyboard()

compass = gyro = accel = True
if sense!=0: sense.set_imu_config(compass, gyro, accel)

yaw_offset = 72

while display.loop_running():
    try: 
        o = sense.get_orientation_radians()
        if o is None:
            pass

        pitch = o["pitch"]
        roll = o["roll"]
        yaw = o["yaw"]
    except:
        pitch += 1
        roll += 1
        yaw +=1 

    yaw_total = yaw + math.radians(yaw_offset)

    sin_y = math.sin(yaw_total)
    cos_y = math.cos(yaw_total)

    sin_p = math.sin(pitch)
    cos_p = math.cos(pitch)

    sin_r = math.sin(roll)
    cos_r = math.cos(roll)

    abs_roll = math.degrees(math.asin(sin_p * cos_y + cos_p * sin_r * sin_y))
    abs_pitch = math.degrees(math.asin(sin_p * sin_y - cos_p * sin_r * cos_y))

    model.rotateToZ(abs_roll)
    model.rotateToX(abs_pitch)
    model.rotateToY(math.degrees(yaw_total))
    model.draw()
    sleep(1)
    keypress = keyb.read()

    if keypress == 27:
        keyb.close()
        display.destroy()
        break
    elif keypress == ord('m'):
        compass = not compass
        if sense!=0: sense.set_imu_config(compass, gyro, accel)
    elif keypress == ord('g'):
        gyro = not gyro
        if sense!=0: sense.set_imu_config(compass, gyro, accel)
    elif keypress == ord('a'):
        accel = not accel
        if sense!=0: sense.set_imu_config(compass, gyro, accel)
    elif keypress == ord('='):
        yaw_offset += 1
    elif keypress == ord('-'):
        yaw_offset -= 1
