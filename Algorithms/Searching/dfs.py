class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class DFS():
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

    def remove(self, value):
        pass

    def inorder(self):
        return traverse_inorder(self.root, [])

    def preorder(self):
        return traverse_preorder(self.root, [])

    def postorder(self):
        return traverse_postorder(self.root, [])


def traverse_inorder(node, dfs_list):
    if node.left:
        traverse_inorder(node.left, dfs_list)
    dfs_list.append(node.value)
    if node.right:
        traverse_inorder(node.right, dfs_list)
    return dfs_list


def traverse_preorder(node, dfs_list):
    dfs_list.append(node.value)
    if node.left:
        traverse_preorder(node.left, dfs_list)
    if node.right:
        traverse_preorder(node.right, dfs_list)
    return dfs_list


def traverse_postorder(node, dfs_list):
    if node.left:
        traverse_postorder(node.left, dfs_list)
    if node.right:
        traverse_postorder(node.right, dfs_list)
    dfs_list.append(node.value)
    return dfs_list


dfs = DFS()
dfs.insert(9)
dfs.insert(4)
dfs.insert(6)
dfs.insert(20)
dfs.insert(170)
dfs.insert(15)
dfs.insert(1)
print(dfs.inorder()) #inorder
print(dfs.preorder()) #preorder
print(dfs.postorder()) #postorder