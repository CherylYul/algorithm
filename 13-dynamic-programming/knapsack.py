def knapsack_prob(profit, weight, capacity):
    table = [[0 for x in range(len(weight) + 1)] for x in range(capacity + 1)]
    for c in range(1, capacity + 1):
        for i in range(1, len(weight) + 1):
            current_player_w = weight[i - 1]
            current_player_p = profit[i - 1]
            if c < current_player_w:
                table[c][i] = table[c][i - 1]
            else:
                table[c][i] = max(
                    table[c][i - 1],
                    table[c - current_player_w][i - 1] + current_player_p,
                )
    print(table)
    return table[-1][-1]


profit = [2, 3, 1, 5, 4, 7]
weight = [4, 5, 1, 3, 2, 5]
capacity = 15

print(knapsack_prob(profit, weight, capacity))
