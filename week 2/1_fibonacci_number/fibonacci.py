def fibonacci_number(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(n-1):
            c = a + b
            b, a = c, b
    return c

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))