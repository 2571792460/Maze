from unittest.mock import patch, mock_open

from models.score_manager import ScoreManager
from models.score import Score
import pytest


@pytest.fixture
def new_player():
    """
    Fixture for a new player
    """
    return Score(player_name="Rico", score=80, date="Sun Nov 29 15:59:51 2020")


def test_items_text(new_player):
    """
    ID : 040A
    Test instance was convert into text properly
    Must be a list of strings, each string is:
    <player_name>: <score> at <date>
    """
    fm = ScoreManager()
    fm.add_item(new_player)
    assert fm.items_text == ["Rico: 80 at Sun Nov 29 15:59:51 2020"]


def test_add_unique_player(new_player):
    """
    ID : 040B
    Tests that the manager does not list duplicate player items
    """
    fm = ScoreManager()
    fm.add_item(new_player)
    fm.add_item(new_player)
    assert fm.count() == 1


def test_items(new_player):
    """
    ID : 040C
    Tests the 'items' property
    """
    fm = ScoreManager()
    fm.add_item(new_player)
    assert fm.items == [new_player]


DATA = """[{"player_name": "Group5", "score": 86, "date": "Sun Nov 29 15:59:51 2020"}]"""


def test_check_load_json_filename():
    """
    ID : 040D
    Makes sure that `open` is called with the correct file name in `load_from_json`
    """
    with patch('builtins.open', mock_open(read_data=DATA)) as mock_file:
        fm = ScoreManager()
        fm.load_from_json("test.json")

        assert "test.json" in tuple(mock_file.call_args)[0]


def test_load_from_json():
    """
    ID : 040D
    Patches `open` to load one Score item in the manager, and check its attributes
    """
    with patch('builtins.open', mock_open(read_data=DATA)) as mock_file:
        fm = ScoreManager()
        fm.load_from_json("test.json")
        assert len(fm.items) == 1
