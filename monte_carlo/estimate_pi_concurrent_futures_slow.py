import numpy as np
import concurrent.futures
import multiprocessing
import timeit

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

    pi_estimate = 4 * points_inside_circle.value / num_samples
    return pi_estimate

def estimate_pi_worker():
    x, y = np.random.uniform(-1, 1), np.random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        with points_inside_circle.get_lock():
            points_inside_circle.value += 1

def run_estimates():
    # sample_sizes = np.geomspace(1000, 10000, num=3, dtype=int)
    sample_sizes = np.geomspace(10000, 3000000, num=3, dtype=int)
    for size in sample_sizes:
        estimate = estimate_pi(size)
        print(f"Sample size: {size}. Pi estimate: {estimate:.5f}")

timer = timeit.Timer(lambda: run_estimates())
execution_time = timer.timeit(number=1)
print(f"\nTotal Execution Time: {execution_time} seconds")