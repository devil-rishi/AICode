graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

heuristic = {
    'A': 5,
    'B': 3,
    'C': 4,
    'D': 6,
    'E': 0,
    'F': 2
}

goal = 'E'


def hill_climbing(start):
    current = start
    path = [current]
    print(f"Start at node {current} (h={heuristic[current]})")

    while True:
        neighbors = graph[current]

        if not neighbors:
            print(f"No neighbors from {current}. Stuck")
            break

        best_neighbor = neighbors[0]
        for node in neighbors:
            if heuristic[node] < heuristic[best_neighbor]:
                best_neighbor = node

        print(f"Current: {current} (h={heuristic[current]}), "
              f"Best Neighbor: {best_neighbor} (h={heuristic[best_neighbor]})")

        if heuristic[best_neighbor] >= heuristic[current]:
            print(f"No better neighbor found. Stopping at {current}")
            break

        current = best_neighbor
        path.append(current)

        if current == goal:
            print(f"Goal {goal} reached!")
            break

    return path


final_path = hill_climbing('A')
print("\nFinal Path:", final_path)
