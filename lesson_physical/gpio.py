from RPi import GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
#GPIO.setup(17,GPIO.OUT,1)

GPIO.setup(36,GPIO.OUT)
GPIO.output(36,1)
for i in range(20):
   GPIO.output(36,i%2)
   sleep(1)


