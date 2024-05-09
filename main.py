import numpy as np
from PIL import Image

class Canvas:
    def __init__(self, w, h, color):
        self.w = w
        self.h = h
        self.color = color

        self.data = np.zeros((self.w, self.h, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, image_path):
        img = Image.fromarray(self.data, 'RGB')
        img.save(image_path)


class Square:
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color


class Rectangle:
    def __init__(self, x, y, a, b, color):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.a, self.y: self.y + self.b] = self.color

canvas = Canvas(400, 500, (255,255,255))
r1 = Rectangle(50, 50, 100, 200, (24,56,200))
r1.draw(canvas)
s1 = Square(150,250, 100, (100, 50, 170))
s1.draw(canvas)
canvas.make("canvas.png")