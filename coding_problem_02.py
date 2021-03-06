# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# 
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# 
# Follow-up: what if you can't use division?
def prod(inp):
    # Because neither side can be included!
    if len(inp) < 3:
        return inp
    s = False
    res = []
    for i in inp:
        if not s:
            s = i
        else:
            s *= i
    for i in inp:
        res.append(s / i)
    return res
# Now let's do it without division. One way to look at
# at the problem is that we are tracking partial products
# for all elements of the array. The result array will
# always be as long as the input array

def prod_without_division(inp):
    res = {}
    for i in range(len(inp)):
        if not i in res:
            res[i] = 1
        for j in range(len(inp)):
            if not i == j:
                res[i] *= inp[j]
    return list(res.values())
# Hrrm, can we do it in near linear time, i mean N*N is not 
# really nice
def prod_fast(inp):
    res = []
    left = []
    right = []
    lt = 1
    rt = 1
    rindex = len(inp) - 1
    for i in range(len(inp)):
        lt *= inp[i]
        left.append(lt)
        rt *= inp[rindex]
        right.insert(0,rt)
        rindex -= 1
    res.append(right[1])
    i = 1
    while i < len(inp) - 1:
        # notice we skip 1 on the right side!
        res.append(left[i - 1] * right[i + 1])
        i += 1
    res.append(left[i - 1])
    return res

print(prod([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24])
print(prod([3, 2, 1]) == [2, 3, 6])
print(prod_without_division([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24])
print(prod_without_division([3, 2, 1]) == [2, 3, 6])
print(prod_fast([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24])
print(prod_fast([3, 2, 1]) == [2, 3, 6])
