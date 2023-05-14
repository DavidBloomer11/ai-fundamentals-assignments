import random
from collections import deque
import heapq
import argparse

def random_search(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])
    
    current = start
    path = [current]
    
    while current != end:
        neighbors = []
        
        if current[0] > 0 and maze[current[0]-1][current[1]] != 'X':
            neighbors.append((current[0]-1, current[1]))  # Up
        if current[0] < rows-1 and maze[current[0]+1][current[1]] != 'X':
            neighbors.append((current[0]+1, current[1]))  # Down
        if current[1] > 0 and maze[current[0]][current[1]-1] != 'X':
            neighbors.append((current[0], current[1]-1))  # Left
        if current[1] < cols-1 and maze[current[0]][current[1]+1] != 'X':
            neighbors.append((current[0], current[1]+1))  # Right
        
        if neighbors:
            current = random.choice(neighbors)
            path.append(current)
        else:
            path.pop()
            if not path:
                return None  # No path found
        
    return path

def depth_first_search(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])

    stack = [(start, [start])]
    visited = set()

    while stack:
        current, path = stack.pop()
        visited.add(current)

        if current == end:
            return path

        neighbors = []
        if current[0] > 0 and maze[current[0] - 1][current[1]] != 'X':
            neighbors.append((current[0] - 1, current[1]))  # Up
        if current[0] < rows - 1 and maze[current[0] + 1][current[1]] != 'X':
            neighbors.append((current[0] + 1, current[1]))  # Down
        if current[1] > 0 and maze[current[0]][current[1] - 1] != 'X':
            neighbors.append((current[0], current[1] - 1))  # Left
        if current[1] < cols - 1 and maze[current[0]][current[1] + 1] != 'X':
            neighbors.append((current[0], current[1] + 1))  # Right

        for neighbor in neighbors:
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
                visited.add(neighbor)

    return None  # No path found

def breadth_first_search(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])

    queue = deque([(start, [start])])
    visited = set(start)

    while queue:
        current, path = queue.popleft()

        if current == end:
            return path

        neighbors = []
        if current[0] > 0 and maze[current[0] - 1][current[1]] != 'X':
            neighbors.append((current[0] - 1, current[1]))  # Up
        if current[0] < rows - 1 and maze[current[0] + 1][current[1]] != 'X':
            neighbors.append((current[0] + 1, current[1]))  # Down
        if current[1] > 0 and maze[current[0]][current[1] - 1] != 'X':
            neighbors.append((current[0], current[1] - 1))  # Left
        if current[1] < cols - 1 and maze[current[0]][current[1] + 1] != 'X':
            neighbors.append((current[0], current[1] + 1))  # Right

        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)

    return None  # No path found

#Greedy search
def calculate_distance(point1, point2):
    # Manhattan distance
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def greedy_search(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])

    queue = [(start, [start], 0)]
    visited = set(start)

    while queue:
        queue.sort(key=lambda x: calculate_distance(x[0], end), reverse=True)
        current, path, _ = queue.pop()

        if current == end:
            return path

        neighbors = []
        if current[0] > 0 and maze[current[0] - 1][current[1]] != 'X':
            neighbors.append((current[0] - 1, current[1]))  # Up
        if current[0] < rows - 1 and maze[current[0] + 1][current[1]] != 'X':
            neighbors.append((current[0] + 1, current[1]))  # Down
        if current[1] > 0 and maze[current[0]][current[1] - 1] != 'X':
            neighbors.append((current[0], current[1] - 1))  # Left
        if current[1] < cols - 1 and maze[current[0]][current[1] + 1] != 'X':
            neighbors.append((current[0], current[1] + 1))  # Right

        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor], calculate_distance(neighbor, end)))
                visited.add(neighbor)

    return None  # No path found

#A star
def calculate_heuristic(point1, point2):
    # Manhattan distance heuristic
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def a_star_search(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])

    heap = []
    heapq.heappush(heap, (0, start, [start]))
    visited = set(start)

    while heap:
        _, current, path = heapq.heappop(heap)

        if current == end:
            return path

        neighbors = []
        if current[0] > 0 and maze[current[0] - 1][current[1]] != 'X':
            neighbors.append((current[0] - 1, current[1]))  # Up
        if current[0] < rows - 1 and maze[current[0] + 1][current[1]] != 'X':
            neighbors.append((current[0] + 1, current[1]))  # Down
        if current[1] > 0 and maze[current[0]][current[1] - 1] != 'X':
            neighbors.append((current[0], current[1] - 1))  # Left
        if current[1] < cols - 1 and maze[current[0]][current[1] + 1] != 'X':
            neighbors.append((current[0], current[1] + 1))  # Right

        for neighbor in neighbors:
            if neighbor not in visited:
                new_cost = len(path) + 1
                total_cost = new_cost + calculate_heuristic(neighbor, end)
                heapq.heappush(heap, (total_cost, neighbor, path + [neighbor]))
                visited.add(neighbor)

    return None  # No path found

# Visualize path
def visualize_path(maze, path):
    start = path[0]
    end = path[-1]
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if (row, col) == start:
                print("S", end=' ')  # Start position
            elif (row, col) == end:
                print("E", end=' ')  # End position
            elif (row, col) in path:
                print("*", end=' ')  # Path
            elif maze[row][col] == 'X':
                print("X", end=' ')  # Walls
            else:
                print(" ", end=' ')  # Empty space
        print()

    print('-------------------------------------\n')
    print('Total steps: ',str(len(path)))

def load_maze(maze_file):
    maze_lines = open(maze_file).read().splitlines()

    maze = []
    for line in maze_lines:
        maze.append(list(line))
    return maze

maze = load_maze('dataset/6.txt')



def main():
    parser = argparse.ArgumentParser(description='Maze Solver')
    parser.add_argument('maze_file', type=str, help='Path to the maze file')
    parser.add_argument('start', type=str, help='Start position in the format "row,column"')
    parser.add_argument('end', type=str, help='End position in the format "row,column"')
    parser.add_argument('algorithm', type=str, help='Algorithm to use (random, dfs, bfs, greedy, astar)')

    args = parser.parse_args()

    # Read the maze file
    maze = load_maze(args.maze_file)

    # Parse the start and end positions
    start = tuple(map(int, args.start.split(',')))
    end = tuple(map(int, args.end.split(',')))


    # Choose the algorithm based on the provided argument
    algorithm = args.algorithm.lower()
    if algorithm == 'random':
        path = random_search(maze, start, end)
    elif algorithm == 'dfs':
        path = depth_first_search(maze, start, end)
    elif algorithm == 'bfs':
        path = breadth_first_search(maze, start, end)
    elif algorithm == 'greedy':
        path = greedy_search(maze, start, end)
    elif algorithm == 'astar':
        path = a_star_search(maze, start, end)
    else:
        print('Invalid algorithm. Available options: random, dfs, bfs, greedy, astar')
        return

    if path is None:
        print('No path found.')
    else:
        visualize_path(maze, path)


if __name__ == '__main__':
    main()
