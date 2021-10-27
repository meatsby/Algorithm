# 저항
import sys
input = sys.stdin.readline

color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
product = [10**i for i in range(10)]

v1 = str(color.index(input().rstrip()))
v2 = str(color.index(input().rstrip()))
p = product[color.index(input().rstrip())]

print(int(v1+v2) * p)
