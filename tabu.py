import random
func = input()

def f(x):
    return - (x - 3)**2 + 5


def tabu_search():
    current_x = random.uniform(0, 6)
    tabu_list = []
    tabu_size = 5
    step_size = 0.1
    max_iterations = 100
    best_x = current_x
    best_eval = f(current_x)
    for _ in range(max_iterations):
        neighbors = [current_x + step_size, current_x - step_size]
        neighbors = [x for x in neighbors if 0 <=
                     x <= 6 and x not in tabu_list]
        if not neighbors:
            break
        neighbor_scores = [f(x) for x in neighbors]
        best_neighbor_idx = neighbor_scores.index(max(neighbor_scores))
        best_neighbor = neighbors[best_neighbor_idx]
        if f(best_neighbor) > best_eval:
            best_x, best_eval = best_neighbor, f(best_neighbor)
        tabu_list.append(current_x)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)
        current_x = best_neighbor
    return best_x, f(best_x)


result_x, result_value = tabu_search()
print(f"Best found x = {result_x:.2f}, value = {result_value:.2f}")