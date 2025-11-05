import random

func = input()

def f(x):
    return eval(func)


def genetic_algorithm():
    population = [random.uniform(0, 6) for _ in range(20)]
    max_generations = 50
    for _ in range(max_generations):
        scores = [f(x) for x in population]
        best = population[scores.index(max(scores))]
        new_population = [best]  # keep best
        while len(new_population) < len(population):
            parents = random.sample(population, 2)
            child = (parents[0] + parents[1]) / 2
            # mutation: small random step
            if random.random() < 0.3:
                child += random.uniform(-0.2, 0.2)
                child = max(0, min(6, child))
            new_population.append(child)
        population = new_population
    scores = [f(x) for x in population]
    best = population[scores.index(max(scores))]
    return best, f(best)


result_x, result_value = genetic_algorithm()
print(f"Best found x = {result_x:.2f}, value = {result_value:.2f}")