from models.maze import Maze
import pytest


def test_constructor():
    """
    ID : 010A
    This is to test the Maze class constructor
    :return: None
    """
    reg_maze = Maze("../maze.txt")
    assert hasattr(reg_maze, '_map')
    assert hasattr(reg_maze, '_numRow')
    assert hasattr(reg_maze, '_numCol')
    assert hasattr(reg_maze, '_player')
    assert hasattr(reg_maze, '_player_position')


def test_can_move_to():
    """
    This is to test if can move to that spot
    :return: None
    """
    reg_maze = Maze("../maze.txt")

    assert reg_maze.can_move_to(1, 1)
    assert not reg_maze.can_move_to(0, 0)


def test_is_item():
    """
    This is to test if the spot is an item
    :return: None
    """
    reg_maze1 = Maze("../maze_1.txt")

    assert reg_maze1.is_item(1, 1)
    assert not reg_maze1.is_item(1, 3)


def test_is_exit():
    """
    This is to test if this is the exit spot
    :return: None
    """
    reg_maze1 = Maze("../maze.txt")

    assert reg_maze1.is_exit(4, 6)
    assert not reg_maze1.is_exit(1, 1)