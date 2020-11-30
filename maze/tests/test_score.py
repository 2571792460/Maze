from models.score import Score
import pytest

@pytest.fixture
def new_player():
    """Fixturen for a new player"""
    return Score(player_name="Rico", score=80, date="Sun Nov 29 15:59:51 2020")


def test_score_attributes(new_player):
    """Check the class has the correct attributs"""
    assert new_player.player_name == "Rico"
    assert new_player.score == 80
    assert new_player.date == "Sun Nov 29 15:59:51 2020"


def test_score_type():
    """Check score input is an integer"""
    with pytest.raises(TypeError):
        Score(player_name="Oliver", score="ten", date="Sun Nov 29 15:59:51 2020")
    assert True


def test_score_list_append(new_player):
    """Check score list append corectlly"""
    assert new_player.score_list == [{"player_name": "Rico", "score": 80, "date": "Sun Nov 29 15:59:51 2020"}]
    assert len(new_player.score_list) == 1

