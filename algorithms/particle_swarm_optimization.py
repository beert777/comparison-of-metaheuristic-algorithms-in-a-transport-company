import random
from utils import calculate_cost

class Particle:
    def __init__(self, route):
        self.route = route
        self.velocity = [0] * len(route)
        self.best_route = list(route)
        self.best_cost = float('inf')

def pso_optimize(distance_matrix, orders, vehicle_capacity, time_windows, num_particles=30, max_iter=100):
    particles = [Particle(random.sample(range(len(orders)), len(orders))) for _ in range(num_particles)]

    def fitness(route):
        return calculate_cost(route, distance_matrix)

    global_best_route = None
    global_best_cost = float('inf')

    for iteration in range(max_iter):
        for particle in particles:
            cost = fitness(particle.route)
            if cost < particle.best_cost:
                particle.best_cost = cost
                particle.best_route = list(particle.route)
            if cost < global_best_cost:
                global_best_cost = cost
                global_best_route = list(particle.route)

        for particle in particles:
            for i in range(len(particle.route)):
                particle.velocity[i] = (random.random() * particle.velocity[i] +
                                        random.random() * (particle.best_route[i] - particle.route[i]) +
                                        random.random() * (global_best_route[i] - particle.route[i]))
                particle.route[i] += particle.velocity[i]
                particle.route[i] = int(particle.route[i]) % len(orders)

    return global_best_route, global_best_cost