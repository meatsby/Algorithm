# 회문
import sys
input = sys.stdin.readline

def isFalse(s, l, r):
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            return False
    return True


def isPalin(s, l, r):
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            lFalse = isFalse(s, l+1, r)
            rFalse = isFalse(s, l, r-1)
            if lFalse or rFalse:
                return 1
            else:
                return 2
    return 0


t = int(input())

for _ in range(t):
    s = input().rstrip()
    l, r = 0, len(s)-1
    print(isPalin(s, l, r))
