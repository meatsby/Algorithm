import sys

N = int(sys.stdin.readline().rstrip())
l = [0 for i in range(26)]
p = 9

for i in range(N):
    word = sys.stdin.readline().rstrip()
    for w in range(len(word)):
        l[ord(word[w])-65] += 10**(len(word)-1-w)

l.sort(reverse=True)

for i in range(len(l)):
    if p == -1:
        break
    l[i] *= p
    p -= 1

print(sum(l))
