from tic_tac_game import GameBoard
from collections import Counter
from io import StringIO
import pytest


@pytest.fixture
def example_board():
    board = GameBoard()
    board._rows = [
        ['x', 'o', 'o'],
        ['o', 'x', 'o'],
        ['x', 'x', 'x'],
    ]
    return board


def test_initial_state():
    assert GameBoard()._rows == [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.'],
    ]


def test_draw(example_board, mocker):
    string_io = StringIO()
    mocker.patch('sys.stdout', string_io)

    example_board.draw()
    assert string_io.getvalue() == 'x o o\no x o\nx x x\n'


def test_get_lines(example_board):
    assert sorted(Counter(example_board.get_lines()).items()) == sorted([
        ('xoo', 1),
        ('oxo', 1),
        ('xxx', 2),

        ('xox', 1),
        ('oxx', 2),
        ('oox', 1),
    ])


def test_set(example_board):
    assert example_board._rows[1 - 1][2 - 1] != 'x'
    example_board.set(1, 2, 'x')
    assert example_board._rows[1 - 1][2 - 1] == 'x'
