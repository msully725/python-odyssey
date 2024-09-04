import numpy as np

def estimate_pi(num_samples):
    points_inside_circle = 0

    for i in range(num_samples):
        x, y = np.random.uniform(-1, 1), np.random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            points_inside_circle += 1
        print_progress(num_samples, i)

    pi_estimate = 4 * points_inside_circle / num_samples
    return pi_estimate

def print_progress(num_samples, current_iteration):
    max_indicators = 10
    indicator_period = num_samples / max_indicators
    if current_iteration % indicator_period == 0:
        print(".")

sample_sizes = np.geomspace(1, 1000000, num=10, dtype=int)
for size in sample_sizes:
    estimate = estimate_pi(size)
    print(f"Sample size: {size}. Pi estimate: {estimate:.5f}")