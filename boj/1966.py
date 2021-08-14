# 프린터 큐
# 정답 참고
# 그냥 인덱싱 하나 만들어서 같이 돌리면됨

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    imp = list(map(int, input().split()))
    idx = list(range(N))
    cnt = 0
    while True:
        if imp[0] == max(imp):
            cnt += 1
            if idx[0] == M:
                print(cnt)
                break
            else:
                imp.pop(0)
                idx.pop(0)
        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))
