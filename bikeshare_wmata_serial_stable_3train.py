import xml.etree.ElementTree as ET
import urllib2
import time
import serial
import json




# define the stations that will be identified
# note that these use the number in <id> not the <terminalName>
# if you want to use <terminalName> change 'id' in the 'for country...' loop
# to 'terminalName'

station1 = '274' # 10th & Fl
station2 = '43' # 10th & U
station3 = '242' # 12th & U
station4 = '15' # 14th & V
station5 =  '272'# 14th & Belmont

#holder for bike serial commands
ser_holder = []

#define empty lists for the empty bikes
sID=[]
embikes=[]

#this is the URL for the metro data
url = "https://api.wmata.com/StationPrediction.svc/json/GetPrediction/E03?api_key=547990fbdfe344f49dfc4df55a88c26a"

#these are empty lists for metro data
green_list = []
yellow_list = []


#opens up the serial connection with arduino
ser = serial.Serial('/dev/ttyACM0', 9600)
#this is necessary because once it opens up the serial port arduino needs a second
time.sleep(2)


# this function returns a color based on the number of bikes remaining
# each serial write needs to be specific to a station
def lighter(id, green, yellow, orange, red):
	#get the number of bikes remaining based on station id
	bk = prov[id]
	print bk
	#numbers below are GRB to sync with neopixels
	if bk >= 6:
		ser_holder.append(green)
	elif bk > 2:
		ser_holder.append(yellow)
	elif bk > 0:
		ser_holder.append(orange)
	else:
		ser_holder.append(red)

