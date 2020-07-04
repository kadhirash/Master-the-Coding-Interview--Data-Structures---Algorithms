numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, 5]
comparisons = 0

def merge_sort(arr):
    length = len(arr)

    if length == 1:
        return arr

    else:
        mid = length // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        print(f'Left Array: {left_arr}')
        print(f'Right Array: {right_arr}\n')
        return merge(merge_sort(left_arr), merge_sort(right_arr))

        # print(f'Iteration: # {i+1} {arr}\n')

   # print(f'comparisons: {comparisons}\n')


def merge(left, right):
    l_length, left_index = len(left), 0
    r_length, right_index = len(right), 0

    sorted_arr = []
    
    while(left_index < l_length and right_index < r_length):
        global comparisons
        comparisons += 1
        if left[left_index] < right[right_index]:
            sorted_arr.append(left[left_index])
            left_index += 1
        else:
            sorted_arr.append(right[right_index])
            right_index += 1
     # print(f'Iteration: # {i+1} {arr}\n')
    print(f'Merge function - Sorted Array, Left, Right: {sorted_arr} + {left[left_index:]} + {right[right_index:]}\n')
    return(sorted_arr + left[left_index:] + right[right_index:])

print(f'Final sorted array: {merge_sort(numbers)}')
print(f'comparisons: {comparisons}')
