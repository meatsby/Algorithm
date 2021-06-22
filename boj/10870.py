n = int(input())
f = [0, 1]

for i in range(2, n+1):
    new = f[i-1] + f[i-2]
    f.append(new)

print(f[n])
