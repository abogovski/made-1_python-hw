from tic_tac_game import TicTacGame, Player


class MockPlayer(Player):
    def __init__(self, name, moves):
        super().__init__(name)
        self._moves = list(moves)
        self._move_idx = 0

    def next_move(self, valid_moves):
        assert self._move_idx < len(self._moves), 'No more moves'
        move = self._moves[self._move_idx]
        self._move_idx += 1

        assert move in valid_moves
        return move


def test_x_win():
    game = TicTacGame([
        MockPlayer('x', [(2, 2), (3, 3), (2, 3), (2, 1)]),
        MockPlayer('o', [(1, 1), (3, 2), (1, 3)]),
    ])

    game_result = None
    while game_result is None:
        game_result = game.play_round()

    assert game_result._winner == 'x'
    assert game.board._rows == [
        ['o', '.', 'o'],
        ['x', 'x', 'x'],
        ['.', 'o', 'x'],
    ]


def test_o_win():
    game = TicTacGame([
        MockPlayer('x', [(1, 2), (1, 3), (2, 3)]),
        MockPlayer('o', [(1, 1), (2, 2), (3, 3)]),
    ])

    game_result = None
    while game_result is None:
        game_result = game.play_round()

    assert game_result._winner == 'o'
    assert game.board._rows == [
        ['o', 'x', 'x'],
        ['.', 'o', 'x'],
        ['.', '.', 'o'],
    ]


def test_tie():
    game = TicTacGame([
        MockPlayer('x', [(1, 1), (1, 3), (2, 2), (2, 3), (3, 2)]),
        MockPlayer('o', [(1, 2), (2, 1), (3, 1), (3, 3)]),
    ])

    game_result = None
    while game_result is None:
        game_result = game.play_round()

    assert game_result._winner is None
    assert game.board._rows == [
        ['x', 'o', 'x'],
        ['o', 'x', 'x'],
        ['o', 'x', 'o'],
    ]
