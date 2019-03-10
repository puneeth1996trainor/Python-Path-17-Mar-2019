import folium
map3 = folium.Map(location=[13.0621233,77.5580256],zoom_start = 18, tiles = 'Stamen Terrain')
# adding some marker to the map

folium.Marker(location=[13.0621233,77.5580256],popup = 'Its my home ', icon = folium.Icon(icon = 'cloud')).add_to(map3)

folium.Marker(location=[13.061939, 77.558750],popup = 'Close by area ...', icon = folium.Icon(icon = 'cloud')).add_to(map3)

print(map3.save('test3.html'))
