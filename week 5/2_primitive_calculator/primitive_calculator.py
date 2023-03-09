def compute_operations(n):
    dp = [0] * (n+1)
    for i in range(2, n+1):
        dp[i] = dp[i-1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)

    result = []
    while n > 0:
        result.append(n)
        if dp[n] == dp[n-1] + 1:
            n = n-1
        elif n % 2 == 0 and dp[n] == dp[n//2] + 1:
            n = n // 2
        else:
            n = n // 3
    result.reverse()
    return result

if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(list(output_sequence)) - 1)
    print(*output_sequence)

