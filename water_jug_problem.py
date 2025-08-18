from collections import deque

def fill_jugs_to_target(maxA, maxB, targetA, targetB):
    visited = set()
    queue = deque()
    queue.append((0, 0, []))
    
    while queue:
        a, b, steps = queue.popleft()
        
        if (a, b) in visited:
            continue
        visited.add((a, b))
        
        if a == targetA and b == targetB:
            return steps
        
        next_states = []
        
        if a < maxA:
            next_states.append((maxA, b, steps + [("Fill jug A", maxA, b)]))
        if b < maxB:
            next_states.append((a, maxB, steps + [("Fill jug B", a, maxB)]))
        if a > 0:
            next_states.append((0, b, steps + [("Empty jug A", 0, b)]))
        if b > 0:
            next_states.append((a, 0, steps + [("Empty jug B", a, 0)]))
        pour = min(a, maxB - b)
        if pour > 0:
            next_states.append((a - pour, b + pour, steps + [(f"Pour {pour} from A to B", a - pour, b + pour)]))
        pour = min(b, maxA - a)
        if pour > 0:
            next_states.append((a + pour, b - pour, steps + [(f"Pour {pour} from B to A", a + pour, b - pour)]))
        
        for state in next_states:
            queue.append(state)
    
    return None

if __name__ == "__main__":
    maxA = 4
    maxB = 3
    targetA = 2
    targetB = 0

    print("Water Jug Problem Solver")
    print("=" * 50)
    print(f"\nTrying to get {targetA} in jug A and {targetB} in jug B")
    print(f"Jug A capacity: {maxA}, Jug B capacity: {maxB}\n")

    result = fill_jugs_to_target(maxA, maxB, targetA, targetB)

    if result:
        print("\nSolution found!")
        print("=" * 50)
        for i, (action, jugA, jugB) in enumerate(result, 1):
            print(f"{i}. {action} -> Jug A: {jugA}, Jug B: {jugB}")
    else:
        print("No solution found!")



