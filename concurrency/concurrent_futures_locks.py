import concurrent.futures
import multiprocessing

total_mp = multiprocessing.Value('i', 0)
total = 0

def work(item):
    global total 
    result = item * item
    total += result
    with total_mp.get_lock():
        total_mp.value += result

def main():
    items = range(10000)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        list(executor.map(work, items))
    print(f"total_mp: {total_mp.value}")
    # This will be zero because total is not actually shared in ProcessPoolExecutor.
    print(f"total: {total}")

if __name__ == '__main__':
    main()