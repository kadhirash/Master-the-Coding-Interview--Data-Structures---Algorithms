# TAKEN FROM GEEKS4GEEKS
# https://www.geeksforgeeks.org/priority-queue-in-python/
class PriorityQueue(object): 
    def __init__(self): 
        self.queue = [] 
  
    def __str__(self): 
        return ' '.join([str(i) for i in self.queue]) 
  
    # for checking if the queue is empty 
    def isEmpty(self): 
        return len(self.queue) == 0
  
    # for inserting an element in the queue 
    def insert(self, data): 
        self.queue.append(data) 
  
    # for popping an element based on Priority 
    def delete(self): 
        try: 
            max = 0
            for i in range(len(self.queue)): 
                if self.queue[i] > self.queue[max]: 
                    max = i 
            item = self.queue[max] 
            del self.queue[max] 
            return item 
        except IndexError: 
            print() 
            exit() 
myPriorityQueue = PriorityQueue()
myPriorityQueue.insert(100)
myPriorityQueue.insert(1)
myPriorityQueue.insert(23)
myPriorityQueue.insert(45)
myPriorityQueue.insert(37)
myPriorityQueue.insert(72)
print(myPriorityQueue)
while not myPriorityQueue.isEmpty():
    print(myPriorityQueue.delete())