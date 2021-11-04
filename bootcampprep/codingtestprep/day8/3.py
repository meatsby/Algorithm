# BABBA
import sys
input = sys.stdin.readline

a, b = 1, 0

for _ in range(int(input())):
    new_a = b
    new_b = a + b
    a, b = new_a, new_b

print(a, b)
