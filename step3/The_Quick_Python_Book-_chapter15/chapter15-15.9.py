'''Modify the Rectangle class’s code to
make the dimension variables private. What restriction will this modification
impose on using the class?'''


class Rectangle:
    def __init__(self):
        self.__width = 1
        self.__length = 2

rec = Rectangle()
# rec.__length and rec.__width can’t be seen outside the methods of Rectanlge class
print(rec.__length) # AttributeError will occur