# 백준 1316번: 그룹 단어 체커

import sys
input = sys.stdin.readline

ans = 0
for i in range(int(input().rstrip())):
    word = input().rstrip()
    if list(word) == sorted(word, key=word.find):
        ans += 1
print(ans)
