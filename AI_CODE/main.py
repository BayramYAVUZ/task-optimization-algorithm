from utils import generate_random_tasks
from scheduler import hill_climbing, calculate_fitness

#========================================================================================

def print_schedule(schedule):
    for t in schedule:
        print(f"{t.name} | p={t.processing_time}, d={t.due_time}, r={t.release_time}")
    print()

#========================================================================================

def main():
    tasks = generate_random_tasks(12)

    print("- INITIAL SCHEDULE -")
    print_schedule(tasks)
    initial_cost = calculate_fitness(tasks)
    print("Initial Lateness:", initial_cost)

    print("\nOptimizing...\n")

    optimized, best_cost = hill_climbing(tasks)

    print("- OPTIMIZED SCHEDULE -")
    print_schedule(optimized)
    print("Optimized Lateness:", best_cost)

    print("\nImprovement:", initial_cost - best_cost)

#========================================================================================

if __name__ == "__main__":
    main()
