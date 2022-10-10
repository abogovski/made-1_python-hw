import argparse
import random


class Player:
    def __init__(self, name):
        self.name = name

    def next_move(self, board):
        raise NotImplementedError()


class ConsolePlayer(Player):
    def next_move(self, valid_moves):
        while True:
            try:
                line = input('Player ' + self.name + ' move: ')
                row, col = tuple(map(int, line.split()))
                if (row, col) not in valid_moves:
                    raise RuntimeError(
                        f'{row} {col} is not among valid moves {valid_moves}'
                     )
                return row, col
            except KeyboardInterrupt:
                raise
            except EOFError:
                print('Input ended')
                raise
            except Exception as ex:
                print('Error:', ex)


class RandomBotPlayer(Player):
    def next_move(self, valid_moves):
        return random.choice(valid_moves)


class GameResult:
    def __init__(self, winner):
        self._winner = winner

    def __str__(self):
        if self._winner is None:
            return 'tie'
        return f'player {self._winner} wins'


class GameBoard:
    def __init__(self):
        self._rows = [['.'] * 3 for _ in range(3)]

    def draw(self):
        for row_str in map(' '.join, self._rows):
            print(row_str)

    def get_valid_moves(self):
        moves = []
        for row in range(1, 4):
            for col in range(1, 4):
                if self._rows[row - 1][col - 1] == '.':
                    moves.append((row, col))
        return moves

    def get_lines(self):
        for row_value in self._rows:
            yield ''.join(row_value)

        for col in range(3):
            yield ''.join(self._rows[row][col] for row in range(3))

        yield ''.join(self._rows[row][row] for row in range(3))
        yield ''.join(self._rows[row][-row - 1] for row in range(3))

    def set(self, row, col, val):
        self._rows[row - 1][col - 1] = val


class TicTacGame(object):
    def __init__(self, players):
        self._rounds = 0
        self._players = list(players)
        self.board = GameBoard()

    def play_round(self):
        self._rounds += 1
        print('\nRound ' + str(self._rounds))
        for player in self._players:
            valid_moves = self.board.get_valid_moves()
            if not valid_moves:
                return GameResult(winner=None)

            self.board.draw()
            row, col = player.next_move(valid_moves)
            self.board.set(row, col, player.name)

            winner = self.__get_winner()
            if winner is not None:
                return GameResult(winner)

    def __get_winner(self):
        for line in self.board.get_lines():
            if line == 'xxx':
                return 'x'
            if line == 'ooo':
                return 'o'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('other_player', choices=['console', 'random_bot'])
    args = parser.parse_args()

    other_player = ConsolePlayer
    if args.other_player == 'random_bot':
        other_player = RandomBotPlayer

    game = TicTacGame([ConsolePlayer('x'), other_player('o')])
    game_result = None

    try:
        while game_result is None:
            game_result = game.play_round()
        print(f'\nGame result: {game_result}!')

    except (KeyboardInterrupt, EOFError):
        print('\nGame cancelled by user')

    print('Final state:')
    game.board.draw()


if __name__ == '__main__':
    main()
