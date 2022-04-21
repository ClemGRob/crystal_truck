from shutil import move
import pytest
from src import main,truck

def test_get_map():
    result = main.get_map()
    assert isinstance(result, list)
    assert result

def test_move():
    truck1 = truck
    truck1.move(3,3)
    assert truck1.x == 3
    assert truck1.y == 3

