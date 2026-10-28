import math

def minmax(depth, node_index, maximizing_player, values, height):
    if depth == height:
        return values[node_index]

    if maximizing_player:
        return max(
            minmax(depth + 1, node_index * 2, False, values, height),
            minmax(depth + 1, node_index * 2 + 1, False, values, height)
        )
    else:
        return min(
            minmax(depth + 1, node_index * 2, True, values, height),
            minmax(depth + 1, node_index * 2 + 1, True, values, height)
        )


if __name__ == "__main__":
    # Terminal leaf values of the game tree
    values = [3, 5, 2, 9, 12, 5, 23, 23]
    height = int(math.log2(len(values)))

    print("Game Tree Terminal Leaf Values:")
    print(" ", values)
    print("Height of Game Tree:", height)
    print()

    optimal_value = minmax(0, 0, True, values, height)
    print("Computed Optimal Value (Root - Maximizer):", optimal_value)
