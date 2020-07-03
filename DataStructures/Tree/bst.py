class Node():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BST():
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    # Left
                    if current_node.left == None:
                        current_node.left = new_node
                        return
                    else:
                        current_node = current_node.left
                else:
                    # Right
                    if current_node.right == None:
                        current_node.right = new_node
                        return
                    else:
                        current_node = current_node.right

    def lookup(self, value):
        if self.root == None:
            return False
        current_node = self.root
        while current_node:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            elif current_node.value == value:
                return current_node
        return False

    # Broken, fix later
    def remove(self, value):
        if self.root == None:
            return False
        current_node = self.root
        parent_node = None
        while current_node:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            elif current_node == value:
                # Option 1: No right child
                if current_node.right == None:
                    if parent_node == None:
                        self.root = current_node.left
                    else:
                        # if parent > curr value, make curr left child a child of parent
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.left
                        # if parent < curr value, make left child a right child of parent
                        elif current_node.value > parent_node.value:
                            parent_node.right = current_node.left

                # Option 2: Right child with no left child
                elif current_node.right.left == None:
                    if parent_node == None:
                        self.root == current_node.left
                    else:
                        current_node.right.left = current_node.left
                        # if parent > curr, make right child of parent's left
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.right
                        # if parents < curr, make right child of parent's right
                        elif current_node.value > parent_node.value:
                            parent_node.right = current_node.right

                # Option 3: Right child with left child
                else:
                    # find right child's left most child
                    left_most = current_node.right.left
                    left_most_parent = current_node.right
                    while left_most.left != None:
                        left_most_parent = left_most
                        left_most = left_most.left

                    # parent's left subtree is not leftmost's right subtree
                    left_most_parent.left = left_most.right
                    left_most.left = current_node.left
                    left_most.right = current_node.right

                    if parent_node == None:
                        self.root = left_most
                    else:
                        if current_node.value < parent_node.value:
                            parent_node.left = left_most
                        elif current_node.value > parent_node.value:
                            parent_node.right = left_most
        return "Not Found"

    def print_tree(self):
        if self.root != None:
            self.print_nodes(self.root)

    def print_nodes(self, curr_node):
        if curr_node != None:
            self.print_nodes(curr_node.left)
            print(str(curr_node.value))
            self.print_nodes(curr_node.right)


myBST = BST()
myBST.insert(9)
myBST.insert(4)
myBST.insert(6)
myBST.insert(170)
myBST.insert(15)
myBST.insert(1)
#myBST.print_tree()

# print(myBST.lookup(171))
myBST.print_tree()