while True:
    #this is the bike section
	try:
		print "Pulling bikeshare data"
		# parse the data using urlib2 and xml
		# it is down here so it hits the site again every time
		site='https://www.capitalbikeshare.com/data/stations/bikeStations.xml'
		htm=urllib2.urlopen(site)
		doc = ET.parse(htm)

		print "Getting the root tag"
		#get the root tag
		root=doc.getroot()
		root.tag
		htm.close()
		#use a for loop to extract the information we are interested in
		for country in root.findall('station'):
			# takes the ID as a string
			sID.append(country.find('id').text)
			# takes the number of bikes as an integer
			embikes.append(int(country.find('nbBikes').text))

		print "using zip to create touples"
		#use zip to create touples and then parse them into a dictionary
		prov=dict(zip(sID,embikes))

		#this cleans out the last loop's ser_holder variables
		ser_holder = []

		lighter(station1, 'A', 'B', 'C', 'D')
		lighter(station2, 'E', 'F', 'G', 'H')
		lighter(station3, 'I', 'J', 'K', 'L')
		lighter(station4, 'M', 'N', 'O', 'P')
		lighter(station5, 'Q', 'R', 'S', 'T')

		#add terminating char to ser_holder for arudino reading
		###ser_holder.append('Z')

		#turns the list ser_holder into string ser_holder_str
		ser_holder_str = ''.join(ser_holder)
		print "Bikeshare ser_holder is %s" % (ser_holder)
		print "Bikeshare ser_holder_str is %s" % (ser_holder_str)

	except:
		print "Some sort of bike error."


    #now run the metro part
	print "Clearning out old wmata data"
    #clears out data from last loop
	wmata_serial = []
	green_list = []
	yellow_list = []

	#the try/except is for handing errors on the WMATA side

	try:
		print "Looking up wmata data"
		response = urllib2.urlopen(url)
		print "reponse line done"
		data = json.loads(response.read())
		# w is the data in the list "trains" which are the trains coming to
		#the station
		print "data line done"
		w = data['Trains']
		print "w line done"
		#this closes the socket to avoid name resolution errors
		response.close()
		print "wmata data lookup success"
	except (ValueError, IOError):
		print "There was a wmata error so I'm using dummy data"
		#this is just a dummy json that only contains a northbound train so that
		#the rest of the script has something to work with if there is  a probelm getting data
		w = [{'Group': '1', 'Min': 'BRD', 'DestinationCode': 'E06', 'Car': '6', 'Destination': 'Ft.Tottn', 'DestinationName': 'Fort Totten', 'LocationName': 'U Street/African-Amer Civil War Memorial/Cardozo', 'Line': 'YL', 'LocationCode': 'E03'}]



	# this iterates through all of the trains and adds all the times for southbound trains either the list green_list[] or yellow_list[].
	#range is (0,len(w)) because the number of trains varies

	print "performing wmata iterations"
	for i in range (0,len(w)):

		if w[i]['Line'] == 'GR':

			#this is the southern train so they get added to the list

			if w[i]['Destination'] == 'Brnch Av':

				#print "green in interation %s is %s" % (i, w[i]['Min'])
				green_list.append(w[i]['Min'])


		elif w[i]['Line'] == 'YL':

			#these are the two desinations of the southern trains so they get added to the list

			if w[i]['Destination'] == 'Hntingtn':

				#print "yellow in interation %s is %s" % (i, w[i]['Min'])
				yellow_list.append(w[i]['Min'])

			elif w[i]['Destination'] == 'Brnch Av':

				#print "yellow in interation %s is %s" % (i, w[i]['Min'])
				yellow_list.append(w[i]['Min'])

			elif w[i]['Destination'] == 'Frnconia':

				#print "yellow in interation %s is %s" % (i, w[i]['Min'])
				yellow_list.append(w[i]['Min'])


		else:
			print "line 174 else"


	# these lists now have the arrival times for as many as the next four trains

	print "the green_list is %s" % (green_list)
	print "the yellow_list is %s" % (yellow_list)



    #you do the greeen and yellow trains differently here
    # both seem to work



	#this chunk assigns the light position for the first green train
	#this limit is to avoid a range error if the isn't a value in the first position
	print "Assigning wmata light positions"

	if len(green_list) == 1:

		green_one = green_list[0]

		if green_one == 'ARR':
				wmata_serial.append('a')
		elif green_one == 'BRD':
				wmata_serial.append('a')
		elif green_one == '':
			pass
		elif int(green_one) <= 7:
				wmata_serial.append('a')
		elif 8 <= int(green_one) <= 11:
				wmata_serial.append('b')
		elif 12 <= int(green_one) <= 17:
				wmata_serial.append('c')
		elif 18 <= int(green_one) <= 30:
				wmata_serial.append('d')
		else:
			print "line 213 else"

	#this chunk assigns the light position for the second green train

	if len(green_list) == 2:

		green_one = green_list[0]

		if green_one == 'ARR':
				wmata_serial.append('a')
		elif green_one == 'BRD':
				wmata_serial.append('a')
		elif green_one == '':
			pass
		elif int(green_one) <= 7:
				wmata_serial.append('a')
		elif 8 <= int(green_one) <= 11:
				wmata_serial.append('b')
		elif 12 <= int(green_one) <= 17:
				wmata_serial.append('c')
		elif 18 <= int(green_one) <= 30:
				wmata_serial.append('d')
		else:
			print "line 235 else"

		green_two = green_list[1]

		if green_two == 'ARR':
				wmata_serial.append('e')
		elif green_two == 'BRD':
				wmata_serial.append('e')
		elif green_two == '':
			pass
		elif int(green_two) <= 7:
				wmata_serial.append('e')
		elif 8 <= int(green_two) <= 11:
				wmata_serial.append('f')
		elif 12 <= int(green_two) <= 17:
				wmata_serial.append('g')
		elif 18 <= int(green_two) <= 30:
				wmata_serial.append('h')
		else:
		 	print "line 253 else"

	if len(green_list) >= 3:

		green_one = green_list[0]

		if green_one == 'ARR':
				wmata_serial.append('a')
		elif green_one == 'BRD':
				wmata_serial.append('a')
		elif green_one == '':
			pass
		elif int(green_one) <= 7:
				wmata_serial.append('a')
		elif 8 <= int(green_one) <= 11:
				wmata_serial.append('b')
		elif 12 <= int(green_one) <= 17:
				wmata_serial.append('c')
		elif 18 <= int(green_one) <= 30:
				wmata_serial.append('d')
		else:
			print "line 235 else"

		green_two = green_list[1]

		if green_two == 'ARR':
				wmata_serial.append('e')
		elif green_two == 'BRD':
				wmata_serial.append('e')
		elif green_two == '':
			pass
		elif int(green_two) <= 7:
				wmata_serial.append('e')
		elif 8 <= int(green_two) <= 11:
				wmata_serial.append('f')
		elif 12 <= int(green_two) <= 17:
				wmata_serial.append('g')
		elif 18 <= int(green_two) <= 30:
				wmata_serial.append('h')
		else:
		 	print "line 253 else"

		green_three = green_list[2]

		if green_three == 'ARR':
				wmata_serial.append('q')
		elif green_three == 'BRD':
				wmata_serial.append('q')
		elif green_three == '':
			pass
		elif int(green_three) <= 7:
				wmata_serial.append('q')
		elif 8 <= int(green_three) <= 11:
				wmata_serial.append('r')
		elif 12 <= int(green_three) <= 17:
				wmata_serial.append('s')
		elif 18 <= int(green_three) <= 30:
				wmata_serial.append('t')
		else:
		 	print "line 307 else"

	#unlike the green section which figures out how many cars there are an then does the whole assignment, the yellow section assigns each letter as it works through the list. So green says "how many trains: all do everything now." Yellow says "if there is one train, I'll assign now.  If there is a second train, I'll do that one here"


	if len(yellow_list) >= 1:

		yellow_one = yellow_list[0]

		if yellow_one == 'ARR':
				wmata_serial.append('i')
		elif yellow_one == 'BRD':
				wmata_serial.append('i')
		elif yellow_one == '':
			pass
		elif int(yellow_one) <= 7:
				wmata_serial.append('i')
		elif 8 <= int(yellow_one) <= 11:
				wmata_serial.append('j')
		elif 12 <= int(yellow_one) <= 17:
				wmata_serial.append('k')
		elif 18 <= int(yellow_one) <= 30:
				wmata_serial.append('l')
		else:
			print "line 274 else"

	#this chunk assigns the light position for the second yellow train

	if len(yellow_list) >= 2:

		yellow_two = yellow_list[1]

		if yellow_two == 'ARR':
				wmata_serial.append('m')
		elif yellow_two == 'BRD':
				wmata_serial.append('m')
		elif yellow_two == '':
			pass
		elif int(yellow_two) <= 7:
				wmata_serial.append('m')
		elif 8 <= int(yellow_two) <= 11:
				wmata_serial.append('n')
		elif 12 <= int(yellow_two) <= 17:
				wmata_serial.append('o')
		elif 18 <= int(yellow_two) <= 30:
				wmata_serial.append('p')
		else:
		 	print "line 296 else"

	if len(yellow_list) >= 3:

		yellow_three = yellow_list[2]

		if yellow_three == 'ARR':
				wmata_serial.append('u')
		elif yellow_three == 'BRD':
				wmata_serial.append('u')
		elif yellow_three == '':
			pass
		elif int(yellow_three) <= 7:
				wmata_serial.append('u')
		elif 8 <= int(yellow_three) <= 11:
				wmata_serial.append('v')
		elif 12 <= int(yellow_three) <= 17:
				wmata_serial.append('w')
		elif 18 <= int(yellow_three) <= 30:
				wmata_serial.append('x')
		else:
		 	print "line 296 else"


	else:
		print "This is the new line you added because there was no else in the wmata light assignment code. Something has gone wrong"


	#combine the bikeshare and wmata serial strings
	merged_serial = wmata_serial + ser_holder

	#adds the terminating character to the newly merged list
	merged_serial.append('Z')
	#turns the list into a string
	merged_string = ''.join(merged_serial)

	print "wmata_serial is %s" % (wmata_serial)
	print "merged_serial is %s" % (merged_serial)
	print "merged_string is %s" % (merged_string)
	#writes the list to the arduino
	ser.write(merged_string)

	print "sleeping for 10 seconds"
	time.sleep(10)
