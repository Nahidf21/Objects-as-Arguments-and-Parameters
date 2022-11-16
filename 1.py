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


p=point(3,4)
q=point(0,0)

print(p.distance(q))