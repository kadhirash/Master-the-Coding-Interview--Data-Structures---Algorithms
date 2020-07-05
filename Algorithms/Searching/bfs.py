class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BFS():
    def __init__(self):
        self.root = None
        self.num_nodes = 0

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

    def breadth_first_search(self):
        curr_node = self.root
        bfs_list = []
        queue = []
        queue.append(curr_node)

        while len(queue) > 0:
            curr_node = queue.pop(0)
            bfs_list.append(curr_node.value)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        return bfs_list
    def recursive_bfs(self,queue,bfs_list):
        if len(queue) == 0:
            return bfs_list
        curr_node = queue.pop(0)
        bfs_list.append(curr_node.value)
        if curr_node.left:
            queue.append(curr_node.left)
        if curr_node.right:
            queue.append(curr_node.right)
        return self.recursive_bfs(queue, bfs_list)

bfs = BFS()
bfs.insert(9)
bfs.insert(4)
bfs.insert(6)
bfs.insert(20)
bfs.insert(170)
bfs.insert(15)
bfs.insert(1)
print(bfs.breadth_first_search())
print(bfs.recursive_bfs([bfs.root],[]))