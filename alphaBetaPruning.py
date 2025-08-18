import math

MAX, MIN = 1000, -1000

def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta, targetDepth):
    if depth == targetDepth:
        return values[nodeIndex], alpha, beta

    if maximizingPlayer:
        best = MIN
        for i in range(2):
            val, alpha, beta = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta, targetDepth)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best, alpha, beta
    else:
        best = MAX
        for i in range(2):
            val, alpha, beta = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta, targetDepth)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best, alpha, beta

if __name__ == "__main__":
    values = []

    num_values = int(input("Enter the number of terminal nodes (must be a power of 2): "))
    if (num_values & (num_values - 1)) != 0 or num_values == 0:
        print("Error: The number of terminal nodes must be a power of 2 and greater than 0.")
    else:
        print(f"Enter {num_values} terminal node values:")
        for i in range(num_values):
            value = int(input(f"Enter value of node {i+1}: "))
            values.append(value)

        tree_depth = int(math.log2(num_values))
        optimal_value, final_alpha, final_beta = minimax(0, 0, True, values, MIN, MAX, tree_depth)

        print(f"The Optimal value is : {optimal_value}")
        print(f"Final Alpha: {final_alpha}")
        print(f"Final Beta: {final_beta}")
