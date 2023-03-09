def edit_distance(first_string, second_string):
    m, n = len(first_string), len(second_string)
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = max(i, j)
            elif first_string[i-1] == second_string[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]


if __name__ == "__main__":
    print(edit_distance(input(), input()))

