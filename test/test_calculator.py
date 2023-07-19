import pytest
from helpers.calculator import Calculator

def test_getter():
    # Arrange
    calc = Calculator(10,11)
    expected_x = 10
    expected_y = 11

    # Act
    actual_x = calc.x
    actual_y = calc.y

    # Assert 
    assert expected_x == actual_x
    assert expected_y == actual_y

def test_setter():
    # Arrange
    calc = Calculator(0,0)
    calc.x = 5
    calc.y = 6

    expected_x = 5
    expected_y = 6

    # Act
    actual_x = calc.x
    actual_y = calc.y

    # Assert
    assert expected_x == actual_x
    assert expected_y == actual_y