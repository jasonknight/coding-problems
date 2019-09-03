def fib0(n):
    if n <= 1:
      return n
    return fib0(n - 1) + fib0(n - 2)

def fib(n,lookup=dict()):
    if n <= 1:
        return n
    if not n in lookup:
        lookup[n] = fib(n - 1, lookup) + fib(n - 2, lookup)
    return lookup[n]
def fib2(n):
    if n <= 1:
        return n
    p = 0
    c = 1
    for i in range(n-1):
        nf = p + c
        p = c
        c = nf
    return c
print(fib2(8))
