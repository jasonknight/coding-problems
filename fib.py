def fib(n,memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        f = 1
    else:
        f = fib(n - 1, memo) + fib(n - 2, memo)
        memo[n] = f
    return f
def fib2(n):
    memo = {}
    for k in range(1,n+1):
        if k <= 2:
            f = 1
        else:   
            f = memo[k-1] + memo[k-2]
        memo[k] = f
    return f
def fib3(n):
    k_1 = 0
    k_2 = 0
    for k in range(1,n+1):
        if k <= 2:
            f = 1
        else:
            f = k_1 + k_2
        k_1 = k_2
        k_2 = f
    return f
print(fib(21))
print(fib2(21))
print(fib3(21))