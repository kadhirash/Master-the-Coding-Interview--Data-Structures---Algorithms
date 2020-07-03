class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first

    def enqueue(self,value):
        new_node = Node(value)
        if (self.length == 0):
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return self
    
    def dequeue(self):
        if not(self.first):
            return None
        if self.first == self.last:
            self.last = None
        self.first = self.first.next
        self.length -= 1
        return self

    def print_queue(self):
        if self.length == 0:
            print("Queue Empty")
            return
        else:
            current_pointer = self.first
            while(current_pointer!= None):
                if current_pointer.next == None:
                    print(current_pointer.value)
                else:
                    print(f'{current_pointer.value}  <<--  ', end='')
                current_pointer = current_pointer.next
            return
    
myQueue = Queue()

myQueue.enqueue('Joy')
myQueue.enqueue('Matt')
myQueue.enqueue('Pavel')
myQueue.enqueue('Samir')

myQueue.peek()

myQueue.print_queue()

myQueue.dequeue()
myQueue.dequeue()

myQueue.print_queue()