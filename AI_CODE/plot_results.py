import pandas as pd
import matplotlib.pyplot as plt # type: ignore
import os

def plot_charts():
    csv_file = "results/experiment_results.csv"

    if not os.path.exists(csv_file):
        print("ERROR: Run experiments.py first!")
        return

    df = pd.read_csv(csv_file)

    algorithms = df["Algorithm"].unique()

    #===============      COST GRAPH     =====================
    plt.figure(figsize=(10, 6))
    for algo in algorithms:
        sub = df[df["Algorithm"] == algo]
        plt.plot(sub["N_Tasks"], sub["Avg_Cost"], marker="o", label=algo)

    plt.title("Average Tardiness Cost Comparison")
    plt.xlabel("Number of Tasks")
    plt.ylabel("Avg Total Tardiness")
    plt.grid(True)
    plt.legend()
    plt.savefig("results/cost_comparison.png")
    print("Saved: results/cost_comparison.png")

    #===============      TIME GRAPH     =====================
    plt.figure(figsize=(10, 6))
    for algo in algorithms:
        if algo == "Random (Initial)":
            continue
        sub = df[df["Algorithm"] == algo]
        plt.plot(sub["N_Tasks"], sub["Avg_Time"], marker="x", linestyle="--", label=algo)

    plt.title("Execution Time Comparison")
    plt.xlabel("Number of Tasks")
    plt.ylabel("Time (sec)")
    plt.grid(True)
    plt.legend()
    plt.savefig("results/time_comparison.png")
    print("Saved: results/time_comparison.png")

if __name__ == "__main__":
    plot_charts()
