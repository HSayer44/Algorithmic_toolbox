from sys import stdin

def optimal_value(capacity, weights, values):
    value = 0.
    items = list(zip(values, weights))
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    for v, w in items:
        if capacity == 0:
            return value
        amount = min(w, capacity)
        value += amount * (v / w)
        capacity -= amount
    return value

if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
    
# to implement this code create a textfile with the input values and then use this command:
#python3 fractional_knapsack.py < inputs.txt

# for more explenation: https://youtu.be/lfQvPHGtu6Q
    
