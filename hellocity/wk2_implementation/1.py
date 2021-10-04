# 백준 1316번: 그룹 단어 체커

import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    word = input().rstrip()
    for w in range(len(word)-1):
        if word[w] != word[w+1] and word[w] in word[w+1:]:
            n -= 1
            break

print(n)
