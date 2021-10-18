# 내 학점을 구해줘
import sys
input = sys.stdin.readline

for t in range(int(input())):
    courses = 0
    gpa = 0
    for n in range(int(input())):
        c, g = map(float, input().split())
        courses += c
        gpa += c*g
    print(int(courses), round(gpa/courses, 1))
