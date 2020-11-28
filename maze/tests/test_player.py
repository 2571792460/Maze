from maze.models.player import Player
import pytest

def test_constructor():
    """
    ID : 020A
    This is to test the Player class constructor
    :return: None
    """
    player1 = Player()

    assert hasattr(player1, '_backpack')
    assert player1._backpack == []


def test_pick_up_item():
    """
    This is to test if the player can pick up an item
    :return: None
    """
    player1 = Player()

    assert hasattr(player1, 'pick_up_item')

    player1.pick_up_item("A")
    assert player1._backpack == ["A"]
