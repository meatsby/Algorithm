# 과제 안 내신 분..?
import sys
input = sys.stdin.readline

students = set(i for i in range(1, 31))
report = set(int(input()) for _ in range(28))

for i in sorted(students - report):
    print(i)
