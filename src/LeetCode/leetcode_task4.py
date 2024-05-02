from typing import List, Tuple


def robot_move(
    current_pos: Tuple[int, int],
    move_orientation: Tuple[int, int],
    obstacles: Tuple[Tuple[int, int]],
    k: int,
):
    x, y = current_pos
    for i in range(k):
        if (x + move_orientation[0], y + move_orientation[1]) in obstacles:
            return x, y
        x += move_orientation[0]
        y += move_orientation[1]
    return x, y


def robot_sim(commands: Tuple[int], obstacles: Tuple[Tuple[int, int]]) -> int:
    ans = 0
    current_pos = (0, 0)  # x, y
    move_orientations = ((0, 1), (1, 0), (0, -1), (-1, 0))
    obstacles = set(obstacles)
    current_orientation_ind = 0
    for command in commands:
        if command == -2:
            current_orientation_ind -= 1
            current_orientation_ind %= len(move_orientations)
        elif command == -1:
            current_orientation_ind += 1
            current_orientation_ind %= len(move_orientations)
        else:
            current_pos = robot_move(
                current_pos,
                move_orientations[current_orientation_ind],
                obstacles,
                command,
            )
            ans = max(ans, current_pos[0] ** 2 + current_pos[1] ** 2)
    return ans
