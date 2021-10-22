# 백설 공주와 일곱 난쟁이
import sys
input = sys.stdin.readline

h = [int(input()) for _ in range(9)]
end = False

for i in range(9):
    for j in range(i+1, 9):
        if sum(h) - h[i] - h[j] == 100:
            del h[j]
            del h[i]
            for n in h:
                print(n)
            end = True
            break
    if end:
        break
