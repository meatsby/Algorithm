# 정보 선생님은 수업을 시작하기 전에 이상한 출석을 부른다.

# 선생님은 출석부를 보고 번호를 부르는데,
# 학생들의 얼굴과 이름을 빨리 익히기 위해 번호를 무작위(랜덤)으로 부른다.

# 그리고 얼굴과 이름이 잘 기억되지 않는 학생들은 번호를 여러 번 불러
# 이름과 얼굴을 빨리 익히려고 하는 것이다.

# 출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자.

n = int(input())
a = list(map(int, input().split()))
d = [0] * 23

for i in a:
    d[i-1] += 1
print(*d)
