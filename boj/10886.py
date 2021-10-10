# 0 = not cute / 1 = cute
import sys
input = sys.stdin.readline

cute, ncute = 0, 0
for _ in range(int(input())):
    vote = int(input())
    if vote == 1:
        cute += 1
    else:
        ncute += 1
if cute > ncute:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
