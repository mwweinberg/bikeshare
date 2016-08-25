import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)
#this is necessary because once it opens up the serial port arduino needs a second
time.sleep(2)

while True:

    ser.write('L')

    time.sleep(10)
