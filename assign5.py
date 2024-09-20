import heapq  # Priority queue library
class Graph:
    def __init__(self, graph, heuristic):
        self.graph = graph
        self.heuristic = heuristic  # Heuristic dictionary

    def a_star(self, start, goal):
        queue = [(self.heuristic[start], 0, start)]
        visited = set()
        costs = {start: 0}

        while queue:
            f_value, g_value, current_node = heapq.heappop(queue)
            if current_node in visited:
                continue
            visited.add(current_node)
            print(f"Visited {current_node}, g:{g_value}, h:{self.heuristic[current_node]}, f:{f_value}")
            if current_node == goal:
                print(f"Goal {goal} reached with cost {g_value}")
                return
            for neighbor, cost in self.graph[current_node]:
                updated_g_value = g_value + cost
                h_value = self.heuristic[neighbor]
                f_value = updated_g_value + h_value  #f=g+h

                if neighbor not in visited:
                    if neighbor not in costs or updated_g_value < costs[neighbor]:
                        costs[neighbor] = updated_g_value
                        heapq.heappush(queue, (f_value, updated_g_value, neighbor))
        print(f"Error: Goal {goal} is not reachable from {start}")

graph = {
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
print('A* Search:')
g.a_star('5', '8')
