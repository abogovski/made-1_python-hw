from tic_tac_game import GameResult


def test_win():
    assert str(GameResult('x')) == 'player x wins'


def test_tie():
    assert str(GameResult(None)) == 'tie'
