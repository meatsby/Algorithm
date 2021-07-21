# 에너지 드링크

N = int(input())
l = sorted(list(map(int, input().split())), reverse=True)
a = l[0]

for i in range(1, N):
    a += l[i]/2

if a == int(a):
    print(int(a))
else:
    print(a)
