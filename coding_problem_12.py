def fib(n):
    a,b = 1,2
    for _ in range(n-1):
        a,b = b, a + b
    return a
def count_basic(n):
    return fib(n)
def count_multi(n,ways):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n in ways:
        return 1 + sum([count_multi(n - x, ways) for x in ways if x < n])
    else:
        return sum([count_multi(n - x, ways) for x in ways if x < n])

def count_dynamic(n,ways):
    memo = [0 for _ in range(n+1)]
    memo[0] = 1 # i.e. n+1
    for i in range(n+1):
        memo[i] += sum([ memo[i-x] for x in ways if i-x > 0])
        memo[i] += 1 if i in ways else 0
    return memo[-1]
print(count_basic(4))
print(count_multi(4,[1,2]))
print(count_multi(4,[1,3,5]))
print(count_dynamic(4,[1,2]))
print(count_dynamic(4,[1,3,5]))
