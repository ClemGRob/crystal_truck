import pytest


def func(x):
    return x + 1

def test_count():
    assert func(3) == 4


