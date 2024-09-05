import concurrent.futures

def work(item):
    return item * item

def main():
    items = range(10)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(work, items))
    print(results)

if __name__ == '__main__':
    main()