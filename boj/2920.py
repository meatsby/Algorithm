# 음계

import sys
input = sys.stdin.readline

note = list(map(int, input().split()))
asc = sorted(note)
dsc = sorted(note, reverse=True)

if note == asc:
    print("ascending")
elif note == dsc:
    print("descending")
else:
    print("mixed")
