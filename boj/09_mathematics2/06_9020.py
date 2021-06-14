import sys
import math

def prime(x):
    if x == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    s = n//2
    while True:
        if prime(s) and prime(n-s):
            print(s, n-s)
            break
        else:
            s -= 1
