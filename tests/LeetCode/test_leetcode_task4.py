import pytest
from src.LeetCode.leetcode_task4 import robot_sim, robot_move


@pytest.mark.parametrize(
    "commands, obstacles, expected",
    (
        ((4, -1, 4, -2, 4), ((2, 4)), 80),
        ((6, -1, -1, 6), (), 36),
        ((4, -1, 3), (), 25),
        ((7, -1, -1, 7), (), 49),
    ),
)
def test_robot_sim(commands, obstacles, expected):
    actual = robot_sim(commands, obstacles)
    assert actual == expected


@pytest.mark.parametrize(
    "position, move_orientation, obstacles, k, expected",
    (
        ((4, 6), (0, 1), ((4, 7),), 5, (4, 6)),
        ((0, 0), (1, 0), ((0, 0),), 5, (5, 0)),
        ((0, 0), (-1, 0), ((1, 0),), 2, (-2, 0)),
        ((-12, 4), (0, -1), ((4, 7), (-11, 3), (-13, 4), (-12, 9)), 4, (-12, 0)),
    ),
)
def test_robot_move(position, move_orientation, obstacles, k, expected):
    new_pos = robot_move(position, move_orientation, obstacles, k)
    assert new_pos == expected
