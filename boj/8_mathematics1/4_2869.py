import math

a, b, v = map(int, input().split())  # a:상승, b:하강, v:높이
hf = v - a
di = a - b

print(math.ceil(hf/di)+1)
