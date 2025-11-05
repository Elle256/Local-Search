
# Nhap ham tu input, thuat toan tim x trong khoang(0,6) de ham nhap vao dat max
import random

func = input("Nhap ham f(x): ")

def f(x):
    return eval(func)


def hill_climb():
    current_x = random.uniform(0, 6)
    step = 0.1
    max_iter= 100
    for i in range(max_iter):
        neighbors = [current_x + step, current_x - step]
        neighbors = [x for x in neighbors if 0<=x<=6]
        score = [f(x) for x in neighbors]

        best_neighbor_ind = score.index(max(score))
        best_neighbor = neighbors[best_neighbor_ind]

        if f(current_x) < f(best_neighbor):
            current_x = best_neighbor
        else:
            break
    return current_x, f(current_x)


result_x, result_value = hill_climb()
print(f"Found maximum at x = {result_x:.2f}, value = {result_value:.2f}")