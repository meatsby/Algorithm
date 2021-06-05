import sys
import math
l = []

def prime(x):
    if x == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    for i in range(n+1, n*2+1):
        if prime(i):
            l.append(i)
    print(len(l))
    l = []
