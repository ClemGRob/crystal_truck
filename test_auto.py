import pytest
import game

def test_get_map():
    result = game.get_map()
    assert isinstance(result, list)
    assert result

    

