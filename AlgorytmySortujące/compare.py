import random
import time


def bubble_sort(arr):
    isChange = True

    while isChange:
        isChange = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                isChange = True

def bubble_sort2(arr):

    max_index = len(arr) - 1

    for max_not_sorted_index in range(max_index, 0, -1):
        isChange = False
        for i in range(max_not_sorted_index):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                isChange = True
        if not isChange:
            break

def insert_sort(arr):
    for sort_border in range(1, len(arr)):
        curr_index = sort_border - 1
        value = arr[curr_index+1]

        while arr[curr_index] > value and curr_index >= 0:
            arr[curr_index+1] = arr[curr_index]
            curr_index = curr_index - 1

        arr[curr_index + 1] = value

max_limit = 1000
listofnumbers = [random.randint(0, max_limit) for _ in range(max_limit)]
listofnumbers2 = listofnumbers.copy()
listofnumbers3 = listofnumbers.copy()

start = time.time()
bubble_sort(listofnumbers)
end = time.time()
print(f"Bubble sort time: {end - start}")

start = time.time()
bubble_sort2(listofnumbers2)
end = time.time()
print(f"Bubble sort2 time: {end - start}")

start = time.time()
insert_sort(listofnumbers3)
end = time.time()
print(f"insert sort time: {end - start}")