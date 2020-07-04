'''
    Given a number N return the index val of Fibonacci seq., where seq. is:
    0, 1, 1, 2, 3, 5, 8 ...
    The pattern of seq is: Each value = sum of 2 previous values 
'''


def FibonacciIterative(n): # O(n)
    arr = [0, 1]

    for i in range(2, n + 1):
        arr.append(arr[i-2] + arr[i-1])
    return arr[n]


#print(FibonacciIterative(43))


def FibonacciIterativeRecursive(n): # O(2^n) --> exponential
    if n <= 1:
        return n
    else:
        return FibonacciIterativeRecursive(n-2) + FibonacciIterativeRecursive(n-1)


print(FibonacciIterativeRecursive(30))
