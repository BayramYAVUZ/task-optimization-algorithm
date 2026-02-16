import random
import math

# --------------------------------------------------------------------
def calculate_fitness(schedule):
    cost = 0
    current_time = 0

    for task in schedule:
        start = max(current_time, task.release_time)
        finish = start + task.processing_time
        lateness = max(0, finish - task.due_time)

        cost += lateness
        current_time = finish

    return cost


# --------------------------------------------------------------------
def get_neighbor(schedule):
    new_schedule = schedule[:]
    i = random.randint(0, len(schedule) - 1)
    j = random.randint(0, len(schedule) - 1)
    new_schedule[i], new_schedule[j] = new_schedule[j], new_schedule[i]
    return new_schedule


# --------------------------------------------------------------------
def hill_climbing(schedule, iterations=2000):
    current = schedule[:]
    current_fitness = calculate_fitness(current)

    for _ in range(iterations):
        neighbor = get_neighbor(current)
        neighbor_fitness = calculate_fitness(neighbor)

        if neighbor_fitness < current_fitness:
            current = neighbor
            current_fitness = neighbor_fitness

    return current, current_fitness


# --------------------------------------------------------------------
def random_restart_hill_climbing(schedule, restarts=10, iterations=2000):
    best_schedule = None
    best_fitness = float("inf")

    for _ in range(restarts):
        random.shuffle(schedule)
        candidate, fit = hill_climbing(schedule, iterations)

        if fit < best_fitness:
            best_fitness = fit
            best_schedule = candidate

    return best_schedule, best_fitness


# --------------------------------------------------------------------
def simulated_annealing(schedule, T_start=100, T_end=0.01, cooling=0.995):
    current = schedule[:]
    current_fitness = calculate_fitness(current)

    T = T_start
    best = current
    best_fitness = current_fitness

    while T > T_end:
        neighbor = get_neighbor(current)
        neighbor_fitness = calculate_fitness(neighbor)

        if neighbor_fitness < current_fitness:
            current = neighbor
            current_fitness = neighbor_fitness
        else:
            p = math.exp((current_fitness - neighbor_fitness) / T)
            if random.random() < p:
                current = neighbor
                current_fitness = neighbor_fitness

        if current_fitness < best_fitness:
            best = current
            best_fitness = current_fitness

        T *= cooling

    return best, best_fitness


# --------------------------------------------------------------------
def genetic_algorithm(tasks, population_size=40, generations=50, mutation_rate=0.1):
    population = []
    for _ in range(population_size):
        s = tasks[:]
        random.shuffle(s)
        population.append(s)

    for _ in range(generations):
        fitness_scores = [(s, calculate_fitness(s)) for s in population]
        fitness_scores.sort(key=lambda x: x[1])

        new_population = [
            fitness_scores[0][0][:],
            fitness_scores[1][0][:]
        ]

        while len(new_population) < population_size:
            parent1 = random.choice(population)
            parent2 = random.choice(population)

            cut1 = random.randint(0, len(tasks) - 1)
            cut2 = random.randint(cut1, len(tasks) - 1)

            child = [None] * len(tasks)
            child[cut1:cut2] = parent1[cut1:cut2]

            p2_index = 0
            for i in range(len(tasks)):
                if child[i] is None:
                    while parent2[p2_index] in child:
                        p2_index += 1
                    child[i] = parent2[p2_index]

            if random.random() < mutation_rate:
                i = random.randint(0, len(tasks) - 1)
                j = random.randint(0, len(tasks) - 1)
                child[i], child[j] = child[j], child[i]

            new_population.append(child)

        population = new_population

    best = min(population, key=lambda s: calculate_fitness(s))
    return best, calculate_fitness(best)
