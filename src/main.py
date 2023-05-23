#Python imports
import types
import time, timeit
import functools

#Local imports
import statistics
import searchingAlgorithms
import util
def time_function(func):
    if isinstance(func, types.LambdaType):
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
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        time_taken = end - start
        print()
        print(f"Elapsed time: {time_taken:0.4f} seconds")
        return value

    return wrapper_timer

def test_algorithm_with_result(algorithm_func, *args, expected_result):
    util.print_line()
    # Get the function name
    func_name = algorithm_func.__name__
    print(f"Testing | {func_name} | algorithm")

    # Call the algorithm function with the provided arguments
    result = algorithm_func(*args)

    # Compare the result with the expected value
    if result == expected_result:
        print(f"Test Passed: Result matches the expected value. ({result})")
    else:
        print("Test Failed: Result does not match the expected value.")
        print(f"Expected: {expected_result}")
        print(f"Actual: {result}")

@timer
def main():
    util.print_line()
    data = [70, 300, 250, 104, 250, 80, 135, 205, 150, 170, 284, 112, 140, 38, 123, 64, 100, 112, 96, 310, 100, 359,
            144, 147, 109, 270, 134, 108, 90, 260, 53, 145, 100, 75, 150, 207, 67, 162, 135, 140, 150, 80, 97]
    statistics.analyze_data_with_CI(data, 0.9, 10, False)

    util.shuffle_array(data, 0.5)
    sorted_data = sorted(data)
    test_algorithm_with_result(searchingAlgorithms.interpolation_search, sorted_data, 112, expected_result=17)

if __name__ == "__main__":
    main()