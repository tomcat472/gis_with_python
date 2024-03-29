import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from shapely.geometry import Point

airports=pd.read_csv(r"airports",
                     delimiter=',',
                     names=['id','name','city','country',
                            'iata', 'icao','lat','long','altitude',
                            'timezone','dst','tx','types','source'])
airport_geometry=[
    Point(xy) for xy in zip(airports['long'],airports['lat'])
]
airport_geodata=gpd.GeoDataFrame(airports,crs="EPSG:4326", geometry=airport_geometry)
fig,ax=plt.subplots(
    facecolor="black",subplot_kw={"projection":ccrs.Robinson()},
    figsize=(20,20)
)
ax.patch.set_facecolor('black')
airport_geodata.plot(ax=ax,transform=ccrs.PlateCarree(),
                     markersize=4,alpha=1,color='crimson',
                     edgecolor='none')
plt.setp(ax.spines.values(),color='black')
plt.setp([ax.get_xticklines(),ax.get_yticklines()],color='black')
ax.set_ylim(-7000000,9000000)
plt.show()

