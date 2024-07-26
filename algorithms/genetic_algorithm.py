import random
from utils import calculate_cost

def genetic_algorithm(distance_matrix, orders, vehicle_capacity, time_windows, population_size=50, generations=100):
    population = [random.sample(range(len(orders)), len(orders)) for _ in range(population_size)]

    def fitness(route):
        return calculate_cost(route, distance_matrix)

    def crossover(parent1, parent2):
        child = [-1] * len(parent1)
        start, end = sorted(random.sample(range(len(parent1)), 2))
        child[start:end] = parent1[start:end]
        for item in parent2:
            if item not in child:
                child[child.index(-1)] = item
        return child
    def mutate(route):
        idx1, idx2 = random.sample(range(len(route)), 2)
        route[idx1], route[idx2] = route[idx2], route[idx1]
        return route
    for generation in range(generations):
        population = sorted(population, key=fitness)
        next_generation = population[:int(0.1 * population_size)]
        for _ in range(int(0.9 * population_size)):
            parent1, parent2 = random.sample(population[:int(0.5 * population_size)], 2)
            child = mutate(crossover(parent1, parent2))
            next_generation.append(child)
        population = next_generation
    """ ZMIANA WYBORU SELEKCJI 
    def selection(population, method):
        if method == 'tournament':
            selected = []
            for _ in range(population_size):
                tournament = random.sample(population, 3)
                selected.append(min(tournament, key=fitness))
            return selected
        elif method == 'roulette':
            max_fitness = sum([fitness(ind) for ind in population])
            pick = random.uniform(0, max_fitness)
            current = 0
            for ind in population:
                current += fitness(ind)
                if current > pick:
                    return ind
    """
    best_route = sorted(population, key=fitness)[0]
    return best_route, fitness(best_route)