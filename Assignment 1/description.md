# Maze Solver

This script solves the problem of finding a path in a maze using various algorithms. The script takes a maze file, start position, end position, and the algorithm to use as command-line arguments.

## Prerequisites

- Python 3.x

## Usage

1. Clone the repository or download the maze_solver.py file.

2. Open a terminal or command prompt and navigate to the directory where the maze_solver.py file is located.

3. Run the following command to execute the script:

   ```bash
   python maze_solver.py <maze_file> <start> <end> <algorithm>
   ```

   Replace `<maze_file>` with the path to the maze file you want to solve. The maze file should be a text file representing the maze structure, where 'X' represents walls and empty spaces represent open paths.

   Replace `<start>` with the starting position in the format "row,column". For example, "1,1" represents the top-left cell. (uses 0 indexing)

   Replace `<end>` with the ending position in the format "row,column". For example, "5,5" represents the bottom-right cell. (uses 0 indexing)

   Replace `<algorithm>` with the algorithm you want to use. Available options are:
   - `random`: Random Search algorithm
   - `dfs`: Depth-First Search algorithm
   - `bfs`: Breadth-First Search algorithm
   - `greedy`: Greedy Search algorithm
   - `astar`: A* Search algorithm

4. The script will display the visualization of the maze with the path marked using 'P'. If a valid path is found, it will be displayed; otherwise, a message indicating that no path was found will be shown.

5. You can try different maze files, start and end positions, and algorithms to experiment with different solutions.

## Example

To solve a maze using the Depth-First Search algorithm, you can use the following command:

```bash
python maze_solver.py maze.txt 1,1 5,5 dfs
```

This will solve the maze specified in the "maze.txt" file, starting from the top-left cell (1,1) and ending at the bottom-right cell (5,5) using the Depth-First Search algorithm.

---
