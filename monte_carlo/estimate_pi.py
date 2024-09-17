import numpy as np
import timeit

def estimate_pi(num_samples):
    points_inside_circle = 0

    for i in range(num_samples):
        x, y = np.random.uniform(-1, 1), np.random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            points_inside_circle += 1
        print_progress(num_samples, i)

    clear_progress()
    pi_estimate = 4 * points_inside_circle / num_samples
    return pi_estimate

def clear_progress():
    print("\r\033[K", end="") 

def print_progress(num_samples, current_iteration):
    max_indicators = 50
    indicator_period = int(num_samples / max_indicators) + 1
    if current_iteration % indicator_period == 0:
        periods = current_iteration / indicator_period
        percent = int(current_iteration / num_samples * 100)
        progress = f"Sample size: {num_samples}. {percent}% "
        for _ in range(int(periods)):
            progress += "."
        print(progress, end="\r")

def run_estimates():
    # sample_sizes = np.geomspace(1000, 10000, num=3, dtype=int)
    sample_sizes = np.geomspace(10000, 3000000, num=3, dtype=int)
    for size in sample_sizes:
        estimate = estimate_pi(size)
        print(f"Sample size: {size}. Pi estimate: {estimate:.5f}")

timer = timeit.Timer(lambda: run_estimates())
execution_time = timer.timeit(number=1)
print(f"\nTotal Execution Time: {execution_time} seconds")