import random

FULL_BLOCK = "█"
SPACE = " "


def print_sprite(sprite):
    for i in range(len(sprite)):
        for j in range(len(sprite[i])):
            print(sprite[i][j], end="")
        print()


def get_symmetrical_coordinates(
    n: int, m: int, x: int, y: int, type_symmetry: int
) -> (int, int):
    if (
        type_symmetry == 1
    ):  # type_symmetry = 1 - vertical | type_symmetry = 2 - horizontal | type_symmetry = 3 - both
        symmetrical_x, symmetrical_y = x, abs(m - y) - 1
    elif type_symmetry == 2:
        symmetrical_x, symmetrical_y = abs(n - x) - 1, y
    elif type_symmetry == 3:
        symmetrical_x, symmetrical_y = abs(n - x) - 1, abs(m - y) - 1
    return symmetrical_x, symmetrical_y


def generate_sprite_config(n, m):
    sprite_basis = [[SPACE for i in range(n)] for j in range(m)]
    type_symmetry = random.randint(
        1, 3
    )  # type_symmetry = 1 - vertical | type_symmetry = 2 - horizontal | type_symmetry = 3 - both
    return sprite_basis, type_symmetry


def generate_sprite(n: int, m: int):
    sprite, type_symmetry = generate_sprite_config(n, m)
    for i in range(random.randint(1, m * n)):
        x_coord, y_coord = random.randint(0, n - 1), random.randint(0, m - 1)
        symmetrical_x, symmetrical_y = get_symmetrical_coordinates(
            n, m, x_coord, y_coord, type_symmetry
        )
        sprite[y_coord][x_coord] = FULL_BLOCK
        sprite[symmetrical_y][symmetrical_x] = FULL_BLOCK
    return sprite


def main():
    try:
        n, m = map(int, input("Hellow! Inpup N and M of your sprite:\n").split())
        s = ""
        while not s:
            sprite = generate_sprite(n, m)
            print_sprite(sprite)
            s = input("\nTap Enter to Continue and something else to Exit\n")
    except ValueError:
        print("ERROR!\nInput integer N and M!")


if __name__ == "__main__":
    main()
