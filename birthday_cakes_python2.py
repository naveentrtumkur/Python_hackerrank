#!/bin/python

import sys

def solve(n, s, d, m):
    # Complete this function
    w = 0
    for i in range(n-m+1):
        l = s[i:i+m]
        if sum(l) == d:
            w += 1
    return w

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d, m = raw_input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)


