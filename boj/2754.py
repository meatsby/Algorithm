# 학점계산
import sys
input = sys.stdin.readline

alp = ["A", "B", "C", "D", "F"]
num = [4.0, 3.0, 2.0, 1.0, 0.0]

gpa = input().rstrip()
cal = num[alp.index(gpa[0])]
if cal == 0.0:
    print(cal)
else:
    if gpa[1] == "+":
        cal += 0.3
    elif gpa[1] == "-":
        cal -= 0.3
    print(cal)
