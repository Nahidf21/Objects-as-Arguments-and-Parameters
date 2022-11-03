import math

class Point:
    

    def __init__(self,initx,inity) :

        self.x=initx
        self.y=inity

    def getx(self):
        return self.x

    def gety(self):
        return self.y
    
    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

def distance_between_two_points(point1,point2):
    xdiff = point1.getx() - point2.getx()
    ydiff = point1.gety() - point2.gety()
    distance= math.sqrt(xdiff**2 + ydiff**2)
    return distance

p= Point(2,3)
q= Point(0,0)
print(distance_between_two_points(p,q))
