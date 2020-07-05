import time


def fibonacci(n):  # O(2^ n)
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def dynamic_fibonacci(n):  # O (n)
    cache = {}
    if n in cache:
        return cache[n]
    else:
        if n < 2:
            return n
        else:
            cache[n] = dynamic_fibonacci(n-1) + dynamic_fibonacci(n-2)
            return cache[n]


def bottom_up_fibonacci(n):
    answer = [0, 1]
    for i in range(2, n):
        answer.append(answer[i-2] + answer[i-1])
    return answer.pop()


t1 = time.time()
print(f'Regular approach:\n {fibonacci(30)}')
t2 = time.time()
print(t2-t1)

t1 = time.time()
print(f'Dynamic Programming approach:\n {dynamic_fibonacci(30)}')
t2 = time.time()
print(t2-t1)

t1 = time.time()
print(f'Bottom up approach:\n {bottom_up_fibonacci(30)}')
t2 = time.time()
print(t2-t1)
