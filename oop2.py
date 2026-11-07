#
import math


class circle(object):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 22/7 * self.radius**2
    def perimeter(self):
        return 22/7* self.radius *2
    def print_details(self):
        print("radius: ", self.radius)
        print("area: ", self.area())
        print("perimeter: ", self.perimeter())

c1 = circle(14)
c2= circle(115.11)
c1.print_details()
c2.print_details()
