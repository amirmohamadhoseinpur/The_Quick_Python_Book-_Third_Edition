'''Update the code for a Rectan-
gle class so that you can set the dimensions when an instance is created, just
as for the Circle class above. Also, add an area() method.'''

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    def area(self):
        return self.width * self.length