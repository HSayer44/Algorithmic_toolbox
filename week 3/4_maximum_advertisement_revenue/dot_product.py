"""
we can sort the sequences in decreasing order and calculate the dot product of the sorted sequences. Sorting the sequences in decreasing order will maximize the dot product because the largest elements will be multiplied with each other, leading to a higher product.
"""
def max_dot_product(first_sequence, second_sequence):
    first_sequence = sorted(first_sequence, reverse=True)
    second_sequence = sorted(second_sequence, reverse=True)
    max_product = 0
    for i in range(len(first_sequence)):
        max_product += first_sequence[i] * second_sequence[i]
    return max_product

if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
