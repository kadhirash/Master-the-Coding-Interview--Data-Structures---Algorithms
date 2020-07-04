numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, 5]


def bubble_sort(arr):
    length = len(arr)
    comparisons = 0
    for i in range(length-1): 
        print(f'Iteration: # {i+1} {arr}\n')
        for j in range(length-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                # swap
                (arr[j], arr[j+1]) = (arr[j+1], arr[j])
    print(f'comparisons: {comparisons}\n')


bubble_sort(numbers)
print(f'Final sorted array: {numbers}')
