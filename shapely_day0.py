# from shapely.geometry import Point

# point=Point(0,0)
# print('Area',point.area)
# print('Length',point.length)
# print('Bounds',point.bounds)
# print('Longitude',point.x)
# print('Latitude',point.y)
# _________________________________________________________
# import matplotlib.pyplot as plt
# from shapely.geometry import Point
# points=[
#     Point(-4,0),
#     Point(-5,12),
#     Point(-6,3),
#     Point(-4,8),
#     Point(-3,2),
#     Point(-1,6)
# ]
# xs=[point.x for point in points]
# ys=[point.y for point in points]
# plt.scatter(xs,ys)
# plt.show()
# _______________________________________________________
# from shapely.geometry import LineString
# line=LineString([(0,0),(1,1)])
# print('Area',line.area)
# print('Length',line.length)
# print('Bounds',line.bounds)
# print('Lonitude, Lattitude',line.xy)
# ______________________________________________________________
import matplotlib.pyplot as plt
from shapely.geometry import LineString,Point
lines=[
    LineString([
        Point(-4,0),
        Point(-5,12),
        Point(-6,3),
    ]),
    LineString(
        [
            Point(-8,7),
            Point(-4,8),
            Point(-2,10),
            Point(2,3),
        ]
    )
]
plt.plot(lines[0].xy[0],lines[0].xy[1])
plt.plot(lines[1].xy[0],lines[1].xy[1])
plt.show()