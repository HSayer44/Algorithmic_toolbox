def fibonacci_partial_sum(m, n):
    if n <= 1:
        return n

    # Calculate Pisano period for mod 10
    pisano_period = [0, 1]
    previous, current = 0, 1
    for i in range(2, 60):
        previous, current = current, (previous + current) % 10
        if (previous, current) == (0, 1):
            pisano_period.pop()
            break
        pisano_period.append(current)

    # Calculate the sum of the last digits of Fibonacci numbers
    # from F(m) to F(n) using the Pisano period
    pisano_period_length = len(pisano_period)
    sum_last_digits = 0
    current = 0
    next_fib = 1
    for i in range(n + 1):
        if i >= m:
            sum_last_digits += current
        current, next_fib = next_fib, (current + next_fib) % 10
        if i >= pisano_period_length:
            current = (current - pisano_period[i % pisano_period_length]) % 10
            next_fib = (next_fib - pisano_period[(i - 1) % pisano_period_length]) % 10

    return sum_last_digits % 10


if __name__ == '__main__':
    m, n = map(int, input().split())
    print(fibonacci_partial_sum(m, n))

