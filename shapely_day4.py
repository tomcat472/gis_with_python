import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from shapely.geometry import Point,LineString

airports = pd.read_csv("airports", delimiter=',', names=['id', 'name', 'city', 'country', 'iata', 
                                                          'icao', 'lat', 'long', 'altitude', 'timezone',
                                                          'dst', 'tz', 'type', 'source'])
routes = pd.read_csv("routes", delimiter=',', names=['airline', 'id', 'source_airport', 'source_airport_id',
                                                     'destination_airport', 'destination_airport_id', 'codeshare',
                                                     'stops', 'equitment'])
source_airports=airports[['name','iata','icao', 'lat', 'long']]
destination_airports=source_airports.copy()
source_airports.columns=[str(col) + '_source' for col in source_airports.columns]
destination_airports.columns=[str(col)+ '_destination' for col in destination_airports.columns]

routes=routes[['source_airport','destination_airport']]
routes=pd.merge(
    routes,
    source_airports,
    left_on='source_airport',
    right_on='iata_source'
)
routes=pd.merge(
    routes,
    destination_airports,
    left_on='destination_airport',
    right_on='iata_destination'
)

routes_geometry=[
    LineString(
        [[routes.iloc[i]['long_source'],routes.iloc[i]['lat_source']],
         [routes.iloc[i]['long_destination'],routes.iloc[i]['lat_destination']]])
        for i in range(routes.shape[0]
    )
]

routes_geodata=gpd.GeoDataFrame(
    routes,geometry=routes_geometry,crs='EPSG:4326'
)

# print(routes.columns)
# fig,ax=plt.subplots(figsize=(20,20))
# ax.patch.set_facecolor('black')
# routes_geodata.plot(ax=ax,color='white',linewidth=0.1)
# plt.show()

fig,ax=plt.subplots(subplot_kw={'projection':ccrs.Robinson()},figsize=(20,20))
ax.patch.set_facecolor('black')
routes_geodata.plot(
    ax=ax,
    transform=ccrs.Geodetic(),
    color='white',
    linewidth=0.1,
    alpha=0.1
)
plt.setp(ax.spines.values(),color='black')
plt.setp([ax.get_xticklines(),ax.get_yticklines()],color='black')
ax.set_ylim(-7000000,8800000)


# plt.savefig('my_plot.png', dpi=1200)  

plt.show()