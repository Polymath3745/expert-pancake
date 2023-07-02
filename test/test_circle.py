import math
from circle import Circle

def test_circle_area():
    # Create a Circle object with radius 3
    circle = Circle(3)

    # Calculate the expected area
    expected_area = math.pi * math.pow(3, 2)

    # Compare the expected area with the actual area from the Circle object
    assert circle.area() == expected_area

def test_circle_circumference():
    # Create a Circle object with radius 3
    circle = Circle(3)

    # Calculate the expected circumference
    expected_circumference = 2 * math.pi * 3

    # Compare the expected circumference with the actual circumference from the Circle object
    assert circle.circumference() == expected_circumference