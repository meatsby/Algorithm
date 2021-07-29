# 체인

N = int(input())
chain = sorted(list(map(int, input().split())))
cnt = 0

while True:
    if len(chain) == 2:
        break
    if chain[0] == 0:
        chain.remove(0)
    if len(chain) == 2:
        break
    chain[0] -= 1
    a = sum(chain[-2:])
    del chain[-2:]
    chain.append(a)
    cnt += 1

if chain[0] != 0:
    cnt += 1

print(cnt)
