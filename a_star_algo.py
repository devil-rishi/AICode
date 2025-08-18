import heapq

graph = {
    'S': ['A', 'B', 'C'],
    'A': ['D', 'E'],
    'B': ['F'],
    'C': ['G'],
    'D': ['H'],
    'E': ['H'],
    'F': ['H'],
    'G': ['H'],
    'H': []
}

heuristics = {
    'S': 10,
    'A': 8,
    'B': 5,
    'C': 7,
    'D': 4,
    'E': 3,
    'F': 2,
    'G': 1,
    'H': 0
}

costs = {
    ('S', 'A'): 1,
    ('S', 'B'): 1,
    ('S', 'C'): 1,
    ('A', 'D'): 1,
    ('A', 'E'): 1,
    ('B', 'F'): 1,
    ('C', 'G'): 1,
    ('D', 'H'): 1,
    ('E', 'H'): 1,
    ('F', 'H'): 1,
    ('G', 'H'): 1,
}

def a_star(graph, start, goal, heuristics, costs):
    pq = [(heuristics[start], 0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}

    while pq:
        f, g, current = heapq.heappop(pq)

        if current == goal:
            break

        for neighbor in graph.get(current, []):
            new_cost = g + costs.get((current, neighbor), float('inf'))
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristics[neighbor]
                heapq.heappush(pq, (priority, new_cost, neighbor))
                came_from[neighbor] = current

    return came_from

start_node = 'S'
goal_node = 'H'

came_from = a_star(graph, start_node, goal_node, heuristics, costs)

path = []
node = goal_node
if node in came_from:
    while node is not None:
        path.append(node)
        node = came_from[node]
    path.reverse()

print("Parent Map:", came_from)
print("A* Search path from", start_node, "to", goal_node, ":", path)
