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

class Node():
    def __init__(self, pos, number):
        self.pos = pos
        self.number = number

    def get_pos(self):
        return self.pos

    def get_number(self):
        return self.number  

class Hamiltonian:
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y
        self.HALF_X = X//2
        self.HALF_Y = Y//2

    def __create_nodes(self):
        nodes = [[Node((x * 2 + 1, y * 2 + 1), x + y * self.HALF_X) for y in range(0, self.HALF_Y)] for x in range(0, self.HALF_X)]
        return nodes

    def __create_edges(self):
        edges = [[0 for y in range(0, self.HALF_Y * self.HALF_X)] for x in range(0, self.HALF_X * self.HALF_Y)]

        skiplist = [self.HALF_X * x for x in range(0, self.HALF_X)]
        for x in range(0, self.HALF_X * self.HALF_Y):
            for y in range(0, self.HALF_Y * self.HALF_X):
                if not (x == y):
                    if (x + 1 == y and y not in skiplist): edges[x][y] = random.randint(1, 3)
                    elif (x + self.HALF_X == y): edges[x][y] = random.randint(1, 3)

        return edges

    def __hamiltonian_cycle(self,nodes, edges):
        points = []
        for edge in edges:
            for pos_x in range(0, self.HALF_X):
                for pos_y in range(0, self.HALF_Y):
                    if (nodes[pos_x][pos_y].get_number() == edge[0][0]):
                        start = nodes[pos_x][pos_y].get_pos()
                    if (nodes[pos_x][pos_y].get_number() == edge[0][1]):
                        end = nodes[pos_x][pos_y].get_pos()
            points.append(start)
            points.append(((start[0]+end[0])//2, (start[1]+end[1])//2))
            points.append(end)

        cycle = [(0, 0)]

        curr = cycle[0]
        dir = (1, 0)

        while len(cycle) < self.X * self.Y:
            x = curr[0]
            y = curr[1]

            if dir == (1, 0): #right
                if ((x + dir[0], y + dir[1] + 1) in points and (x + 1, y) not in points):
                    curr = (x + dir[0], y + dir[1])
                else:
                    if ((x, y + 1) in points and (x + 1, y + 1) not in points):
                        dir = (0, 1)
                    else:
                        dir = (0, -1)
            
            elif dir == (0, 1): #down
                if ((x + dir[0], y + dir[1]) in points and (x + dir[0] + 1, y + dir[1]) not in points):
                    curr = (x + dir[0], y + dir[1])
                else:
                    if ((x, y + 1) in points and (x + 1, y + 1) in points):
                        dir = (1, 0)
                    else:
                        dir = (-1, 0)

            elif dir == (-1, 0): #left
                if ((x, y) in points and (x, y+1) not in points):
                    curr = (x + dir[0], y + dir[1])
                else:
                    if ((x, y + 1) not in points):
                        dir = (0, -1)
                    else:
                        dir = (0, 1)

            elif dir == (0, -1): #up
                if ((x, y) not in points and (x + 1, y) in points):
                    curr = (x + dir[0], y + dir[1])
                else:
                    if ((x + 1, y) in points):
                        dir = (-1, 0)
                    else:
                        dir = (1, 0)

            if curr not in cycle:
                cycle.append(curr)

        return points, cycle

    def __prims_algoritm(self,edges):
        clean_edges = []
        for x in range(0, self.HALF_X * self.HALF_Y):
            for y in range(0, self.HALF_Y * self.HALF_X):
                if not (edges[x][y] == 0):
                    clean_edges.append(((x, y), edges[x][y]))
                
        visited = []
        unvisited = [x for x in range(self.HALF_X * self.HALF_Y)]
        curr = 0

        final_edges = []
        while len(unvisited) > 0:
            visited.append(curr)

            for number in unvisited:
                if number in visited:
                    unvisited.remove(number)

            my_edges = []
            for edge in clean_edges:
                if ((edge[0][0] in visited or edge[0][1] in visited) and not (edge[0][0] in visited and edge[0][1] in visited)):
                    my_edges.append(edge)

            min_edge = ((-1, -1), 999)

            for edge in my_edges:
                if (edge[1] < min_edge[1]):
                    min_edge = edge
            
            if len(unvisited) == 0:
                break

            final_edges.append(min_edge)

            if min_edge[0][0] == -1:
                curr = unvisited[0]
            else:
                if (min_edge[0][1] in visited):
                    curr = min_edge[0][0]
                else:
                    curr = min_edge[0][1]

        return final_edges

    def get_hamiltonian_cycle(self):
        nodes = self.__create_nodes()
        edges = self.__create_edges()
        final_edges = self.__prims_algoritm(edges)
        points, cycle = self.__hamiltonian_cycle(nodes,final_edges)

        return cycle

class SnakeGame:
    def __init__(self,x,y,game_speed):
        # Initialize Pygame
        pygame.init()

        #Game speed
        self.game_speed = game_speed

        #Grid
        self.x = x
        self.y = y


        self.cell_size = 20
        # Set up the game window
        window_width = x*20
        window_height = y*20
        self.window = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Snake Game")

        # Define colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)

        

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
            
    def __update_snake(self, x, y):
        '''Updates the snake after every frame'''
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

    def __get_state(self):
        '''Returns grid, snake head(y,x), food(y,x)'''

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

    def play_hamiltonian(self):
        hamiltonian_path = Hamiltonian(self.x,self.y).get_hamiltonian_cycle()
        path_found = False
        while not self.game_over:
            self.handle_events()

            
            if path_found == False:
                grid, head, food = self.__get_state()
                path = self.calculate_shortest_path(head,hamiltonian_path[0],grid)
                for i in path:
                    self.__update_snake(i[1],i[0])
                    self.draw()
                    self.clock.tick(self.game_speed)  # Adjust the frame rate (speed) of the game
                    path_found = True
            
            
            for i in hamiltonian_path:
                self.__update_snake(i[0],i[1])
                self.draw()
                self.clock.tick(self.game_speed)  # Adjust the frame rate (speed) of the game



        self.game_over_screen()
        pygame.quit()
        quit()
        
    def play_astar(self):
        while not self.game_over:
            self.handle_events()
            
            grid, start, end = self.__get_state()

            path = self.calculate_shortest_path(start,end,grid)

            if path == None:
                #Survival mode
                print('Survival mode')
                accessible_indices = self.find_accessible_indices(grid)
                path = self.calculate_shortest_path(start,accessible_indices[-1],grid)


            
            for i in path:
                self.__update_snake(i[1],i[0])
                self.draw()
                self.clock.tick(self.game_speed)  # Adjust the frame rate (speed) of the game



        self.game_over_screen()
        pygame.quit()
        quit()

    def find_accessible_indices(self,grid, border_symbol = 'B',start_symbol ='H'):
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return
            if grid[i][j] == border_symbol:
                return
            if (i, j) in visited:
                return
            
            visited.add((i, j))
            accessible_indices.append((i, j))
            
            dfs(i - 1, j)  # Up
            dfs(i + 1, j)  # Down
            dfs(i, j - 1)  # Left
            dfs(i, j + 1)  # Right
        
        accessible_indices = []
        visited = set()
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == start_symbol:
                    dfs(i, j)
        
        return accessible_indices
    
    def calculate_shortest_path(self,start,end,grid):
        search = AstarSearch(wall = 'B')
        path = search.a_star_search(grid,start, end)
        if path !=None:
            path.pop(0)
        return path



import argparse

def main():
    parser = argparse.ArgumentParser(description='Snake game')
    parser.add_argument('speed', type=int, help='Speed of the game')
    parser.add_argument('size', type=str, help='Size of the snake grid "rows,columns"')
    parser.add_argument('algorithm', type=str, help='Algorithm to use (hamiltonian, astar)')

    args = parser.parse_args()

    # Parse the size argument
    game_size = tuple(map(int, args.size.split(',')))

    # Extract other arguments
    game_speed = args.speed
    algorithm = args.algorithm.lower()
    game = SnakeGame(game_size[0], game_size[1], game_speed)
    if algorithm == 'hamiltonian':
        game.play_hamiltonian()
    elif algorithm == 'astar':
        game.play_astar()
    else:
        print('Invalid algorithm. Available options: hamiltonian, astar')


if __name__ == '__main__':
    main()