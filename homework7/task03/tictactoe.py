"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from typing import List, Optional


def tic_tac_toe_checker(board: List[List]) -> str:
    diagonals_result = check_diagonals(board)
    if diagonals_result:
        return f"{diagonals_result} wins!"

    trans_board = [*zip(*board)]
    for b in [board, trans_board]:
        rows_result = check_rows(b)
        if rows_result:
            return f"{rows_result} wins!"

    return "draw!" if is_draw(board) else "unfinished!"


def check_rows(board: List[List]) -> Optional[str]:
    for row in board:
        if "-" not in row and len(set(row)) == 1:
            return row[0]
    return None


def check_diagonals(board: List[List]) -> Optional[str]:
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0] if board[0][0] != "-" else None
    if len(set([board[i][len(board) - i - 1] for i in range(len(board))])) == 1:
        return board[0][len(board) - 1] if board[0][len(board) - 1] != "-" else None
    return None


def is_draw(board: List[List]) -> bool:
    for row in board:
        if "-" in set(row):
            return False
    return True


if __name__ == "__main__":
    print(tic_tac_toe_checker([["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]]))
    print(tic_tac_toe_checker([["-", "-", "-"], ["-", "o", "o"], ["x", "x", "x"]]))
