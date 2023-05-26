import random

def generate_maze(width, height):
    maze = [[False] * width for _ in range(height)]
    current_cell = (random.randint(0, height-1), random.randint(0, width-1))
    maze[current_cell[0]][current_cell[1]] = True
    frontier = [current_cell]
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while frontier:
        current_cell = random.choice(frontier)
        frontier.remove(current_cell)

        for movement in movements:
            next_row = current_cell[0] + movement[0]
            next_col = current_cell[1] + movement[1]

            if 0 <= next_row < height and 0 <= next_col < width and not maze[next_row][next_col]:
                maze[next_row][next_col] = True
                frontier.append((next_row, next_col))

    return maze


def get_adjacent_cells(row, col, width, height):
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    adjacent_cells = []

    for movement in movements:
        next_row = row + movement[0]
        next_col = col + movement[1]

        if 0 <= next_row < height and 0 <= next_col < width:
            adjacent_cells.append((next_row, next_col))

    return adjacent_cells


def left_turn(direction):
    return (direction - 1) % 4


def generate_hamiltonian_cycle(n, start_point):
    width = n
    height = n
    maze = generate_maze(width, height)
    start_cell = (start_point[0], start_point[1])
    current_cell = start_cell
    current_direction = 1  # 0: up, 1: right, 2: down, 3: left
    path = [current_cell]

    while current_cell != start_cell or len(path) < width * height:
        adjacent_cells = get_adjacent_cells(current_cell[0], current_cell[1], width, height)
        found_next_cell = False

        for cell in adjacent_cells:
            if not maze[cell[0]][cell[1]]:
                maze[cell[0]][cell[1]] = True
                current_cell = cell
                found_next_cell = True
                path.append(current_cell)
                break

        if not found_next_cell:
            current_direction = left_turn(current_direction)
            next_row = current_cell[0] + [(0, -1), (1, 0), (0, 1), (-1, 0)][current_direction][0]
            next_col = current_cell[1] + [(0, -1), (1, 0), (0, 1), (-1, 0)][current_direction][1]
            current_cell = (next_row, next_col)
            path.append(current_cell)

    return tuple(path)


n = 3
start_point = (0, 1)
hamiltonian_path = generate_hamiltonian_cycle(n, start_point)
print(hamiltonian_path)
