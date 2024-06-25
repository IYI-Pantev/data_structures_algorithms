
memo = [None] * 100
counter = 0

def fib(n):
    global counter
    counter += 1

    if memo[n] is not None:
        return memo[n]

    if n == 1 or n == 0:
        return n
    
    memo[n] = fib(n - 1) + fib(n - 2)

    return memo[n]

# print(fib(7))
# print(*memo)

n = 35

print('Fib of', n, '=', fib(n))
print('Counter', counter)