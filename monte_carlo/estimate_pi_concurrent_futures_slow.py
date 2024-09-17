import numpy as np
import concurrent.futures
import multiprocessing

def set_global(shared_points_inside_circle):
    global points_inside_circle  
    points_inside_circle = shared_points_inside_circle

# Turns out this is pretty slow. 
# Will need to dig in more to nail down why - likely the overhead of sharing points_inside_circle, including managing a shared lock across processes
def estimate_pi(num_samples):
    iterations = range(num_samples)
    points_inside_circle = multiprocessing.Value('i', 0)
    with concurrent.futures.ProcessPoolExecutor(initializer=set_global, initargs=(points_inside_circle,)) as executor:
        futures = [executor.submit(estimate_pi_worker) for _ in iterations]
        concurrent.futures.wait(futures)

    print("points_inside_circle.value:", points_inside_circle.value)
    pi_estimate = 4 * points_inside_circle.value / num_samples
    return pi_estimate

def estimate_pi_worker():
    x, y = np.random.uniform(-1, 1), np.random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        with points_inside_circle.get_lock():
            points_inside_circle.value += 1

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

# sample_sizes = np.geomspace(1000, 10000, num=3, dtype=int)
sample_sizes = np.geomspace(10000, 7500000, num=3, dtype=int)
for size in sample_sizes:
    estimate = estimate_pi(size)
    print(f"Sample size: {size}. Pi estimate: {estimate:.5f}")