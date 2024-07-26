from random import random

import numpy as np
from data.data_preparation import prepare_data
from algorithms.genetic_algorithm import genetic_algorithm
from algorithms.ant_colony_optimization import ACO
from algorithms.particle_swarm_optimization import pso_optimize
from algorithms.simulated_annealing import simulated_annealing

#GŁÓWNA FUNKCJA
""" 
def run_experiment():
    distance_matrix, orders, vehicle_capacity, time_windows = prepare_data()

    ga_route, ga_cost = genetic_algorithm(distance_matrix, orders, vehicle_capacity, time_windows)
    print(f"GA Route: {ga_route}, Cost: {ga_cost}")

    aco = ACO(distance_matrix, n_ants=10, n_best=5, n_iterations=100, decay=0.95)
    aco_route, aco_cost = aco.run()
    print(f"ACO Route: {aco_route}, Cost: {aco_cost}")

    pso_route, pso_cost = pso_optimize(distance_matrix, orders, vehicle_capacity, time_windows)
    print(f"PSO Route: {pso_route}, Cost: {pso_cost}")

    sa_route, sa_cost = simulated_annealing(distance_matrix, orders, vehicle_capacity, time_windows)
    print(f"SA Route: {sa_route}, Cost: {sa_cost}")
"""


# Funkcja eksperymentalna zmiana ilości klientów
"""
def experiment_vary_clients(num_clients_list):
    results = []
    for num_clients in num_clients_list:
        distance_matrix, orders, vehicle_capacity, time_windows = prepare_data(num_clients)

        ga_route, ga_cost = genetic_algorithm(distance_matrix, orders, vehicle_capacity, time_windows)

        aco = ACO(distance_matrix, n_ants=10, n_best=5, n_iterations=100, decay=0.95)
        aco_route, aco_cost = aco.run()

        pso_route, pso_cost = pso_optimize(distance_matrix, orders, vehicle_capacity, time_windows)

        sa_route, sa_cost = simulated_annealing(distance_matrix, orders, vehicle_capacity, time_windows)

        results.append({
            'num_clients': num_clients,
            'GA': {'route': ga_route, 'cost': ga_cost},
            'ACO': {'route': aco_route, 'cost': aco_cost},
            'PSO': {'route': pso_route, 'cost': pso_cost},
            'SA': {'route': sa_route, 'cost': sa_cost},
        })
    return results


# Główna funkcja zmiana ilości klientów
def run_experiment():
    # Test z różną liczbą klientów
    num_clients_list = [5, 10, 15, 20]
    results_clients = experiment_vary_clients(num_clients_list)
    for result in results_clients:
        print("Number of clients:", result['num_clients'])
        for algorithm in ['GA', 'ACO', 'PSO', 'SA']:
            route = result[algorithm]['route']
            cost = result[algorithm]['cost']
            # Formatowanie wyniku kosztu z przecinkiem zamiast kropki
            formatted_cost = f"{cost:.2f}".replace('.', ',')
            print(f"{algorithm} Route: {route}, Cost: {formatted_cost}")
"""

"""
# Funkcja eksperymentalna zmieniająca wielkość zamówień
def experiment_vary_order_sizes(order_size_ranges):
    results = []
    num_clients = 10  # Stała liczba klientów dla tego eksperymentu
    for min_order_size, max_order_size in order_size_ranges:
        distance_matrix, orders, vehicle_capacity, time_windows = prepare_data(num_clients, min_order_size,
                                                                               max_order_size)

        ga_route, ga_cost = genetic_algorithm(distance_matrix, orders, vehicle_capacity, time_windows)

        aco = ACO(distance_matrix, n_ants=10, n_best=5, n_iterations=100, decay=0.95)
        aco_route, aco_cost = aco.run()

        pso_route, pso_cost = pso_optimize(distance_matrix, orders, vehicle_capacity, time_windows)

        sa_route, sa_cost = simulated_annealing(distance_matrix, orders, vehicle_capacity, time_windows)

        results.append({
            'order_size_range': (min_order_size, max_order_size),
            'GA': {'route': ga_route, 'cost': ga_cost},
            'ACO': {'route': aco_route, 'cost': aco_cost},
            'PSO': {'route': pso_route, 'cost': pso_cost},
            'SA': {'route': sa_route, 'cost': sa_cost},
        })
    return results


# Główna funkcja eksperymentalna
def run_experiment():
    # Test z różnymi zakresami wielkości zamówień
    order_size_ranges = [(5, 15), (10, 20), (15, 25), (20, 30)]
    results_order_sizes = experiment_vary_order_sizes(order_size_ranges)
    for result in results_order_sizes:
        print("Order size range:", result['order_size_range'])
        for algorithm in ['GA', 'ACO', 'PSO', 'SA']:
            route = result[algorithm]['route']
            cost = result[algorithm]['cost']
            formatted_cost = f"{cost:.2f}".replace('.', ',')
            print(f"{algorithm} Route: {route}, Cost: {formatted_cost}")
"""

