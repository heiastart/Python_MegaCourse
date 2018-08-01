import folium
import pandas

data = pandas.read_csv('Volcanoes_USA.txt')
lon = list(data['LON'])
lat = list(data['LAT'])
elev = list(data['ELEV'])
#name = list(data['NAME'])

def color_producer(elevation):
    if elevation <= 2000:
        return 'green'
    elif elevation > 2000 and elevation <= 3500:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name='Volcanoes')

for lati, long, ele in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lati, long], radius=5, popup=str(ele) + " moh", fill_color=color_producer(ele), color='grey', fill=True, fill_opacity=0.8))
    # fg.add_child(folium.Marker -> for andre ikoner på kartet)

fgp = folium.FeatureGroup(name='Population')

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
                                                      else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                                                      else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save('Map1.html')
