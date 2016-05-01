# from http://www.plotsofdots.com/archives/68


import xml.etree.ElementTree as ET
import urllib2

#we parse the data using urlib2 and xml
site='https://www.capitalbikeshare.com/data/stations/bikeStations.xml'
htm=urllib2.urlopen(site)
doc = ET.parse(htm)

#we get the root tag
root=doc.getroot()
root.tag

#we define empty lists for the empty bikes
sID=[]
embikes=[]
#we now use a for loop to extract the information we are interested in
for country in root.findall('station'):
	# format is [variable].append(country.find('[name_of_target_tag]').text)
	sID.append(country.find('id').text)
	#we want the number of bikes to be an integer
	embikes.append(int(country.find('nbBikes').text))

#These 2 print statements are used to make sure that the for statement works
#print embikes
#print sID

#use zip to create touples and then parse them into a dataframe
prov=dict(zip(sID,embikes))

print prov


