# 덩치
# 브루트포스
# 정답 참고
# for문 두 번

N = int(input())
people = [tuple(map(int, input().split())) for i in range(N)]
l = []

for x, y in people:
    size = 1
    for a, b in people:
        if x < a and y < b:
            size += 1
    l.append(size)

print(*l)
