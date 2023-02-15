import pyfirmata
import time

pin1 = 11
pin2 = 12
pin3 = 13
port = 'COM4'
board = pyfirmata.Arduino(port)

#看到人臉1
board.digital[pin1].write(1)

#看到人臉2
board.digital[pin2].write(1)

#看到人臉3
board.digital[pin3].write(1)
