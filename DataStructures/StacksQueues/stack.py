### ------ INTRODUCTION ------ ###

# LinkedList implementation
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def print_stack(self):
        if self.top == None:
            print("Empty Stack")
        else:
            current_pointer = self.top
            while(current_pointer != None):
                print(current_pointer.value)
                current_pointer = current_pointer.next
        return

    def peek(self):
        return self.top

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            holding_pointer = self.top
            self.top = new_node
            self.top.next = holding_pointer
        self.length += 1
        return self

    def pop(self):
        if not(self.top):
            return None
        if (self.top == self.bottom):
            self.bottom = None
        #holding_pointer = self.top
        self.top = self.top.next
        self.length -= 1
        # return holding_pointer
        return self


myStack = Stack()
myStack.peek()

myStack.push('google')
myStack.push('udemy')
myStack.push('discord')

myStack.pop()
myStack.pop()
myStack.pop()

# myStack.print_stack()


# Array implementation

class Stack2():
    def __init__(self):
        self.array = []

    def __str__(self):
        return str(self.__dict__)

    def peek(self):
        return self.array[len(self.array)-1]

    def push(self, value):
        self.array.append(value)
        return self

    def pop(self):
        self.array.pop()
        return self


myStack2 = Stack2()

myStack2.push('google')
myStack2.push('udemy')
myStack2.push('discord')

print(myStack2)

print(myStack2.peek())

print(myStack2.pop())
