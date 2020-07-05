def linear_search(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i # index
    return -1

print(linear_search([1,2,3,4], 3))