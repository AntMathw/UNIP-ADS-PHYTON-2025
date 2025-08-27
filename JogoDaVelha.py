#Jogo da Velha

from enum import IntEnum

design = """
{n0} | {n1} | {n2}
{n3} | {n4} | {n5}
{n6} | {n7} | {n8}
"""

class Players(IntEnum):
    X = 0
    O = 1
    UNSET = 2
    
class TTTImplementation:
    __slots__ = ('table', 'turn')

    def __init__(self):
        self.table = (
            [Players.UNSET, Players.UNSET, Players.UNSET],
            [Players.UNSET, Players.UNSET, Players.UNSET],
            [Players.UNSET, Players.UNSET, Players.UNSET],
        )

        self.turn = Players.X

    def _valid_moves_iter(self):
        for column, rows in enumerate(self.table):
            for row, value in enumerate(rows):
                if value == Players.UNSET:
                    yield (3 * column + 1) + row

    def _get_position(self, n):
        return self.table[n // 3][n % 3]

    @property
    def valid_moves(self):
        return tuple(self._valid_moves_iter())

    def make_move(self, n):
        if not (0 <= n < 9):
            raise ValueError('n should be in range(9)')

        if self._get_position(n) != Players.UNSET:
            raise ValueError(f'{n} is already taken.')

        column = n // 3
        row = n % 3

        self.table[column][row] = self.turn
        self.turn = Players(not self.turn)

    @property
    def winner(self):
        check = self._get_position

        # Check vertical
        for n in range(3):
            if check(n) == check(n + 3) == check(n + 6) != Players.UNSET:
                return check(n)

        # Check horizontal:
        for n in range(3):
            col = 3 * n
            if check(col) == check(col + 1) == check(col + 2) != Players.UNSET:
                return check(col)

        # Check diagonals
        if check(0) == check(4) == check(8) != Players.UNSET:
            return check(0)
        if check(2) == check(4) == check(6) != Players.UNSET:
            return check(2)

        try:
            next(self._valid_moves_iter())
        except StopIteration:
            return Players.UNSET
        else:
            return None

def print_table(table):
    mapping = {0: '\033[32mX\033[m', 1: '\033[31mO\033[m'}
    pos = {f'n{n}': mapping.get(table[n // 3][n % 3], f'\033[90m{n}\033[m') for n in range(0, 9)}
    print(design.format(**pos))

game = TTTImplementation()
while game.winner is None:
    print_table(game.table)
    while True:
        try:
            n = int(input(f'{"O" if game.turn else "X"} > '))
            game.make_move(n)
        except ValueError:
            pass
        else:
            break
print_table(game.table)
if game.winner is Players.X:
    print(f'X ganhou!')
elif game.winner is Players.O:
    print(f'O ganhou!')
else:
    print('Deu velha!')
