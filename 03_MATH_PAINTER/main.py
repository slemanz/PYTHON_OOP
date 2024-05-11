import numpy as np
from PIL import Image

class Canvas:
    '''
        Object where all shapes are going to be drawn
    '''

    def __init__(self, height, width, color):
        self.color = color
        self.height = height
        self.width = width

        # create a 3d numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)

        # change [0, 0, 0], with user given values for color
        self.data[:] = self.color

    def make(self, imagepath):
        """
            converts the current array into an image file
        """
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)



class Rectangle:
    '''
        A rectangle shape that can be dran an a canvas object
    '''
    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color

    
    def draw(self, canvas):
        # draws itself into the canvas
        canvas.data[self.x : self.x + self.width, self.y : self.y + self.height] = self.color

    


class Square:
    '''
        A square shape that can be dran an a canvas object
    '''
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    
    def draw(self, canvas):
        # draws itself into the canvas
        canvas.data[self.x : self.x + self.side, self.y : self.y + self.side] = self.color




canvas = Canvas(height=200, width=300, color=(255, 255, 255))

r1 = Rectangle(x=10, y=60, height=70, width=100, color=(100,100,100))
r1.draw(canvas)

s1 = Square(x=10, y=30, side=30, color=(0,100,222))
s1.draw(canvas)

canvas.make('canvas.png')
print("Arquivo criado")