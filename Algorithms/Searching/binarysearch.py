# recursive

def binary_search(arr, low, high, item):
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == item:
            return mid

        elif arr[mid] > item:
            return binary_search(arr, low, mid - 1, item)
        else:
            return binary_search(arr, mid + 1, high, item)
    else:
        return -1

# arr = [1,2,3,4,5,35,70,100]
# item = 100
# print(binary_search(arr, 0, len(arr), item))


# iterative

def binary_searchi(arr, item):
    low = 0
    mid = 0
    high = len(arr)

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < item:
            low = mid + 1

        elif arr[mid] > item:
            high = mid - 1
        else:
            return mid
    return -1


arr = [1,2,3,4,5,35,70,100]
item = 100
print(binary_searchi(arr, item))