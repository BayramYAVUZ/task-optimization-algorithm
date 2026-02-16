import time
import csv
import os
from utils import generate_random_tasks
from scheduler import (calculate_fitness)
from scheduler import (hill_climbing)
from scheduler import (random_restart_hill_climbing)
from scheduler import (simulated_annealing)
from scheduler import (genetic_algorithm)
#========================================================================================

def run_experiments():
    if not os.path.exists("results"):
        os.makedirs("results")
    n_values = [10, 20, 30, 40, 50]
    TRIALS = 5 
    results_data = []
    print(f"\n--- EXPERIMENTS STARTED ({TRIALS} trials each) ---\n")

    for n in n_values:
        print(f">>> Running tests for N = {n} tasks...\n")

        algos = {
            "Random (Initial)": {"cost": 0, "time": 0},
            "Hill Climbing": {"cost": 0, "time": 0},
            "Random Restart HC": {"cost": 0, "time": 0},
            "Simulated Annealing": {"cost": 0, "time": 0},
            "Genetic Algorithm": {"cost": 0, "time": 0}
        }

        for t in range(TRIALS):
            print(f"   Trial {t+1}/{TRIALS}")
            tasks = generate_random_tasks(n, max_deadline=n * 3)

            start = time.time()
            cost = calculate_fitness(tasks)
            algos["Random (Initial)"]["cost"] += cost
            algos["Random (Initial)"]["time"] += (time.time() - start)

            start = time.time()
            _, cost = hill_climbing(tasks, iterations=1200)
            algos["Hill Climbing"]["cost"] += cost
            algos["Hill Climbing"]["time"] += (time.time() - start)

            start = time.time()
            _, cost = random_restart_hill_climbing(tasks, restarts=6, iterations=600)
            algos["Random Restart HC"]["cost"] += cost
            algos["Random Restart HC"]["time"] += (time.time() - start)
           
            start = time.time()
            _, cost = simulated_annealing(tasks, T_start=900, cooling=0.94)
            algos["Simulated Annealing"]["cost"] += cost
            algos["Simulated Annealing"]["time"] += (time.time() - start)

            start = time.time()
            _, cost = genetic_algorithm(tasks, population_size=30, generations=40)
            algos["Genetic Algorithm"]["cost"] += cost
            algos["Genetic Algorithm"]["time"] += (time.time() - start)

        for algo, data in algos.items():
            results_data.append([
                n,
                algo,
                data["cost"] / TRIALS,
                data["time"] / TRIALS
            ])

    csv_file = "results/experiment_results.csv" # FOR CSV
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["N_Tasks", "Algorithm", "Avg_Cost", "Avg_Time"])
        writer.writerows(results_data)

    print(f"\n✔ Experiment finished → results saved to: {csv_file}")

if __name__ == "__main__":
    run_experiments()
