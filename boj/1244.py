# 스위치 켜고 끄기

import sys
input = sys.stdin.readline

def change(sex, idx):
    global s
    if sex == 1:
        for i in range(1, n+1):
            if i%idx == 0:
                s[i] = abs(s[i] - 1)
    elif sex == 2:
        s[idx] = abs(s[idx] - 1)
        for i in range(1, min(n+1-idx, idx)):
            if s[idx-i] == s[idx+i]:
                s[idx-i], s[idx+i] = abs(s[idx-i] - 1), abs(s[idx+i] - 1)
            else:
                break

n = int(input())
s = ["X"] + list(map(int, input().split()))
students = int(input())
operations = []
for _ in range(students):
    sex, idx = map(int, input().split())
    change(sex, idx)

for i in range(0, n, 20):
    print(*s[i+1:i+21])
