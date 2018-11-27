def sum_non_adj(inp):
    l = 0
    s1 = 0
    s2 = 0
    for i in range(len(inp)):
        if l == inp[i]:
            continue
        s1 += inp[i]
        tmp = s1
        s1 = s2
        s2 = tmp
        l = inp[i]
    return max(s1,s2)

print(sum_non_adj([2,4,6,2,5]) == 13)
print(sum_non_adj([5,1,1,5]) == 10)