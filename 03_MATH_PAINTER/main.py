from canvas import Canvas
from shapes import Rectangle, Square


canvas = Canvas(height=200, width=500, color=(255, 255, 255))

r1 = Rectangle(x=10, y=60, height=70, width=100, color=(100,100,100))
r1.draw(canvas)

s1 = Square(x=10, y=30, side=30, color=(0,100,222))
s1.draw(canvas)

canvas.make('canvas.png')
print("Arquivo criado")