# 카약과 강풍
# 정답 참고
# 없는팀, 있는팀, 남는팀 을 -1, 0, 1 로 구분 짓고 각 요소 양 옆을 비교

N, S, R = map(int, input().split())
damaged = sorted(list(map(int, input().split())))
onemore = sorted(list(map(int, input().split())))
team = [0 for i in range(N+2)]

for i in damaged:
    team[i] = -1

for i in onemore:
    if team[i] == -1:
        team[i] = 0
    else:
        team[i] = 1

for i in range(1, N+2):
    if team[i] == -1:
        if team[i-1] == 1:
            team[i] = 0
            team[i-1] = 0
        elif team[i+1] == 1:
            team[i+1] = 0
            team[i] = 0

print(team.count(-1))
