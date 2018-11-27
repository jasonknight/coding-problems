import sys
def mprod(inp):
    one,two,three = sys.maxsize,sys.maxsize,sys.maxsize
    lone,ltwo = -sys.maxsize-1,-sys.maxsize-1
    for i in inp:
        if i < one:
            three = two
            two = one
            one = i
        elif i < two:
            three = two
            two = i
        elif i < three:
            three = i
        if i > ltwo:
            lone = ltwo
            ltwo = i
        elif i > lone:
            lone = i         
    return min(one * (two * three),one * (lone * ltwo))

print(mprod([4,-1,3,5,9]) == -45)
print(mprod([1,4,10,-2,4]) == -80)
print(mprod([3,4,1,2,5]) == 6)