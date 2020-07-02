### ------ INTRODUCTION ------ ###

user = dict()
user = {
	'age' : 54,
	'name' :'Kylie',
	'magic': True,
	'scream': 'ahhh!'
}

# print(user['age']) # 0(1)

user['spell'] = 'abra kadabra' # O(1)

# print(user['scream']) # 0(1)

### ------ COLLISION ------ ###
# READING/WRITING
# O(n/k), k = size of hash table --> O(n)


### ------ IMPLEMENTATION ------ ###
class HashTable():
    def __init__(self, size):
        self.size = size
        self.data = [None] * self.size

    def __str__(self):
        return str(self.__dict__)

    def _hash(self, key):  # 0(1)
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % self.size
            # print(hash)
        return hash

    def set(self, key, value):  # O(1)
        address = self._hash(key)
        if not(self.data[address]):
            self.data[address] = []
        self.data[address].append([key, value])
        return self.data

    def get(self, key):  # O(1), or O(n) w/ collisions
        address = self._hash(key)
        current_bucket = self.data[address]
        # print(currentBucket)
        if current_bucket:
            for i in range(len(current_bucket)):
                if current_bucket[i][0] == key:
                    return current_bucket[i][1]
        return None

    def keys(self):
        keys_array = []
        for i in range(len(self.data)):
            if self.data[i] != None:
                for j in range(len(self.data[i])):
                    keys_array.append(self.data[i][j][0])
        return keys_array

    def values(self):
        values_array = []
        for i in range(len(self.data)):
            if self.data[i] != None:
                for j in range(len(self.data[i])):
                    values_array.append(self.data[i][j][1])
        return values_array


# myHashTable = HashTable(50)
# myHashTable._hash('grapes')
# myHashTable.set('grapes', 10000)
# myHashTable.set('apples', 54)
# myHashTable.set('oranges', 2)
# myHashTable.get('grapes')
# print(myHashTable.keys())
# print(myHashTable.values())


### ------ (GOOGLE) FIRST RECURRING CHARACTER ------ ###

# Given an array = [2,5,1,2,3,5,1,2,4]:
# Return 2

# Given an array = [2,1,1,2,3,5,1,2,4]:
# Return 1

# Given an array = [2,3,4,5]:
# Return undefined/None


# naive: O(n^2), SC: O(1)
def first_recurring_char(input):
    for i in range(len(input)):
        for j in range(i-1,0,-1):
            if input[i] == input[j]:
                return input[i]
    return None

#print(first_recurring_char([2, 5, 1, 2, 3, 5, 1, 2, 4]))

# optimized: O(n), SC: O(n) now because of hash_table

def first_recurring_char2(input):
    hash_table = dict()
    for i in input:
        #print(hash_table)
        if i in hash_table != None:
            return i
        else:
            hash_table[i] = i
    #print(hash_table)
    return None

array = [2, 5, 5, 2, 3, 5, 1, 2, 4]
array2 = [2, 1, 1, 2, 3, 5, 1, 2, 4]
array3 = [2, 3, 4, 5]
#print(first_recurring_char(array3))
