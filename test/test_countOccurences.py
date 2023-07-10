import pytest
from countOccurences import count_occurences

def test_count_occurences():
    assert count_occurences([1,1,1,2,3,4,5,6,7], 1) == 3
    assert count_occurences([1,1,1,2,3,4,5,6,7], 3) == 1