"""
# Funkcja eksperymentalna zmieniająca okna czasowe
def experiment_vary_time_windows(time_window_ranges):
    results = []
    num_clients = 10  # Stała liczba klientów dla tego eksperymentu
    for time_window_start_range, time_window_end_range in time_window_ranges:
        distance_matrix, orders, vehicle_capacity, time_windows = prepare_data(num_clients,
                                                                               time_window_start_range=time_window_start_range,
                                                                               time_window_end_range=time_window_end_range)

        ga_route, ga_cost = genetic_algorithm(distance_matrix, orders, vehicle_capacity, time_windows)

        aco = ACO(distance_matrix, n_ants=10, n_best=5, n_iterations=100, decay=0.95)
        aco_route, aco_cost = aco.run()

        pso_route, pso_cost = pso_optimize(distance_matrix, orders, vehicle_capacity, time_windows)

        sa_route, sa_cost = simulated_annealing(distance_matrix, orders, vehicle_capacity, time_windows)

        results.append({
            'time_window_start_range': time_window_start_range,
            'time_window_end_range': time_window_end_range,
            'GA': {'route': ga_route, 'cost': ga_cost},
            'ACO': {'route': aco_route, 'cost': aco_cost},
            'PSO': {'route': pso_route, 'cost': pso_cost},
            'SA': {'route': sa_route, 'cost': sa_cost},
        })
    return results


# Główna funkcja eksperymentalna
def run_experiment():
    # Test z różnymi zakresami okien czasowych
    time_window_ranges = [((0, 5), (6, 10)), ((0, 10), (10, 15)), ((0, 15), (15, 20)), ((5, 10), (15, 20))]
    results_time_windows = experiment_vary_time_windows(time_window_ranges)
    for result in results_time_windows:
        print("Time window range:", result['time_window_start_range'], "-", result['time_window_end_range'])
        for algorithm in ['GA', 'ACO', 'PSO', 'SA']:
            route = result[algorithm]['route']
            cost = result[algorithm]['cost']
            formatted_cost = f"{cost:.2f}".replace('.', ',')
            print(f"{algorithm} Route: {route}, Cost: {formatted_cost}")
"""

"""
# Funkcja eksperymentalna zmieniająca pojemność pojazdów
def experiment_vary_vehicle_capacities(vehicle_capacities):
    results = []
    num_clients = 10  # Stała liczba klientów dla tego eksperymentu
    for capacity in vehicle_capacities:
        distance_matrix, orders, vehicle_capacity, time_windows = prepare_data(num_clients, vehicle_capacity=capacity)

        ga_route, ga_cost = genetic_algorithm(distance_matrix, orders, vehicle_capacity, time_windows)

        aco = ACO(distance_matrix, n_ants=10, n_best=5, n_iterations=100, decay=0.95)
        aco_route, aco_cost = aco.run()

        pso_route, pso_cost = pso_optimize(distance_matrix, orders, vehicle_capacity, time_windows)

        sa_route, sa_cost = simulated_annealing(distance_matrix, orders, vehicle_capacity, time_windows)

        results.append({
            'vehicle_capacity': capacity,
            'GA': {'route': ga_route, 'cost': ga_cost},
            'ACO': {'route': aco_route, 'cost': aco_cost},
            'PSO': {'route': pso_route, 'cost': pso_cost},
            'SA': {'route': sa_route, 'cost': sa_cost},
        })
    return results


# Główna funkcja eksperymentalna
def run_experiment():
    # Test z różnymi pojemnościami pojazdów
    vehicle_capacities = [30, 50, 70, 100]
    results_vehicle_capacities = experiment_vary_vehicle_capacities(vehicle_capacities)
    for result in results_vehicle_capacities:
        print("Vehicle capacity:", result['vehicle_capacity'])
        for algorithm in ['GA', 'ACO', 'PSO', 'SA']:
            route = result[algorithm]['route']
            cost = result[algorithm]['cost']
            formatted_cost = f"{cost:.2f}".replace('.', ',')
            print(f"{algorithm} Route: {route}, Cost: {formatted_cost}")
"""


# Funkcja eksperymentalna zmieniająca maksymalny czas pracy kierowców
def experiment_vary_driver_hours(max_driver_hours_list):
    results = []
    num_clients = 10  # Stała liczba klientów dla tego eksperymentu
    vehicle_capacity = 50  # Stała pojemność pojazdu dla tego eksperymentu
    for max_hours in max_driver_hours_list:
        distance_matrix, orders, vehicle_capacity, time_windows, max_driver_hours = prepare_data(num_clients,
                                                                                                 vehicle_capacity,
                                                                                                 max_hours)

        ga_route, ga_cost = genetic_algorithm(distance_matrix, orders, vehicle_capacity, time_windows, max_driver_hours)

        aco = ACO(distance_matrix, n_ants=10, n_best=5, n_iterations=100, decay=0.95)
        aco_route, aco_cost = aco.run()

        pso_route, pso_cost = pso_optimize(distance_matrix, orders, vehicle_capacity, time_windows, max_driver_hours)

        sa_route, sa_cost = simulated_annealing(distance_matrix, orders, vehicle_capacity, time_windows,
                                                max_driver_hours)

        results.append({
            'max_driver_hours': max_hours,
            'GA': {'route': ga_route, 'cost': ga_cost},
            'ACO': {'route': aco_route, 'cost': aco_cost},
            'PSO': {'route': pso_route, 'cost': pso_cost},
            'SA': {'route': sa_route, 'cost': sa_cost},
        })
    return results


# Główna funkcja eksperymentalna
def run_experiment():
    # Test z różnymi maksymalnymi czasami pracy kierowców
    max_driver_hours_list = [6, 8, 10, 12]
    results_driver_hours = experiment_vary_driver_hours(max_driver_hours_list)
    for result in results_driver_hours:
        print("Max driver hours:", result['max_driver_hours'])
        for algorithm in ['GA', 'ACO', 'PSO', 'SA']:
            route = result[algorithm]['route']
            cost = result[algorithm]['cost']
            formatted_cost = f"{cost:.2f}".replace('.', ',')
            print(f"{algorithm} Route: {route}, Cost: {formatted_cost}")


if __name__ == "__main__":
    run_experiment()