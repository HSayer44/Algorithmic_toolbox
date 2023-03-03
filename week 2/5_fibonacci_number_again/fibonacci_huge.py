"""
It turns out that for any integer m ≥ 2, the sequence Fn mod m is periodic.
The period always starts with 01 and is known as Pisano period
(Pisano is another name of Fibonacci).
"""
def fibonacci_huge(n, m):
    if n <= 1:
        return n

    a, b = 0, 1
    pisano_period = None

    for i in range(m * m):
        a, b = b, (a + b) % m
        if a == 0 and b == 1:
            pisano_period = i + 1
            break

    if pisano_period is None:
        raise ValueError('Invalid value of m')

    n = n % pisano_period

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge(n, m))


