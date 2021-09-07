# 에라토스테네스의 체

import sys

input = sys.stdin.readline

def isPrime(x):
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

n, k = map(int, input().split())
primes = []

for i in range(2, n+1):
    if isPrime(i):
        primes.append(i)
        for j in range(i+1, n+1):
            if j%i == 0 and (j not in primes):
                primes.append(j)

print(primes[k-1])
