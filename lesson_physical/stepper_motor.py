#!/usr/bin/python3
 
# import required libs
import time
import RPi.GPIO as GPIO

GPIO.cleanup() #cleaning up in case GPIOS have been preactivated
 
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
 
# be sure you are setting pins accordingly
# GPIO10,GPIO9,GPIO11,GPI25
StepPins = [10,9,11,25]
 
# Set all pins as output
for pin in StepPins:
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)

#wait some time to start
time.sleep(0.5)
 
# Define some settings
StepCounter = 0
WaitTime = 0.0015
 
# Define simple sequence
StepCount1 = 4
Seq1 = []
#Seq1 = range(0, StepCount1)
#Seq1[0] = [1,0,0,0]
#Seq1[1] = [0,1,0,0]
#Seq1[2] = [0,0,1,0]
#Seq1[3] = [0,0,0,1]
Seq1.append([1,0,0,0])
Seq1.append([0,1,0,0])
Seq1.append([0,0,1,0])
Seq1.append([0.0,0,1])
 
 
# set
Seq = Seq1
StepCount = StepCount1
 
# Start main loop
try:
  while 1==1:
    for pin in range(0, 4):
      xpin = StepPins[pin]
      if Seq[StepCounter][pin]!=0:
        print(" Step ", StepCounter ,"Enable" ,xpin)
        GPIO.output(xpin, True)
      else:
        GPIO.output(xpin, False)
    StepCounter += 1

  # If we reach the end of the sequence
  # start again
    if (StepCounter==StepCount):
      StepCounter = 0
    if (StepCounter<0):
      StepCounter = StepCount
 
  # Wait before moving on
    time.sleep(WaitTime)
except:
  GPIO.cleanup();
finally: #cleaning up and setting pins to low again (motors can get hot if you wont) 
  GPIO.cleanup();
  GPIO.setmode(GPIO.BCM)
  for pin in StepPins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin, False)

