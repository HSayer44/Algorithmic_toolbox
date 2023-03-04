"""
distance: an integer representing the total distance to be covered
tank: an integer representing the maximum distance the car can travel on a full tank
stops: a list of integers representing the distances of gas stations along the route

The function returns the minimum number of refills needed to cover the entire distance, or -1
if it's not possible to reach the destination with the given tank capacity and gas stations.

In the main code block, the input values are read from stdin using the map and split functions. The function is called with these input values, and the result is printed to the console.
"""
def min_refills(distance, tank, stops):
    # initialize variables
    num_refills = 0
    current_refill = 0
    last_refill = 0
    
    # add the start and end points to the list of stops
    stops = [0] + stops + [distance]
    
    # iterate over the stops
    while current_refill < len(stops) - 1:
        last_refill = current_refill
        
        # move current_refill as far as possible
        while (current_refill < len(stops) - 1 and 
               stops[current_refill+1] - stops[last_refill] <= tank):
            current_refill += 1
        
        # if we haven't moved from the last_refill, it means the current tank
        # is not enough to reach the next stop
        if current_refill == last_refill:
            return -1
        
        # if we can move to the next stop, increment num_refills
        if current_refill < len(stops) - 1:
            num_refills += 1
    
    return num_refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
