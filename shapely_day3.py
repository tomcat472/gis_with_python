import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from shapely.geometry import Point,LineString
data = gpd.read_file("ne_10m_time_zones.shp")
countries = gpd.read_file("ne_10m_admin_0_countries.shp")
data = data.sort_values('name')
# print(data.columns)

# fig, ax = plt.subplots(facecolor='#FCF6F5FF')
# ax.set_facecolor('#FCF6F5FF')
# data.plot(ax=ax, color='#FCF6F5FF', edgecolor='black', lw=1)
# plt.show()

uk = data.loc[data['name'] == '0']
texas = data.loc[data['name'] == '-6']
my_flight = pd.concat([uk, texas])
print(my_flight)
airports = pd.read_csv("airports", delimiter=',', names=['id', 'name', 'city', 'country', 'iata', 
                                                          'icao', 'lat', 'long', 'altitude', 'timezone',
                                                          'dst', 'tz', 'type', 'source'])
routes = pd.read_csv("routes", delimiter=',', names=['airline', 'id', 'source_airport', 'source_airport_id',
                                                     'destination_airport', 'destination_airport_id', 'codeshare',
                                                     'stops', 'equitment'])
geometry = [Point(xy) for xy in zip(airports['long'], airports['lat'])]
airports = gpd.GeoDataFrame(airports, crs="EPSG:4326", geometry=geometry)
new_airports = gpd.sjoin(airports, my_flight, op='within')
new_airports = new_airports.rename(columns = {'name_left': 'airport_name', 'name_right': 'timezone_name'})
# print(new_airports.airport_name.unique())
# print(new_airports.timezone_name.unique())

source_airports = new_airports[['airport_name', 'iata', 'icao', 
                                'lat', 'long', 'timezone_name']]

destination_airports = source_airports.copy()
source_airports.columns = [str(col) + '_source' for col in source_airports.columns]
destination_airports.columns = [str(col) + '_destination' for col in destination_airports.columns]

routes = routes[['source_airport', 'destination_airport']]
routes = pd.merge(routes, source_airports, left_on='source_airport', right_on='iata_source')
routes = pd.merge(routes, destination_airports, left_on='destination_airport', right_on='iata_destination')

routes = routes[routes['timezone_name_source'] != routes['timezone_name_destination']]

routes_geometry = [LineString([[routes.iloc[i]['long_source'], routes.iloc[i]['lat_source']], [routes.iloc[i]['long_destination'], routes.iloc[i]['lat_destination']]]) for i in range(routes.shape[0])]
routes_geodata = gpd.GeoDataFrame(routes, geometry=routes_geometry, crs='EPSG:4326')

# fig, ax = plt.subplots(subplot_kw={'projection': ccrs.Mercator()}, figsize=(10,10))
# ax.patch.set_facecolor('#FCF6F5FF')
# routes_geodata.plot(ax=ax, color='black', linewidth=0.1)
# ax.axis('off')
# plt.show()

fig, ax = plt.subplots(facecolor='#FCF6F5FF', figsize=(10,10))

countries.plot(ax=ax, color='none', edgecolor='black', lw=1)
data.plot(ax=ax, column='name', cmap='jet', edgecolor='white', lw=1, alpha=0.6)
routes_geodata.plot(ax=ax, color='black', linewidth=0.1)

ax.axis('off')
plt.show()