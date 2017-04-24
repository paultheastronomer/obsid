import pandas as pd
from geopy.geocoders import GoogleV3
import sys

# Define which geolocater to use with geopy
geolocator = GoogleV3()

def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)

# Load the data
df1 = pd.read_csv("../data/1013.csv")
df2 = pd.read_csv("../data/1617.csv")

df 	= df2
crime = "robbery"

df["Crime Class"] = df["Crime Class"].str.lower()

# Only work with data of a certain crime
df = df[df["Crime Class"] == crime]

# Convert all addresses to lower case (for conveniance)
loc = df.Location.str.lower()

# Change 'cor' (short for corner) to and (which Google can read)
loc = loc.str.replace('cor', 'and')

# Pick out the addresses with numbers in them
loc_num = [h for h in loc if hasNumbers(h)]

# Pick out the corner addresses
loc_corner = [h for h in loc if "and" in h]

# Add all the addresses together
addr = loc_num + loc_corner

print((len(loc_corner)/len(addr))*100.," % of "+crime+" related crime happens on corners.")
sys.exit()
# Add more location info so Google can find the address
addr = [h + ", Observatory, Cape Town" for h in addr]

# Write all the addresses to a .txt file
f1=open('coords_'+crime+'.txt', 'w+')
for i in range(len(addr)):
	print (addr[i])
	location = geolocator.geocode(addr[i], timeout=10)
	try:
		print("new google.maps.LatLng"+str((location.latitude, location.longitude))+", // "+addr[i]+"\n", end = '', file=f1)
	except:
		pass
f1.close()