from lab_python_oop.color import Color
from lab_python_oop.figure import Figure

class Rectangle(Figure):

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = Color()
        self.color.colorproperty = color

    def area(self):
        return self.width * self.height