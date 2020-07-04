'''
    Write 2 functions that finds the factorial of any #.
    One is recursive, and other uses for loop.
'''


def findFactorialRecursive(number): # O(n)
    if (number == 2):
        return 2
    else:
        return number * findFactorialRecursive(number-1)


def findFactorialIterative(number): # O(n)
    answer = 1
    if number == 2:
        return 2
    for i in range(2, number+1):
        answer = answer * i
    return answer


print(findFactorialRecursive(5))

#print(findFactorialIterative(5))
