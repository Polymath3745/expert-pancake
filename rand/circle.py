import math

class Circle:
    def __init__(self, radius):
        self.m_radius = radius

    def get_radius(self):
        return self.m_radius
    
    def set_radius(self, radius):
        self.m_radius = radius

    def area(self):
        return math.pi * math.pow(self.m_radius, 2)

    def circumference(self):
        return 2 * math.pi * self.m_radius


def main():
    circle = Circle(2)
    print(circle.area())
    print(circle.circumference())


if __name__== '__main__':
    main()