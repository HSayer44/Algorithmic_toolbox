def change(money):
    dp = [10**6] * (money+1)
    dp[0] = 0
    coins = [1, 3, 4]
    for j in range(1, money+1):
        for c in coins:
            if j >= c:
                dp[j] = min(dp[j], dp[j-c]+1)
    return dp[money]

if __name__ == '__main__':
    m = int(input())
    print(change(m))

