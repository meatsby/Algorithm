# 시간 초과
# 정답 참고
# 왜 이게 더 적은 시간이 걸릴까?

n = int(input())
arr = [0 for _ in range(50000 + 1)]
for i in map(int, input().split()):
    arr[i] += 1
print(max(arr))
