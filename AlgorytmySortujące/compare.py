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

def Select_sort(arr):

    for run in range(len(arr)):
        min_index = run
        for i in range(run+1, len(arr)):
            if arr[i] < arr[min_index]:
                min_index = i
        arr[run], arr[min_index] = arr[min_index], arr[run]

def Merge_sort(arr):

    list_len = len(arr)
    sorted_list = []

    if list_len <= 1:
        sorted_list = arr
    else:
        middle_point = list_len // 2
        list_left = Merge_sort(arr[:middle_point])
        list_right = Merge_sort(arr[middle_point:])

        idx_left = idx_right = 0
        while idx_left < len(list_left) and idx_right < len(list_right):
            if list_left[idx_left] < list_right[idx_right]:
                sorted_list.append(list_left[idx_left])
                idx_left += 1
            else:
                sorted_list.append(list_right[idx_right])
                idx_right += 1

        sorted_list.extend(list_left[idx_left:])
        sorted_list.extend(list_right[idx_right:])

    return sorted_list

def divide(arr, start, end):

    i = start
    border_value = arr[end]

    for j in range(start, end):

        if arr[j] <= border_value:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[end] = arr[end], arr[i]
    return i

def quick_sort(arr, start, end):

    if start < end:

        border_index = divide(arr, start, end)
        quick_sort(arr, start, border_index - 1)
        quick_sort(arr, border_index + 1, end)

max_limit = 5000
listofnumbers = [random.randint(0, max_limit) for _ in range(max_limit)]
listofnumbers2 = listofnumbers.copy()
listofnumbers3 = listofnumbers.copy()
listofnumbers4 = listofnumbers.copy()
listofnumbers5 = listofnumbers.copy()
listofnumbers6 = listofnumbers.copy()

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

start = time.time()
Select_sort(listofnumbers4)
end = time.time()
print(f"Select sort time: {end - start}")

start = time.time()
Merge_sort(listofnumbers5)
end = time.time()
print(f"Merge sort time: {end - start}")

start = time.time()
quick_sort(listofnumbers6, 0, len(listofnumbers6) - 1)
end = time.time()
print(f"Quick sort time: {end - start}")