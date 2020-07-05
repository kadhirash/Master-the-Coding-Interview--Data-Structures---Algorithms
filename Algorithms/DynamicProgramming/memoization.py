# learn to cache
from functools import lru_cache


def addTo80(n):
    return n + 80


addTo80(5)

cache = {}


def memoizeAddTo80(n):
    if n in cache:
        return cache[n]
    else:
        print('long time')
        answer = n + 80
        cache[n] = answer
        return answer


print(memoizeAddTo80(6))
print(cache)
print('-----------')
print(memoizeAddTo80(6))

# let's make that better with no global scope.

@lru_cache(maxsize=1000)
def memoize_twoAddTo80(n):
    return n + 80


print(memoize_twoAddTo80(6))
print(cache)
print('-----------')
print(memoize_twoAddTo80(6))
print(memoize_twoAddTo80.cache_info())
