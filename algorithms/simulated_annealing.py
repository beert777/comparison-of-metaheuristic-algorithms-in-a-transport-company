import random
import math
from utils import calculate_cost

def simulated_annealing(distance_matrix, orders, vehicle_capacity, time_windows, initial_temp=100, cooling_rate=0.99, max_iter=1000):
    current_route = random.sample(range(len(orders)), len(orders))
    current_cost = calculate_cost(current_route, distance_matrix)
    best_route = list(current_route)
    best_cost = current_cost
    temp = initial_temp

    for iteration in range(max_iter):
        new_route = list(current_route)
        idx1, idx2 = random.sample(range(len(new_route)), 2)
        new_route[idx1], new_route[idx2] = new_route[idx2], new_route[idx1]
        new_cost = calculate_cost(new_route, distance_matrix)
        if new_cost < current_cost or math.exp((current_cost - new_cost) / temp) > random.random():
            current_route = new_route
            current_cost = new_cost
            if new_cost < best_cost:
                best_route = new_route
                best_cost = new_cost
        temp *= cooling_rate

    """  ZMIANA SYSTEMU CHŁODZENIA
            if cooling_schedule == 'linear':
                temperature -= cooling_rate
            elif cooling_schedule == 'exponential':
                temperature *= cooling_rate
    """
    return best_route, best_cost