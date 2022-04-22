from shutil import move
import pytest
from src import truck,file_tool
import main

#truck
truck1 = truck.truck(None,1,1)

def test_init():
    map1 = [["0","2","0","0"],["0","0","0""0"]]
    truck1 =truck.truck(map1,10,10,10)

    assert truck1.x == 10
    assert truck1.y == 10
    assert truck1.id == 10
    assert truck1.map == map1

def test_abs_value():
    i = 3
    truck1.abs_value(i)
    assert i == 3
    i == -5
    truck1.abs_value(i)
    assert i == 5

def test_move_up():
    truck1.move_up()
    assert truck1.y == 2

def test_move_down():
    truck1.move_down()
    assert truck1.y == 0

def test_move_left():
    truck1.move_left()
    assert truck1.x == 0

def test_move_right():
    truck1.move_right()
    assert truck1.x == 2

def test_move():
    truck1._move(3,3)
    assert truck1.x == 3
    assert truck1.y == 3

def test_digg():
    map = [["0","2","0","0"],["0","0","0""0"]]
    truck1 = truck.truck(map,0,1)
    truck1.digg()
    truck1.digg()
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
    truck1.get_path_to_destination(0,1)
    assert truck1.map[0][1] == '0'

# def test_wright():
#     truck1 = truck.truck(None,1,1)
#     truck1.wright(action = "GOOD")
#     assert 

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



#def test_wright():
#   truck1 = truck.truck(None,1,1)
#   truck1.wright(action = "GOOD")
#   assert 