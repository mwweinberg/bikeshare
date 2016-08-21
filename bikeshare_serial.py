# from http://www.plotsofdots.com/archives/68


import xml.etree.ElementTree as ET
import urllib2
# this is for the pause
import time
import serial

# parse the data using urlib2 and xml
site='https://www.capitalbikeshare.com/data/stations/bikeStations.xml'
htm=urllib2.urlopen(site)
doc = ET.parse(htm)

# define the stations that will be identified
# note that these use the number in <id> not the <terminalName>
# if you want to use <terminalName> change 'id' in the 'for country...' loop
# to 'terminalName'

station1 = '274' # 10th & Fl
station2 = '43' # 10th & U
station3 = '242' # 12th & U
station4 = '15' # 14th & V


ser_holder = []

#opens up the serial connection with arduino
#ser = serial.Serial('/dev/ttyACM0', 9600)
#this is necessary because once it opens up the serial port arduino needs a second
time.sleep(2)





#define empty lists for the empty bikes
sID=[]
embikes=[]


# this function returns a color based on the number of bikes remaining
# each serial write needs to be specific to a station
def lighter(id, green, yellow, orange, red):
	#get the number of bikes remaining based on station id
	bk = prov[id]
	print bk
	#numbers below are GRB to sync with neopixels
	if bk >= 6:
		print "Station %s is green - 255, 0, 0" % id
		ser_holder.append(green)
	elif bk > 2:
		print "Station %s is yellow - 255, 255, 0" % id
		ser_holder.append(yellow)
	elif bk > 0:
		print "Station %s is orange - 128, 255, 0" % id
		ser_holder.append(orange)
	else:
		print "Station %s is red - 0, 255, 0" % id
		ser_holder.append(red)

# now run the function taking all of the stations as an argument
while True:

	#get the root tag
	root=doc.getroot()
	root.tag
	#use a for loop to extract the information we are interested in
	for country in root.findall('station'):
		# takes the ID as a string
		sID.append(country.find('id').text)
		# takes the number of bikes as an integer
		embikes.append(int(country.find('nbBikes').text))


	#use zip to create touples and then parse them into a dictionary
	prov=dict(zip(sID,embikes))

	#this cleans out the last loop's ser_holder variables
	ser_holder = []

	lighter(station1, 'A', 'B', 'C', 'D')
	lighter(station2, 'E', 'F', 'G', 'H')
	lighter(station3, 'I', 'J', 'K', 'L')
	lighter(station4, 'M', 'N', 'O', 'P')

	#add terminating char to ser_holder for arudino reading
	ser_holder.append('Z')

	#turns the list ser_holder into string ser_holder_str
	ser_holder_str = ''.join(ser_holder)
	#TODO: add %/n or whatever terminal character is needed
	print ser_holder
	print ser_holder_str
	#ser.write(ser_holder)
	time.sleep(10)
