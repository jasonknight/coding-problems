# We need to find the substring with at most k distinct, or unique, characters.
# 
# For me, this was a little confusing at first, but if we restate it a little
# different it becomes clear.
# 
# If k = 2, then what we are looking for is the longest possible substring
# that only has 2 characters. So if you have s = "abcba", then "bcb" is the
# longest substring, because it only contains b and c (k=2). If s had
# equaled "abcbcbbcca", then the longest would have been: "bcbcbbcc".

# Let's try first with a brute force solution, this one is
# not too bad, O(n^2*k)

def longest_distinct_substring(s,k):
    longest = ''
    for i,c in enumerate(s):
        # making j bigger than s, ensures we'll get to the end of
        # of the string. Going over is okay.
        for j in range(i + 1, len(s) + 1):
            sub = s[i:j]
            # converting it to a set gives
            # gives us unique elements
            sub_set = set(sub)
            if len(sub_set) <= k and len(sub) > len(longest):
                longest = sub
    return len(longest)

# Another way to look at this problem is tracking a "window", that
# is, just keeping track of the start position and end position
#  (0,0) (0,1) (0,2)
#    0     1     2     3     4
#    a     b     c     b     a
#                OOPs, more than k unique!
#        (1,1) (1,2) (1,3) (1,4)
#    0     1     2     3     4
#    a     b     c     b     a
#                            OOPs, more than k unique!
#   final_window is (1,3) = 3 for "bcb"
# 
def longest_distinct_substring_fast(s,k):
    window = (0,0)
    memo = {}
    length = 0
    for i,c in enumerate(s):
        memo[c] = i # need to track the "start" offset
        new_start_position = window[0]
        if len(memo) > k:
            # the important moment, the dict will look like this
            # {'a': 4, 'c': 2, 'b': 3}
            # so the key we're looking for, to make a new start
            # is c, of course, this new substring will not be
            # longer than the bcb one...
            # the order in the hash table doesn't matter,
            # we are just tracking offsets
            ky = min(memo,key=memo.get)
            new_start_position = memo.pop(ky) + 1 # i.e. advance one position past.
            # remember, we store i at the key, 
        # we advance the window on each iteration
        window = (new_start_position, window[1] + 1) 
        length = max(length, window[1] - window[0])
    return length
print(longest_distinct_substring("abcba",2))
print(longest_distinct_substring_fast("abcba",2))
