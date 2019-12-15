class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __sub__(self,other):
        return Point(self.x - other.x, self.y-other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f'P({self.x},{self.y})'


def Odleglodc(p1,p2):
    if p1 == p2:
        print('Odleglosc wynosi 0')
    else:
        print(p1-p2)
Odleglodc(p1 = Point(3,4),p2 = Point(3,4))

