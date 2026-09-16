import time

def measure_search_time(container, target):
    start = time.perf_counter()
    _ = target in container
    return (time.perf_counter() - start) * 1000  # у мілісекундах

def run_task5():
    print("=== Завдання 5. Алгоритмічна складність і обґрунтування вибору структури ===")
    sizes = [1000, 10000, 100000]
    
    print(f"{'Розмір (n)':<10} | {'Пошук у List (мс)':<20} | {'Пошук у Set (мс)':<20}")
    print("-" * 55)
    
    for n in sizes:
        data_list = list(range(n))
        data_set = set(data_list)
        target = n - 1
        
        t_list = measure_search_time(data_list, target)
        t_set = measure_search_time(data_set, target)
        
        print(f"{n:<10} | {t_list:<20.5f} | {t_set:<20.5f}")
    print()

if __name__ == "__main__":
    run_task5()