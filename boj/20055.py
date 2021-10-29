# 컨베이어 벨트 위의 로봇
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
robot = [0] * n
belt = list(map(int, input().split()))
cnt = 1

while True:
    # 1
    b = belt.pop()
    r = robot.pop()
    belt.insert(0, b)
    robot.insert(0, r)
    robot[n-1] = 0

    # 2
    for i in range(n-1, 0, -1):
        if robot[i] == 0 and belt[i] > 0 and robot[i-1] == 1:
            robot[i] = 1
            belt[i] -= 1
            robot[i-1] = 0
    robot[n-1] = 0

    # 3
    if belt[0] != 0:
        robot[0] = 1
        belt[0] -= 1

    # 4
    if belt.count(0) >= k:
        print(cnt)
        break
    cnt += 1
