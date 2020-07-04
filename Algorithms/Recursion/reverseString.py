# Implement a function that reverses a string using iteration...and then recursion!
def reverseStringIteration(string):
    reversed_string = ''
    for i in range(len(string)):
        reversed_string = reversed_string + string[len(string)-i-1]
    return reversed_string


def reverseStringRecursion(string):
    if string == '':
        return ''
    else:
        return reverseStringRecursion(string[1:]) + string[0]

#reverseString('yoyo mastery')
# should return: 'yretsam oyoy'


print(reverseStringIteration('hello'))
print(reverseStringRecursion('hello'))
