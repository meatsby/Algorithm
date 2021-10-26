# 프린터 큐
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    imp = list(map(int, input().split()))
    temp = [i for i in range(n)]
    target = temp[m]
    cnt = 0
    while True:
        if imp[0] == max(imp):
            cnt += 1
            if temp[0] == target:
                print(cnt)
                break
            imp.pop(0)
            temp.pop(0)
        else:
            i = imp.pop(0)
            t = temp.pop(0)
            imp.append(i)
            temp.append(t)