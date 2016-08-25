import urllib, json
url = "https://api.wmata.com/StationPrediction.svc/json/GetPrediction/E03?api_key=547990fbdfe344f49dfc4df55a88c26a"
response = urllib.urlopen(url)
data = json.loads(response.read())


w = data['Trains']
green_list = []
yellow_list = []



#this is the syntax to get the line for the first train from the data
#print w[0]['Line']




# this iterates through all of the trains and adds all the times for southbound trains either the list green_list[] or yellow_list[].

for i in range (0,4):

	if w[i]['Line'] == 'GR':

		#this is a northern-bound train so it doesn't matter for the final product

		if w[i]['Destination'] == 'Grnbelt':
			print "The first green train is going to Greenbelt and will arrive in %s minutes" % (w[i]['Min'])

		#this is the southern train so they get added to the list


		elif w[i]['Destination'] == 'Brnch Av':
			print "The first green train is going to Branch Ave. and will arrive in %s minutes" % (w[i]['Min'])

			green_list.append(w[i]['Min'])


		else:
			print "Another metro data screwup"

	#There weren't any yellow line trains when I was doing this so the variables are wrong.  TODO: change the destination station codes once you can see what they are

	elif w[i]['Line'] == 'YL':

		#this is a northern-bound train so it doesn't matter for the final product

		if w[i]['Destination'] == 'Grnbelt':
			print "The first yellow train is going to Greenbelt and will arrive in %s minutes" % (w[i]['Min'])

		#these are the two desinations of the southern trains so they get added to the list

		elif w[i]['Destination'] == 'Brnch Av':
			print "The first yellow train is going to Huntington and will arrive in %s minutes" % (w[i]['Min'])

			yellow_list.append(int(w[i]['Min']))

		elif w[i]['Destination'] == 'Brnch Av':
			print "The first yellow train is going to Franconia-Springfield and will arrive in %s minutes" % (w[i]['Min'])

			yellow_list.append(int(w[i]['Min']))


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
			print "you missed it because it is arriving"

	elif green_one == 'BRD':
			print "you missed it because it is boarding"

	elif int(green_one) <= 4:
			print "you missed it"
			#light up the light for the station
	elif 5 <= int(green_one) <= 9:
			print "leave now!"
			#light up the light one before the station
	elif 10 <= int(green_one) <= 15:
			print "coming soon"
			#light up the light two before the station
	elif 16 <= int(green_one) <= 25:
			print "long way off"
			#liht up the ilght three before the station

#this chunk assigns the light position for the second green train

if len(green_list) >= 2:

	green_two = green_list[1]

	if green_two == 'ARR':
			print "you missed it because it is arriving"

	elif green_two == 'BRD':
			print "you missed it because it is boarding"

	if green_two <= 4:
			print "you missed it"
			#light up the light for the station
	elif 5 <= green_two <= 9:
			print "leave now!"
			#light up the light one before the station
	elif 10 <= green_two <= 15:
			print "coming soon"
			#light up the light two before the station
	elif 16 <= green_two <= 25:
			print "long way off"
			#liht up the ilght three before the station


if len(yellow_list) >= 1:

	yellow_one = yellow_list[0]

	if yellow_one == 'ARR':
			print "you missed it because it is arriving"

	elif yellow_one == 'BRD':
			print "you missed it because it is boarding"

	elif int(yellow_one) <= 4:
			print "you missed it"
			#light up the light for the station
	elif 5 <= int(yellow_one) <= 9:
			print "leave now!"
			#light up the light one before the station
	elif 10 <= int(yellow_one) <= 15:
			print "coming soon"
			#light up the light two before the station
	elif 16 <= int(yellow_one) <= 25:
			print "long way off"
			#liht up the ilght three before the station

#this chunk assigns the light position for the second yellow train

if len(yellow_list) >= 2:

	yellow_two = yellow_list[1]

	if yellow_two == 'ARR':
			print "you missed it because it is arriving"

	elif yellow_two == 'BRD':
			print "you missed it because it is boarding"

	if yellow_two <= 4:
			print "you missed it"
			#light up the light for the station
	elif 5 <= yellow_two <= 9:
			print "leave now!"
			#light up the light one before the station
	elif 10 <= yellow_two <= 15:
			print "coming soon"
			#light up the light two before the station
	elif 16 <= yellow_two <= 25:
			print "long way off"
			#liht up the ilght three before the station
