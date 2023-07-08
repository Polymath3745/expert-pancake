import pytest
from evenSum import calculate_even_sum

def test_calculate_even_sum():
    assert calculate_even_sum(10) == 30
    assert calculate_even_sum(5) == 6
    assert calculate_even_sum(0) == 0