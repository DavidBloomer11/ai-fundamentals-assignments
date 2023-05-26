# Running the TSP Genetic Algorithm

To run the TSP Genetic Algorithm (GA) implemented in Python, follow the steps below:

## Step 1: Set up the environment

Make sure you have the necessary dependencies installed:
- random
- numpy
- matplotlib

You can install the dependencies using pip:
```shell
pip install numpy matplotlib
```

## Step 2: Copy the code

Copy the code provided into a Python file with the `.py` extension, for example, `tsp_ga.py`. Alternatively, you can create a Markdown file (`.md`) and place the code within a code block.

## Step 3: Run the code

Open a terminal or command prompt and navigate to the directory where you saved the file. Run the Python script using the following command:

```shell
python tsp_ga.py
```

## Understanding the code

The code performs the TSP (Traveling Salesman Problem) using a Genetic Algorithm. Here's a brief explanation of the main components and their functionality:

### Importing libraries

The necessary libraries are imported at the beginning of the code:
- `random`: For generating random numbers and shuffling the cities.
- `numpy`: For numerical operations and probability calculations.
- `matplotlib.pyplot`: For visualizing the best distance per generation.

### TSP problem parameters

The TSP problem is defined using the following parameters:
- `cities`: A list of cities represented by letters.
- `distances`: A dictionary containing the distances between each pair of cities.

### GA parameters

The parameters for the Genetic Algorithm are defined:
- `population_size`: The size of the population (number of individuals).
- `elite_size`: The number of best individuals to retain in each generation.
- `mutation_rate`: The probability of mutation occurring for each individual.
- `num_generations`: The number of generations to evolve the population.

### Helper functions

The code defines several helper functions used in the GA process:
- `create_individual`: Creates a random TSP tour by shuffling the cities.
- `create_population`: Creates an initial population of individuals.
- `calculate_fitness`: Calculates the total distance of a TSP tour.
- `selection`: Selects individuals for reproduction using roulette wheel selection.
- `crossover`: Performs crossover between two parents to create two offspring.
- `mutation`: Performs mutation on an individual by swapping two cities.
- `evolve`: Creates the next generation of the population.
- `visualize_best_solution`: Visualizes the best distance per generation using a line plot.

### TSP GA algorithm

The main function `tsp_ga` solves the TSP using the Genetic Algorithm:
- It initializes the population.
- It iterates through the specified number of generations, evolving the population.
- It tracks the best individual and its distance in each generation.
- It prints the best solution found at the end.
- It visualizes the best distance per generation using a line plot.

### Running the algorithm

The code includes a conditional check to run the `tsp_ga` function if the file is executed directly.

That's it! You can now run the TSP Genetic Algorithm and observe the best solution found for the given TSP problem.