N, M, K = map(int, input().split())
score = [0 for i in range(N)]

for i in range(M):
    l = list(input().split())
    for j in range(0, len(l), 2):
        if score[int(l[j])-1] < float(l[j+1]):
            score[int(l[j])-1] = float(l[j+1])

print(round(sum(sorted(score, reverse=True)[:K]), 1))
