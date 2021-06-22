n, k = map(int, input().split())
money = []
result = 0

for i in range(n):
    money.append(int(input()))
money = sorted(money, reverse=True)

for i in money:
    result += k//i
    k %= i

print(result)
