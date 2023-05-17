import util

def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            util.swap(arr, j, j - 1)
            j -= 1

def selection_sort(arr: list):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        util.swap(arr, min_index, i)

def quick_sort(arr: list):
    def partition(array: list, low: int, high: int):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] < pivot:
                i += 1
                util.swap(array, i, j)
        util.swap(array, i + 1, high)
        return i + 1

    def quick_sort_helper(array, low, high):
        size = high - low
        if size == 0:
            return
        if len(array) == 1:
            return

        if low < high:
            pi = partition(array, low, high)
            quick_sort_helper(array, low, pi - 1)
            quick_sort_helper(array, pi + 1, high)

    quick_sort_helper(arr, 0, len(arr) - 1)