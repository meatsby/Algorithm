a, b, c = map(int, input().split()) # a:고정비용, b:가변비용, c:판매비용
profit = c - b # profit:이익

if profit > 0:
    print(a//profit+1)
else:
    print(-1)
