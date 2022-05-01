# General Problems:  We have some cards with numbers written on which are arranged in decreasing order.
# We will try to pick the card containing the value you are thinking of in a fewest step.
tests = []
# Case 1: search value occurs in the cards, first position, middle position and last position
tests.append(
    {
        "input": {
            "cards": [37, 28, 25, 15, 14, 8, 4, 3, 0, -4, -9, -78],
            "search_value": -4,
        },
        "output": 9,
    }
)
# Case 2: search value does not occur in the cards because the cards do not have the seeking value or do not contain any numbers
# We return -1 position when cannot find it
tests.append(
    {
        "input": {"cards": [10, 9, 7, 4, 2, 1, -4, -9, -12], "search_value": 28},
        "output": -1,
    }
)
# Case 3: search value occurs in the cards multiple times
# We return the first position of it
tests.append(
    {
        "input": {
            "cards": [29, 16, 5, 5, 5, 5, -2, -2, -2, -6, -20, -29, -33, -33],
            "search_value": -2,
        },
        "output": 6,
    }
)
print(tests)
        # if not increment the position by adding 1 and continue checking next value in the list
        i += 1
    # If the value was not found then return -1
    return -1


for i, v in enumerate(tests):
    print(linear_search(v["input"]["cards"], v["input"]["search_value"]) == v["output"])

# Complexity Analysis: in the worst case of scenario, the searching value will be at the final position in the cards list.
# With N array, we have to check n times to find out the position, which means our Big O is O(N)
