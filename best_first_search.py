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

def greedy_best_first_search(graph, start, goal, heuristics):
    pq = [(heuristics[start], start)]
    came_from = {start: None}
    visited = set()
    
    while pq:
        _, current = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            break

        for neighbor in graph.get(current, []):
            if neighbor not in visited and neighbor not in came_from:
                came_from[neighbor] = current
                heapq.heappush(pq, (heuristics[neighbor], neighbor))

    return came_from


start_node = 'S'
goal_node = 'H'


came_from = greedy_best_first_search(graph, start_node, goal_node, heuristics)


path = []
node = goal_node
if node in came_from:
    while node is not None:
        path.append(node)
        node = came_from[node]
    path.reverse()
    
print("Parent Map:", came_from)
print("Greedy Best-First Search path from", start_node, "to", goal_node, ":", path)
