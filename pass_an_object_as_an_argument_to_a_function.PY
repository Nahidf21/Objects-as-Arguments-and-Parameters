import math

class Point:
    
    def __init__(self,initx,inity) :
        self.x=initx
        self.y=inity

    def getx(self):
        return self.x
    def gety(self):
        return self.y
    
    def dic_from_origin(self):
        
        x=math.sqrt(self.x**2+self.y**2)
        return x

point1= Point(2,3)

print(point1.dic_from_origin())