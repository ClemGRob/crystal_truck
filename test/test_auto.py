from shutil import move
from . import main
import pytest
from src import truck

def test_get_map():
    result = main.get_map()
    assert isinstance(result, list)
    assert result

def test_move():
    truck1 = truck.truck(None,1,1)
    truck1._move(3,3)
    assert truck1.x == 3
    assert truck1.y == 3

