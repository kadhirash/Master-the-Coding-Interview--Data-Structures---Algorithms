# # Edge List
# graph = [[0, 2], [2, 3], [2, 1], [1, 3]]

# # Adjacenct List
# # index = value of node, val = node's neighbors
# graph_one =  [[2],[2,3], [0,1,3], [1,2]]


# # Adjacent Matrix
# graph_two = [
#     0: [0,0,1,0],
#     1: [0,0,1,1],
#     2: [1,1,0,1],
#     3: [0,1,1,0]
# ]

#undirect, unweighted 
class Graph():
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_list = {}

    def __str__(self):
        return str(self.__dict__)

    def add_vertex(self,node):
        self.adjacent_list[node] = []
        self.number_of_nodes += 1

    def add_edge(self,node1,node2):
        self.adjacent_list[node1].append(node2)
        self.adjacent_list[node2].append(node2)

    def show_connections(self):
        for node in self.adjacent_list:
            print (node, end = '-->')
            for vertex in self.adjacent_list[node]:
                print(vertex, end = ' ')
            print()
    
myGraph = Graph()
myGraph.add_vertex('0')
myGraph.add_vertex('1')
myGraph.add_vertex('2')
myGraph.add_vertex('3')
myGraph.add_vertex('4')
myGraph.add_vertex('5')
myGraph.add_vertex('6')
print(myGraph)
myGraph.add_edge('3', '1') 
myGraph.add_edge('3', '4') 
myGraph.add_edge('4', '2') 
myGraph.add_edge('4', '5') 
myGraph.add_edge('1', '2') 
myGraph.add_edge('1', '0') 
myGraph.add_edge('0', '2') 
myGraph.add_edge('6', '5')
myGraph.show_connections()



