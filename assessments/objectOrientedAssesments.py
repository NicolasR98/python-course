"""
Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
"""

import math

class Line():
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2 - y1) / (x2 - x1)

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

print(li.distance())    # 9.433981132056603
print(li.slope())       # 1.6


"""
Fill in the class
"""

class Cylinder():
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius
        self.area = math.pi * radius**2

    def volume(self):
        return self.area * self.height

    def surface_area(self):
        return (2 * math.pi * self.radius * self.height) + (2 * self.area)

c = Cylinder(2,3)
print(c.volume())       # 56.548667764616276
print(c.surface_area()) # 94.24777960769379