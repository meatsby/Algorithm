# 방 번호

import math

N = list(map(int, input()))
num_set = [0 for i in range(10)]

for i in N:
    num_set[i] += 1

num_set[6] = math.ceil((num_set[6] + num_set[9])/2)
num_set.pop()

print(max(num_set))
