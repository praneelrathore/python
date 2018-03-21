from googlemaps import Client
import requests
import json
from geopy.geocoders import Nominatim
# Add you API key here
mapService = Client('your key here')

send_url = 'http://freegeoip.net/json'
r = requests.get(send_url)
j = json.loads(r.text)
lat = j['latitude']
lon = j['longitude']
geolocator = Nominatim()
a = str(lat) + ', ' + str(lon)
location = geolocator.reverse(a)
print location.address
