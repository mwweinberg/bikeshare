import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)
#this is necessary because once it opens up the serial port arduino needs a second
time.sleep(1)

choice= raw_input("1 or 2?")


if choice == "1":

    while True:

        ser.write('H')

        time.sleep(3)

        print "hi"

elif choice == "2":

    while True:

        ser.write('L')

        time.sleep(3)

else:
    print "nope"
