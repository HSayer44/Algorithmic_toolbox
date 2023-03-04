def change(money):
    num_coins = 0
    coins = [10, 5, 1]
    for coin in coins:
        num_coins += money // coin
        money = money % coin
    return num_coins
if __name__ == '__main__':
    m = int(input())
    print(change(m))

