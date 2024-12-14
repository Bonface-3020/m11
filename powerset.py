def printPowerSet(input_set):
    set_size = len(input_set)
    power_set_size = 2 ** set_size  # Total number of subsets
    power_set = []

    # Generate each subset
    for outer in range(power_set_size):
        subset = []
        for inner in range(set_size):
            # Check if the j-th element of the set is included in the current subset
            if (outer & (1 << inner)) > 0:
                subset.append(input_set[inner])
        power_set.append(subset)

    # Print the power set
    for subset in power_set:
        print(subset)

# Example usage
input_set = [1, 2, 3]
printPowerSet(input_set)