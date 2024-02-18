from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    def _vertical_check():
        boolean_ans = True
        for j in range(len(board[0])):
            check_vertical = [board[i][j] for i in range(len(board))]
            check_vertical = list(filter(lambda elem: elem != ".", check_vertical))
            boolean_ans = (
                False
                if len(check_vertical) != len(set(check_vertical))
                else boolean_ans
            )
        return boolean_ans

    def _horizontal_check():
        boolean_ans = True
        for i in range(len(board)):
            check_horizontal = [board[i][j] for j in range(len(board[i]))]
            check_horizontal = list(filter(lambda elem: elem != ".", check_horizontal))
            boolean_ans = (
                False
                if len(check_horizontal) != len(set(check_horizontal))
                else boolean_ans
            )
        return boolean_ans

    def _square_check():
        boolean_ans = True
        for i in range(0, len(board), 3):
            for j in range(0, len(board[i]), 3):
                check_square = [
                    board[l][k] for k in range(j, j + 3) for l in range(i, i + 3)
                ]
                check_square = list(filter(lambda elem: elem != ".", check_square))
                boolean_ans = (
                    False
                    if len(check_square) != len(set(check_square))
                    else boolean_ans
                )
        return boolean_ans

    return _vertical_check() and _horizontal_check() and _square_check()
