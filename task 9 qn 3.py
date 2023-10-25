def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibonacci = generate_fibonacci(n - 1)
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
        return fibonacci

n = 50
fibonacci_series = generate_fibonacci(n)
print(fibonacci_series)