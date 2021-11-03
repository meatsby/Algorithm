# 줄 세우기
import sys
input = sys.stdin.readline

num = input().rstrip()
ans = 0
isTrue = False

while True:
    temp = 0

    if len(num) > 1:
        for n in num:
            temp += int(n)
        ans += 1
        num = str(temp)
    else:
        if int(num)%3 == 0:
            isTrue = True
        break

print(ans)
print("YES" if isTrue else "NO")
