class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x \
                and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False

    def distance_from_point(self, point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5

class Rectangle:

    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright


point1 = Point(1,1)
point2 = Point(3,3)

print(point1.distance_from_point(point2))

rect = Rectangle(point1, point2)

point3 = Point(2,2)
print(point3.falls_in_rectangle(rect))
