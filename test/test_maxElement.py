import pytest
from maxElement import find_max_element

def test_find_max_element():
    assert find_max_element([1,2,3,4,5]) == 5
    #assert find_max_element([1,2,34,5]) == 34