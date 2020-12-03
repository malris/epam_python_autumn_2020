from typing import List

import pytest
from homework7.task03.tictactoe import tic_tac_toe_checker


@pytest.mark.parametrize(
    ["board", "expected_result"],
    [
        [[["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]], "unfinished!"],
        [[["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]], "unfinished!"],
        [[["-", "-", "-"], ["-", "o", "o"], ["x", "x", "x"]], "x wins!"],
        [[["o", "x", "o"], ["o", "x", "x"], ["x", "o", "x"]], "draw!"],
    ],
)
def test_tic_tac_toe_checker_conditions(board: List[List], expected_result: str):
    assert tic_tac_toe_checker(board) == expected_result
