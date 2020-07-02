# ### ------ INTRO ------ ###
# strings = ['a','b','c','d']
# # 4*4 = 16 bytes of storage is used

# print(strings[2]) #c

# #push
# strings.append('e')      # O(1) or {O(n) if dynamic}
# print(f'Adding e at the end{strings}')
# #pop
# strings.pop()
# strings.pop()            # O(1)
# print(f'Popping off last 2 elements {strings}')
# #addfirstelement
# strings.insert(0,'x')    #O(n)
# print(f'Inserting x at the beg. {strings}')
# #splice
# strings.insert(2,'alien')   #O(n)

# print(f'Splicing alien at pos. 2{strings}')

### ------ IMPLEMENTATION ------ ###

# class MyArray():
#     def __init__(self):
#         self.length = 0
#         self.data = {}

#     def __str__(self):
#         return str(self.__dict__)

#     def get(self, index):
#         return self.data[index]

#     def push(self, item):
#         self.data[self.length] = item
#         self.length += 1
#         return self.length

#     def pop(self):
#         lastItem = self.data[self.length - 1]
#         del self.data[self.length - 1]
#         self.length -= 1
#         return lastItem

#     def delete_at_index(self, index):
#         item = self.data[index]
#         self.shift_items(index)
#         return item

#     def shift_items(self, index):
#         for i in range(index, self.length - 1):
#             self.data[i] = self.data[i + 1]
#         del self.data[self.length - 1]
#         self.length -= 1

# arr = MyArray()

# arr.push('hi')
# arr.push('you')
# arr.push('!')
# arr.delete_at_index(0)
# arr.push('are')
# arr.push('nice')
# print(arr)
# arr.delete_at_index(1)
# print(arr)

### ------ REVERSE A STRING ------ ###

# def reverse(string):
#     #check input
#     if not (string) or len(string) < 2 or not (type(string)):
#         return 'hmm thats not good'
#     backwards = []
#     total_items = len(string) - 1
#     for i in range(total_items, -1, -1):
#         backwards.append(string[i])
#     #print(backwards)
#     return ''.join(backwards)

# def reverse2(string):
#     """
# 	Function that reverse a string.

# 	Parameters:
# 		string: a string

# 	Returns:
# 		rev_str: reversed string
# 	"""
#     rev_str = str()
#     for i in range(len(string) - 1, -1, -1):
#         rev_str = rev_str + string[i]
#     return rev_str

# string = 'Hello'

# print(reverse('test'))


### ------ MERGE SORTED ARRAYS ------ ###

def merge(arr1, arr2):
    """
    Function that merges two arrays, lowest to highest.

    Parameters:
            arr1: array 1 
            arr2: array 2

    Returns:
            merged_arr: merged array
    """
    # base case
    if len(arr1) == 0 or len(arr2) == 0:
        return arr1 + arr2
    merged_arr = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
            print(merged_arr)
        elif arr1[i] > arr2[j]:
            merged_arr.append(arr2[j])
            j += 1
            print(merged_arr)
    return merged_arr + arr1[i:] + arr2[j:]


arr1 = [0, 3, 4, 31]
arr2 = [4, 6, 30]

print(merge(arr1, arr2))
