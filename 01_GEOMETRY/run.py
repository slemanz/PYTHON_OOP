from random import randint
import turtle


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

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x -self.point1.x) * (self.point2.y - self.point1.y)


class GuiRectangle(Rectangle):

    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)

        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90) # 90 degrees
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
 
        turtle.done()

gui_rectangle = GuiRectangle(
    Point(randint(0,400), randint(0,400)),
    Point(randint(10,400), randint(10,400))
)

myturtle = turtle.Turtle()
gui_rectangle.draw(canvas=myturtle)



'''
# create rectangle object
rectangle = Rectangle(
    Point(randint(0,400), randint(0,400)),
    Point(randint(10,400), randint(10,400))
)

# Print rectangle coordinates
print("Rectangle coordinates: ",
        rectangle.lowleft.x, ",",
        rectangle.lowleft.y, "and",
        rectangle.upright.x, ",",
        rectangle.upright.y)

# get point and area from user
user_point = Point(float(input("Guess X: ")), float(input("Guess Y: ")))
user_area = float(input("Guess rectangle area: "))

# Print out the game result
print("Your point was inside rectangle: ", user_point.falls_in_rectangle(rectangle))
print("Your area was:", rectangle.area())
'''