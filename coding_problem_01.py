# Givine a list of numbers and a number k, return
# whether or not ANY two numbers add up to 17
def find_sum(inp,k):
    for i in range(len(inp)):
        for j in range(len(inp)):
            if not j == k:
                if inp[i] + inp[j] == k:
                    return True
    return False
# But can we do it better? We can use a kind
# of memoization by seeing if the difference between
# k and i have been seen
# on the first pass, 17 - 10 = 7 doesn't return
# true, but with 17 - 7 = 10, we get true!
def find_sum2(inp,k):
    seen = {}
    for i in inp:
        if k-i in seen:
            return True
        seen[i] = True
    return False
print(find_sum([10,15,3,7],17) == True)
print(find_sum2([10,15,3,7],17) == True)

