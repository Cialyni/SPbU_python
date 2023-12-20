import pytest
from io import StringIO
from src.Tests.final_test.Sprites import (
    generate_sprite,
    main,
    generate_sprite_config,
    get_symmetrical_coordinates,
)


def check_symmetrical(sprite) -> bool:
    vertical_sym, horizontal_sym, mixed_sym = True, True, True
    n, m = len(sprite), len(sprite[0])
    for i in range(n):
        for j in range(m):
            if sprite[i][j] != sprite[i][abs(m - j) - 1]:
                horizontal_sym = False
            if sprite[i][j] != sprite[abs(n - i) - 1][j]:
                vertical_sym = False
            if sprite[i][j] != sprite[abs(n - i) - 1][abs(m - j) - 1]:
                mixed_sym = False
    return vertical_sym or horizontal_sym or mixed_sym


@pytest.mark.parametrize(
    "n, m, x, y, type_symmetry, expected_x, expected_y",
    (
        (5, 5, 3, 4, 3, 1, 0),
        (5, 5, 3, 2, 3, 1, 2),
        (5, 5, 2, 2, 2, 2, 2),
        (5, 5, 4, 1, 3, 0, 3),
        (5, 5, 4, 2, 1, 4, 2),
        (5, 5, 4, 2, 3, 0, 2),
        (10, 10, 3, 3, 2, 6, 3),
        (4, 8, 1, 7, 1, 1, 0),
        (7, 3, 1, 0, 1, 1, 2),
        (2, 9, 0, 1, 1, 0, 7),
        (7, 5, 3, 0, 3, 3, 4),
    ),
)
def test_get_symmetrical_coordinates(n, m, x, y, type_symmetry, expected_x, expected_y):
    assert get_symmetrical_coordinates(n, m, x, y, type_symmetry) == (
        expected_x,
        expected_y,
    )


def test_generate_config():
    sprite, symmetry = generate_sprite_config(5, 8)
    assert sprite == [[" " for i in range(5)] for j in range(8)] and symmetry in [
        1,
        2,
        3,
    ]
    sprite, symmetry = generate_sprite_config(1, 1)
    assert sprite == [[" " for i in range(1)] for j in range(1)] and symmetry in [
        1,
        2,
        3,
    ]


@pytest.mark.parametrize(
    "n, m, expected",
    ((5, 5, True), (10, 5, True), (5, 10, True), (100, 100, True)),
)
def test_generate_sprite(n, m, expected):
    sprite = generate_sprite(n, m)
    flag = check_symmetrical(sprite)
    assert flag == expected


@pytest.mark.parametrize(
    "imitation_input, expected",
    (("5 5", "True"), ("10 5", "True"), ("5 10", "True"), ("10 10", "True")),
)
def test_main(monkeypatch, imitation_input, expected):
    monkeypatch.setattr("builtins.input", lambda _: imitation_input)
    imitation_output = StringIO()
    monkeypatch.setattr("sys.stdout", imitation_output)
    main()
    output = imitation_output.getvalue()
    matrix = []
    line = []
    for i in output:
        if i == "\n":
            matrix.append(line)
            line = []
        else:
            line.append(i)
    assert check_symmetrical(matrix) == True
