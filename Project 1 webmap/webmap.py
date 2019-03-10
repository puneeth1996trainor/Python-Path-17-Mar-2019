import folium
print(dir(folium))
#create a map object 
map = folium.Map(location=[13.0621233,77.5580256],zoom_start = 10)
print(map)
#need html file out of this object - to create a map 
#look in the Map method directory to see all the methods we can apply to MAP

print(dir(folium.Map))
print(map.save('test.html'))
#go look under your files for the html file 
#open the html file in browser 

# change zoom to required tiles ="Stamen Terrain" can be changed 

map2 = folium.Map(location=[13.0621233,77.5580256],zoom_start = 13, tiles = 'Stamen Terrain')
print(map2)
print(map2.save('test2.html'))
