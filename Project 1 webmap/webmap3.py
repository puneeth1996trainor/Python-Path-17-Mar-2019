#location.txt file to generate markers for map

import folium
import pandas as pd

#original map object can stay put 
map4 = folium.Map(location=[13.0621233,77.5580256],zoom_start = 18, tiles = 'Stamen Terrain')

#lets read the csv file into python
df = pd.read_csv('location.txt')

#we have 2 iterators in this loop and so put them in a zip function 
#read as iterator and then where id df to "grab" that iterators value 
#read as iterator, and then where is df to "grab" that iterators valur 

for lat,lon,name in zip(df['LAT'], df['LON'], df['NAME']):
	folium.Marker(location=[lat, lon], popup = name, icon = folium.Icon(icon = 'cloud')).add_to(map4)

print(map4.save('test4.html'))
