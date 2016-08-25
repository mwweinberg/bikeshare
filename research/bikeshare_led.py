# original scraping from http://www.plotsofdots.com/archives/68



import xml.etree.ElementTree as ET
import urllib2
# this is for the pause
import time
import RPi.GPIO as GPIO

# parse the data using urlib2 and xml
site='https://www.capitalbikeshare.com/data/stations/bikeStations.xml'
htm=urllib2.urlopen(site)
doc = ET.parse(htm)

# Set GPIO to correct setmode and set RGB pin numbers
# will eventually need to build this out to "red1, red2, ..."
GPIO.setmode(GPIO.BOARD)
red = 17
green = 18
blue = 27

# Set pins to output mode
# will eventually need to build thi out to "red1, red2,..."
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

# may be able to pull the freq and then also pull the references in setup
Freq = 100 #Hz

# Set up and initialize all LEDs at 0
RED = GPIO.PWM(red, Freq)
RED.start(0)
GREEN = GPIO.PWM(green, Freq)
GREEN.start(0)
BLUE = GPIO.PWM(blue, Freq)
BLUE.start(0)


# define the stations that will be identified
# note that these use the number in <id> not the <terminalName>
# if you want to use <terminalName> change 'id' in the 'for country...' loop
# to 'terminalName'

station1 = '274' # 10th & Fl
station2 = '43' # 10th & U
station3 = '242' # 12th & U
station4 = '15' # 14th & V



#we get the root tag
root=doc.getroot()
root.tag

#we define empty lists for the empty bikes
sID=[]
embikes=[]
#we now use a for loop to extract the information we are interested in
for country in root.findall('station'):
	# takes the ID as a string
	sID.append(country.find('id').text)
	# takes the number of bikes as an integer
	embikes.append(int(country.find('nbBikes').text))


#use zip to create touples and then parse them into a dictionary
prov=dict(zip(sID,embikes))

#this print command was for testing and can be removed
#print prov['15']

# this function returns a color based on the number of bikes remaining
def lighter(id):
	#get the number of bikes remaining based on station id
	bk = prov[id]
	print bk
	if bk >= 6:
		print "Station %s is green - 0, 128, 0" % id
		# it is possible that this is the correct way to 
		# address these colors
		GPIO.output(red, 0)
		GPIO.output(green, 128)
		GPIO.output(blue, 0)
	elif bk > 2:
		print "Station %s is yellow - 255, 255, 0" % id
		# it is possible that this is the correct way to 
		# address these colors
		GPIO.output(red, 255)
		GPIO.output(green, 255)
		GPIO.output(blue, 0)
	elif bk > 0:
		print "Station %s is orange - 255, 128, 0" % id
		# it is possible that this is the correct way to 
		# address these colors
		GPIO.output(red, 255)
		GPIO.output(green, 128)
		GPIO.output(blue, 0)
	else:
		print "Station %s is red - 255, 0, 0" % id
		# it is possible that this is the correct way to 
		# address these colors
		GPIO.output(red, 255)
		GPIO.output(green, 0)
		GPIO.output(blue, 0)

# now run the function taking all of the stations as an argument
while True:
	lighter(station1)
	lighter(station2)
	lighter(station3)
	lighter(station4)
	time.sleep(10)


