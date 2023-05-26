import random
import numpy as np
import matplotlib.pyplot as plt

# Define the TSP problem parameters
cities = ['A', 'B', 'C', 'D', 'E']  # Example cities
distances = {
    'A': {'A': 0, 'B': 2, 'C': 9, 'D': 10, 'E': 6},
    'B': {'A': 2, 'B': 0, 'C': 4, 'D': 8, 'E': 3},
    'C': {'A': 9, 'B': 4, 'C': 0, 'D': 7, 'E': 12},
    'D': {'A': 10, 'B': 8, 'C': 7, 'D': 0, 'E': 11},
    'E': {'A': 6, 'B': 3, 'C': 12, 'D': 11, 'E': 0}
}

# GA parameters
population_size = 50
elite_size = 5
mutation_rate = 0.01
num_generations = 100

def create_individual():
    # Create a random TSP tour
    individual = cities[:]
    random.shuffle(individual)
    return individual

def create_population():
    # Create an initial population of individuals
    population = []
    for _ in range(population_size):
        individual = create_individual()
        population.append(individual)
    return population

def calculate_fitness(individual):
    # Calculate the total distance of a TSP tour
    total_distance = 0
    for i in range(len(individual)):
        city_a = individual[i]
        city_b = individual[(i + 1) % len(individual)]  # Wrap around to the first city
        total_distance += distances[city_a][city_b]
    return total_distance

def selection(population):
    # Select individuals for reproduction using roulette wheel selection
    fitness_scores = [1 / calculate_fitness(individual) for individual in population]
    total_fitness = sum(fitness_scores)
    probabilities = [score / total_fitness for score in fitness_scores]
    selected_indices = np.random.choice(len(population), size=(population_size - elite_size), replace=False, p=probabilities)
    selected_population = [population[i] for i in selected_indices]
    return selected_population

def crossover(parent1, parent2):
    # Perform crossover between two parents to create two offspring
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + [city for city in parent2 if city not in parent1[:crossover_point]]
    child2 = parent2[:crossover_point] + [city for city in parent1 if city not in parent2[:crossover_point]]
    return child1, child2

def mutation(individual):
    # Perform mutation on an individual by swapping two cities
    if random.random() < mutation_rate:
        swap_indices = random.sample(range(len(individual)), 2)
        individual[swap_indices[0]], individual[swap_indices[1]] = individual[swap_indices[1]], individual[swap_indices[0]]
    return individual

def evolve(population):
    # Create the next generation of the population
    selected_population = selection(population)
    elites = sorted(population, key=lambda ind: calculate_fitness(ind))[:elite_size]
    offspring = []
    while len(offspring) < population_size - elite_size:
        parent1, parent2 = random.choices(selected_population, k=2)
        child1, child2 = crossover(parent1, parent2)
        child1 = mutation(child1)
        child2 = mutation(child2)
        offspring.append(child1)
        offspring.append(child2)
    next_generation = elites + offspring
    return next_generation

def visualize_best_solution(best_distance, best_individual, generation):
    plt.figure()
    plt.plot(range(generation + 1), best_distance)
    plt.xlabel("Generation")
    plt.ylabel("Best Distance")
    plt.title("GA TSP: Best Distance per Generation")
    plt.grid(True)
    plt.show()

def tsp_ga():
    # Solve the TSP using a Genetic Algorithm
    population = create_population()
    best_distance = []
    best_individual = None
    for generation in range(num_generations):
        population = evolve(population)
        current_best = min(population, key=lambda ind: calculate_fitness(ind))
        current_distance = calculate_fitness(current_best)
        if best_individual is None or current_distance < calculate_fitness(best_individual):
            best_individual = current_best
        best_distance.append(current_distance)
        print(f"Generation {generation + 1}: Best Distance = {current_distance}, Best Tour = {current_best}")
    print(f"Best solution found: Distance = {calculate_fitness(best_individual)}, Tour = {best_individual}")
    visualize_best_solution(best_distance, best_individual, generation)

# Run the TSP GA algorithm
if __name__ == '__main__':
    tsp_ga()

