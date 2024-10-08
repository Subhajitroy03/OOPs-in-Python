class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"({self.x},{self.y})"
    def distance(self,other):
        return (((self.x-other.x)**2)+((self.y-other.y)**2))**0.5
    def is_collinear(self,first,second):
        area=self.x*(first.y-second.y)+first.x*(second.y-self.y)+second.x*(self.y-second.y)
        if(area!=0):
            return True
        else:
            return False
    def slope(self,other):
        return (self.y-other.y)/(self.x-other.x)
    def __add__(self,other):
        p=point(0,0)
        p.x=self.x+other.x
        p.y=self.y+other.y
        return p
    def __sub__(self,other):
        p=point(0,0)
        p.x=self.x-other.x
        p.y=self.y-other.y
        return p
    def magnitude(self):
        p=point(0,0)
        return self.distance(p)
    def midpoint(self,other):
        p=point(0,0)
        p.x=(self.x+other.x)/2
        p.y=(self.y+other.y)/2
        return p
    def quadrant(self):
        if(self.x>0 and self.y>0):
            return "First"
        elif(self.x<0 and self.y>0):
            return "Second"
        elif(self.x<0 and self.y<0):
            return "Third"
        else:
            return "Fourth"
    def reflect_x(self):
        p=point(0,0)
        p.x=self.x
        p.y=-self.y
        return p
    def reflect_y(self):
        p=point(0,0)
        p.x=-self.x
        p.y=self.y
        return p
    def reflect_origin(self):
        p=point(0,0)
        p.x=-self.x
        p.y=-self.y
        return p
    def __eq__(self,other):
        return(self.x==other.x and self.y==other.y)

p1=point(5,2)
p2=point(-5,-2)
p3=point(-6,-4)
print("Distance: ",p1.distance(p2))
print("Slope: ",p1.slope(p3))
print("ADD:  ",p1+p2)
print("Sub:  ",p1-p2)
print("Magnitude:  ",p1.magnitude())
print("Midpoint: ",p1.midpoint(p2))
print(p3.quadrant())
print(p3.reflect_origin())
print(p1==p2)