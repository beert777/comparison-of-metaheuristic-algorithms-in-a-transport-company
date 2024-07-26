import numpy as np

#GŁÓWNE DANE
"""
def prepare_data():
    distance_matrix = np.random.rand(10, 10) * 100
    orders = [10, 15, 20, 10, 25, 5, 10, 15, 10, 5]
    vehicle_capacity = 50
    time_windows = [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9), (5, 10), (6, 11), (7, 12), (8, 13), (9, 14)]
    return distance_matrix, orders, vehicle_capacity, time_windows
"""
# ZMIANA LICZBY KLIENTÓW
"""
def prepare_data(num_clients=10):
    distance_matrix = np.random.rand(num_clients, num_clients) * 100
    orders = np.random.randint(5, 25, size=num_clients).tolist()
    vehicle_capacity = 50
    time_windows = [(np.random.randint(0, 5), np.random.randint(6, 10)) for _ in range(num_clients)]
    return distance_matrix, orders, vehicle_capacity, time_windows
"""
"""
#ZMIANA WIELKOŚCI ZAMOÓWIENIA
def prepare_data(num_clients=10, min_order_size=5, max_order_size=25):
    distance_matrix = np.random.rand(num_clients, num_clients) * 100
    orders = np.random.randint(min_order_size, max_order_size, size=num_clients).tolist()
    vehicle_capacity = 50
    time_windows = [(np.random.randint(0, 5), np.random.randint(6, 10)) for _ in range(num_clients)]
    return distance_matrix, orders, vehicle_capacity, time_windows
"""
"""
#ZMIANA OKIEN CZASOWYCH
def prepare_data(num_clients=10, time_window_start_range=(0, 5), time_window_end_range=(6, 10)):
    distance_matrix = np.random.rand(num_clients, num_clients) * 100
    orders = np.random.randint(5, 25, size=num_clients).tolist()
    vehicle_capacity = 50
    time_windows = [(np.random.randint(time_window_start_range[0], time_window_start_range[1]),
                     np.random.randint(time_window_end_range[0], time_window_end_range[1]))
                    for _ in range(num_clients)]
    return distance_matrix, orders, vehicle_capacity, time_windows
"""
"""
#ZMIANA WIELKOŚCI POJAZDU
def prepare_data(num_clients=10, vehicle_capacity=50):
    distance_matrix = np.random.rand(num_clients, num_clients) * 100
    orders = np.random.randint(5, 25, size=num_clients).tolist()
    time_windows = [(np.random.randint(0, 5), np.random.randint(6, 10)) for _ in range(num_clients)]
    return distance_matrix, orders, vehicle_capacity, time_windows
"""
def prepare_data(num_clients=10, vehicle_capacity=50, max_driver_hours=8):
    distance_matrix = np.random.rand(num_clients, num_clients) * 100
    orders = np.random.randint(5, 25, size=num_clients).tolist()
    time_windows = [(np.random.randint(0, 5), np.random.randint(6, 10)) for _ in range(num_clients)]
    return distance_matrix, orders, vehicle_capacity, time_windows, max_driver_hours