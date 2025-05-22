import time
import random

def binary_search(arr, target):

    start = 0
    end = len(arr) - 1
    found = False

    while start <= end and not found:
        mid = (start + end) // 2
        if arr[mid] == target:
            found = True
        else:
            if target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
    if found:
        return mid
    else:
        return None

def linear_search(number_to_find, list_to_search):
    idx = 0
    found = False

    while not found and idx < len(list_to_search):
        if list_to_search[idx] == number_to_find:
            found = True
        else:
            idx += 1
    return found, idx if idx < len(list_to_search) else None

max_number = 100000000
list_of_numbers = [i for i in range(max_number)]

target_number = random.uniform(0, max_number)

start = time.time()
linear_search(target_number, list_of_numbers)
end = time.time()
print(f"Linear search took {end - start} seconds")

start = time.time()
binary_search(list_of_numbers, target_number)
end = time.time()
print(f"Binary search took {end - start} seconds")

