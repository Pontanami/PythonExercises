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

def merge_sort(arr: list):

    def merge(array: list, left: int, middle: int, right: int):
        left_array = array[left:middle + 1]
        right_array = array[middle + 1:right + 1]
        left_index = 0
        right_index = 0
        merged_index = left

        while left_index < len(left_array) and right_index < len(right_array):
            if left_array[left_index] <= right_array[right_index]:
                array[merged_index] = left_array[left_index]
                left_index += 1
            else:
                array[merged_index] = right_array[right_index]
                right_index += 1
            merged_index += 1

        for i in range(left_index, len(left_array)):
            array[merged_index] = left_array[i]
            merged_index += 1

        for j in range(right_index, len(right_array)):
            array[merged_index] = right_array[j]
            merged_index += 1


    def merge_sort_helper(array: list, left: int, right: int):
        if left < right:
            middle = (left + right) // 2
            merge_sort_helper(array, left, middle)
            merge_sort_helper(array, middle + 1, right)
            merge(array, left, middle, right)

    merge_sort_helper(arr, 0, len(arr) - 1)