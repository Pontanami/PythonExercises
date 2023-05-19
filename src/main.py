#Python imports
import types
import time, timeit
import functools

#Local imports
import statistics



def main():
    print("Main")

    data = [70, 300, 250, 104, 250, 80, 135, 205, 150, 170, 284, 112, 140, 38, 123, 64, 100, 112, 96, 310, 100, 359,
            144, 147, 109, 270, 134, 108, 90, 260, 53, 145, 100, 75, 150, 207, 67, 162, 135, 140, 150, 80, 97]
    time_function(lambda: statistics.analyze_data_with_CI(data, 0.9, 10, False))

def time_function(func):
    if isinstance(func, types.LambdaType):
        # The function is passed as a lambda expression
        start_time = timeit.default_timer()
        func()
        end_time = timeit.default_timer()
    else:
        raise ValueError("Invalid function type")
    
    elapsed_time = end_time - start_time
    print()
    print(f"Elapsed time: {elapsed_time:.6f} seconds")

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        tic = time.perf_counter()
        value = func(*args, **kwargs)
        toc = time.perf_counter()
        time_taken = toc - tic
        print(f"Elapsed time: {time_taken:0.4f} seconds")
        return value

    return wrapper_timer


if __name__ == "__main__":
    main()