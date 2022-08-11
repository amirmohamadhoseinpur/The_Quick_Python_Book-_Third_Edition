'''Write a class method similar to total_area()
that returns the total circumference of all circles.'''




class Circle:
    """Circle class"""
    all_circles = []
    pi = 3.14159
    def __init__(self, r=1):
        """Create a Circle with the given radius"""
        self.radius = r
        self.__class__.all_circles.append(self)
    def circumference(self):
        """determine the circumference of the Circle"""
        return self.__class__.pi * self.radius * 2
    @classmethod
    def total_circumference(cls):
        total = 0
        for c in cls.all_circles:
            total = total + c.circumference()
        return total