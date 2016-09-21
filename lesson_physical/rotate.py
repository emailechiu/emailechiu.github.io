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
light=pi3d.Light((0,0,-5),(0,0,5))
cam = pi3d.Camera.instance()
cam.position((10, 10, -10))
cam.point_at((0, 0, 0))
cam2d = pi3d.Camera(is_3d=False)
texture1=pi3d.Texture("worldmap.jpg")
texture2=pi3d.Texture("worldmap2.png")
texture3=pi3d.Texture("worldmap1.png")
shader = pi3d.Shader("uv_flat")
model = pi3d.Model( file_string="apollo-soyuz.obj",name="model", x=0, y=0, z=0, sx=0.5, sy=0.5, sz=0.5)
#model = pi3d.Model(file_string="models/teapot.obj",camera=cam,sx=2,sy=2,sz=2)
#model.set_draw_details(shader,[texture2,texture1])
model.set_shader(shader)
keyb = pi3d.Keyboard()
#model=pi3d.Sphere(z=0,sx=4,sy=4,sz=4)
#model=pi3d.Cuboid(4,5,6)
compass = gyro = accel = True
if sense!=0: sense.set_imu_config(compass, gyro, accel)

#yaw_offset = 72
#model.rotateToZ(-22.5)
while display.loop_running():
    try: 
        o = sense.get_orientation_radians()
        if o is None:
            pass

        pitch = o["pitch"]
        roll = o["roll"]
        yaw = o["yaw"]
    except:
        yaw =math.radians(-45) #around y axis
        pitch =math.radians(0) #around x axis
        roll =math.radians(-20) #around z axis vertical
        #yaw=int(input('yaw= ') )
        #pitch=int(input('pitch= ') )
        #roll=int(input('roll= ') )
    
    yaw_total=yaw
    sin_y = math.sin(yaw_total)
    cos_y = math.cos(yaw_total)

    sin_p = math.sin(pitch)
    cos_p = math.cos(pitch)

    sin_r = math.sin(roll)
    cos_r = math.cos(roll)

    abs_roll = math.degrees(math.asin(sin_p * cos_y + cos_p * sin_r * sin_y))
    #if abs_roll<0: abs_roll=180-abs_roll
    abs_pitch = math.degrees(math.asin(sin_p * sin_y - cos_p * sin_r * cos_y))
    #if abs_pitch<0: abs_roll=180-abs_pitch

    model.rotateToY(math.degrees(yaw_total))
    model.rotateToZ(abs_roll)
    model.rotateToX(abs_pitch)
    #mytext=str(round(abs_roll,2))+" "+str(round(abs_pitch,2))+ " "+str(round(math.degrees(yaw_total),2))
    mytext=str(round(math.degrees(roll),2))+" "+str(round(math.degrees(pitch),2))+ " "+str(round(math.degrees(yaw),2))
    str1=pi3d.FixedString('fonts/FreeSans.ttf',mytext,camera=cam2d,background_color=(200,140,20,235), font_size=32,shader=pi3d.Shader('uv_flat') ,f_type='SMOOTH')
    str1.sprite.positionX(-300) 
    str1.draw()
    model.draw(shader,[texture2])
    sleep(0.1)
    keypress = keyb.read()
    #try:
    #   sense.setpixel 
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
