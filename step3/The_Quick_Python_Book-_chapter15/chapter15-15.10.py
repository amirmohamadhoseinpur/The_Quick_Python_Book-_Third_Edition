'''Update the dimensions of the Rectangle class to be
properties with getters and setters that don’t allow negative sizes.'''

class Rectangle:
    def __init__(self, width, length):
        self.__width = 1
        self.__length = 2
    
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width):
        self.__width = abs(new_width)
    
    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, new_width):
        self.__length = abs(new_width)

