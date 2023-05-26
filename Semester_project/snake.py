import pygame
import random
import heapq
import time
import sys

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
            elif maze[row][col] == 'B':
                print("B", end=' ')  # Walls
            else:
                print(" ", end=' ')  # Empty space
        print()

    print('-------------------------------------\n')
    print('Total steps: ',str(len(path)))

class AstarSearch:
    def __init__(self, wall):
        self.wall = wall
        pass

    def calculate_heuristic(self, point1, point2):
    # Manhattan distance heuristic
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    def a_star_search(self, maze, start, end):
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
            if current[0] > 0 and maze[current[0] - 1][current[1]] != self.wall:
                neighbors.append((current[0] - 1, current[1]))  # Up
            if current[0] < rows - 1 and maze[current[0] + 1][current[1]] != self.wall:
                neighbors.append((current[0] + 1, current[1]))  # Down
            if current[1] > 0 and maze[current[0]][current[1] - 1] != self.wall:
                neighbors.append((current[0], current[1] - 1))  # Left
            if current[1] < cols - 1 and maze[current[0]][current[1] + 1] != self.wall:
                neighbors.append((current[0], current[1] + 1))  # Right

            for neighbor in neighbors:
                if neighbor not in visited:
                    new_cost = len(path) + 1
                    total_cost = new_cost + self.calculate_heuristic(neighbor, end)
                    heapq.heappush(heap, (total_cost, neighbor, path + [neighbor]))
                    visited.add(neighbor)

        return None  # No path found




class HamiltonSearch:
    def find_hamiltonian_path(self,maze,start):
        rows = len(maze)
        cols = len(maze[0])
        path = []
        
        # Find the starting point (head of the snake)
        start_row, start_col = start 
        
        # Run depth-first search (DFS) to find the Hamiltonian path
        visited = [[False] * cols for _ in range(rows)]
        self.dfs(start_row, start_col, maze, visited, path)
        
        return path

    

    def dfs(self,row, col, maze, visited, path):
        rows = len(maze)
        cols = len(maze[0])
        
        # Check if the current point is a valid position
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return False
        
        # Check if the current point is already visited or blocked
        if visited[row][col] or maze[row][col] == 'B':
            return False
        
        # Mark the current point as visited
        visited[row][col] = True
        
        # Add the current point to the path
        path.append((row, col))
        
        # Check if all the points have been visited
        if len(path) == rows * cols:
            return True
        
        # Explore the adjacent points in a specific order (e.g., clockwise)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            if self.dfs(row + dr, col + dc, maze, visited, path):
                return True
        
        # Backtrack if no valid path is found
        path.pop()
        visited[row][col] = False
        
        return False




class LongestSearch:
    def longest_path(self,maze, start_cell):
        # Helper function to get the neighbors of a cell
        def get_neighbors(cell):
            neighbors = []
            row, col = cell
            if row > 0 and maze[row - 1][col] != 'B':
                neighbors.append((row - 1, col))
            if row < len(maze) - 1 and maze[row + 1][col] != 'B':
                neighbors.append((row + 1, col))
            if col > 0 and maze[row][col - 1] != 'B':
                neighbors.append((row, col - 1))
            if col < len(maze[0]) - 1 and maze[row][col + 1] != 'B':
                neighbors.append((row, col + 1))
            return neighbors

        # Helper function to perform DFS
        def dfs(cell, visited, path):
            path.append(cell)
            visited.add(cell)

            max_path = []
            for neighbor in get_neighbors(cell):
                if neighbor not in visited:
                    new_path = dfs(neighbor, visited, path)
                    if len(new_path) > len(max_path):
                        max_path = new_path

            path.pop()
            visited.remove(cell)

            return [cell] + max_path

        # Initialize visited set and call DFS
        visited = set()
        path = []
        longest = dfs(start_cell, visited, path)
        
        return longest

