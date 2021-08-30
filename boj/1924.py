# 2007년

import sys
input = sys.stdin.readline

x, y = map(int, input().split())
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
d = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
total = sum(days[:x]) + y

print(d[total%7])
