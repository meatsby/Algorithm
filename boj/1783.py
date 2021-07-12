# 정답참고
# 나이트가 방문한 칸은 시작점과 끝점만 세는거였음

N, M = map(int, input().split())

if N == 1:
    print(1)
elif N == 2:
    print(min(4, (M+1)//2))
else:
    if M <= 6:
        print(min(4, M))
    else:
        print(M-2)
