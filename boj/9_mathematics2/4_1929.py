import math
import sys
m, n = map(int, sys.stdin.readline().split())

def prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

for num in range(m, n+1):
    if prime(num):
        print(num)
