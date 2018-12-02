# This is one I really didn't like because it is partially a math
# problem masquerading as a programming problem. It's possible to 
# be completely unable to solve this problem if you do not have 
# certain mathematical facts.
# 
# You will need to know that a circle is PI * radius^2.
# 
# You will need to know that a cartesian plane has a center
# of 0, and that it has 4 quadrants, to the left is 0 to -1
# and to the right it is 0 to 1.
# 
# You will need to know that the monte carlo method, 
# is a pseudo random method for generating numbers,
# but really we should be calling it the dart board method.
# 
# We are going to take a cartesian plane, and we are going
# to "throw" darts at it, and if any of those "darts" could
# be within our circle (with a radius of 1 to make it easy),
# then we will "count" the hits, which with build our "random"
# number.

import random
def rand():
    return random.uniform(-1,1)
def throw_dart():
    return (rand(),rand())
def hit_board(point,r):
    # anoth math fact you need to know, we
    # can tell if a point is inside the circle
    # with x^2 + y^2 < r^2
    return point[0] * point[0] + point[1] * point[1] < r*r
def guess_pi():
    tries = 1000000
    hits = 0
    for _ in range(tries):
        if hit_board(throw_dart(),1):
            hits += 1
    pi_div_four = hits / tries
    return pi_div_four * 4
print(guess_pi())
# admittedly though, this is kinda fucking cool no? 
