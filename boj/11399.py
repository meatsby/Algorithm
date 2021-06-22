n = int(input())

atm = sorted(list(map(int, input().split())))
ttl = 0

for i in range(1, n+1):
    ttl += sum(atm[:i])

print(ttl)
