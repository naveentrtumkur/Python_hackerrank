#!/bin/python3

import sys

def solve(n, s, d, m):
    # Complete this function
    count = 0
    if n==1 and d == s[0] and m == 1:
        return 1
    for (i) in range(0,n):
        if i == n-m:
            break
        for j in range(i+1,i+m):
            sum = s[i] + s[j]
            if sum == d:
                count = count + 1
    return count

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)


