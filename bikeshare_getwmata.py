# https://api.wmata.com/StationPrediction.svc/GetPrediction/E03?api_key=547990fbdfe344f49dfc4df55a88c26a



import xml.etree.ElementTree as ET
import urllib2

#we parse the data using urlib2 and xml
site='https://api.wmata.com/StationPrediction.svc/GetPrediction/E03?api_key=547990fbdfe344f49dfc4df55a88c26a'
htm=urllib2.urlopen(site)
doc = ET.parse(htm)

#we get the root tag
root=doc.getroot()
root.tag

#we define empty lists for the data needed
destination=[]
minutes=[]

#we now use a for loop to extract the information we are interested in
for country in root.findall('station'):
	# format is [variable].append(country.find('[name_of_target_tag]').text)
	destination.append(country.find('Destination').text)
	minutes.append(int(country.find('Min').text))

#These 2 print statements are used to make sure that the for statement works
print destination
print minutes

#use zip to create touples and then parse them into a dataframe
prov=dict(zip(destination,minutes))

print prov
