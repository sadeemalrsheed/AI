class Graph:
    def __init__(self):
        #Initialize an empty dictionary to store the graph str
        self.graph = {}

    def add_edge(self, node, neighbors):
        #Add an edge to the graph: the node and its list of neighbors
        self.graph[node] = neighbors

    def bfs(self, start_node):
        #Initialize an empty list to keep track of visited nodes
        visited = []
        #Initialize an empty queue to store nodes to be explored
        queue = []

        #Start the BFS by visiting the start_node
        visited.append(start_node)
        queue.append(start_node)

        #Continue until there are no more nodes left to explore
        while queue:
            #Dequeue a node from the front of the queue
            node = queue.pop(0)
            print(node, end=" ")

            #For each neighbor of the current node
            for neighbor in self.graph[node]:

                if neighbor not in visited:
                    # Mark the neighbor as visited
                    visited.append(neighbor)
                    queue.append(neighbor)

#Create an instance of the Graph class
graph = Graph()

graph.add_edge('5', ['3', '7'])
graph.add_edge('3', ['2', '4'])
graph.add_edge('7', ['7'])
graph.add_edge('2', [])
graph.add_edge('4', ['8'])
graph.add_edge('8', [])

# Perform BFS starting from node 5
print('Breadth-First Search:')
graph.bfs('5')