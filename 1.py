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
    

    def __add__(self,Other):
        return (self.getx()+Other.x, self.gety()+Other.y)

    def __sub__(self,Other):
        return (self.getx()-Other.x, self.gety()+Other.y)
    
    def halfway(self,terget):
        midx=(self.x+terget.x)/2
        midy=(self.y+terget.y)/2
        return point(midx,midy)

    def __str__(self):
        return '(x={},y={}) '.format(self.x, self.y)


p=point(3,4)
q=point(2,4)

mid= p.halfway(q)

print(mid)
print(mid.getx())
print(mid.gety())