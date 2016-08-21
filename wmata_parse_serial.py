import urllib, json
url = "https://api.wmata.com/StationPrediction.svc/json/GetPrediction/E03?api_key=547990fbdfe344f49dfc4df55a88c26a"

green_list = []
yellow_list = []
wmata_serial = []



#this is the syntax to get the line for the first train from the data
#print w[0]['Line']

response = urllib.urlopen(url)
data = json.loads(response.read())
w = data['Trains']


# this iterates through all of the trains and adds all the times for southbound trains either the list green_list[] or yellow_list[].

for i in range (0,4):

	if w[i]['Line'] == 'GR':

		#this is a northern-bound train so it doesn't matter for the final product

		if w[i]['Destination'] == 'Grnbelt':
			print "A green train that is going to Greenbelt will arrive in %s minutes" % (w[i]['Min'])

		#this is the southern train so they get added to the list


		elif w[i]['Destination'] == 'Brnch Av':
			print "A green train that is going to Branch Ave. will arrive in %s minutes" % (w[i]['Min'])

			green_list.append(w[i]['Min'])




		else:
			print "Another metro data screwup"



	elif w[i]['Line'] == 'YL':

		#this is a northern-bound train so it doesn't matter for the final product

		if w[i]['Destination'] == 'Grnbelt':
			print "A yellow train that is going to Greenbelt will arrive in %s minutes" % (w[i]['Min'])

		elif w[i]['Destination'] == 'Ft.Tottn':
			print "A yellow train that is going to Ft. Totten will arrive in %s minutes" % (w[i]['Min'])

		#these are the two desinations of the southern trains so they get added to the list

		elif w[i]['Destination'] == 'Hntingtn':
			print "A yellow train that is going to Huntington and will arrive in %s minutes" % (w[i]['Min'])

			yellow_list.append(w[i]['Min'])

		elif w[i]['Destination'] == 'Brnch Av':
			print "A yellow train that is going to Franconia-Springfield will arrive in %s minutes" % (w[i]['Min'])

			yellow_list.append(w[i]['Min'])


		else:
			print "Another metro data screwup"

# these lists now have the arrival times for as many as the next four trains

print green_list
print yellow_list

# TODO: now assign lights based on the first two numbers in the green and yellow lists



#this chunk assigns the light position for the first green train
#this limit is to avoid a range error if the isn't a value in the first position
if len(green_list) >= 1:

	green_one = green_list[0]

	if green_one == 'ARR':
			print "you missed the next southbound green train because it is arriving"
			wmata_serial.append('a')

	elif green_one == 'BRD':
			print "you missed the next southbound green train because it is boarding"
			wmata_serial.append('a')

	elif int(green_one) <= 4:
			print "you missed the next southbound green train"
			wmata_serial.append('a')
	elif 5 <= int(green_one) <= 9:
			print "leave now for the next southbound green train!"
			wmata_serial.append('b')
	elif 10 <= int(green_one) <= 15:
			print "the next southbound green train is coming soon"
			wmata_serial.append('c')
	elif 16 <= int(green_one) <= 25:
			print "the next southbound green train is a long way off"
			wmata_serial.append('d')

#this chunk assigns the light position for the second green train

if len(green_list) >= 2:

	green_two = green_list[1]

	if green_two == 'ARR':
			print "you missed the next southbound green train because it is arriving"
			wmata_serial.append('e')

	elif green_two == 'BRD':
			print "you missed the next southbound green train because it is boarding"
			wmata_serial.append('e')

	if int(green_two) <= 4:
			print "you missed the next southbound green train"
			wmata_serial.append('e')
	elif 5 <= int(green_two) <= 9:
			print "leave now for the next southbound green train!"
			wmata_serial.append('f')
	elif 10 <= int(green_two) <= 15:
			print "the next southbound green train is coming soon"
			wmata_serial.append('g')
	elif 16 <= int(green_two) <= 25:
			print "the next southbound green train is a long way off"
			wmata_serial.append('h')


if len(yellow_list) >= 1:

	yellow_one = yellow_list[0]

	if yellow_one == 'ARR':
			print "you missed it because it is arriving"
			wmata_serial.append('i')

	elif yellow_one == 'BRD':
			print "you missed it because it is boarding"
			wmata_serial.append('i')

	elif int(yellow_one) <= 4:
			print "you missed it"
			wmata_serial.append('i')
	elif 5 <= int(yellow_one) <= 9:
			print "leave now!"
			wmata_serial.append('j')
	elif 10 <= int(yellow_one) <= 15:
			print "coming soon"
			wmata_serial.append('k')
	elif 16 <= int(yellow_one) <= 25:
			print "long way off"
			wmata_serial.append('l')

#this chunk assigns the light position for the second yellow train

if len(yellow_list) >= 2:

	yellow_two = yellow_list[1]

	if yellow_two == 'ARR':
			print "you missed it because it is arriving"
			wmata_serial.append('m')

	elif yellow_two == 'BRD':
			print "you missed it because it is boarding"
			wmata_serial.append('m')

	if int(yellow_two) <= 4:
			print "you missed it"
			wmata_serial.append('m')
	elif 5 <= int(yellow_two) <= 9:
			print "leave now!"
			wmata_serial.append('n')
	elif 10 <= int(yellow_two) <= 15:
			print "coming soon"
			wmata_serial.append('o')
	elif 16 <= int(yellow_two) <= 25:
			print "long way off"
			wmata_serial.append('p')

#adds the terminating character
wmata_serial.append('z')
#turns wmata_serial into a string
wmata_serial_str = ''.join(wmata_serial)
print wmata_serial
print wmata_serial_str
