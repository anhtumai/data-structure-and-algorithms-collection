"""
N queens is the problem of placing N chess queens on an NxN chessboard
so that no 2 queens attack each other.

Solution: We will place queens to the board continuously.
If the new queen position is not valid, we remove the queen from that position and continue with other positions.
"""

import copy


def nqueens(n: int):
    """
    Return a list of 2-dimension array marking queens position
    """

    def backtrack(
        row: int,
        diagonals_set: set[int],
        anti_diagonals_set: set[int],
        cols_set: set[int],
        state: list[list[bool]],
    ):
        def place_queen(row: int, col: int):
            cols_set.add(col)
            diagonals_set.add(row - col)
            anti_diagonals_set.add(row + col)
            state[row][col] = True

        def remove_queen(row: int, col: int):
            cols_set.remove(col)
            diagonals_set.remove(row - col)
            anti_diagonals_set.remove(row + col)
            state[row][col] = False

        def can_queen_be_placed(row: int, col: int):
            return not (
                col in cols_set
                or (row - col) in diagonals_set
                or (row + col) in anti_diagonals_set
            )

        if row == n:
            solutions.append(copy.deepcopy(state))
            return

        for col in range(n):
            if not can_queen_be_placed(row, col):
                continue
            place_queen(row, col)
            backtrack(row + 1, diagonals_set, anti_diagonals_set, cols_set, state)
            remove_queen(row, col)

    solution_board = [[False for _ in range(n)] for _ in range(n)]
    solutions: list[list[list[bool]]] = []
    backtrack(0, set(), set(), set(), solution_board)
    return solutions


def main():
    print(nqueens(4))


main()
