### ------ INTRODUCTION ------ ###
# linked list: apples -> grapes -> pears

# 10 --> 15 --> 16


### ------ IMPLEMENTATION ------ ###

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():
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
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            return self

    # Prepend to beginning of linkedList
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
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
        holding_pointer = leader.next
        leader.next = new_node
        new_node.next = holding_pointer
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
        leader.next = unwanted_node.next
        self.length -= 1
        return self.print_list()

    def reverse(self):
        if not(self.head.next):
            return self.head
        first = self.head
        print(first)
        self.tail = self.head
        second = first.next
        print(second)
        while second:
            temp = second.next  # set temp to hold second node's next pointer val
            second.next = first  # set second pointer next back to first
            first = second  # set first to second
            second = temp  # set second to temp
        self.head.next = None
        self.head = first
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


myLinkedList = LinkedList()

myLinkedList.append(10)
myLinkedList.append(5)
myLinkedList.append(16)
myLinkedList.prepend(1)
myLinkedList.print_list()
myLinkedList.insert(2, 99)
myLinkedList.insert(20, 88)
myLinkedList.print_list()
myLinkedList.remove(2)
myLinkedList.reverse()
