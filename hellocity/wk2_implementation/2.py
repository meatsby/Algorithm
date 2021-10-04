# 백준 2941번: 크로아티아 알파벳

import sys
input = sys.stdin.readline

word = input().rstrip()
print(len(word) - sum(map(word.count, ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="])))
