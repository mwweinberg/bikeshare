import urllib, json
import time
import serial
url = "https://api.wmata.com/StationPrediction.svc/json/GetPrediction/E03?api_key=547990fbdfe344f49dfc4df55a88c26a"

green_list = []
yellow_list = []
wmata_serial = []





#opens up the serial connection with arduino
ser = serial.Serial('/dev/ttyACM0', 9600)
#this is necessary because once it opens up the serial port arduino needs a second
time.sleep(2)



#this is the syntax to get the line for the first train from the data
#print w[0]['Line']

while True:

	#clears out data from last loop
	wmata_serial = []
	green_list = []
	yellow_list = []


	response = urllib.urlopen(url)
	data = json.loads(response.read())
	# w is the data in the list "trains" which are the trains coming to
	#the station
	w = data['Trains']


	# this iterates through all of the trains and adds all the times for southbound trains either the list green_list[] or yellow_list[].
	#range is (0,len(w)) because the number of trains varies
	#if you choose too many you get an error
	#if you chose too few you miss some

	for i in range (0,len(w)):

		if w[i]['Line'] == 'GR':

			#this is the southern train so they get added to the list

			if w[i]['Destination'] == 'Brnch Av':

				print "green in interation %s is %s" % (i, w[i]['Min'])
				green_list.append(w[i]['Min'])


		elif w[i]['Line'] == 'YL':

			#these are the two desinations of the southern trains so they get added to the list

			if w[i]['Destination'] == 'Hntingtn':

				print "yellow in interation %s is %s" % (i, w[i]['Min'])
				yellow_list.append(w[i]['Min'])

			elif w[i]['Destination'] == 'Brnch Av':

				print "yellow in interation %s is %s" % (i, w[i]['Min'])
				yellow_list.append(w[i]['Min'])



		print "green_list after %s iterations is %s." % (i, green_list)
		print "yellow_list after %s iterations is %s." % (i, yellow_list)
		print ""


	# these lists now have the arrival times for as many as the next four trains

	print "the green_list is %s" % (green_list)
	print "the yellow_list is %s" % (yellow_list)



#TODO: you do the greeen and yellow trains differently here
#does it matter?
# there need to be multiple  yellow trains to find out

	#this chunk assigns the light position for the first green train
	#this limit is to avoid a range error if the isn't a value in the first position
	if len(green_list) == 1:

		green_one = green_list[0]

		if green_one == 'ARR':
				wmata_serial.append('a')
		elif green_one == 'BRD':
				wmata_serial.append('a')
		elif green_one == '':
			pass
		elif int(green_one) <= 4:
				wmata_serial.append('a')
		elif 5 <= int(green_one) <= 9:
				wmata_serial.append('b')
		elif 10 <= int(green_one) <= 15:
				wmata_serial.append('c')
		elif 16 <= int(green_one) <= 25:
				wmata_serial.append('d')

	#this chunk assigns the light position for the second green train

	if len(green_list) >= 2:

		green_one = green_list[0]

		if green_one == 'ARR':
				wmata_serial.append('a')
		elif green_one == 'BRD':
				wmata_serial.append('a')
		elif green_one == '':
			pass
		elif int(green_one) <= 4:
				wmata_serial.append('a')
		elif 5 <= int(green_one) <= 9:
				wmata_serial.append('b')
		elif 10 <= int(green_one) <= 15:
				wmata_serial.append('c')
		elif 16 <= int(green_one) <= 25:
				wmata_serial.append('d')

		green_two = green_list[1]

		if green_two == 'ARR':
				wmata_serial.append('e')
		elif green_two == 'BRD':
				wmata_serial.append('e')
		elif green_two == '':
			pass
		if int(green_two) <= 4:
				wmata_serial.append('e')
		elif 5 <= int(green_two) <= 9:
				wmata_serial.append('f')
		elif 10 <= int(green_two) <= 15:
				wmata_serial.append('g')
		elif 16 <= int(green_two) <= 25:
				wmata_serial.append('h')


	if len(yellow_list) >= 1:

		yellow_one = yellow_list[0]

		if yellow_one == 'ARR':
				wmata_serial.append('i')
		elif yellow_one == 'BRD':
				wmata_serial.append('i')
		elif yellow_one == '':
			pass
		elif int(yellow_one) <= 4:
				wmata_serial.append('i')
		elif 5 <= int(yellow_one) <= 9:
				wmata_serial.append('j')
		elif 10 <= int(yellow_one) <= 15:
				wmata_serial.append('k')
		elif 16 <= int(yellow_one) <= 25:
				wmata_serial.append('l')

	#this chunk assigns the light position for the second yellow train

	if len(yellow_list) >= 2:

		yellow_two = yellow_list[1]

		if yellow_two == 'ARR':
				wmata_serial.append('m')
		elif yellow_two == 'BRD':
				wmata_serial.append('m')
		elif yellow_two == '':
			pass
		if int(yellow_two) <= 4:
				wmata_serial.append('m')
		elif 5 <= int(yellow_two) <= 9:
				wmata_serial.append('n')
		elif 10 <= int(yellow_two) <= 15:
				wmata_serial.append('o')
		elif 16 <= int(yellow_two) <= 25:
				wmata_serial.append('p')

	#adds the terminating character
	wmata_serial.append('z')

	print "wmata_serial is %s" % (wmata_serial)

	ser.write(wmata_serial)
	time.sleep(10)
