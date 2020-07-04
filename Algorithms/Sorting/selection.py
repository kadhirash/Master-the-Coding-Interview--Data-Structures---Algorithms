numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, 5]


def selection_sort(arr):
    length = len(arr)
    comparisons = 0
    for i in range(length-1):
        print(f'Iteration: # {i+1} {arr}\n')
        # curr index as minimum
        min = i
        for j in range(i+1, length):
            comparisons += 1
            if arr[min] > arr[j]:
                # update min if curr is lower than what we had prev
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    print(f'comparisons: {comparisons}\n')


selection_sort(numbers)
print(f'Final sorted array: {numbers}')
