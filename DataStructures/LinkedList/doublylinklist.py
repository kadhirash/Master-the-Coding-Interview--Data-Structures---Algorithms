### ------ INTRODUCTION ------ ###


### ------ IMPLEMENTATION ------ ###

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 1

    # Append to end of linkedList
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            return self

    # Prepend to beginning of linkedList
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1
        return self

    # Insert method
    def insert(self, index, value):
        # Insert at end
        if index >= self.length:
            if index > self.length:
                print('Index of node is greater than length, inserting at end.')
            return self.append(value)
        # Insert at beginning
        if (index == 0):
            self.prepend(value)
            return self.print_list()
        # Insert in between nodes
        new_node = Node(value)
        leader = self.traverseToIndex(index-1)
        follower = leader.next
        leader.next = new_node
        new_node.prev = leader
        new_node.next = follower
        follower.prev = new_node
        self.length += 1
        return self.print_list()

    def traverseToIndex(self, index):
        counter = 0
        current_node = self.head
        while(counter != index):
            current_node = current_node.next
            counter += 1
        return current_node

    def remove(self, index):
        leader = self.traverseToIndex(index - 1)
        unwanted_node = leader.next
        follower = unwanted_node.next
        leader.next = follower
        follower.prev = leader
        self.length -= 1
        return self.print_list()

    # Print Linked List

    def print_list(self):
        array = []
        if self.head == None:
            print("Empty")
        else:
            current_node = self.head
            while current_node != None:
                array.append(current_node.value)
                current_node = current_node.next
            print(array)


myDoublyLinkedList = DoublyLinkedList()

myDoublyLinkedList.append(10)
myDoublyLinkedList.append(5)
myDoublyLinkedList.append(16)
myDoublyLinkedList.prepend(1)
myDoublyLinkedList.print_list()
myDoublyLinkedList.insert(2, 99)
myDoublyLinkedList.insert(20, 88)
myDoublyLinkedList.print_list()
myDoublyLinkedList.remove(1)
