# 전구와 스위치
# 정답 참고

N = int(input())
srt = list(map(int, list(input())))
end = list(map(int, list(input())))

# 0번째부터 바꿔놓고 시작
def zero(state):
    count = 1
    state[0] = 1 - state[0]
    state[1] = 1 - state[1]

    for i in range(1,N):
        if state[i-1] != end[i-1]:
            count += 1
            state[i-1] = 1 - state[i-1]
            state[i] = 1 - state[i]
            if i != N-1:
                state[i+1] = 1 - state[i+1]
    if state == end:
        return count
    else:
        return -1

# 1번째부터 바꿔놓고 시작
def non_zero(state):
    count = 0

    for i in range(1,N):
        if state[i-1] != end[i-1]:
            count += 1
            state[i-1] = 1 - state[i-1]
            state[i] = 1 - state[i]
            if i != N-1:
                state[i+1] = 1 - state[i+1]
    if state == end:
        return count
    else:
        return -1

# srt[:] 를 쓰는 이유 : 첫번째 함수를 거치면서 srt 가 바뀌기 때문에 srt의 복사본인 srt[:] 를 사용
cnt1 = zero(srt[:])
cnt2 = non_zero(srt[:])

if cnt1 >= 0 and cnt2 >= 0:
    print(min(cnt1, cnt2))
elif cnt1 >= 0 and cnt2 < 0:
    print(cnt1)
elif cnt1 < 0 and cnt2 >= 0:
    print(cnt2)
else:
    print(-1)
