import random


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def shuffle_array(array: list, randomness: int):
    for i in range(len(array)):
        j = random.randint(0, len(array) - 1)
        if random.random() <= randomness:
            swap(array, i, j)