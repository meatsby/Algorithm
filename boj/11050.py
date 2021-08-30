# 이항 계수 1

import sys, math
input = sys.stdin.readline

N, K = map(int, input().split())

print(int(math.factorial(N)/(math.factorial(K) * math.factorial(N-K))))
