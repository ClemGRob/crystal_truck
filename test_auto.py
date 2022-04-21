from asyncio.windows_events import NULL
import game
import sys
import io
import pytest
import src.main
from contextlib import redirect_stdout





def test_get_map():
    result = src.main.get_map()
    assert isinstance(result, list)
    assert result

    

