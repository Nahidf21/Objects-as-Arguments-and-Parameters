import math
class point:

    """ point class for representing and manipuleting x,y coordinats. """

    def __init__(self, initx,intiy):
        self.x=initx
        self.y=intiy

    def getx(self):
        return self.x
    def gety(self):
        return self.y

    def distance(self, point2):
        xdistance= (point2.getx()-self.x)
        ydistance=(point2.gety()-self.y)

        distance= math.sqrt(xdistance**2+ydistance**2)

        return distance
    def __str__(self):
        return 'Our points are point A ({},{}) '.format(self.x, self.y)

    def __add__(self,Other):
        return (self.getx()+Other.x, self.gety()+Other.y)



p=point(3,4)
q=point(2,4)

print(p.distance(q))
print(p)
print(p+q)