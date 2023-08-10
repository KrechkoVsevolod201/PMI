import numpy as np


def array_generator(lowest_int, highest_int, size):
    return np.random.randint(lowest_int, highest_int, size)


def find_cube(arr):
    print(arr)
    positive_numbers_arr = arr[arr > 0]
    positive_cubes_arr = positive_numbers_arr ** 3
    return np.prod(positive_cubes_arr)


if __name__ == '__main__':
    arr = array_generator(-10, 10, 20)
    print(find_cube(arr))