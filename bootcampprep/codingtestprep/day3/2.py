# 분수찾기
import sys
input = sys.stdin.readline

x = int(input())
lv = 0 # 지그재그층
lv_max = 0 # 해당층에서 제일 큰 수

while lv_max < x:
    lv += 1
    lv_max += lv

oe = lv%2 # 지그재그층 홀짝구분
a = 1 + (lv_max - x)
b = lv - (lv_max - x)

if oe == 0:
    print(f"{b}/{a}")
else:
    print(f"{a}/{b}")
