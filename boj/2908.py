a = list(map(int, input().split()))
l = []

for i in a:
    l.append(i%10*100 + i//10%10*10 + i//10//10)

print(max(l))
