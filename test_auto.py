import pytest
import src.main






def test_get_map():
    result = src.main.get_map()
    assert isinstance(result, list)
    assert result

    

