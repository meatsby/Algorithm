N = int(input())
score = list(reversed([int(input()) for i in range(N)]))
dcrs = 0

for i in range(1, N):
    if score[i] >= score[i-1]:
        dcrs += score[i] - (score[i-1] - 1)
        score[i] = score[i-1] - 1

print(dcrs)
