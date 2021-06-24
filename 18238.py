import sys

word = sys.stdin.readline().rstrip()
start = 'A'
result = 0

for w in word:
    if ord(start) - ord(w) < -13:
        result += abs(ord(start)-ord(w)+ 26)
    elif ord(start) - ord(w) > 13:
        result += abs(ord(start)-ord(w)-26)
    else:
        result += abs(ord(start)-ord(w))
    start = w

print(result)
