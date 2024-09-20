class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()  #To keep track of visited nodes

    def dfs(self, node):
        if node not in self.visited:
            print(node, end=" ")
            self.visited.add(node)
            for neighbor in self.graph[node]:
                self.dfs(neighbor)

#Example:
graph={
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['7'],
    '2': [],
    '4': ['8'],
    '8': []}

g1 = Graph(graph)
print('Depth First Search:')
g1.dfs('5')
