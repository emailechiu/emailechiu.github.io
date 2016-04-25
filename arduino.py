from time import sleep
from pyfirmata import Arduino,util
board = Arduino('/dev/ttyUSB0')
#board.digital[2].write(0)
#print(board.digital[2].read())
board.digital[2].write(1)
board.digital[3].write(1)
board.digital[4].write(1)
for i in range(20):
   print(board.digital[2].read())
   sleep(1)


