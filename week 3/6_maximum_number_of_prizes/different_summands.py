
def optimal_summands(n):
    summands = []
    i = 1
    while n > 2 * i:
    	summands.append(i)
    	n -= i
    	i += 1
    summands.append(n)
    return summands
    
if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)

