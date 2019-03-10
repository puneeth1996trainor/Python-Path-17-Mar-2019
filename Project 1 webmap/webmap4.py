import folium 
import pandas as pd 

map4 = folium.Map(location = [13.0621233,77.5580256],zoom_start = 18, tiles = 'Stamen Terrain')
df = pd.read_csv('location.txt')

for lat,lon,name,elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
# lets make we have different makers at elevation ... or something else can be added as diffrent makers
	folium.Marker(location=[lat,lon],popup= name,icon = folium.Icon(color = 'green' if elev in range(0,200) else 'orange' if elev in range (201,999) else 'blue' if elev in range(1000,3000) else 'red',icon = 'cloud')).add_to(map4)
print(map4.save('test5.html'))