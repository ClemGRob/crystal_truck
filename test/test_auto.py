from src import truck, file_tool, map

# file_tool


def test_write_from_scratch():
    name = "test.txt"
    content = "test decriture sur le fichier"
    file_tool.write_from_sratch(content, name)
    with open(name, "r") as file:
        content = file.read()
    assert content == "test decriture sur le fichier"


def test_write_new_line():
    name = "test.txt"
    content = "test decriture sur le fichier"
    file_tool.write_from_sratch(content, name)
    content2 = "test"
    file_tool.write_new_line(content2, name)
    with open(name, "r") as file:
        content = file.read()
    assert content == "test decriture sur le fichiertest"


# truck

turn = 0


def test_abs_value():
    truck1 = truck.truck(None, 1, 1)
    a = 1
    i = -1
    a = truck1.abs_value(a)
    i = truck1.abs_value(i)
    assert a == 1
    assert i == 1


def test_init():
    map1 = [["0", "2", "0", "0"], ["0", "0", "0", "0"]]
    truck1 = truck.truck(map1, 10, 10, 10)

    assert truck1.x == 10
    assert truck1.y == 10
    assert truck1.id == 10
    assert truck1.map == map1


def test_move_up():
    truck1 = truck.truck(None, 1, 1)
    fichier = "test1.txt"
    truck1.move_up(turn, fichier)
    assert truck1.y == 2


def test_move_down():
    truck1 = truck.truck(None, 1, 1)
    fichier = "test1.txt"
    truck1.move_down(turn, fichier)
    assert truck1.y == 0


def test_move_left():
    fichier = "test1.txt"
    truck1 = truck.truck(None, 1, 1)
    truck1.move_left(turn, fichier)
    assert truck1.x == 0


def test_move_right():
    truck1 = truck.truck(None, 1, 1)
    fichier = "test1.txt"
    truck1.move_right(turn, fichier)
    assert truck1.x == 2


def test_digg():
    map = [["0", "2", "0", "0"], ["0", "0", "0" "0"]]
    truck1 = truck.truck(map, 0, 1)
    fichier = "test1.txt"
    truck1.digg(turn, fichier)
    truck1.digg(turn, fichier)
    assert truck1.map[0][1] == "0"


def test_recherch():
    map = [["0", "2", "0", "0"], ["0", "0", "0" "0"]]
    truck1 = truck.truck(map, 1, 1)
    x_ref, y_ref = truck1.recherch()
    assert x_ref == 0
    assert y_ref == 1


def test_recherch2():
    map = [["0", "2", "0", "0"], ["0", "0", "0" "0"]]
    truck1 = truck.truck(map, 1, 1)
    x_ref, y_ref = truck1.recherch(0, 0, 1, 3)
    assert x_ref == 0
    assert y_ref == 1


def test_recherch3():
    map = [["0", "2", "0", "0"], ["0", "0", "0" "0"]]
    truck1 = truck.truck(map, 1, 3)
    x_ref, y_ref = truck1.recherch(0, 0, 1, 3)
    assert x_ref == 0
    assert y_ref == 1


def test_get_path_to_dest():
    map = [["2", "0", "0", "0"], ["0", "0", "0" "0"]]
    truck1 = truck.truck(map, 1, 1)
    fichier = "test1.txt"
    truck1.get_path_to_destination(0, 0, turn, fichier)
    assert truck1.map[0][0] == "1"
    truck1.get_path_to_destination(0, 0, turn, fichier)
    assert truck1.map[0][0] == "0"


def test_get_path_to_dest2():
    map = [["0", "0", "0", "0"], ["0", "2", "0" "2"]]
    truck1 = truck.truck(map, 0, 0)
    fichier = "test1.txt"
    truck1.get_path_to_destination(1, 1, turn, fichier)
    assert truck1.map[1][1] == "1"
    truck1.get_path_to_destination(1, 1, turn, fichier)
    assert truck1.map[1][1] == "0"


def test_write():
    name = "map1.txt"
    truck1 = truck.truck(None, 1, 1, 33)
    truck1.write(turn, "GOOD", name)
    with open(name, "r") as file:
        content = file.read()
    assert content == "0 GOOD 33 1 1\n"


# map
def test_get_map():
    result, a, b, c = map.get_map()
    assert isinstance(result, list)
    assert result
