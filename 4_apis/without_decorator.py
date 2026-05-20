from time import perf_counter
def sum_with_loop(n):
    start_time = perf_counter()
    total = 0
    for i in range(n):
        total += i
    end_time = perf_counter()
    print(f"sum_with_loop: {end_time - start_time}")
    return total
    
def sum_with_formula(n):
    start_time = perf_counter()
    total = n * (n + 1) // 2
    end_time = perf_counter()
    print(f"sum_with_formula: {end_time - start_time}")
    return total

def sum_with_recursion(n):
    if n == 1:
        return 1
    else:
        return n + sum_with_recursion(n-1)

if __name__ == "__main__":
    sum_with_loop(100)
    sum_with_formula(100)