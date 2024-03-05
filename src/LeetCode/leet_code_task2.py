from typing import List, Any


def _vertical_check(board: List[List[str]]):
    for j in range(len(board[0])):
        check_vertical = [board[i][j] for i in range(len(board))]
        check_vertical = list(filter(lambda elem: elem != ".", check_vertical))
        if len(check_vertical) != len(set(check_vertical)):
            return False
    return True


def _horizontal_check(board: List[List[str]]):
    transpose_board = [
        [board[j][i] for j in range(len(board[i]))] for i in range(len(board))
    ]
    return _vertical_check(list(transpose_board))


def _square_check(board: List[List[str]]):
    for i in range(0, len(board), 3):
        for j in range(0, len(board[i]), 3):
            check_square = [
                board[l][k] for k in range(j, j + 3) for l in range(i, i + 3)
            ]
            check_square = list(filter(lambda elem: elem != ".", check_square))
            if len(check_square) != len(set(check_square)):
                return False
    return True


def is_valid_sudoku(board: List[List[str]]) -> bool:
    return _vertical_check(board) and _horizontal_check(board) and _square_check(board)
