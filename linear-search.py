# General Problems:  We have some cards with numbers written on which are arranged in decreasing order.
# We will try to pick the card containing the value you are thinking of in a fewest step.
        # if not increment the position by adding 1 and continue checking next value in the list
        i += 1
    # If the value was not found then return -1
    return -1


for i, v in enumerate(tests):
    print(linear_search(v["input"]["cards"], v["input"]["search_value"]) == v["output"])

# Complexity Analysis: in the worst case of scenario, the searching value will be at the final position in the cards list.
# With N array, we have to check n times to find out the position, which means our Big O is O(N)
