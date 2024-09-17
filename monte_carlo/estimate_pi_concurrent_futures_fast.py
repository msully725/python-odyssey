import numpy as np
import concurrent.futures
import multiprocessing

def estimate_pi(num_samples):
    # Goal: Aiming for a speed up compared to using shared points_inside_circle.
    # Implementation Plan: Since iterations can run completely indepdently, 
    #   give a block of iterations to each executor,
    #   then sum each executor's points.
    desired_workers = 4
    worker_num_samples = int(num_samples / 4)
    print("worker_num_samples: ", worker_num_samples)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        workers = [executor.submit(estimate_pi_worker, worker_num_samples) for _ in range(desired_workers)]
        concurrent.futures.wait(workers)

    points_inside_circle = sum(worker.result() for worker in workers)
    pi_estimate = 4 * points_inside_circle / num_samples
    return pi_estimate

def estimate_pi_worker(worker_num_samples):
    points_inside_circle = 0
    for _ in range(worker_num_samples):
        x, y = np.random.uniform(-1, 1), np.random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            points_inside_circle += 1

    return points_inside_circle

# sample_sizes = np.geomspace(1000, 10000, num=3, dtype=int)
sample_sizes = np.geomspace(10000, 7500000, num=3, dtype=int)
for size in sample_sizes:
    estimate = estimate_pi(size)
    print(f"Sample size: {size}. Pi estimate: {estimate:.5f}")