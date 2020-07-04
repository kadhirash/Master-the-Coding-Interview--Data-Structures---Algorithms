numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, 5]


def insertion_sort(arr):
    length = len(arr)
    comparisons = 0
    for i in range(1, length):
        print(f'Iteration: # {i+1} {arr}\n')
        current_val = arr[i]
        pos = i
        while pos > 0 and arr[pos-1] > current_val:
            comparisons += 1
            arr[pos] = arr[pos-1]
            pos = pos-1
        arr[pos] = current_val
    print(f'comparisons: {comparisons}\n')


insertion_sort(numbers)
print(f'Final sorted array: {numbers}')
