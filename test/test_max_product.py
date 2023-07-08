import pytest
from max_product import find_max_product

def test_find_max_product():
    assert find_max_product([1,2,3,4,5]) == 20
    assert find_max_product([5,6,7,8]) == 56
    assert find_max_product([0,0,0]) == 0