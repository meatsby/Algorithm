# 카드게임
import sys
input = sys.stdin.readline

def sameColor(cards):
    temp = cards[0][0]
    for c, n in cards[1:]:
        if c != temp:
            return False
    return True

def isContinuous(cards):
    temp = int(cards[0][1])
    for c, n in cards[1:]:
        if int(n) != temp + 1:
            return False
        else:
            temp = int(n)
    return True

def countNumber(cards):
    if 4 in numbers:
        return 800 + numbers.index(4)
    elif 3 in numbers and 2 in numbers:
        return 700 + numbers.index(3)*10 + numbers.index(2)
    elif 3 in numbers:
        return 400 + numbers.index(3)
    elif numbers.count(2) == 2:
        for i in range(10):
            if numbers[i] == 2:
                lower = i
                break
        for i in range(9, -1, -1):
            if numbers[i] == 2:
                upper = i
                break
        return 300 + upper*10 + lower
    elif 2 in numbers:
        return 200 + numbers.index(2)
    else:
        return 100 + int(cards[4][1])

cards = sorted([list(input().rstrip().split()) for _ in range(5)], key=lambda x : x[1])
numbers = [0]*10

for c, n in cards:
    numbers[int(n)] += 1

if sameColor(cards) and isContinuous(cards):
    ans = 900 + int(cards[4][1])
elif sameColor(cards):
    ans = 600 + int(cards[4][1])
elif isContinuous(cards):
    ans = 500 + int(cards[4][1])
else:
    ans = countNumber(cards)

print(ans)
