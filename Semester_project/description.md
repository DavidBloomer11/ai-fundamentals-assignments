# Snake Game

This is a snake game implemented in Python using the Pygame library. The game allows the snake to navigate through a grid and collect food while avoiding collisions with the boundaries and its own body.

## Requirements

The game requires the Pygame library to be installed. You can install it using the following command:

```
pip install pygame
```

## Usage

The game can be executed from the command line. Here's an example command:

```
python snake_game.py <speed> <size> <algorithm>
```

- `<speed>`: Speed of the game (integer).
- `<size>`: Size of the snake grid in the format "rows,columns" (e.g., "10,10").
- `<algorithm>`: Algorithm to use for controlling the snake (options: hamiltonian, astar).

## Game Algorithms

### Hamiltonian Algorithm

The Hamiltonian algorithm generates a Hamiltonian cycle on a grid and uses it to control the movement of the snake. The Hamiltonian cycle ensures that the snake visits each cell in the grid exactly once. This algorithm provides a deterministic path for the snake.

### A* Algorithm

The A* algorithm is used to find the shortest path from the snake's current position to the food. If a direct path is not available, the algorithm falls back to a survival mode where the snake moves towards the farthest accessible cell in the grid.

## Implementation Details

The code consists of the following classes and functions:

- `SnakeGame`: Represents the main game class that handles the game logic, including the snake's movement, collisions, and rendering.
- `Hamiltonian`: Implements the Hamiltonian algorithm to generate a Hamiltonian cycle on a grid.
- `AstarSearch`: Implements the A* search algorithm to find the shortest path between two points on a grid.
- `find_accessible_indices`: Utility function to find the accessible indices in a grid.

## Running the Game

To run the game, execute the following command:

```
python snake.py <speed> <size> <algorithm>
```

Replace `<speed>`, `<size>`, and `<algorithm>` with the desired values.

Enjoy playing the Snake Game!
```

