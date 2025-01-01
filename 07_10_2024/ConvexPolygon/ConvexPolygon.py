
def isConvex(points):
    if len(points) < 4:
        return True
    for i in range(0, len(points)):
        a, b, c = points[i], points[(i + 1) % len(points)], points[(i + 2) % len(points)]
        x = [b[0] - a[0], b[1] - a[1]]
        y = [c[0] - a[0], c[1] - a[1]]
        cur = 1 if x[0]*y[1] >= y[0]*x[1] else -1
        if cur < 0:
            return False
        
    return True
          
          
from math import *  

points = list()
while s := input():
    x, y = map(int, s.split(','))
    points.append((x, y))  
minpoint = min(points, key= lambda x: (x[1], x[0]))
points.sort(key=lambda x: atan2(x[1] - minpoint[1], x[0] - minpoint[0]))
print(isConvex(points))

# from math import *

# def vector_product(o, a, b):
#     return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

# def convex_polygon(points):
#     if len(points) < 3:
#         return False
#     start = min(points, key=lambda p: (p[1], p[0]))
#     points.sort(key=lambda p: atan2(p[1] - start[1], p[0] - start[0]))
#     for i in range(len(points)):
#         o = points[i]
#         a = points[(i + 1) % len(points)]
#         b = points[(i + 2) % len(points)]
#         if vector_product(o, a, b) <= 0:
#             return False 
#     return True

# args = []
# while a:= input():
#     x, y = map(int, a.split(", "))
#     args.append((x, y))
# print(convex_polygon(args))