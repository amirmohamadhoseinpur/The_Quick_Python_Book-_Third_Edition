'''Rewrite the code for a Rectangle class to inherit
from Shape. Because squares and rectangles are related, would it make sense
to inherit one from the other? If so, which would be the base class, and which
would inherit?
How would you write the code to add an area() method for the Square
class? Should the area method be moved into the base Shape class and
inherited by circle, square, and rectangle? If so, what issues would result?'''


class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
class Rectangle(Shape):
    def __init__(self,x,y,width,length):
        super().__init__(x, y)
        self.width = width
        self.length = length

'''would it make sense to inherit one from the other?'''
class Rectangle:
    def __init__(self, x, y):
        self.width = y
        self.length = x

    def area(self):
        return self.width * self.length
    
    def perimeter(self):
        return 2 * (self.width + self.length)

class Square(Rectangle):
    def __init__(self, x):
        super().__init__(x,x)


'''How would you write the code to add an area() method for the Square
class?'''

class Square:
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side


'''Should the area method be moved into the base Shape class and
inherited by circle, square, and rectangle? -----------> NO '''

'''If so, what issues would result?  There is nothing to inherit'''