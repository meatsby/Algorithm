# 모두의 마블

n = int(input())
cards = sorted(list(map(int, input().split())), reverse=True)
result = 0

for i in range(1, n):
    result += cards[0] + cards[i]

print(result)
