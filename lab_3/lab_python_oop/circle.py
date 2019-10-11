from lab_python_oop.figure import Figure
from lab_python_oop.color import Color
import math

class Circle(Figure):

    def __init__(self, radius, color):
        self.radius = radius
        self.color = Color()
        self.color.colorproperty = color

    def area(self):
        return math.pi * (self.radius ** 2)