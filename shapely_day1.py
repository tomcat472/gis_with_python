# from shapely.geometry import Polygon
# polygon=Polygon([(0,0),(1,1),(1,0)])
# print('Area',polygon.area)
# print('Length',polygon.length)
# print('Bounds',polygon.bounds)
# print('Boundary',polygon.boundary)
# print('Center',polygon.centroid)
# ______________________________________________
# from shapely.geometry import Polygon
# import matplotlib.pyplot as plt
# Polygons=Polygon([
#     (-4,0),
#     (-5,0),
#     (-6,3),
#     (-8,7),
#     (-4,8),
#     (-3,2),
#     (-1,3)
# ])
# plt.figure(figsize=(10,5))
# plt.fill(*Polygons.exterior.xy)
# plt.show()
# __________________________________________________
import shapely.ops as so
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, MultiPolygon

# Define your polygons
r1 = Polygon([(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)])
r2 = Polygon([(1, 1), (1, 2), (2, 2), (2, 1), (1, 1)])
r3 = Polygon([(0.5, 0.5), (0.5, 1.5), (1.5, 1.5), (1.5, 0.5), (0.5, 0.5)])
r4 = Polygon([(3, 3), (3, 4), (4, 4), (4, 3), (3, 3)])

# Compute new_shape and multipolygon
new_shape = so.unary_union([r1, r2, r3])
multipolygon = so.unary_union([r1, r2, r3, r4])

# Plot the polygons
fig, ax = plt.subplots(figsize=(6, 6))

# Plot individual polygons
for poly in [r1, r2, r3, r4]:
    x, y = poly.exterior.xy
    ax.plot(x, y, label="Polygon")

# Plot new_shape (handles MultiPolygon case)
if isinstance(new_shape, MultiPolygon):
    for poly in new_shape.geoms:
        x, y = poly.exterior.xy
        ax.plot(x, y, label="New Shape", linestyle="--")
else:
    x, y = new_shape.exterior.xy
    ax.plot(x, y, label="New Shape", linestyle="--")

# Plot multipolygon (handles MultiPolygon case)
if isinstance(multipolygon, MultiPolygon):
    for poly in multipolygon.geoms:
        x, y = poly.exterior.xy
        ax.plot(x, y, label="Multipolygon", linestyle=":")
else:
    x, y = multipolygon.exterior.xy
    ax.plot(x, y, label="Multipolygon", linestyle=":")

# Set axis limits
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 5)

# Add legend
ax.legend()

# Show the plot
plt.title("Polygon Visualization")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
