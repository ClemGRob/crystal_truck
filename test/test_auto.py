from shutil import move
from unicodedata import name
import pytest
from src import truck,file_tool
import main

#truck
truck1 = truck.truck(None,1,1)
turn = 0

def test_abs_value():
    a = 1
    i = -1
    truck1.abs_value(a)
    truck1.abs_value(i)
    assert a == 1
    assert i == 1


def test_init():
    map1 = [["0","2","0","0"],["0","0","0""0"]]
    truck1 =truck.truck(map1,10,10,10)

    assert truck1.x == 10
    assert truck1.y == 10
    assert truck1.id == 10
    assert truck1.map == map1


def test_move_up():
    truck1.move_up(turn)
    assert truck1.y == 2

def test_move_down():
    truck1.move_down(turn)
    assert truck1.y == 0

def test_move_left():
    truck1.move_left(turn)
    assert truck1.x == 0

def test_move_right():
    truck1.move_right(turn)
    assert truck1.x == 2

def test_digg():
    map = [["0","2","0","0"],["0","0","0""0"]]
    truck1 = truck.truck(map,0,1)
    truck1.digg(turn)
    truck1.digg(turn)
    assert truck1.map[0][1] == '0'

def test_recherch():
    map = [["0","2","0","0"],["0","0","0""0"]]
    truck1 = truck.truck(map,4,4)
    x_ref,y_ref = truck1.recherch()
    assert x_ref == 0
    assert y_ref == 1 

def test_get_path_to_dest():
    map = [["0","2","0","0"],["0","0","0""0"]]
    truck1 = truck.truck(map,4,4)
    truck1.get_path_to_destination(0,1,turn)
    assert truck1.map[0][1] == '0'

def test_wright():
    name = "map1.txt"
    truck1 = truck.truck(None,1,1,33)
    truck1.wright(turn,"GOOD",name)
    with open (name, "r") as file:
        content = file.read
    assert content == "0 GOOD 33 1 1"

#map
def test_get_map():
    result = main.get_map()
    assert isinstance(result, list)
    assert result

#file_tool
def test_write_from_scratch():
    name = "test.txt"
    content ="test d'écriture sur le fichier"
    file_tool.write_from_sratch(content, name )
    with open (name, "r") as file:
        content = file.read
    assert content == "test d'écriture sur le fichier"

def test_write_new_line():
    name = "test.txt"
    content ="test d'écriture sur le fichier"
    file_tool.write_from_sratch(content, name )
    content2 = "test"
    file_tool.write_new_line(content2,name)
    with open (name, "r") as file:
        content = file.read
    assert content == "test d'écriture sur le fichier test"



