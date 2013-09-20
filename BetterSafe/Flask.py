from urllib2 import urlopen
from json import load
from flask import Flask
from flask import render_template
# http://localhost:5000/search/lat/long/
app = Flask(__name__)
@app.route("/search/<string:lat>/<string:lon>/") #/search/lat/long/
def search(lat, lon):
	randomness = "lat: %s lon: %s" % (lat, lon)
	lat_lon = "%s,%s" % (lat,lon)
	
	key = "AIzaSyDdxVDEz0tAVh6199Rz-fjZnp4h2Sf-rIo"

	url = 'https://maps.googleapis.com/maps/api/place/search/json?location='
	url = url + lat_lon
	url = url + '&radius=500&sensor=true&keyword=hospital&key='
	url = url + key
	response = urlopen(url)
	json_obj = load(response)
	list_n = json_obj['results']

	all_names = list()

	for place in list_n:
		all_names.append(place['name'])
	names = unicode(all_names)

	all_addresses = list()

	for address in list_n:
		all_addresses.append(address['vicinity'])
	address = unicode(all_addresses)

	return render_template('hello.html', hospital_names=all_names, hospital_addresses=all_addresses)


@app.route('/')
def getLocation():
	return render_template('gpslocator.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
#http:// IP address:5000
#1. / geolocation javascript: handle function should connect to another flask url: /q?lat=50&long=50
#2. /q   get info from lat and long and print it out
#3. stick it as google place location variable
#https://maps.googleapis.com/maps/api/place/search/json?location=37.80674930910263,-122.27011963221332&radius=500&sensor=true&key=AIzaSyDdxVDEz0tAVh6199Rz-fjZnp4h2Sf-rIo


