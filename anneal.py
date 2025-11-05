import math
import random

func = input("Nhap ham f(x): ")
def f(x):
    return eval(func)


def get_neighbor(x, step_size=0.1):
    return x + random.uniform(-step_size, step_size)


def simulated_annealing():
    current_x = random.uniform(0, 6)
    best_x = current_x
    best_eval = f(current_x)
    temp = 10
    max_iterations = 1000
    for i in range(max_iterations):
        t = temp / float(i + 1)
        candidate = get_neighbor(current_x)
        candidate = max(0, min(6, candidate))
        candidate_eval = f(candidate)
        if candidate_eval > best_eval or random.random() < math.exp((candidate_eval - best_eval) / t):
            current_x = candidate
            best_eval = candidate_eval
            best_x = current_x
    return best_x, f(best_x)


result_x, result_value = simulated_annealing()
print(f"Best found x = {result_x:.2f}, value = {result_value:.2f}")