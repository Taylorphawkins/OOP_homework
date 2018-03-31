# Udemy homework
import math

class Line():
    
    def __init__(self,coor1,coor2):
        pass
    
    def distance(p0, p1):
        return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)
    
    def slope(x1, y1, x2, y2):
        m = (y2-y1)/(x2-x1)
        return m

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

li.distance