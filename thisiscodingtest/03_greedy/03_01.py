N = 1260
money = [500, 100, 50, 10]
count = 0

for m in money:
    count += N//m
    N %= m

print(count)
