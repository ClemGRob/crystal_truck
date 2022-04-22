from shutil import move
import pytest
from src import main,truck


def test_get_map():
    result = main.get_map()
    assert isinstance(result, list)
    assert result

def test_move_up():
    truck1 = truck.truck(None,1,1)
    truck1.move_up()
    assert truck1.y == 2

def test_move_down():
    truck1 = truck.truck(None,1,1)
    truck1.move_down()
    assert truck1.y == 0

def test_move_left():
    truck1 = truck.truck(None,1,1)
    truck1.move_left()
    assert truck1.x == 0

def test_move_right():
    truck1 = truck.truck(None,1,1)
    truck1.move_right()
    assert truck1.x == 2

def test_move():
    truck1 = truck.truck(None,1,1)
    truck1._move(3,3)
    assert truck1.x == 3
    assert truck1.y == 3

def test_digg():
    map = [["0","2","0","0"],["0","0","0""0"]]
    truck1 = truck.truck(map,0,1)
    truck1.digg()
    assert truck1.map[0][1] == '0'