class SnakeGame:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Set up the game window
        window_width = 640
        window_height = 480
        self.window = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Snake Game")

        # Define colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)

        # Define the size of each grid cell
        self.cell_size = 20

        # Set up the clock to control the game's frame rate
        self.clock = pygame.time.Clock()

        # Define the font for the game over message
        self.font_style = pygame.font.SysFont(None, 50)

        # Initialize other game variables
        self.snake_size = 1
        self.snake_body = []
        self.snake_head = [window_width / 2, window_height / 2]
        self.snake_body.append(self.snake_head)
        self.x_change = 0
        self.y_change = 0
        self.food_x = round(random.randrange(0, window_width - self.cell_size) / self.cell_size) * self.cell_size
        self.food_y = round(random.randrange(0, window_height - self.cell_size) / self.cell_size) * self.cell_size
        self.game_over = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.x_change = -self.cell_size
                    self.y_change = 0
                elif event.key == pygame.K_RIGHT:
                    self.x_change = self.cell_size
                    self.y_change = 0
                elif event.key == pygame.K_UP:
                    self.x_change = 0
                    self.y_change = -self.cell_size
                elif event.key == pygame.K_DOWN:
                    self.x_change = 0
                    self.y_change = self.cell_size

    def __check_for_border_colision(self):
        if (
            self.snake_head[0] >= self.window.get_width()
            or self.snake_head[0] < 0
            or self.snake_head[1] >= self.window.get_height()
            or self.snake_head[1] < 0
        ):
            self.game_over = True

    def __check_for_body_colision(self):
        for segment in self.snake_body[1:]:
            if segment == self.snake_head:
                self.game_over = True

    def __check_for_food_colision(self):
        if self.snake_head[0] == self.food_x and self.snake_head[1] == self.food_y:
            while True:
                self.food_y = round(random.randrange(0, self.window.get_height() - self.cell_size) / self.cell_size) * self.cell_size
                self.food_x = round(random.randrange(0, self.window.get_width() - self.cell_size) / self.cell_size) * self.cell_size
                self.snake_size += 1
                if [self.food_x, self.food_y] not in self.snake_body:
                    break
            
    def update_snake(self):
        self.snake_head[0] += self.x_change
        self.snake_head[1] += self.y_change

        # Check for collisions with the window boundaries
        self.__check_for_border_colision()

        # Check for collisions with the snake's body
        self.__check_for_body_colision()

        # Update the snake's body
        self.snake_body.append(list(self.snake_head))
        if len(self.snake_body) > self.snake_size:
            del self.snake_body[0]

        # Check for collisions with the food
        self.__check_for_food_colision()

    def __update_snake(self, x, y):
        self.snake_head[0] = x*self.cell_size
        self.snake_head[1] = y*self.cell_size

        # Check for collisions with the window boundaries
        self.__check_for_border_colision()

        # Check for collisions with the snake's body
        self.__check_for_body_colision()

        # Update the snake's body
        self.snake_body.append(list(self.snake_head))
        if len(self.snake_body) > self.snake_size:
            del self.snake_body[0]

        # Check for collisions with the food
        self.__check_for_food_colision()

    def draw(self):
        # Clear the game window
        self.window.fill(self.black)

        # Draw the snake
        for segment in self.snake_body:
            pygame.draw.rect(self.window, self.green, [segment[0], segment[1], self.cell_size, self.cell_size])

        # Draw the food
        pygame.draw.rect(self.window, self.red, [self.food_x, self.food_y, self.cell_size, self.cell_size])

        # Update the display
        pygame.display.update()

    def game_over_screen(self):
        # Display game over message
        game_over_text = self.font_style.render("Game Over", True, self.white)
        self.window.blit(game_over_text, [self.window.get_width() / 2 - 100, self.window.get_height() / 2])
        pygame.display.update()

        # Wait for 2 seconds before quitting the game
        pygame.time.wait(20000)

    def play(self):
        while not self.game_over:
            self.handle_events()

            path = 



            for i in path:
                self.__update_snake(i[1],i[0])
                self.draw()
                self.clock.tick(100)  # Adjust the frame rate (speed) of the game
        

        self.game_over_screen()
        pygame.quit()
        quit()

    def __get_state(self):
        # Create a 2D array with dimensions based on the game window size and cell size
        grid_width = self.window.get_width() // self.cell_size
        grid_height = self.window.get_height() // self.cell_size


        grid = [[0] * grid_width for _ in range(grid_height)]

        # Set the values in the grid for the snake's body and head
        for segment in self.snake_body:
            x, y = segment
            grid[int(y // self.cell_size)][int(x // int(self.cell_size))] = 'B'

        

        # Set the value in the grid for the food
        food_x = self.food_x // self.cell_size
        food_y = self.food_y // self.cell_size
        grid[food_y][food_x] = 'F'

        head_x, head_y = self.snake_head
        grid[int(head_y // self.cell_size)][int(head_x // int(self.cell_size))] = 'H'

        return grid, (int(head_y // self.cell_size),int(head_x // self.cell_size)), (food_y,food_x)
    
    def calculate_shortest_path(self):
        grid, start, end = self.__get_state()

        
        search = AstarSearch(wall = 'B')
        path = search.a_star_search(grid,start, end)
        if path !=None:
            path.pop(0)
        return path

    def calculate_longest_path(self):
        grid, start, end = self.__get_state()

        print('Longest path start')


        search = HamiltonSearch()

        path = search.find_hamiltonian_path(grid,start)
        path.pop(0)
        print(path)

        return path







# Create an instance of the SnakeGame class
game = SnakeGame()
game.play()

