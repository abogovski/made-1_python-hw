from tic_tac_game import ConsolePlayer, RandomBotPlayer
from io import StringIO
import pytest


def test_players_have_names():
    assert ConsolePlayer('x').name == 'x'
    assert RandomBotPlayer('o').name == 'o'


def test_console_player_should_read_input(mocker):
    mocker.patch('sys.stdin', StringIO('2 3\n'))
    assert ConsolePlayer('o').next_move([(1, 2), (2, 3)]) == (2, 3)


def test_console_player_should_pass_eof_error(mocker):
    mocker.patch('sys.stdin', StringIO('\n'))
    with pytest.raises(EOFError):
        ConsolePlayer('x').next_move([(1, 2)])


def test_console_player_should_pass_keyboard_interrupt(mocker):
    def mock_input(_):
        raise KeyboardInterrupt()

    mocker.patch('builtins.input', mock_input)
    with pytest.raises(KeyboardInterrupt):
        ConsolePlayer('o').next_move([(1, 2)])


def test_console_player_should_retry_on_other_errors(mocker):
    mocker.patch('sys.stdin', StringIO('a b\n1\n1 2\n2 3\n'))
    assert ConsolePlayer('x').next_move([(2, 3)]) == (2, 3)


def test_random_bot_player_should_pick_from_valid_moves():
    assert RandomBotPlayer('o').next_move([(1, 2)]) == (1, 2)
