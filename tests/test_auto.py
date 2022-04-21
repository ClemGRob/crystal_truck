import pytest
from src import main

def test_get_map():
    result = main.get_map()
    assert isinstance(result, list)
    assert result

    

