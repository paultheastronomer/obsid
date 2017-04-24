import pandas as pd
from geopy.geocoders import GoogleV3
import sys

# Define which geolocater to use with geopy
geolocator = GoogleV3()

addr = "james rd 4, Observatory, Cape Town"

location = geolocator.geocode(addr, timeout=10)
print("new google.maps.LatLng"+str((location.latitude, location.longitude))+", // "+addr+"\n")

