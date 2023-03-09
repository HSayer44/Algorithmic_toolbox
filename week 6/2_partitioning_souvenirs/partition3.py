from sys import stdin


def partition3(values):
    # Check if there are at least 3 integers in the input
    if len(values) < 3:
        return 0
    
    # Calculate the target sum
    target_sum = sum(values) // 3
    
    # If the sum is not evenly divisible by 3, we cannot partition
    if sum(values) % 3 != 0:
        return 0
    
    # Sort the values in decreasing order to speed up the search
    values.sort(reverse=True)
    
    # Define a recursive function to search for the solution
    def search(groups):
        # If we have assigned all values to groups, check if they all have the same sum
        if not values:
            return len(set(groups)) == 1
        
        # Try to assign the next value to each group and recursively search
        v = values.pop()
        for i in range(3):
            if groups[i] + v <= target_sum:
                groups[i] += v
                if search(groups):
                    return True
                groups[i] -= v
        
        # If no solution is found, put the value back and backtrack
        values.append(v)
        return False
    
    # Start the search with empty groups
    return int(search([0, 0, 0]))

if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
