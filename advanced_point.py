from colorpoint import ColorPoint

class AdvancedColorPoint(ColorPoint): #this is a class that inherits from ColorPoint!
    # AdvancedColorpoint is a subclass of ColorPoint, meaning that it inherits all the methods and attributes of ColorPoint
#inhertitance
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = color


new_point = AdvancedColorPpint(10, 10, "blue")
print(new_point)
new_point.color = "red"
print(new_point)


