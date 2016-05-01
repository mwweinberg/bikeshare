# from http://www.plotsofdots.com/archives/68


import xml.etree.ElementTree as ET
import urllib2
# this is for the pause
import time

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
	elif bk > 2:
		print "Station %s is yellow - 255, 255, 0" % id
	elif bk > 0:
		print "Station %s is orange - 255, 128, 0" % id
	else:
		print "Station %s is red - 255, 0, 0" % id

# now run the function taking all of the stations as an argument
while True:
	lighter(station1)
	lighter(station2)
	lighter(station3)
	lighter(station4)
	time.sleep(10)


