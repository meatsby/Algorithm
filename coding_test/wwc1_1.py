import sys

money = int(sys.stdin.readline())

def Solution(money):
    money_type = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 1]
    answer = []
    for m in money_type:
        if money%m != money:
            answer.append(money//m)
            money %= m
        else:
            answer.append(0)
    return answer

print(Solution(money))
