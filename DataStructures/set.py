import random
import timeit


def list_unique(arr):
    unique_list = []
    for item in arr:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


array1 = random.sample(range(1, 100001), 50000)
array2 = random.sample(range(50000, 150001), 50000)

set1 = set(array1)
set2 = set(array2)


def measure_time(func, *args):
    start_time = timeit.default_timer()
    func(*args)
    end_time = timeit.default_timer()
    return end_time - start_time


array_time = measure_time(list_unique, array1 + array2)

set_time = measure_time(set.union, set1, set2)

print(f"Время для массивов: {array_time} секунд")
print(f"Время для множеств: {set_time} секунд")
