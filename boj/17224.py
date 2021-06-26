import sys

n, l, k = map(int, sys.stdin.readline().split())
# prob = []
# score = 0

# for i in range(n):
#     s1, s2 = map(int, sys.stdin.readline().split())
#     prob.append([s1, s2])

# prob = sorted(prob, key = lambda pro: pro[1])

# while True:
#     for i in range(n):
#         if prob[i][1] <= l:
#             score += 140
#             k -= 1
#             if k == 0:
#                 break
#         elif prob[i][0] <= l:
#             score += 100
#             k -= 1
#             if k == 0:
#                 break
#     break

# print(score)

easy, hard = 0, 0

for i in range(n):
    s1, s2 = map(int, sys.stdin.readline().split())
    if s2 <= l:
        hard += 1
    elif s1 <= l:
        easy += 1

score = min(hard, k) * 140
if hard < k:
    score += min(easy, k-hard) * 100

print(score)

