

def binary_search(array: list, target: str):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            return middle
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1

def interpolation_search(sorted_array: list, target: int) -> int:
    def interpolation_search_recursive(array: list, left: int, right: int, x: int) -> int:
        if left <= right and array[left] <= x <= array[right]:
            # Probing the position with keeping
            # uniform distribution in mind.
            mid_index = left + ((right - left) // (array[right] - array[left])) * (x - array[left])

            # Condition of target found
            if array[mid_index] == x:
                return mid_index

            # target is in the right subarray
            elif array[mid_index] < x:
                return interpolation_search_recursive(array, mid_index + 1, right, x)

            # target is in the left subarray
            elif array[mid_index] > x:
                return interpolation_search_recursive(array, left, mid_index - 1, x)

        return -1

    return interpolation_search_recursive(sorted_array, 0, len(sorted_array) - 1, target)
