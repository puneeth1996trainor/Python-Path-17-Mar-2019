import folium 
import pandas as pd 

map4 = folium.Map(location = [13.0621233,77.5580256],zoom_start = 18, tiles = 'Stamen Terrain')
df = pd.read_csv('location.txt')
#we are having the code much cleaner than the previous version thats achived by the help of function ...
def color(elev):
	if elev in range(0,200):
	 	col = 'green';
	elif elev in range (201,999):
	 	col = 'orange';
	elif elev in range(1000,3000):
	 	col = 'blue';	 	
	else: 
	  	col = 'red';
	return col

for lat,lon,name,elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
# lets make we have different makers at elevation ... or something else can be added as diffrent makers
	folium.Marker(location=[lat,lon],popup= name,icon = folium.Icon(color = color(elev),icon = 'cloud')).add_to(map4)
print(map4.save('test6.html'))