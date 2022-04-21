import pytest
import src.game

def test_get_map():
    result = src.main.get_map()
    assert isinstance(result, list)
    assert result

    

