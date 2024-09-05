import concurrent.futures
import multiprocessing

total_shared_locked = multiprocessing.Value('i', 0)
total_shared = multiprocessing.Value('i', 0)
total = 0

def work(item):
    global total 
    result = item * item
    total += result
    total_shared.value += result
    with total_shared_locked.get_lock():
        total_shared_locked.value += result

def main():
    items = range(1000)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(work, items)
    print(f"total_shared_locked {total_shared_locked.value}")
    # This will be slightly different every run since we will be loosing total updates to race conditions
    print(f"total_shared: {total_shared.value}")
    # This will be zero because total is not actually shared in ProcessPoolExecutor.
    print(f"total: {total}")

if __name__ == '__main__':
    main()