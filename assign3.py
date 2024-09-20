import heapq  #Priority queue library
class Graph:
    def __init__(self, graph):
        self.graph = graph

    def ucs(self, start, goal):
        queue = [(0, start)]
        visited = set()
        costs = {start: 0}

        while queue:
            current_cost, current_node = heapq.heappop(queue)
            if current_node in visited:
                continue
            visited.add(current_node)
            print(f"Visited {current_node}, Cost: {current_cost}")

            if current_node == goal:
                print(f"Goal {goal} reached with cost {current_cost}")
                return current_cost
            for neighbor, cost in self.graph[current_node]:
                if neighbor not in visited:
                    new_cost = current_cost + cost

                    if neighbor not in costs or new_cost < costs[neighbor]:
                        costs[neighbor] = new_cost
                        heapq.heappush(queue, (new_cost, neighbor))
        return float('inf')  #If goal is not reachable

graph = {
    '5': [('3', 6), ('7', 3)],
    '3': [('2', 4), ('4', 12)],
    '7': [('7', 11)],
    '2': [],
    '4': [('8', 5)],
    '8': []}

g = Graph(graph)
print('Uniform Cost Search:')
g.ucs('5', '8')
