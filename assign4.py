import heapq  #Priority queue library
class Graph:
    def __init__(self, graph, heuristic):
        self.graph = graph
        self.heuristic = heuristic  # Heuristic dictionary

    def greedy_bfs(self, start, goal):
        queue = [(self.heuristic[start], start)]
        visited = set()

        while queue:
            heuristic_value, current_node = heapq.heappop(queue)
            if current_node in visited:
                continue
            visited.add(current_node)
            print(f"Visited {current_node}")
            if current_node == goal:
                print(f"Goal {goal} reached")
                return

            for neighbor, cost in self.graph[current_node]:
                if neighbor not in visited:
                    heapq.heappush(queue, (self.heuristic[neighbor], neighbor))

        # If the goal is not reached after all nodes are processed
        print(f"Error: Goal {goal} is not reachable from {start}")

graph ={
    '5': [('3', 2), ('7', 3)],
    '3': [('2', 4), ('4', 1)],
    '7': [('7', 11)],
    '2': [],
    '4': [('8', 5)],
    '8': []}

heuristic = {
    '5': 7,
    '3': 6,
    '7': 10,
    '2': 9,
    '4': 1,
    '8': 0}
g = Graph(graph, heuristic)
print('Greedy Search:')
g.greedy_bfs('5', '8')



