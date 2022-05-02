def binary_search(array, search_value):
    # Create variable position of lowest and highest position
    lo, hi = 0, len(array) - 1
    while lo <= hi:
        # Chose the midle position
        mid = (lo + hi) // 2
        # if matches with the search value then checking if the position is the smallest, if yes return position
        # if not, search first half of the list
        if array[mid] == search_value:
            if mid > 0 and array[mid - 1] == search_value:
                hi = mid - 1
            else:
                return mid
        # if the guessing number is smaller than the search value then search second half of the list
        elif array[mid] < search_value:
            lo = mid + 1
        # if the gussing number is larger than the search value then search first half of the list
        else:
            hi = mid - 1
    # if the value was not found then return -1
    return -1


for i, v in enumerate(tests):
    print(binary_search(v["input"]["cards"], v["input"]["search_value"]) == v["output"])

# Complexity Analysis: in the worst case of scenario, the output we finding are the the first or last position of the list
# then with N numbers, we need log(N) step to pick the right cards, O(N) = log(N)

